bl_info = {
    "name": "BlendAI",
    "description": "Generates and executes Blender scripts based on a prompt",
    "author": "Rahil",
    "version": (1, 3),
    "blender": (4, 3, 2),
    "location": "View3D > Sidebar > AI Generator",
    "category": "3D View",
}


import bpy  # type: ignore
import google.generativeai as genai
import textwrap
import re
import time
import os

LOG_FILE = os.path.join(bpy.app.tempdir, "ai_log.txt")

# Replace Placeholder with your Gemini API Key
genai.configure(api_key="Placeholder")

generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config)

DEPRECATED_FUNCTIONS = [
    "bpy.ops.mesh.primitive_cube_add",
    "bpy.ops.mesh.primitive_uv_sphere_add",
    "bpy.ops.mesh.primitive_cone_add",
    "bpy.ops.mesh.primitive_cylinder_add",
    "bpy.ops.object.mode_set",
    "bpy.ops.object.select_by_type",
    "bpy.ops.object.select_all",
    "bpy.ops.view3d.view_selected",
    "bpy.types.SpaceView3D.draw_handler_add",
    "bpy.ops.object.grease_pencil_add",
    "bpy.ops.object.curve_add"
]

# Implementing a Log file
def read_log_history():
    """Read previous prompts and responses from the log file."""
    if not os.path.exists(LOG_FILE):
        return ""
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return f.read()[-2000:]

def append_to_log(prompt, response):
    """Append new prompt and response to the log file."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"Prompt: {prompt}\nResponse:\n{response}\n{'-'*50}\n")

def get_gemini_generated_code(prompt):
    try:
        history = read_log_history()

        system_prompt = f"""You are an AI specialized in generating Blender 4.3 Python scripts.
- Always return **valid and executable** Python code compatible with Blender 4.3.
- Do **NOT** include explanations or formatting—just the raw script.
- **Avoid using the following deprecated functions:** 
{', '.join(DEPRECATED_FUNCTIONS)}

## Previous Interactions:
{history}

## User Request:
{prompt} in Blender 4.3"""

        response = model.generate_content(system_prompt)

        if response and response.text:
            code = response.text.strip()
            code = re.sub(r'^```[a-zA-Z]*\n|```$', '', code, flags=re.MULTILINE)

            if code.startswith('"""') and code.endswith('"""'):
                code = code[3:-3]
            elif code.startswith("'''") and code.endswith("'''"):
                code = code[3:-3]

            append_to_log(prompt, code)
            return code
        else:
            return "# Error: No code generated."
    except Exception as e:
        return f"# Error generating code: {str(e)}"

def execute_script_with_retries(code, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            if not code.strip() or code.strip().startswith("#"):
                return "No valid code to execute."

            compile(code, '<string>', 'exec')
            exec(code, globals())
            return "Script executed successfully."
        except SyntaxError as e:
            return f"# Syntax Error: {e}"
        except Exception as e:
            if attempt < max_retries:
                time.sleep(0.5)
                continue
            return f"# Error executing the script after {max_retries} attempts: {str(e)}"

class AI_CodeGeneratorPanel(bpy.types.Panel):
    bl_label = "AI Code Generator (Gemini)"
    bl_idname = "VIEW3D_PT_ai_code_generator_gemini"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "AI Script"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Enter prompt:")
        layout.prop(context.scene, "ai_prompt", text="")

        row = layout.row()
        row.operator("script.generate_and_run_code", text="Generate & Run")

        layout.separator(factor=2.0)
        layout.label(text="Generated Code:")
        _label_multiline(context, context.scene.ai_response, layout)

        layout.separator(factor=1.5)
        layout.label(text="Execution Status:")
        layout.prop(context.scene, "ai_execution_status", text="")

class GenerateAndRunCodeOperator(bpy.types.Operator):
    bl_idname = "script.generate_and_run_code"
    bl_label = "Generate Prompt"

    def execute(self, context):
        prompt = context.scene.ai_prompt
        script_code = get_gemini_generated_code(prompt)

        if "Error" not in script_code:
            context.scene.ai_response = script_code
            execution_result = execute_script_with_retries(script_code)
            context.scene.ai_execution_status = execution_result
        else:
            context.scene.ai_execution_status = script_code

        return {'FINISHED'}

def _label_multiline(context, text, parent):
    chars = int(context.region.width / 7)
    wrapper = textwrap.TextWrapper(width=chars)

    text_lines = wrapper.wrap(text=text)
    for text_line in text_lines:
        parent.label(text=text_line)

def register():
    bpy.utils.register_class(AI_CodeGeneratorPanel)
    bpy.utils.register_class(GenerateAndRunCodeOperator)
    bpy.types.Scene.ai_prompt = bpy.props.StringProperty(name="Prompt", default="")
    bpy.types.Scene.ai_response = bpy.props.StringProperty(name="Generated Code", default="")
    bpy.types.Scene.ai_execution_status = bpy.props.StringProperty(name="Execution Status", default="")

def unregister():
    bpy.utils.unregister_class(AI_CodeGeneratorPanel)
    bpy.utils.unregister_class(GenerateAndRunCodeOperator)
    del bpy.types.Scene.ai_prompt
    del bpy.types.Scene.ai_response
    del bpy.types.Scene.ai_execution_status

if __name__ == "__main__":
    register()

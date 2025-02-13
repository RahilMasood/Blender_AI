bl_info = {
    "name": "AI Code Generator 3",
    "description": "Generates any code based on Prompt",
    "author": "Rahil",
    "version": (1, 1),
    "blender": (4, 3, 0),
    "location": "View3D > Sidebar > Cube Tools",
    "category": "3D View",
}

import bpy  # type: ignore
import google.generativeai as genai
import textwrap
import re

genai.configure(api_key="AIzaSyCPOGLnUv1-hTp8Qt1GFTI_dJjAPKphbqs")

generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config)

def get_gemini_generated_code(prompt):
    try:
        response = model.generate_content(f"""You are a specialized Python code generator for Blender 4.3. 
        Your job is to provide valid Blender Python scripts based on user input. 
        Always return only executable Python code for Blender 4.3. 
        No explanations, no formatting, just the raw script. 
        User Request: {prompt} in Blender 4.3""")

        if response and response.text:
            code = response.text.strip()

            # 1. Remove Triple Backticks (Code Fencing)
            code = re.sub(r'^```[a-zA-Z]*\n|```$', '', code, flags=re.MULTILINE)

            # 2. Remove Triple Quotes
            if code.startswith('"""') and code.endswith('"""'):
                code = code[3:-3]
            elif code.startswith("'''") and code.endswith("'''"):
                code = code[3:-3]

            return code
        else:
            return "# Error: No code generated."
    except Exception as e:
        return f"# Error generating code: {str(e)}"

def execute_script(code):
    try:
        if not code.strip() or code.strip().startswith("#"):
            return "No valid code to execute."

        # Check for syntax errors
        compile(code, '<string>', 'exec')

        exec(code, globals())
        return "Script executed successfully."
    except SyntaxError as e:
        return f"# Syntax Error: {e}"
    except Exception as e:
        return f"# Error executing the script: {str(e)}"

def _label_multiline(context, text, parent):
    chars = int(context.region.width / 7)
    wrapper = textwrap.TextWrapper(width=chars)

    text_lines = wrapper.wrap(text=text)
    for text_line in text_lines:
        parent.label(text=text_line)

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
        row.operator("script.generate_code_gemini", text="Generate")
        row.operator("script.run_generated_code", text="Run")

        layout.separator(factor=2.0)
        layout.label(text="Generated Code:")
        _label_multiline(context, context.scene.ai_response, layout)

        layout.separator(factor=1.5)
        layout.label(text="Execution Status:")
        layout.prop(context.scene, "ai_execution_status", text="")

class GenerateCodeOperatorGemini(bpy.types.Operator):
    bl_idname = "script.generate_code_gemini"
    bl_label = "Generate Code (Gemini)"

    def execute(self, context):
        prompt = context.scene.ai_prompt
        script_code = get_gemini_generated_code(prompt)

        if "Error" not in script_code:
            context.scene.ai_response = script_code
            context.scene.ai_execution_status = "Code generated. Click 'Run' to execute."
        else:
            context.scene.ai_execution_status = script_code

        return {'FINISHED'}

class RunGeneratedCodeOperator(bpy.types.Operator):
    bl_idname = "script.run_generated_code"
    bl_label = "Run Generated Code"

    def execute(self, context):
        script_code = context.scene.ai_response
        if script_code and not script_code.startswith("#"):
            execution_result = execute_script(script_code)
            context.scene.ai_execution_status = execution_result
        else:
            context.scene.ai_execution_status = "No valid code to run. Generate code first."
        return {'FINISHED'}

def register():
    bpy.utils.register_class(AI_CodeGeneratorPanel)
    bpy.utils.register_class(GenerateCodeOperatorGemini)
    bpy.utils.register_class(RunGeneratedCodeOperator)
    bpy.types.Scene.ai_prompt = bpy.props.StringProperty(name="Prompt", default="")
    bpy.types.Scene.ai_response = bpy.props.StringProperty(name="Generated Code", default="")
    bpy.types.Scene.ai_execution_status = bpy.props.StringProperty(name="Execution Status", default="")

def unregister():
    bpy.utils.unregister_class(AI_CodeGeneratorPanel)
    bpy.utils.unregister_class(GenerateCodeOperatorGemini)
    bpy.utils.unregister_class(RunGeneratedCodeOperator)
    del bpy.types.Scene.ai_prompt
    del bpy.types.Scene.ai_response
    del bpy.types.Scene.ai_execution_status

if __name__ == "__main__":
    register()

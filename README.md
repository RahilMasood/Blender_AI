# BlendAI: Unleash Your Imagination with AI-Powered 3D Modeling

BlendAI is a Blender add-on that empowers you to create 3D models simply by describing them.  No more tedious manual manipulation – just tell BlendAI what you envision, and let the power of AI bring it to life.

## Getting Started

### 1. Install the Required Module

BlendAI leverages the `google-generativeai` library. To install it within Blender's Python environment:

1.  Follow the instructions in [this tutorial](https://www.youtube.com/watch?v=DSRha-8Zk8w) to install the Python Module Installer for Blender.
2.  Use the Python Module Installer to install the `google-generativeai` package.

### 2. Configure Your API Key

1.  Obtain your Gemini API key from [AI Studio](https://aistudio.google.com/).
2.  Open the BlendAI Python script and replace the temporary tag with your actual API key, ensuring it remains within the quotes.

### 3. Install BlendAI

1.  Open Blender.
2.  Navigate to Edit > Preferences > Add-ons > Install.
3.  Locate the BlendAI Python script and click "Install."

### 4. Enable BlendAI

In the Add-ons tab, find BlendAI and enable it by checking the box next to its name.

### 5. Start Creating!

Access BlendAI by pressing N in the 3D Viewport to open the sidebar. You'll find it under "AI Code Generator 2."

## Current Limitations

BlendAI is still under development, and we're working to improve its reliability and functionality.  Current challenges include:

- Intermittent scripting issues.
- The need for more robust code execution to minimize errors.
- Implementing comprehensive error handling for cases where Gemini doesn't provide valid code.

## Upcoming Features

We're excited about the future of BlendAI and are actively developing the following features:

1.  **Better Implementation:** Reducing number of errors we face and increasing rate of Accuracy.
2.  **Speech-to-Model:** Describe your creations using your voice, making the design process even more seamless.
3.  **Enhanced Contextual Awareness:** Implement logging to store previous inputs, allowing BlendAI to better understand your evolving design vision.

## Contributing
We welcome contributions!  If you're interested in helping us improve BlendAI, please feel free to contribute.

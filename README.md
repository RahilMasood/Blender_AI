# BlendAI: Unleash Your Imagination with AI-Powered 3D Modeling

BlendAI is a Blender add-on that empowers you to create 3D models simply by describing them. No more tedious manual manipulation, just tell BlendAI what you envision, and let the power of AI bring it to life.

## What's New in Version 1.3
- **Major Bug Fixes:** Improved code execution and stability.
- **Log Files:** Implemented logging to track previous inputs, allowing for better contextual awareness and debugging.

## Getting Started

### 1. Install the Required Module

BlendAI leverages the `google-generativeai` library. To install it within Blender's Python environment:

1. Follow the instructions in [this tutorial](https://www.youtube.com/watch?v=DSRha-8Zk8w) to install the Python Module Installer for Blender.
2. Use the Python Module Installer to install the `google-generativeai` package.

### 2. Configure Your API Key

1. Obtain your Gemini API key from [AI Studio](https://aistudio.google.com/).
2. Open the BlendAI Python script and replace the placeholder with your actual API key, ensuring it remains within the quotes.

### 3. Install BlendAI

1. Open Blender.
2. Navigate to Edit > Preferences > Add-ons > Install.
3. Locate the BlendAI Python script on your computer and click "Install"

### 4. Enable BlendAI

In the Add-ons tab, find "BlendAI" and enable it by checking the box next to its name.

### 5. Start Creating!

Access BlendAI by pressing `N` in the 3D Viewport to open the sidebar. You'll find it under "AI Generator"

## Current Limitations

While BlendAI has improved, I'm still working to enhance its capabilities. Current challenges include:
- **Handling Complex Scripts:** Some generated scripts may still need manual tweaking.
- **Error Handling:** While log files improve debugging, some cases may still require manual intervention.

## Upcoming Features

I'm excited about the future of BlendAI! Here’s what’s coming soon:

1. **Enhanced Accuracy:** Further reducing errors and improving output precision.
2. **Speech-to-Model:** Describe your creations using voice input for an even more intuitive design process.

## Contributing

Welcoming contributions! If you're interested in helping improve BlendAI, feel free to contribute via this repository.

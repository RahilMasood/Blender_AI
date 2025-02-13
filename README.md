# BlendAI
A Blender AddOn coded to integrate AI that builds anything that the user tells it to without having to directly interact with Blender.

## How to Use:
### 1. Install Required Modules in Blender's Python Installation

To install the required module "google-generativeai" in Blender's Python installation, follow these steps:

- [Follow this tutorial](https://www.youtube.com/watch?v=DSRha-8Zk8w) to install the Python Module Installer.
- Use the Python Module Installer to install "google-generativeai".

### 2. Get Your Gemini API Key and Add It to the Script

To obtain your Gemini API key:

- Go to [aistudio.google.com](https://aistudio.google.com/) and obtain an API key.
- Replace "YOUR_API_KEY_HERE" in the addon Python script with your actual API key (ensure it's within the quotes).

### 3. Install the Addon in Blender

To install the addon in Blender:

- Open Blender.
- Go to Edit > Preferences > Addons > Install.
- Navigate to the addon Python script in the window that pops up and click "Install".

### 4. Enable the Addon

After the addon appears in the list of addons:

- Enable it by checking the small tick mark next to it.

### 5. Start Using the Addon

Once the addon is enabled:

- Access it by pressing N to bring up the right-side menu in the View3D workspace.
- You will find the addon under AI Code Generator 2.


## Issues
- Still not scripting all the time.
- Have to find ways to execute the code every time reducing errors.
- Have to manage good error handling in case code is not given by Gemini.


## Future Fixes
1) chatbot interface
2) speech to model
3) Adding log files so previous input can be stored so model can better understand what needs to be done.

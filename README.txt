Blender Pub Addon

Overview
    Blender Pub is a Blender addon designed to streamline the process of managing scene versions, making linked objects local, and saving files efficiently. It is ideal for ensuring consistent project workflows and maintaining organized file structures.


Features
    Publish Scene:
    Automatically increments the file version, makes all linked objects local, and saves the scene as a _MASTER file in the parent directory.

Create New Scene Types:
    Quickly create and save new scene types, such as LAYOUT, ANIMATION, or LIGHTING, with version tracking.

File Structure
    The addon organizes your files efficiently:
    _MASTER files: Saved in the parent directory of your project.
    Versioned files: Saved with incremented numbers, e.g., Scene_001.blend.

Auto-Updater Support:
    Includes a built-in updater to check for and apply updates directly within Blender.


Installation
    Download the latest version of the addon as a .zip file from the GitHub Releases page.
    Open Blender and navigate to: Edit > Preferences > Add-ons > Install....
    Select the downloaded .zip file and click Install Add-on.
    Enable the addon by checking the box next to Blender Pub in the addon list.


How to Use

Create New Scene
    1. In the Tool tab, select the type of scene you want to create:
    Create New LAYOUT Scene
    Create New ANIMATION Scene
    Create New LIGHTING Scene

    2. Choose a desired path for the scene in your project directory.
    Name the shot, for example "sh010_demoscene". Press "Save scene".

    3. A new folder called "Versions" will be created automaticly with the scene you just saved inside of it.
    If you for example chose "Create New LAYOUT Scene" the full name of your scene will be "sh010_demoscene_LAYOUT_001".
    So it adds the scene type and version number to the name of the scene.

Click on Publish Scene to:
    Increment save the current file version.
    Make all linked objects local.
    Save the scene as a _MASTER file in the parent directory.
    Note: If the current file is already a _MASTER file, publishing will be disabled. You can only publish a version file.

Auto-Updater Settings
    Open Edit > Preferences > Add-ons and find Blender Pub.
    Configure the auto-update settings, including update intervals and manual update checks.



Development
    If you encounter issues or have suggestions, feel free to open an issue on the GitHub repository.
    https://github.com/Jimmyvpfr/Blender_Pub/issues

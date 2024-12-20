bl_info = {
    "name": "Blender Pub",
    "blender": (3, 0, 0),
    "category": "Scene",
    "version": (1, 0, 1),
    "author": "Jimmy Grafström",
    "description": "Tools to publish scenes and create new scenes with proper naming conventions.",
    "tracker_url": "https://github.com/Jimmyvpfr/Blender_Pub/issues",
}

import bpy
import os
import re
from .preferences import AddonPreferences
from . import addon_updater_ops


# Operator for publish scene
class PublishSceneOperator(bpy.types.Operator):
    bl_idname = "scene.publish_scene"
    bl_label = "Publish Scene"
    bl_description = "Increments version, makes all linked objects local and saves the file as _MASTER in parent directory."
    
    def execute(self, context):
        
        # Control if filename contains _MASTER
        if "_MASTER" in bpy.path.basename(bpy.data.filepath):
            self.report({'ERROR'}, "Cannot publish a _MASTER file. Please open a versioned file.")
            return {'CANCELLED'}

        #switch to object mode
        if bpy.context.mode != 'OBJECT':
            try:
                bpy.ops.object.mode_set(mode='OBJECT')
            except:
                print(f"Failed to switch to Object Mode: {e}")
                raise RuntimeError("Script stopped because Object Mode could not be activated")

        self.increment_version_save()
        bpy.ops.object.make_local(type='ALL')
        self.save_as_master_in_parent_dir()
        return {'FINISHED'}
    
    def increment_version_save(self):
        """Increment the version number and save the scene."""
        filepath = bpy.data.filepath
        if not filepath:
            self.report({'ERROR'}, "File has not been saved before.")
            return

        directory, filename = os.path.split(filepath)
        name, ext = os.path.splitext(filename)

        match = re.search(r"_(\d{3})$", name)
        if match:
            current_version = int(match.group(1))
            new_version = f"_{current_version + 1:03}"
            new_name = re.sub(r"_(\d{3})$", new_version, name)
        else:
            self.report({'ERROR'}, "No version number found in the filename.")
            return

        new_filepath = os.path.join(directory, new_name + ext)
        bpy.ops.wm.save_as_mainfile(filepath=new_filepath)
        self.report({'INFO'}, f"File saved as {new_filepath}")

    def save_as_master_in_parent_dir(self):
        """Save the current Blender file with _MASTER suffix in the parent directory."""
        filepath = bpy.data.filepath
        if not filepath:
            self.report({'ERROR'}, "File has not been saved before.")
            return

        current_directory, filename = os.path.split(filepath)
        name, ext = os.path.splitext(filename)
        new_name = re.sub(r"_(\d{3})$", "_MASTER", name)
        parent_directory = os.path.dirname(current_directory)
        new_filepath = os.path.join(parent_directory, new_name + ext)
        bpy.ops.wm.save_as_mainfile(filepath=new_filepath)
        self.report({'INFO'}, f"File saved as {new_filepath}")

        # Open new empty scene to prevent working in _MASTER
        bpy.ops.wm.read_homefile(app_template="")
        print("Switched to a new empty project to prevent editing the _MASTER file.")


# Operator for creating different scene types
class SaveSceneOperator(bpy.types.Operator):
    bl_idname = "scene.save_new_scene"
    bl_label = "Create New Scene"
    
    # Property for scene type (e.g., LAYOUT, ANIMATION, LIGHTING)
    scene_type: bpy.props.StringProperty()

    # Path to save file
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    
    # Default filename
    filename: bpy.props.StringProperty(name="Filename", default="NewScene")
    
    def execute(self, context):
        dir_path = os.path.dirname(self.filepath)
        filename = self.filename

        versions_folder = os.path.join(dir_path, "Versions")
        if not os.path.exists(versions_folder):
            os.makedirs(versions_folder)

        versioned_filename = f"{filename}_{self.scene_type}_001.blend"
        full_path = os.path.join(versions_folder, versioned_filename)

        bpy.ops.wm.save_as_mainfile(filepath=full_path)
        self.report({'INFO'}, f"File saved to: {full_path}")

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

# Button panel
class PublishScenePanel(bpy.types.Panel):
    bl_label = "Publish Scene Panel"
    bl_idname = "SCENE_PT_publish_scene"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    
    def draw(self, context):
        layout = self.layout
        layout.operator("scene.publish_scene", text="Publish Scene")
        
        # Dynamically create scenes with different scene types
        op = layout.operator("scene.save_new_scene", text="Create New LAYOUT Scene")
        op.scene_type = "LAYOUT"
        
        op = layout.operator("scene.save_new_scene", text="Create New ANIMATION Scene")
        op.scene_type = "ANIMATION"
        
        op = layout.operator("scene.save_new_scene", text="Create New LIGHTING Scene")
        op.scene_type = "LIGHTING"

# Registreringsfunctions
def register():
    addon_updater_ops.register(bl_info)
    bpy.utils.register_class(AddonPreferences)
    bpy.utils.register_class(PublishSceneOperator)
    bpy.utils.register_class(SaveSceneOperator)
    bpy.utils.register_class(PublishScenePanel)
    
def unregister():
    bpy.utils.unregister_class(PublishSceneOperator)
    bpy.utils.unregister_class(SaveSceneOperator)
    bpy.utils.unregister_class(PublishScenePanel)
    bpy.utils.unregister_class(AddonPreferences)

if __name__ == "__main__":
    register()

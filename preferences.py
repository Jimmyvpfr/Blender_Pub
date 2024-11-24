from . import addon_updater_ops
import bpy

class AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = "BlenderPub"

    # Defining the updater parameters
    auto_check_update: bpy.props.BoolProperty(
        name="Auto-check for Update",
        description="If enabled, auto-check for updates using an interval",
        default=False,
    )

    updater_interval_months: bpy.props.IntProperty(
        name='Months',
        description="Number of months between checking for updates",
        default=0,
        min=0,
    )

    updater_interval_days: bpy.props.IntProperty(
        name='Days',
        description="Number of days between checking for updates",
        default=7,
        min=0,
        max=31,
    )

    updater_interval_hours: bpy.props.IntProperty(
        name='Hours',
        description="Number of hours between checking for updates",
        default=0,
        min=0,
        max=23,
    )

    updater_interval_minutes: bpy.props.IntProperty(
        name='Minutes',
        description="Number of minutes between checking for updates",
        default=0,
        min=0,
        max=59,
    )

    # Draw preference panel
    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.label(text="Updater Settings", icon="SYSTEM")

        # Add settings for the uppdater system
        addon_updater_ops.update_settings_ui(self, context)

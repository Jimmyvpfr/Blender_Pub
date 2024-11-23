from . import addon_updater_ops
import bpy

class AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = "BlenderPub"

    # Definiera uppdateringsrelaterade egenskaper
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

    # Rita ut preferenspanelen
    def draw(self, context):
        layout = self.layout
        layout.label(text="Minimal Addon Preferences Test")

        # Lägger till inställningar för updateringssystemet
        addon_updater_ops.update_settings_ui(self, context)

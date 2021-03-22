"""File containing main UI for maketarget"""

import bpy
from mpfb import ClassManager
from mpfb.services.logservice import LogService
from mpfb.services.uiservice import UiService
from mpfb.entities.objectproperties import GeneralObjectProperties

from mpfb.ui.maketarget import MakeTargetObjectProperties

_LOG = LogService.get_logger("maketarget.maketargetpanel")
_LOG.set_level(LogService.DEBUG)

class MPFB_PT_MakeTarget_Panel(bpy.types.Panel):
    """MakeTarget main panel."""

    bl_label = "MakeTarget"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = UiService.get_value("TARGETSCATEGORY")

    def _create_box(self, layout, box_text, box_icon=None):
        _LOG.enter()
        box = layout.box()
        box.label(text=box_text, icon=box_icon)
        return box

    def _initialize_target(self, blender_object, layout):
        box = self._create_box(layout, "Initialize", "TOOL_SETTINGS")
        props = ["name"]
        MakeTargetObjectProperties.draw_properties(blender_object, box, props)
        box.operator('mpfb.create_maketarget_target')
        box.operator('mpfb.import_maketarget_target')

    def _save_target(self, scene, layout):
        box = self._create_box(layout, "Save target", "TOOL_SETTINGS")
        box.operator('mpfb.write_maketarget_target')

    def _symmetrize_target(self, scene, layout):
        box = self._create_box(layout, "Symmetrize", "TOOL_SETTINGS")
        box.operator('mpfb.symmetrize_maketarget_left')
        box.operator('mpfb.symmetrize_maketarget_right')

    def _debug_target(self, scene, layout):
        box = self._create_box(layout, "Debug", "TOOL_SETTINGS")
        box.operator('mpfb.print_maketarget_target')

    def draw(self, context):
        _LOG.enter()
        layout = self.layout
        scene = context.scene

        blender_object = context.active_object
        if blender_object is None:
            return

        object_type = GeneralObjectProperties.get_value("object_type", entity_reference=blender_object)

        if object_type == "Basemesh":
            if not blender_object.data.shape_keys:
                self._initialize_target(blender_object, layout)
            else:
                self._save_target(scene, layout)
                self._symmetrize_target(scene, layout)
                self._debug_target(scene, layout)


ClassManager.add_class(MPFB_PT_MakeTarget_Panel)


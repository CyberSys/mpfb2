"""Asset library subpanels"""

import bpy, os, json
from bpy.props import FloatProperty
from mpfb import ClassManager
from mpfb.services.logservice import LogService
from mpfb.services.locationservice import LocationService
from mpfb.services.objectservice import ObjectService
from mpfb.services.assetservice import AssetService

_LOG = LogService.get_logger("assetlibrary.assetlibrarypanel")

_NOASSETS = [
    "No assets in this section.",
    "Maybe set MH user data preference",
    "or install assets in MPFB user data"
    ]


class _Abstract_Asset_Library_Panel(bpy.types.Panel):
    """Asset library panel."""

    bl_label = "SHOULD BE OVERRIDDEN"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "MPFB_PT_Assets_Panel"
    bl_options = {'DEFAULT_CLOSED'}

    asset_subdir = "-"
    asset_type = "mhclo"
    skin_overrides = False
    eye_overrides = False

    def _draw_section(self, scene, layout):
        _LOG.enter()
        items = AssetService.get_asset_list(self.asset_subdir, self.asset_type)
        names = list(items.keys())
        if len(names) < 1:
            for line in _NOASSETS:
                layout.label(text=line)
            return
        names.sort()
        for name in names:
            box = layout.box()
            box.label(text=name)
            asset = items[name]
            _LOG.debug("Asset", asset)
            if "thumb" in asset and not asset["thumb"] is None:
                box.template_icon(icon_value=asset["thumb"].icon_id, scale=6.0)
            op = None
            if self.asset_type == "mhclo":
                op = box.operator("mpfb.load_library_clothes")
            if self.asset_type == "mhmat":
                if self.skin_overrides:
                    op = box.operator("mpfb.load_library_skin")
            if not op is None:
                op.filepath = asset["full_path"]

    def draw(self, context):
        _LOG.enter()
        layout = self.layout
        scene = context.scene

#===============================================================================
#         if not context.object:
#             return
#
#         if not ObjectService.object_is_basemesh(context.object):
#             return
#
#         basemesh = context.object
#===============================================================================

        self._draw_section(scene, layout)


_SECTIONS = [
        #=======================================================================
        # {
        #     "bl_label": "Topologies library",
        #     "asset_subdir": "proxymeshes",
        #     "asset_type": "proxy",
        #     "eye_overrides": False,
        #     "skin_overrides": True
        #     },
        #=======================================================================
        {
            "bl_label": "Skins library",
            "asset_subdir": "skins",
            "asset_type": "mhmat",
            "eye_overrides": False,
            "skin_overrides": True
            },
        {
            "bl_label": "Eyes library",
            "asset_subdir": "eyes",
            "asset_type": "mhclo",
            "eye_overrides": True,
            "skin_overrides": False
            },
        {
            "bl_label": "Eyebrows library",
            "asset_subdir": "eyebrows",
            "asset_type": "mhclo",
            "eye_overrides": False,
            "skin_overrides": False
            },
        {
            "bl_label": "Eyelashes library",
            "asset_subdir": "eyelashes",
            "asset_type": "mhclo",
            "eye_overrides": False,
            "skin_overrides": False
            },
        {
            "bl_label": "Hair library",
            "asset_subdir": "hair",
            "asset_type": "mhclo",
            "eye_overrides": False,
            "skin_overrides": False
            },
        {
            "bl_label": "Teeth library",
            "asset_subdir": "teeth",
            "asset_type": "mhclo",
            "eye_overrides": False,
            "skin_overrides": False
            },
        {
            "bl_label": "Tongue library",
            "asset_subdir": "tongue",
            "asset_type": "mhclo",
            "eye_overrides": False,
            "skin_overrides": False
            },
        {
            "bl_label": "Clothes library",
            "asset_subdir": "clothes",
            "asset_type": "mhclo",
            "eye_overrides": False,
            "skin_overrides": False
            }

    ]

for _definition in _SECTIONS:
    _LOG.dump("Definition", _definition)
    _sub_panel = type("MPFB_PT_Asset_Library_Panel_" + _definition["asset_subdir"], (_Abstract_Asset_Library_Panel,), _definition)
    _LOG.debug("sub_panel", _sub_panel)
    ClassManager.add_class(_sub_panel)

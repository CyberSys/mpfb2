"""
{
    "attributes": {
        "color": {
            "class": "Color",
            "name": "color",
            "value": [
                0.6079999804496765,
                0.6079999804496765,
                0.6079999804496765
            ]
        },
        "extension": {
            "class": "enum",
            "name": "extension",
            "value": "REPEAT"
        },
        "height": {
            "class": "float",
            "name": "height",
            "value": 100.0
        },
        "image": {
            "class": "NoneType",
            "name": "image",
            "value": null
        },
        "interpolation": {
            "class": "str",
            "name": "interpolation",
            "value": "Linear"
        },
        "location": {
            "class": "Vector",
            "name": "location",
            "value": [
                0.0,
                0.0
            ]
        },
        "projection": {
            "class": "enum",
            "name": "projection",
            "value": "FLAT"
        },
        "projection_blend": {
            "class": "float",
            "name": "projection_blend",
            "value": 0.0
        },
        "width": {
            "class": "float",
            "name": "width",
            "value": 240.0
        }
    },
    "class": "ShaderNodeTexImage",
    "inputs": {
        "Vector": {
            "class": "NodeSocketVector",
            "default_value": [
                0.0,
                0.0,
                0.0
            ],
            "identifier": "Vector",
            "name": "Vector",
            "value_type": "VECTOR"
        }
    },
    "outputs": {
        "Alpha": {
            "class": "NodeSocketFloat",
            "default_value": 0.0,
            "identifier": "Alpha",
            "name": "Alpha",
            "value_type": "VALUE"
        },
        "Color": {
            "class": "NodeSocketColor",
            "default_value": [
                0.0,
                0.0,
                0.0,
                0.0
            ],
            "identifier": "Color",
            "name": "Color",
            "value_type": "RGBA"
        }
    }
}"""

from .abstractnodewrapper import AbstractNodeWrapper

class NodeWrapperShaderNodeTexImage:
    def __init__(self):
        pass

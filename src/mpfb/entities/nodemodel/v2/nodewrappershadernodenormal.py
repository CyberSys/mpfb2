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
        "height": {
            "class": "float",
            "name": "height",
            "value": 100.0
        },
        "location": {
            "class": "Vector",
            "name": "location",
            "value": [
                0.0,
                0.0
            ]
        },
        "width": {
            "class": "float",
            "name": "width",
            "value": 140.0
        }
    },
    "class": "ShaderNodeNormal",
    "inputs": {
        "Normal": {
            "class": "NodeSocketVectorDirection",
            "default_value": [
                0.0,
                0.0,
                1.0
            ],
            "identifier": "Normal",
            "name": "Normal",
            "value_type": "VECTOR"
        }
    },
    "outputs": {
        "Dot": {
            "class": "NodeSocketFloat",
            "default_value": 0.0,
            "identifier": "Dot",
            "name": "Dot",
            "value_type": "VALUE"
        },
        "Normal": {
            "class": "NodeSocketVectorDirection",
            "default_value": [
                0.0,
                0.0,
                1.0
            ],
            "identifier": "Normal",
            "name": "Normal",
            "value_type": "VECTOR"
        }
    }
}"""

from .abstractnodewrapper import AbstractNodeWrapper

class NodeWrapperShaderNodeNormal:
    def __init__(self):
        pass

"""
{
    "attributes": {
        "clamp_type": {
            "class": "enum",
            "name": "clamp_type",
            "value": "MINMAX"
        },
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
    "class": "ShaderNodeClamp",
    "inputs": {
        "Max": {
            "class": "NodeSocketFloat",
            "default_value": 1.0,
            "identifier": "Max",
            "name": "Max",
            "value_type": "VALUE"
        },
        "Min": {
            "class": "NodeSocketFloat",
            "default_value": 0.0,
            "identifier": "Min",
            "name": "Min",
            "value_type": "VALUE"
        },
        "Value": {
            "class": "NodeSocketFloat",
            "default_value": 1.0,
            "identifier": "Value",
            "name": "Value",
            "value_type": "VALUE"
        }
    },
    "outputs": {
        "Result": {
            "class": "NodeSocketFloat",
            "default_value": 0.0,
            "identifier": "Result",
            "name": "Result",
            "value_type": "VALUE"
        }
    }
}"""

from .abstractnodewrapper import AbstractNodeWrapper

class NodeWrapperShaderNodeClamp:
    def __init__(self):
        pass

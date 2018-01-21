bl_info = {
    'name': 'Camera Management',
    'category': 'Camera',
    'description': 'allow individual or group camera rendering',
    'author': 'Niccolò Cantù (nicokant)',
    'version': (0, 3),
}

import sys
import os

path = sys.path
flag = False
for item in path:
    if "camera_managment" in item:
        flag = True
if flag is False:
    sys.path.append(
        os.path.join(os.path.dirname(__file__), '..', 'camera_managment'))


if "bpy" in locals():
    import imp

    imp.reload(cm_layouts)
    imp.reload(cm_operators)
    print("camera_managment: Reloaded multifiles")
else:
    from . import cm_layouts, cm_operators, cm_render_queue
    print("camera_managment: Imported multifiles")

import bpy


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()

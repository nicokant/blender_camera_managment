# Blender Addon to render all the cameras in the scene
import bpy;
import time;

bl_info = {
    'name': 'Render all cameras',
    'category': 'Object'
}

class RenderAllCameras(bpy.types.Operator):

    bl_idname = 'camera.render_all'
    bl_label = 'Render All Cameras'

    def execute(self, context):
        cameras_list = list(filter(lambda x: x.type == 'CAMERA', bpy.data.scenes[context.scene.name].objects))

        for camera in cameras_list:
            self.render(context, camera)

        return { 'FINISHED' }

    def render(self, context, camera):
        context.scene.camera = camera
        ts = time.time()
        bpy.data.scenes[context.scene.name].render.filepath = 'blender_camera/render_' + str(ts)
        bpy.ops.render.render(write_still=True)

def register():
    bpy.utils.register_class(RenderAllCameras)

def unregister():
    bpy.utils.unregister_class(RenderAllCameras)

if __name__ == "__main__":
    register()


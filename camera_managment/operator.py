import bpy
import time
from . import helpers;

class ActionButton(bpy.types.Operator):
    bl_idname = "render.button"
    bl_label = "Button"

    name = bpy.props.StringProperty()
    type = bpy.props.StringProperty()

    def draw(self, context):
        self.layout.label(text=self.name)

    def execute(self, context):
        if self.type == 'ACTIVATE':
            context.scene.camera = bpy.data.objects[self.name]
            #context.scene.objects.active.select = False
            #context.scene.objects.active = bpy.data.objects[self.name]
            #context.scene.objects.active.select = True
        elif self.type == 'RENDER':
            old_camera = context.scene.camera
            context.scene.camera = bpy.data.objects[self.name]
            self.render(context)
            context.scene.camera = old_camera
        elif self.type == 'ALL':
            old_camera = context.scene.camera
            for camera in helpers.get_all_cameras(context):
                context.scene.camera = camera
                self.render(context)

            context.scene.camera = old_camera
        else:
            pass
        return {'FINISHED'}

    def render(self, context):
        filename = str(time.time())
        bpy.data.scenes[context.scene.name].render.filepath = 'blender_camera/render_' + filename
        bpy.ops.render.render(write_still=True)

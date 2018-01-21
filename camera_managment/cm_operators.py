import bpy
from . import helpers
from cm_render_queue import RenderQueue


class ActionButton(bpy.types.Operator):
    bl_idname = "render.button"
    bl_label = "Button"

    name = bpy.props.StringProperty()
    type = bpy.props.StringProperty()

    def __init__(self):
        self.renderQueue = RenderQueue()

    def draw(self, context):
        self.layout.label(text=self.name)

    def execute(self, context):
        camera = bpy.data.objects[self.name]
        if self.type == 'ACTIVATE':
            context.scene.camera = camera
            # context.scene.objects.active.select = False
            # context.scene.objects.active = bpy.data.objects[self.name]
            # context.scene.objects.active.select = True
        elif self.type == 'RENDER':
            self.renderQueue.add_camera(camera)
        elif self.type == 'ALL':
            map(
                lambda c: self.renderQueue.add_camera(c),
                helpers.get_all_cameras(context)
            )
        else:
            pass
        return {'FINISHED'}

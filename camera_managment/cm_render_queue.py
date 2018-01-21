from collections import deque
from datetime import datetime
import bpy


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs)

        return cls._instances[cls]


class RenderQueue(metaclass=Singleton):
    queue = deque([])
    is_rendering = False
    old = None
    render_path = 'blender_camera'

    def __init__(self):
        bpy.app.handlers.render_post.append(self.on_render_finish)
        bpy.app.handlers.render_cancel.append(self.clear)

    def render(self):
        print('called rendering...')
        if len(self.queue) < 0 or self.is_rendering:
            return

        print('rendering...')
        camera = self.queue.popleft()
        self.is_rendering = True
        self.old = bpy.context.scene.camera
        bpy.context.scene.camera = camera
        now = datetime.now()

        path = '{0}/{1}-{2}-{3}/{4}:{5}-{6}'.format(
            self.render_path,
            now.year, now.month, now.day,
            now.hour, now.minute,
            camera.name)
        bpy.context.scene.render.filepath = path

        bpy.ops.render.render('INVOKE_DEFAULT', write_still=True)

    def on_render_finish(self):
        # the event is launched also when user calls render
        if self.is_rendering:
            print('render ended')
            bpy.context.scene.camera = self.old
            self.old = None
            self.is_rendering = False

            # continue the loop
            self.render()

    def add_camera(self, camera):
        print('add camera')
        self.queue.append(camera)

        # try to render if possible
        self.render()

    def clear(self):
        self.queue = deque([])
        self.is_rendering = False
        self.old = None

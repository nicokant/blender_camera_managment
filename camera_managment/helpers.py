def get_all_cameras(context):
    return list(
        filter(
            lambda x: x.type == 'CAMERA',
            context.scene.objects
        )
    )

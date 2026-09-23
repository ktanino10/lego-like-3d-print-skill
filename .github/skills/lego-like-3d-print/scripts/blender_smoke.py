"""Test-only box in a separate background Blender process; no rendering."""

from pathlib import Path
import tempfile


def run():
    import bpy

    if not bpy.app.background:
        raise RuntimeError("Use a separate Blender --background process, not a live UI/MCP scene.")
    if bpy.data.filepath:
        raise RuntimeError("Start with --factory-startup and without an existing .blend file.")

    output = Path(tempfile.mkdtemp(prefix="brick-skill-blender-"))
    scene = bpy.data.scenes.new("BrickSkillSmoke")
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 1.0
    vertices = [
        (0, 0, 0), (0.008, 0, 0), (0.008, 0.008, 0), (0, 0.008, 0),
        (0, 0, 0.0032), (0.008, 0, 0.0032),
        (0.008, 0.008, 0.0032), (0, 0.008, 0.0032),
    ]
    faces = [
        (3, 2, 1, 0), (4, 5, 6, 7), (0, 1, 5, 4),
        (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7),
    ]
    mesh = bpy.data.meshes.new("BrickSkillSmokeMesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new("BrickSkillSmokeBox", mesh)
    scene.collection.objects.link(obj)
    bpy.context.window.scene = scene
    bpy.context.view_layer.update()
    target = output / "test-only-box.blend"
    bpy.ops.wm.save_as_mainfile(filepath=str(target))
    bpy.ops.wm.open_mainfile(filepath=str(target))
    restored = bpy.data.objects["BrickSkillSmokeBox"]
    if len(restored.data.vertices) != 8 or len(restored.data.polygons) != 6:
        raise RuntimeError("Blender smoke: saved mesh did not round-trip")
    if any(abs(a - b) > 1e-7 for a, b in zip(restored.dimensions, (0.008, 0.008, 0.0032))):
        raise RuntimeError("Blender smoke: dimensions changed")
    if target.stat().st_size == 0:
        raise RuntimeError("Blender smoke: empty .blend")
    print("BLENDER_SMOKE_OK", bpy.app.version_string, "8 x 8 x 3.2 mm")
    print("TEST ONLY - not a block, render, fit coupon or print approval.")
    print("New temporary output:", output)
    return output


if __name__ == "__main__":
    run()

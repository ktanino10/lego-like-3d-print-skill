"""Test-only 8 x 8 x 3.2 mm box; run in FreeCAD's Python, not system Python."""

from pathlib import Path
import tempfile


def run():
    import FreeCAD as App
    import Mesh
    import Part

    output = Path(tempfile.mkdtemp(prefix="brick-skill-freecad-"))
    previous = App.activeDocument()
    previous_name = previous.Name if previous else None
    owned = set()
    try:
        document = App.newDocument("BrickSkillSmoke")
        document_name = document.Name
        owned.add(document_name)
        box = document.addObject("PartDesign::Feature", "TestOnlyBox")
        box.Shape = Part.makeBox(8.0, 8.0, 3.2)
        document.recompute()
        if not box.Shape.isValid() or len(box.Shape.Solids) != 1:
            raise RuntimeError("FreeCAD smoke: invalid test solid")
        native = output / "test-only-box.FCStd"
        document.saveAs(str(native))
        Part.export([box], str(output / "test-only-box.step"))
        Mesh.export([box], str(output / "test-only-box.stl"))
        App.closeDocument(document_name)
        owned.remove(document_name)

        reopened = App.openDocument(str(native))
        owned.add(reopened.Name)
        restored = reopened.getObject("TestOnlyBox")
        bounds = restored.Shape.BoundBox
        dimensions = (bounds.XLength, bounds.YLength, bounds.ZLength)
        if any(abs(a - b) > 1e-6 for a, b in zip(dimensions, (8.0, 8.0, 3.2))):
            raise RuntimeError(f"FreeCAD smoke: native dimensions changed: {dimensions}")
        step = Part.read(str(output / "test-only-box.step"))
        if not step.isValid() or abs(step.Volume - 204.8) > 1e-5:
            raise RuntimeError("FreeCAD smoke: STEP round-trip failed")
        mesh = Mesh.Mesh(str(output / "test-only-box.stl"))
        if mesh.CountFacets == 0 or not mesh.isSolid():
            raise RuntimeError("FreeCAD smoke: STL is not a closed test mesh")
        for label, geometry in (("STEP", step), ("STL", mesh)):
            bounds = geometry.BoundBox
            dimensions = (bounds.XLength, bounds.YLength, bounds.ZLength)
            if any(abs(a - b) > 1e-5 for a, b in zip(dimensions, (8.0, 8.0, 3.2))):
                raise RuntimeError(f"FreeCAD smoke: {label} dimensions changed: {dimensions}")
        for path in output.iterdir():
            if not path.is_file() or path.stat().st_size == 0:
                raise RuntimeError(f"FreeCAD smoke: empty or unexpected output: {path.name}")
        print("FREECAD_SMOKE_OK", ".".join(App.Version()[:3]), "8 x 8 x 3.2 mm")
        print("TEST ONLY - not a block, fit coupon, sliced file or print approval.")
        print("New temporary output:", output)
        return output
    finally:
        for name in owned:
            if name in App.listDocuments():
                App.closeDocument(name)
        if previous_name and previous_name in App.listDocuments():
            App.setActiveDocument(previous_name)


if __name__ == "__main__":
    run()

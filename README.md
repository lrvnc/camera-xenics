# camera-xenics

Control of Xenics cameras (Bobcat-320).

**Status:** skeleton; no device code yet. Planned main class: `camera_xenics.BobcatCamera`.

## Supported platforms

Importing the package and running the non-hardware tests works on Windows, Linux and macOS.
Device control depends on the vendor SDK (to be decided); supported OSes will be listed here.

## Install in another project

Live (follows edits in this folder):

```toml
[tool.uv.sources]
camera-xenics = { path = "<path-to-Modules>/camera-xenics", editable = true }
```

Pinned to a release:

```toml
[tool.uv.sources]
camera-xenics = { git = "file:///<path-to-Modules>/camera-xenics", tag = "vX.Y.Z" }
```

Then `uv add camera-xenics` (or list it in `[project].dependencies`).

## Tests

```
uv run pytest              # no hardware needed
uv run pytest -m hardware  # needs the device connected
```

## Releasing

1. Bump `version` in `pyproject.toml`.
2. Move the `Unreleased` entries in `CHANGELOG.md` under the new version.
3. Commit, then `git tag vX.Y.Z`. Never move or delete a tag.

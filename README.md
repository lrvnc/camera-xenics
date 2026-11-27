# camera-xenics

Control of Xenics cameras (Bobcat-320).

**Status:** skeleton; no device code yet. Planned main class: `camera_xenics.BobcatCamera`.

## Supported platforms

Importing the package and running the non-hardware tests works on Windows, Linux and macOS.
Device control depends on the vendor SDK (to be decided); supported OSes will be listed here.

## Install in another project

There are three ways to depend on this library. Use **live** while developing it alongside an
experiment, and **pinned** once the experiment works, so later changes here can't break it.

Replace `vX.Y.Z` with a released tag (see the [tags](https://github.com/lrvnc/camera-xenics/tags)) and `<path-to-Modules>`
with where this repo is cloned (on the lab PC: `C:/Users/ModeLab/Documents/Leandro/Modules`).

### Pinned to a release (recommended for finished projects)

```
uv add git+https://github.com/lrvnc/camera-xenics --tag vX.Y.Z
```

which writes this to the project's `pyproject.toml`:

```toml
[tool.uv.sources]
camera-xenics = { git = "https://github.com/lrvnc/camera-xenics", tag = "vX.Y.Z" }
```

To move to a newer release, change the tag and run `uv sync`.

### Live (follows local edits)

```
uv add --editable <path-to-Modules>/camera-xenics
```

```toml
[tool.uv.sources]
camera-xenics = { path = "<path-to-Modules>/camera-xenics", editable = true }
```

Edits in this folder take effect the next time Python starts (restart the kernel or script).
If this library's dependencies change, run `uv sync` in the project.

### Latest commit on `main`

```
uv add git+https://github.com/lrvnc/camera-xenics --branch main
```

uv locks the exact commit in `uv.lock`; pull newer commits with `uv lock --upgrade-package camera-xenics`.

### Environments without a `pyproject.toml`

```
uv pip install "camera-xenics @ git+https://github.com/lrvnc/camera-xenics@vX.Y.Z"      # pinned
uv pip install -e <path-to-Modules>/camera-xenics      # live
```

If the GitHub repo is private, the machine must be signed in to GitHub through git (the first
`git clone` or `git push` prompts for it).

## Tests

```
uv run pytest              # no hardware needed
uv run pytest -m hardware  # needs the device connected
```

## Releasing

1. Bump `version` in `pyproject.toml`.
2. Move the `Unreleased` entries in `CHANGELOG.md` under the new version.
3. Commit, then `git tag vX.Y.Z` and `git push origin main vX.Y.Z`. Never move or delete a tag.

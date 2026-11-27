"""Control of Xenics cameras (Bobcat-320)."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("camera-xenics")
except PackageNotFoundError:  # running from a source tree without installation
    __version__ = "0+unknown"

__all__ = ["__version__"]

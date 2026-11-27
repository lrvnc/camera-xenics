import camera_xenics


def test_import_without_sdk():
    """The package must import on any OS, with no vendor SDK installed."""
    assert isinstance(camera_xenics.__version__, str)

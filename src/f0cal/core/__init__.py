import sys

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "f0cal.core"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError

import wrapt
from .state import StateManager

CORE = StateManager()
plugin = CORE.scanner.make_plugin_decorator
entrypoint = CORE.cli.entrypoint

@wrapt.decorator
def api_entrypoint(fn, _, args, dargs):
    CORE.scanner.scan("f0cal")
    return fn(CORE, *args, **dargs)


@plugin(name="f0cal", sets="config_file")
def config():
    prefix = CORE.prefix
    return (
        f"""
    [f0cal]
    prefix={prefix}
    """
        + """
    [env]
    LD_LIBRARY_PATH=${f0cal:prefix}/lib
    """
    )

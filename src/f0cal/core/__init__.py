# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound
__import__("pkg_resources").declare_namespace(__name__)

import wrapt

from f0cal.core.state import StateManager

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound


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

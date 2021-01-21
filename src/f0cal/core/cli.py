import os
import sys
import logging

LOG = logging.getLogger(__name__)

from f0cal import core

def _env_args(parser):
    parser.add_argument(
        "-a",
        "--append-to-venv-activate",
        dest="append",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "-s", "--silent", dest="silent", default=False, action="store_true"
    )

@core.entrypoint(["env", "activate"], args=_env_args)
def _env_activate(parser, core, append, silent, **_):
    env_str = core.env_activate_str
    if silent and not append:
        parser.error("Use of --silent without other options is a no-op.")
    if not silent:
        print(env_str)
    if append:
        core.append_to_venv_activate()

@core.entrypoint(["env", "deactivate"])
def _env_deactivate(parser, core):
    raise NotImplementedError()

@core.entrypoint(["ini"])
def _ini(parser, core):
    core.run_all_ini()

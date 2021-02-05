#PYTHON_ARGCOMPLETE_OK
import plugnparse
import f0cal.core

@plugnparse.modifier([])
def _top_level_args(parser):
    # # parser.add_argument("-f0d", "--f0cal-debug", default=None, action='store_const', const="DEBUG")
    # parser.add_argument(
    #     "-c", "--config", default=f0cal.CORE.config, type=f0cal.CORE.config.from_file
    # )
    # # parser.add_argument('-f0o', '--f0cal-config-override', action='append')
    parser.add_argument("-c", "--core", default=f0cal.core.CORE)

def main():
    f0cal.core.CORE.scanner.scan("f0cal")
    plugnparse.scan_and_run("f0cal")


if __name__ == "__main__":
    main()

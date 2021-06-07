import json
import logging

from medallion import set_config, application_instance, register_blueprints
from medallion.scripts.run import _get_argparser

log = logging.getLogger("medallion")

if __name__ == "__main__":
    log.info("Setting up medaillon in uwsgi mode")
    medallion_parser = _get_argparser()
    medallion_args = medallion_parser.parse_args()
    log.setLevel(medallion_args.log_level)

    with open(medallion_args.CONFIG_PATH, "r") as f:
        configuration = json.load(f)

    set_config(application_instance, "users", configuration)
    set_config(application_instance, "taxii", configuration)
    set_config(application_instance, "backend", configuration)
    register_blueprints(application_instance)
    log.debug(f"host: {medallion_args.host}")
    log.info("Medaillon set up")

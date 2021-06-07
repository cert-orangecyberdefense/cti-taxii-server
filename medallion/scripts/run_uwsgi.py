import json
import logging

from medallion import set_config, application_instance, register_blueprints
from medallion.scripts.run import _get_argparser

LOG_FILE = 'app.log'

log = logging.getLogger("medallion")
fh = logging.FileHandler('app.log')
fh.setFormatter(logging.Formatter("[%(name)s] [%(levelname)-8s] %(message)s"))
log.addHandler(fh)

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
log.critical("Medaillon config set up")

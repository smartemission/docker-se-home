import os
import logging

# local config, change on server for real config
config = {
    'loglevel': int(os.getenv('HOME_LOG_LEVEL', logging.DEBUG))
}

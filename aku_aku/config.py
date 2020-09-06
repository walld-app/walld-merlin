from os import getenv
import logging

RMQ_HOST = getenv('RMQ_HOST', 'localhost')
RMQ_USER = getenv('RMQ_USER', 'guest')
RMQ_PASS = getenv('RMQ_PASS', 'guest')
RMQ_PORT = getenv('RMQ_PORT', '5672')
DB_HOST = getenv('DB_HOST', 'localhost')
DB_PORT = getenv('DB_PORT', '5432')
DB_NAME = getenv('DB_NAME', 'postgres')
DB_USER = getenv('DB_USER', 'postgres')
DB_PASS = getenv('DB_PASS', '1234')
PIC_FOLDER = getenv('PIC_FOLDER', 'pics')
PIC_URL = f"https://{getenv('PIC_URL', 'image.walld.net')}"
LOG_LEVEL = getenv('LOG_LEVEL', 'INFO')


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=LOG_LEVEL)

log = logging.getLogger('pika')
log.setLevel('CRITICAL')

log = logging.getLogger('Walld aku-aku')

log.info(f'got this vars!\n'
         f'DB_HOST = {DB_HOST}\n'
         f'DB_PORT = {DB_PORT}\n'
         f'DB_NAME = {DB_NAME}\n'
         f'LOG_LEVEL = {LOG_LEVEL}\n'
         f'RMQ_HOST = {RMQ_HOST}\n'
         f'RMQ_PORT = {RMQ_PORT}\n'
         f'PIC_URL = {PIC_URL}\n'
         f'PIC_FOLDER = {PIC_FOLDER}')

import logging

from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession


class EstablishmentsService:
    logger = logging.getLogger('EstablishmentsService')

    name = 'bacana-maneiro-establishments'

    db = DatabaseSession(DeclarativeBase)

    @rpc
    def create(self, establishment):
        self.logger.info('create: start')
        self.logger.info('create: end')

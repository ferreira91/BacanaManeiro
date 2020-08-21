import logging

from gateway.entrypoints import http
from gateway.exceptions import EstablishmentNotFound
from gateway.schemas import CreateEstablishmentSchema, UpdateEstablishmentPassword, EstablishmentSchema
from marshmallow import ValidationError
from nameko.exceptions import BadRequest
from nameko.rpc import RpcProxy
from werkzeug import Response

PATH_ESTABLISHMENT = '/establishments'


class GatewayService(object):
    logger = logging.getLogger('GatewayService')

    name = 'bacana-maneiro-gateway'

    establishments_rpc = RpcProxy('bacana-maneiro-establishments')

    @http('POST', f'{PATH_ESTABLISHMENT}',
          expected_exceptions=(ValidationError, BadRequest))
    def create_establishment(self, request):
        self.logger.info('create_establishment: start')
        result = CreateEstablishmentSchema().loads(request.get_data(as_text=True))
        self.logger.info('create_establishment: end')
        return Response()

    @http('GET', f'{PATH_ESTABLISHMENT}')
    def get_establishments(self, request):
        self.logger.info('get_establishments: start')
        self.logger.info('get_establishments: end')
        return Response()

    @http('GET', f'{PATH_ESTABLISHMENT}/<string:document>',
          expected_exceptions=EstablishmentNotFound)
    def get_establishment(self, request, document):
        self.logger.info('get_establishment: start')
        self.logger.info('get_establishment: end')
        return Response()

    @http('PUT', f'{PATH_ESTABLISHMENT}/<string:document>',
          expected_exceptions=(EstablishmentNotFound, ValidationError, BadRequest))
    def update_establishment(self, request, document):
        self.logger.info('update_establishment: start')
        result = EstablishmentSchema().loads(request.get_data(as_text=True))
        self.logger.info('update_establishment: end')
        return Response()

    @http('DELETE', f'{PATH_ESTABLISHMENT}/<string:document>',
          expected_exceptions=EstablishmentNotFound)
    def delete_establishment(self, request, document):
        self.logger.info('delete_establishment: start')
        self.logger.info('delete_establishment: end')
        return None

    @http('PATCH', f'{PATH_ESTABLISHMENT}/<string:document>/password',
          expected_exceptions=(EstablishmentNotFound, ValidationError, BadRequest))
    def update_establishment_password(self, request, document):
        self.logger.info('update_establishment_password: start')
        result = UpdateEstablishmentPassword().loads(request.get_data(as_text=True))
        self.logger.info('update_establishment_password: end')
        return Response()

from django.core.management.base import BaseCommand, CommandError

from dbfread import DBF

from fias import models


class Command(BaseCommand):
    help = 'Import .dbf file to db'

    def __str_to_int(self, value):
        response = 0
        if value != '':
            response = int(value)
        return response

    def write_dbf_to_db(self, path):
        for record in DBF(path):
            addr = models.AddrObj()
            addr.status = bool(record.get('ACTSTATUS', 0))
            addr.IFNSFL = self.__str_to_int(record.get('IFNSFL', 0))
            addr.IFNSUL = self.__str_to_int(record.get('IFNSUL', 0))
            addr.OKATO = self.__str_to_int(record.get('OKATO', 0))
            addr.OKTMO = self.__str_to_int(record.get('OKTMO', 0))
            addr.postal_code = self.__str_to_int(record.get('POSTALCODE', 000000))
            addr.formal_name = record.get('FORMALNAME', '')
            addr.official_name = record.get('OFFNAME', '')
            addr.short_name = record.get('SHORTNAME', '')
            addr.update_date = record.get('UPDATEDATE')
            addr.save()

    def add_arguments(self, parser):
        parser.add_argument('path_to_dbf', nargs='+', type=str)

    def handle(self, *args, **options):
        for path_to_dbf in options['path_to_dbf']:
            try:
                self.stdout.write('import from {}...'.format(path_to_dbf))
                self.write_dbf_to_db(path_to_dbf)
                self.stdout.write('...successful')
            except:
                self.stderr.write('file {} does not exist or cannot be read as .dbf'.format(path_to_dbf))

import sys

from dbfread import DBF

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_skill_test.settings')

import django
django.setup()

from fias import models


def str_to_int(value):
    response = 0
    if value != '':
        response = int(value)
    return response


def write_dbf_to_db(path):
    for record in DBF(path):
        addr = models.AddrObj()
        addr.status = bool(record.get('ACTSTATUS', 0))
        addr.IFNSFL = str_to_int(record.get('IFNSFL', 0))
        addr.IFNSUL = str_to_int(record.get('IFNSUL', 0))
        addr.OKATO = str_to_int(record.get('OKATO', 0))
        addr.OKTMO = str_to_int(record.get('OKTMO', 0))
        addr.postal_code = str_to_int(record.get('POSTALCODE', 000000))
        addr.formal_name = record.get('FORMALNAME', '')
        addr.official_name = record.get('OFFNAME', '')
        addr.short_name = record.get('SHORTNAME', '')
        addr.update_date = record.get('UPDATEDATE')
        addr.save()


if len(sys.argv) != 2:
    print('using: python this_scriptname path_to_dbf')
else:
    write_dbf_to_db(sys.argv[1])

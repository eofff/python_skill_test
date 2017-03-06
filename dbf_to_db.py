import sys

from dbfread import DBF

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_skill_test.settings')

import django
django.setup()

from fias import models


def write_dbf_to_db(path):
    for record in DBF(path):
        addr = models.AddrObj()
        addr.status = bool(record.get('ACTSTATUS', 0))
        if record.get('IFNSFL') != '':
            addr.IFNSFL = int(record.get('IFNSFL', 0))
        else:
            addr.IFNSFL = 0
        if record.get('IFNSUL') != '':
            addr.IFNSUL = int(record.get('IFNSUL', 0))
        else:
            addr.IFNSUL = 0
        if record.get('OKATO') != '':
            addr.OKATO = int(record.get('OKATO', 0))
        else:
            addr.OKATO = 0
        if record.get('OKTMO') != '':
            addr.OKTMO = int(record.get('OKTMO', 0))
        else:
            addr.OKTMO = 0
        if record.get('POSTALCODE') != '':
            addr.postal_code = int(record.get('POSTALCODE', 0))
        else:
            addr.postal_code = 0
        addr.formal_name = record.get('FORMALNAME', '')
        addr.official_name = record.get('OFFNAME', '')
        addr.short_name = record.get('SHORTNAME', '')
        addr.update_date = record.get('UPDATEDATE')
        addr.save()


if len(sys.argv) != 2:
    print('using: python this_scriptname path_to_dbf')
else:
    write_dbf_to_db(sys.argv[1])

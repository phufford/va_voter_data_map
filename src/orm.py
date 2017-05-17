#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__appname__     = ""
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "msirabel@gmail.com"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""


class Row(dict):
    table = None
    def __init__(self, values=[]):
        assert self.table is not None
        super().__init__()
        self.table.append(self)
        for column in self.columns:
            self[column] = None
        if values:
            assert len(self.columns) == len(values)
            for column, value in zip(self.columns, values):
                self[column] = value
    @property
    def columns(self):
        return self.table.columns
    def __setattr__(self, key, value):
        assert key in self.columns
        super().__setattr__(key, value)
    def __repr__(self):
        return '\t|\t'.join(str(x) for x in self.values())

class Table(list):
    name = ''
    columns = ()
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        class row(Row):
            table = self
        self.Row = row

    def insert(self, index, row):
        raise TypeError('Method not implemented')
    def append(self, row):
        assert isinstance(row, Row)
        assert row.table == self
        super().append(row)

    def __repr__(self):
        name = self.name + type(self).__name__
        return '{}(\n{}\n)'.format(name, '\n'.join(str(r) for r in self))


import datetime
#z = Table('elections', ('id', 'date', 'type', 'winner'))
#z.Row((1, datetime.datetime.now(), 'Presidential', 'Trump'))
z = Table('county', ('id', 'name'))
z.Row((1, 'Accomack'))
z.Row((2, 'Albermarle'))
z.save('filename')
print(z)

#z = Table.import('db', 'elections')
#[i for i in z if i['id'] is 0]

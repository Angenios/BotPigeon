#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#  
#  Copyright 2021 Lord Pigeon <angeloxd1@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import ruamel.yaml as yaml
import Utility.logger as log

def dataread(bank):
    try:
        with open(f"Databank/{bank}.yaml") as bf:
            databank = yaml.safe_load(bf)
            log.d(f"Il databank {bank} è stato letto")
            return databank
    except Exception as err:
        log.e(err)

def datawrite(bank, data):
    try:
        with open(f'Databank/{bank}.yaml', "w") as bf:
            newdb = yaml.dump(data, bf)
            log.d(f"Il databank {bank} è stato modificato")
            return newdb
    except Exception as err:
        log.e(err)

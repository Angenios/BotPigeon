#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  codegen.py
#  
#  Copyright 2020 Lord Pigeon <angeloxd1@gmail.com>
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
import hashlib
import Utility.logger as log

def tripcode(arcanum, key):
    try:
        hashtripcode = hashlib.sha1(str(arcanum).encode("UTF-8")).hexdigest() # Encrypts the arcanum
        hashtrip = hashtripcode[:int(key)] # Takes only the first "key" characters of the encrypted arcanum
        tripcode = str("#"+str(hashtrip)) # Formats the character in a way similar to tripcodes
        return tripcode
    except Exception as err:
        log.e(err)

def caesarcode(arcanum, taxon):
    try:
        if taxon == "number":
            quadruarcanum = int(round(float(float(arcanum)/4), 4)*10**4)
            caesarcode = ""
            for i in range(len(str(quadruarcanum))):
                dig = int(str(quadruarcanum)[i])
                caesarcode += chr((dig-97) % 26 + 97)
            return caesarcode
        elif taxon == "word":
            caesarcode = ""
            for i in range(len(arcanum)):
                char = arcanum[i]
                if (char.isupper()):
                    caesarcode += chr((ord(char) + len(arcanum) -65) % 26 + 65)
                else:
                    caesarcode += chr((ord(char) + len(arcanum) -97) % 26 + 97)
            return caesarcode
    except Exception as err:
        log.e(err)

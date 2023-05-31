################################################################################
#  
#  Copyright (C) 2012-2023 Jack Araz, Eric Conte & Benjamin Fuks
#  The MadAnalysis development team, email: <ma5team@iphc.cnrs.fr>
#  
#  This file is part of MadAnalysis 5.
#  Official website: <https://github.com/MadAnalysis/madanalysis5>
#  
#  MadAnalysis 5 is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  MadAnalysis 5 is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with MadAnalysis 5. If not, see <http://www.gnu.org/licenses/>
#  
################################################################################


import six

class metaclass(type):
        def __getattr__(self, name):
                return list(self.values.keys()).index(name)

        def latexscript(self,script):
                name = list(self.values.keys())[script]
                return self.values[name][0]

        def latexscriptclose(self,script):
                name = list(self.values.keys())[script]
                return self.values[name][1]

        def htmlscript(self,script):
                name = list(self.values.keys())[script]
                return self.values[name][2]
        
        def htmlscriptclose(self,script):
                name = list(self.values.keys())[script]
                return self.values[name][3]


@six.add_metaclass(metaclass)
class ScriptType(object):
        values = {'none' : ['','','',''],\
                          'SUB'   : ['$_{','}$','<sub>','</sub>'],\
                          'SUP'   : ['$^{','}$','<sup>','</sup>']}


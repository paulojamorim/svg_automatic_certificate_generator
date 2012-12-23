#Copyright (C) 2012 - Paulo Henrique Junqueira Amorim (paulojamorim at gmail.com)

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  
#02110-1301, USA.

#See http://www.gnu.org/licenses/gpl-2.0.html for more information.


import os
from optparse import OptionParser

def GenerateCertificate(file_svg, label_name, file_names):
    
    svg_file = open(file_svg,'r').read()
    names = open(file_names, 'r').readlines()
   
    for name in names:

        name = name.replace('\n','')
        new_svg_file = svg_file.replace(label_name, name)

        tmp_file = open('tmp.svg', 'w') 
        tmp_file.write(new_svg_file)
        tmp_file.close()

        command = 'inkscape %s.svg -A %s.pdf' % ('tmp', name)
        os.system(command)
        
        os.remove('tmp.svg')



if __name__=="__main__":
    
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="file_svg",
                      help="svg template file")

    parser.add_option("-r", "--replace", dest="label_name",
                      help="replace label name")

    parser.add_option("-n", "--names", dest="file_names",
                      help="txt file with a name on each line")

    (opt, args) = parser.parse_args()
   
    GenerateCertificate(opt.file_svg, opt.label_name, opt.file_names) 

from data import *
from figure import *
from utility import *
from crystal import *

#=============================

setting_dir="examples/KNO3/"

#=============================

tmp1=variable_read(setting_dir+"Result/CSD.csv")
size=tmp1[0]
number_fraction=tmp1[1]

size,volume_fraction=NF_to_VF(size,number_fraction)
output=[size,volume_fraction]
variable_output(output,setting_dir+"Result/CSD.csv")

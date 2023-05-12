from data import *
from figure import *
from utility import *
from crystal import *

#=============================

setting_dir="examples/KNO3/"

#=============================

tmp1=variable_read(setting_dir+"Result/CSD.csv")
size=tmp1[0]
CSD=tmp1[1]
xlim=[0,0]
ylim=[0,0]
form="o--"

auto_plot(size,CSD,xlim,ylim,form)
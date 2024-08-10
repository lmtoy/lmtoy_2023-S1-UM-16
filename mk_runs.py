#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2023-S1-UM-16"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["G1.7+3.7-234"] =  [ 110041, 110049, 110053,]                                      # may 26

# parameters for the first pass of the pipeline
pars1 = {}

# both banks
pars1["G1.7+3.7-234"] = "pix_list=-0,13 extent=600 dv=20 dw=80 vlsr=-234 otf_cal=1 b_order=2"

# pars1["G1.7+3.7-234"] = "bank=1 pix_list=-0,13 extent=600 dv=10 dw=10 vlsr=-234"


pars2 = {}
pars2["G1.7+3.7-234"] = "bank=0"

pars3 = {}
pars3["G1.7+3.7-234"] = "bank=1"

# Found 1 source(s)

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)

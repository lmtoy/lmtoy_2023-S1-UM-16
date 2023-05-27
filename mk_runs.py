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

pars1["G1.7+3.7-234"] = ""

# parameters for the (optional) second pass of the pipeline
pars2 = {}

pars2["G1.7+3.7-234"] = ""

# Found 1 source(s)

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2)

# takes the standard closed census and groups the manifolds which have identical geom. info
import sys, re, os

in_file = open("closed_manifolds")
start = 1
names = []

for line in in_file.readlines():
    # check to see if this  a line of all repeats 
    parts = re.split("\t", line)
    # remove all spaces
    vol, cs, hom, geod, name, geom = map(lambda x: re.subn("\s", "", x)[0], parts)

    if start:
        names = [name]
        curr_vol, curr_cs, curr_hom, curr_geod = vol, cs, hom, geod
        start = 0
        continue
    
    if (vol == "=" and (cs == "+" or cs == "-") and hom == "=" and geod == "="):
        names.append(name)
    else:
        print curr_vol + "\t" + curr_cs + "\t" + curr_hom + "\t" + curr_geod + "\t%s" % names 
        names = []
        names.append(name)
        if vol != "=":
            curr_vol = vol
        if (cs != "+" and cs != "-"):
            curr_cs = cs
        if  hom != "=":
            curr_hom = hom
        if geod != "=":
            curr_geod = geod


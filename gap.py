from SnapPea import *
import os, sys, re


# Returns a string containing a presentation of the given group in
# GAP format


def fp_group_to_GAP(G):
    o = "F := FreeGroup( "
    letters = G.gens()
    for letter in letters[:-1]:
        o = o +  '"' + letter + '", '
    o = o + '"' + letters[-1] + '");\n'
    for i in range(0, len(letters)):
        o = o + "%s := F.%d;;  %s := F.%s^-1;; " % (letters[i], i + 1, chr(ord(letters[i]) - 32) , i +1) 
        
    o = o +  "\nG := F / " 

    t = repr(G.relations())
    t = re.subn("\'", "", t)[0]
    t = re.subn("([a-zA-Z])([a-zA-Z])", lambda m: m.group(1) + "*" + m.group(2), t)[0]
    t = re.subn("([a-zA-Z])([a-zA-Z])", lambda m: m.group(1) + "*" + m.group(2), t)[0]
    o = o + t + ";"
    return o

# creates code for a GAP function which returns the group.
def gap_manifold_group_record(manifold, record_name):
    o = "GroupFn := function()\n"
    G = fundamental_group(manifold)
    letters = G.gens()
    o = o + "local F, "
    for i in range(0, len(letters)-1):
        o = o + "%s, %s, " % (letters[i], chr(ord(letters[i]) - 32))
    o = o + "%s, %s; " % (letters[-1], chr(ord(letters[-1]) - 32)) 
    o = o + "F := FreeGroup( "
    for letter in letters[:-1]:
        o = o +  '"' + letter + '", '
    o = o + '"' + letters[-1] + '"); '
    for i in range(0, len(letters)):
        o = o + "%s := F.%d;;  %s := F.%s^-1;; " % (letters[i], i + 1, chr(ord(letters[i]) - 32) , i +1) 
        
    o = o +  " return F / " 

    t = repr(G.relations())
    t = re.subn("\'", "", t)[0]
    t = re.subn("([a-zA-Z])([a-zA-Z])", lambda m: m.group(1) + "*" + m.group(2), t)[0]
    t = re.subn("([a-zA-Z])([a-zA-Z])", lambda m: m.group(1) + "*" + m.group(2), t)[0]
    o = o + t + ';\nend;\n'
    o = o + record_name +  ' := rec( Name := "' + repr(manifold)+ '", Group := GroupFn);\n'
    return o 



# Below function retriangulates the given manifold until it finds a
# presentatation for pi_1 with <= 2 generators.  Returns 1 if
# succeeds, 0 if fails.  NOTE: modifies the triangulation of the
# original manifold.

def find_pres_with_2_generators(manifold, max_trys=20):
    for i in range(max_trys):
        G = fundamental_group(manifold)
        if G.num_gens() <= 2:
            return 1
        else:
            randomize_triangulation(manifold)

    return 0

def gap_manifold_record(manifold, name):
    o = name + ":= rec(\n"
    H = homology(manifold)
    G = fundamental_group(manifold)
    o = o + ' Name := "%s", Volume := "%f", Homology := %s, \n' % (
        repr(manifold), manifold.volume(), H.coefficient_list() )
    o = o + 'KnownPosBettiCover := false, GoodCover := false, Reason := false\n'
    o = o + ')\n'
    return o
       
    

    
    


##if __name__ == "__main__":
##    manifolds_file = open(sys.argv[1], "w")
##    groups_file = open(sys.argv[2], "w")
##    i = 0
##    for manifold in orientable_closed_manifolds(100):
##        H = homology(manifold)
##        if len(H.coefficient_list()) == 0:
##            # do whatever to manifold, e.g.
##            #print "Manifold: ", manifold

            
##            find_pres_with_2_generators(manifold, 100)
            
##            i = i + 1
##            groups_file.write(gap_manifold_group_record(manifold,  "G%d" % i) + ";\n\n")
##            manifolds_file.write(gap_manifold_record(manifold, "M%d" % i) + ";\n\n")

##    groups_file.write( "ManifoldGroups := [")
##    for j in range(1,i):
##        groups_file.write( "G%d," % j)
##    groups_file.write( "G%d];\n" % i )
##    manifolds_file.write( "Manifolds := [")
##    for j in range(1,i):
##        manifolds_file.write( "M%d," % j)
##    manifolds_file.write( "M%d];\n" % i )







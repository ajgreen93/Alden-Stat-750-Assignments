import numpy as np

def best_cuts(stick_length, cuts):
    ##recursively determines the best cut order by iterating over a choice
    ##of cut, finding the best cut order for the LHS and RHS sticks
    ##and then taking the minimum
    
    ##base case is no more cuts to be made
    if len(cuts) == 0:
        return 0,[]
        
    n = len(cuts)
    minCutLength = np.inf
    minCut = None
    
    ##iterate over the (sorted) list of cuts
    for i in range(n):
        cut = cuts[i]
        if i == 0:
            left_cuts = []
            
        else:
            left_cuts = cuts[0:(i)]
            
        if i == n-1:
            right_cuts = []
            
        else:
            right_cuts = cuts[(i+1):(n)]
        
        ##calculate the RHS cuts and RHS stick_length to be the distance from "cut", so that
        ##we have the right stick lengths when we go to do the subproblems    
        rightStickLength = stick_length - cut
        rightCuts = [right_cut-cut for right_cut in right_cuts]
        
        ##do the LHS and RHS subproblem, converting the solution for RHS
        ##back to the initial coordinates
        leftLengthCut,bestLeftCut = best_cuts(cut,left_cuts)
        rightLengthCut,bestRightCut = best_cuts(rightStickLength,rightCuts)
        bestRightCut = [rightCut + (i+1) for rightCut in bestRightCut]
        
        ##see if it's the minimum or not. 
        ##Note that this solution is not unique in two ways. One is that
        ##multiple cuts may achieve the minimum. The other is that for any
        ##cut, we could do the RHS and then the LHS or vice versa, and the
        ##same answer is achieved.
        if leftLengthCut + rightLengthCut + stick_length < minCutLength:
            minCutLength = leftLengthCut + rightLengthCut + stick_length
            bestCut = [i] + bestLeftCut + bestRightCut
            
    return minCutLength,bestCut

def best_cuts_complete(stick_length,cuts):
    ##sort cuts, so that we don't have to find which cuts
    ##are smaller and larger every time
    cuts.sort()
    minCutLength,bestCut = best_cuts(stick_length,cuts)
    return [cuts[cut] for cut in bestCut]

from csp import *
from a2_q1 import rand_graph
import time
import search

### Helper function:
### This function takes a CSP solution and returns the number
### of the teams created for that graph solution.
def teamCounter(cspInstanceSolution):
    teamList = []
    for i in range (len(cspInstanceSolution)):
        if (cspInstanceSolution[i] not in teamList):
            teamList.append(cspInstanceSolution[i])
    return len(teamList)

### Helper function:
### This function takes a CSP solution and returns the number
### of the maximum members of the teams created for that graph solution.
def maxTeamCounter(cspInstanceSolution):
    temp = 0
    team = {}
    for i in range(len(cspInstanceSolution)):
        if cspInstanceSolution[i] not in team:
            team[cspInstanceSolution[i]] = 0
            
    for i in range(len(team)):
        for j in range(len(cspInstanceSolution)):
            if i == cspInstanceSolution[j]:
                team[i] += 1
                
    for i in range(len(team)):
        if team[i] > temp:
            temp = team[i]   
    return temp

### Question 4
def run_q4():
    temp = 0
    teams = []       ### AKA domain of colors
    graphs = [rand_graph(0.1, 105), rand_graph(0.2, 105), rand_graph(0.3, 105),
      rand_graph(0.4, 105), rand_graph(0.5, 105), rand_graph(0.6, 105)]
    start = time.time()

    for graph in graphs:        ### Traversing the graphs list created above
        temp += 1
        for j in range(104):
            teams.append(j)
            cspInstance = MapColoringCSP(teams, graph)
            AC3(cspInstance)
            cspInstanceSolution = min_conflicts(cspInstance) ### Max_steps has been changed to 1000
            end = time.time() - start

            if (cspInstanceSolution != None):
                print("\n***   This is the result for graph #", temp, ":   ***")
                print("Number of the teams: ", teamCounter(cspInstanceSolution))
                print("Running time: ", end)
                print("Number of the assigned CSP variables: ", cspInstance.nassigns)
                print("Number of the unassigned CSP variables: ", cspInstance.returnUnassign())
                ### As the additional information, the code gives the number 
                ### of the members in the largest team.
                print("Number of people in the largest team: ", maxTeamCounter(cspInstanceSolution), "\n")
                break       ### Gets out of the for loop and proceeds for the next graph


### Main function
if __name__ == "__main__":
    run_q4()

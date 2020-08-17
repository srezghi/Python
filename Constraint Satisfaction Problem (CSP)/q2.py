### Question 2 (warm-up: Checking Solutions)
### Write a function called check_teams(graph, csp_sol) that returns True 
### if the given CSP solution dictionary csp_sol satisfies all the constraints 
### in the friendship graph, and False otherwise. graph and csp_sol are dictionaries formatted as described.

def check_teams(graph, csp_sol):
    temp = 1
    for i in range(len(graph)):
        team = csp_sol[i]
        friends = graph[i]
        for j in range(len(friends)):
            if (team == csp_sol[friends[j]]):
                temp = 0
                return False
    
    if (temp == 1):
        return True


if __name__ == "__main__":

    ### Testing the check_teams function with 2 different graphs
    graph1 = {0: [1 ,2], 1: [0], 2: [0], 3: []}
    csp_sol1 = {0:0, 1:1, 2:1, 3:0}     ### This is a correct solutions
    csp_sol2 = {0:0, 1:0, 2:1, 3:0}     ### This is a wrong solutions
    result = check_teams(graph1, csp_sol1)
    print(result)       ### This will retrun TRUE
    result = check_teams(graph1, csp_sol2)
    print(result)       ### This will retrun FALSE

    graph2 = {0: [1 ,3 ,4], 1: [0], 2: [3], 3: [0 ,2], 4: [0]}
    csp_sol1 = {0:2, 1:0, 2:0, 3:1, 4:1}    ### This is a correct solutions
    csp_sol2 = {0:1, 1:0, 2:0, 3:1, 4:1}    ### This is a wrong solutions
    result = check_teams(graph2, csp_sol1)
    print(result)       ### This will retrun TRUE
    result = check_teams(graph2, csp_sol2)
    print(result)       ### This will retrun FALSE    

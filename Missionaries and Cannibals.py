import math
class State():
    def __init__(self,cl,ml,boat,cr,mr):
        self.cl=cl
        self.ml=ml
        self.boat=boat
        self.cr=cr
        self.mr=mr
        self.parent=None
    def is_goal(self):
        if self.cl==0 and self.ml==0:
            return True
        else:
            return False
    def is_valid(self):
        if ((self.cl>=0) and (self.cr>=0) and (self.ml>=0) and (self.mr>=0) and (self.ml==0 or self.ml>=self.cl) and (self.mr==0 or self.mr>=self.cr)):
            return True
        else:
            return False
   
def successor(cur_state):
    children=[];
    if cur_state.boat=='left':
        new_state=State(cur_state.cl,cur_state.ml-2,'right',cur_state.cr,cur_state.mr+2)
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.cl-2,cur_state.ml,'right',cur_state.cr+2,cur_state.mr)
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.cl-1,cur_state.ml-1,'right',cur_state.cr+1,cur_state.mr+1)
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.cl,cur_state.ml-1,'right',cur_state.cr,cur_state.mr+1)
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.cl-1,cur_state.ml,'right',cur_state.cr+1,cur_state.mr)
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
    else:
        new_state=State(cur_state.cl,cur_state.ml+2,'left',cur_state.cr,cur_state.mr-2)
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.cl+2,cur_state.ml,'left',cur_state.cr-2,cur_state.mr)
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.cl+1,cur_state.ml+1,'left',cur_state.cr-1,cur_state.mr-1)
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.cl,cur_state.ml+1,'left',cur_state.cr,cur_state.mr-1)
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
        new_state=State(cur_state.cl+1,cur_state.ml,'left',cur_state.cr-1,cur_state.mr)
        if new_state.is_valid():
            new_state.parent=cur_state
            children.append(new_state)
    return children
def bfs():
    initial_state=State(3,3,'left',0,0)
    if initial_state.is_goal():
        return initial_state
    f=list()
    e=set()
    f.append(initial_state)
    while f:
        state=f.pop(0)
        if state.is_goal():
            return state
        e.add(state)
        children=successor(state)
        for child in children:
            if child not in e or child not in f:
                f.append(child)
    return None
def print_solution(solution):
        path = []
        path.append(solution)
        parent = solution.parent
        while parent:
                path.append(parent)
                parent = parent.parent

        for t in range(len(path)):
                state = path[len(path) - t - 1]
                print("(" + str(state.cl) + "," + str(state.ml) \
                              + "," + state.boat + "," + str(state.cr) + "," + \
                              str(state.mr) + ")")

def main():
    solution = bfs()
    print ("Missionaries and Cannibals solution:")
    print ("(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)")
    print_solution(solution)


if __name__ == "__main__":
    main()



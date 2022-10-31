class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        q = deque() # creating queue
        indegree = [0]*numCourses # creating indegree with array of numcourses
        courseStudied = 0 # declaring course studied to 0
        
        adj = defaultdict(list) # declaring defaultdict
        for course,prereq in prerequisites:
            adj[prereq].append(course) # appending course to adjacency matrix
            indegree[course]+=1 # incrementing course by 1
        
        for i in range(len(indegree)):
            if indegree[i] == 0: # if indegree of i is equal to 0 then append i to queue
                q.append(i)
                
        if not q:
            return False
        
        while q:
            curr = q.popleft() # popping from queue and storing in curr
            courseStudied+=1 # incrementing by 1
            for dependent in adj[curr]:
                indegree[dependent] -= 1 # decrement dependent by 1
                if indegree[dependent] == 0: # if dependent is equal to 0
                    q.append(dependent) # appending dependent to queue
        
        if courseStudied == numCourses: # if course studied is equal to numcourses
            return True
        return False
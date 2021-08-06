from collections import deque 

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def find_shortest_path2(graph, start, end):
    dist = {start: [start]}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = dist[at] + [next]
                q.append(next)
    return dist.get(end)


if __name__ == "__main__":

    graph = {'a':['b','c','d'],'b':['f'],'c':'e', 'd':[], 'e':['f'], 'f': []}

    start = 'a'
    end = 'f'
    path = find_path(graph, start, end)
    print(path)


    all_paths = find_all_paths(graph, start, end)
    print(all_paths)

    shortest2 = find_shortest_path2(graph, start, end)
    print(shortest2)
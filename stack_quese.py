stack=[1,2,3,4]
stack.append(5)
stack.append(6)
print(stack)
stack.pop()
print(stack)
stack.pop()
stack.pop()
stack.pop()

#check if stack is empty or not
print(len(stack)==0)
print(stack)
stack.pop()
stack.pop()
print(len(stack)==0)

#queue
from collections import deque
queue=[1,2,3,4]
queue.append(5)
queue.append(6)
print(queue)
queue.popleft()
print(queue)
queue.popleft()
queue.popleft()
queue.popleft()

#check if queue is empty or not
print(len(queue)==0)
print(queue)
queue.popleft()
queue.popleft()
print(len(queue)==0)

import importlib.util

TASKLIST_PATH = r"C:\Users\HP\OneDrive - Hochschule Düsseldorf\Desktop\Materialien\ProfMarblesTaskList.py"

spec = importlib.util.spec_from_file_location("tasklist", TASKLIST_PATH)
tasklist = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tasklist)

ProfMarblesTaskList = tasklist.ProfMarblesTaskList
m = tasklist.MarblePosition

MAP = {m.RED: "r", m.YELLOW: "y", m.GREEN: "g", m.EMPTY: "e"}

def tube_to_term(tube):
    cap = len(tube)
    balls = [MAP[x] for x in tube if x != m.EMPTY]  # حذف empty
    return f"tube({cap},[{','.join(balls)}])" if balls else f"tube({cap},[])"

def tubes_to_list(tubes):
    return "[" + ", ".join(tube_to_term(t) for t in tubes) + "]"

tl = ProfMarblesTaskList()

print("% ----------- Tasks (generated from ProfMarblesTaskList.py) -----------\n")
for t in tl.GameTasks:
    no = t.Name
    minm = t.Moves
    start = tubes_to_list(t.StartConditions)
    goal  = tubes_to_list(t.Goal)
    print(f"task({no}, {minm},\n     {start},\n     {goal}).\n")
print(f"% total: {len(tl.GameTasks)} tasks")

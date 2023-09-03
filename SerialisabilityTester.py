# Methods for checking whether an execution schedule is serialisable.

from Schedule import *




# Takes as input a Schedule of IOOperations and returns the lexicographically
# smallest serial SimpleSchedule that is conflict-equivalent to it. If the provided
# schedule is not conflict-serialisable, then this methods returns None (i.e., the python
# built-in type that represents a null value)
def to_serial( schedule = Schedule() ):
    tids = sorted(list(set([op.transaction_id for op in schedule.operations])))

    # Create a dictionary to store conflicts between transactions
    conflicts = {tid: set() for tid in tids}

    # Find all conflicts between transactions
    for i, op1 in enumerate(schedule.operations):
        for op2 in schedule.operations[i + 1:]:
            if op1.database_element == op2.database_element and op1.transaction_id != op2.transaction_id:
                if op1.operation == "WRITE" or op2.operation == "WRITE":
                    conflicts[op1.transaction_id].add(op2.transaction_id)
                    if op2.operation == "WRITE":
                        break

    # Topological sort to find serial order
    serial_order = []
    visited = set()

    def visit(tid):
        if tid not in visited:
            visited.add(tid)
            for other_tid in conflicts[tid]:
                visit(other_tid)
            serial_order.insert(0, tid)

    for tid in tids:
        visit(tid)

    # Check if the schedule is serialisable
    for tid, conflict_tids in conflicts.items():
        for conflict_tid in conflict_tids:
            if serial_order.index(tid) > serial_order.index(conflict_tid):
                return None

    # Implement me!
    serial_order.sort()
    return SimpleSchedule(serial_order)

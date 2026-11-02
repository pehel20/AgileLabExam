EMPLOYEES = {"EMP001": {"name": "Alice", "leaves": 12}}

def leave_request(emp_id, days):
    emp = EMPLOYEES.get(emp_id)
    if not emp or days > emp["leaves"]:
        return "Rejected"
    emp["leaves"] -= days
    return f"Approved: {days} day(s) for {emp['name']}, Balance: {emp['leaves']}"

"""
Employee Leave Management System
Base module for managing employee records and leave balances.
"""

# In-memory employee database
EMPLOYEES = {
    "EMP001": {
        "name": "Alice Johnson",
        "department": "Engineering",
        "leave_balances": {"sick": 10, "casual": 12, "paid": 15},
    },
    "EMP002": {
        "name": "Bob Smith",
        "department": "Human Resources",
        "leave_balances": {"sick": 8, "casual": 10, "paid": 14},
    },
    "EMP003": {
        "name": "Charlie Davis",
        "department": "Finance",
        "leave_balances": {"sick": 12, "casual": 15, "paid": 20},
    },
}

LEAVE_REQUESTS = []


def get_employee(emp_id: str):
    """Retrieve employee details by ID."""
    return EMPLOYEES.get(emp_id)


def get_leave_balance(emp_id: str, leave_type: str = None):
    """Retrieve available leave balance for an employee."""
    emp = get_employee(emp_id)
    if not emp:
        raise ValueError(f"Employee with ID '{emp_id}' not found.")
    
    if leave_type:
        leave_type = leave_type.lower()
        if leave_type not in emp["leave_balances"]:
            raise ValueError(f"Invalid leave type '{leave_type}'. Allowed types: sick, casual, paid.")
        return emp["leave_balances"][leave_type]
    
    return emp["leave_balances"]


def list_employees():
    """List all employees in the system."""
    return [
        {"id": emp_id, "name": data["name"], "department": data["department"]}
        for emp_id, data in EMPLOYEES.items()
    ]

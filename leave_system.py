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


def leave_request(emp_id: str, leave_type: str, days: int, reason: str = "") -> dict:
    """
    Submit and process an employee leave request.
    
    Args:
        emp_id: Unique employee identifier (e.g. 'EMP001')
        leave_type: Type of leave ('sick', 'casual', 'paid')
        days: Number of days requested
        reason: Optional description/reason for the leave
        
    Returns:
        dict: Processed leave request record with status 'APPROVED'
        
    Raises:
        ValueError: If employee not found, invalid leave type, non-positive days,
                    or insufficient leave balance.
    """
    emp = get_employee(emp_id)
    if not emp:
        raise ValueError(f"Employee with ID '{emp_id}' not found.")
    
    if not isinstance(days, int) or days <= 0:
        raise ValueError("Leave days requested must be a positive integer.")
    
    leave_type = leave_type.lower()
    if leave_type not in emp["leave_balances"]:
        raise ValueError(f"Invalid leave type '{leave_type}'. Allowed types: sick, casual, paid.")
    
    available_balance = emp["leave_balances"][leave_type]
    if days > available_balance:
        raise ValueError(
            f"Insufficient {leave_type} leave balance. Available: {available_balance}, Requested: {days}."
        )
    
    # Deduct leave balance
    emp["leave_balances"][leave_type] -= days
    
    request_record = {
        "request_id": f"REQ-{len(LEAVE_REQUESTS) + 1:04d}",
        "emp_id": emp_id,
        "employee_name": emp["name"],
        "leave_type": leave_type,
        "days": days,
        "reason": reason,
        "status": "APPROVED",
        "remaining_balance": emp["leave_balances"][leave_type],
    }
    
    LEAVE_REQUESTS.append(request_record)
    return request_record


def get_leave_requests(emp_id: str = None):
    """Retrieve all or employee-specific leave requests."""
    if emp_id:
        return [req for req in LEAVE_REQUESTS if req["emp_id"] == emp_id]
    return list(LEAVE_REQUESTS)


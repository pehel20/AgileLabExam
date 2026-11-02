import pytest
from leave_system import (
    EMPLOYEES,
    LEAVE_REQUESTS,
    get_employee,
    get_leave_balance,
    leave_request,
)


@pytest.fixture(autouse=True)
def reset_state():
    """Reset employee leave balances and requests before each test."""
    EMPLOYEES["EMP001"]["leave_balances"] = {"sick": 10, "casual": 12, "paid": 15}
    EMPLOYEES["EMP002"]["leave_balances"] = {"sick": 8, "casual": 10, "paid": 14}
    LEAVE_REQUESTS.clear()


def test_successful_leave_request():
    result = leave_request("EMP001", "casual", 3, "Vacation with family")
    assert result["status"] == "APPROVED"
    assert result["days"] == 3
    assert result["leave_type"] == "casual"
    assert result["remaining_balance"] == 9
    assert get_leave_balance("EMP001", "casual") == 9


def test_insufficient_leave_balance():
    with pytest.raises(ValueError, match="Insufficient sick leave balance"):
        leave_request("EMP001", "sick", 20, "Medical emergency")


def test_invalid_employee_id():
    with pytest.raises(ValueError, match="not found"):
        leave_request("NONEXISTENT", "paid", 2)


def test_invalid_leave_type():
    with pytest.raises(ValueError, match="Invalid leave type"):
        leave_request("EMP001", "holiday", 2)


def test_non_positive_days():
    with pytest.raises(ValueError, match="positive integer"):
        leave_request("EMP001", "casual", 0)


import pytest
from irrigation_scheduler import should_irrigate, water_volume, schedule


# =====================================
# BRANCH COVERAGE TESTS
# =====================================

# should_irrigate()

def test_moisture_true_branch():
    assert should_irrigate(60, 0, "seedling") is False

def test_moisture_false_branch():
    assert should_irrigate(30, 0, "seedling") is True

def test_rain_true_branch():
    assert should_irrigate(30, 10, "seedling") is False

def test_rain_false_branch():
    assert should_irrigate(30, 0, "seedling") is True

def test_seedling_true_branch():
    assert should_irrigate(40, 0, "seedling") is True

def test_seedling_false_branch():
    assert should_irrigate(50, 0, "seedling") is False

def test_flowering_true_branch():
    assert should_irrigate(50, 0, "flowering") is True

def test_flowering_false_branch():
    assert should_irrigate(55, 0, "flowering") is False

def test_other_stage_rain_true():
    assert should_irrigate(30, 5, "fruiting") is False

def test_other_stage_rain_false():
    assert should_irrigate(30, 0, "fruiting") is True

def test_other_stage_moisture_true():
    assert should_irrigate(30, 0, "fruiting") is True

def test_other_stage_moisture_false():
    assert should_irrigate(40, 0, "fruiting") is False


# water_volume()

def test_area_valid_branch():
    assert water_volume(10, "seedling", 20) == 20

def test_area_invalid_branch():
    with pytest.raises(ValueError):
        water_volume(0, "seedling", 20)

def test_seedling_stage_branch():
    assert water_volume(10, "seedling", 20) == 20

def test_flowering_stage_branch():
    assert water_volume(10, "flowering", 20) == 50

def test_other_stage_branch():
    assert water_volume(10, "fruiting", 20) == 40

def test_high_temperature_branch():
    assert water_volume(10, "seedling", 40) == 30

def test_normal_temperature_branch():
    assert water_volume(10, "seedling", 20) == 20

def test_low_temperature_branch():
    assert water_volume(10, "seedling", 5) == 10


# schedule()

def test_schedule_continue_branch():
    zones = [("A", 2, 70, 0, "seedling", 20)]
    assert schedule(zones, 100) == []

def test_schedule_irrigate_branch():
    zones = [("A", 2, 30, 0, "seedling", 20)]
    assert schedule(zones, 100) == ["A"]

def test_schedule_budget_exceeded():
    zones = [("A", 10, 30, 0, "seedling", 20)]
    assert schedule(zones, 5) == []

def test_schedule_budget_sufficient():
    zones = [("A", 2, 30, 0, "seedling", 20)]
    assert schedule(zones, 4) == ["A"]

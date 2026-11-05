
import pytest
from irrigation_scheduler import should_irrigate, water_volume, schedule


# =====================================
# CODE COVERAGE TESTS
# =====================================

# should_irrigate()

def test_wet_soil():
    assert should_irrigate(70, 0, "seedling") is False

def test_heavy_rain():
    assert should_irrigate(40, 10, "seedling") is False

def test_seedling_dry():
    assert should_irrigate(30, 0, "seedling") is True

def test_seedling_moist():
    assert should_irrigate(50, 0, "seedling") is False

def test_flowering_dry():
    assert should_irrigate(50, 0, "flowering") is True

def test_flowering_moist():
    assert should_irrigate(56, 0, "flowering") is False

def test_fruiting_rain():
    assert should_irrigate(35, 5, "fruiting") is False

def test_fruiting_dry():
    assert should_irrigate(30, 0, "fruiting") is True

def test_fruiting_moist():
    assert should_irrigate(45, 0, "fruiting") is False


# water_volume()

def test_seedling_volume():
    assert water_volume(10, "seedling", 20) == 20

def test_flowering_volume():
    assert water_volume(10, "flowering", 20) == 50

def test_other_stage_volume():
    assert water_volume(10, "fruiting", 20) == 40

def test_zero_area():
    with pytest.raises(ValueError):
        water_volume(0, "seedling", 20)

def test_negative_area():
    with pytest.raises(ValueError):
        water_volume(-5, "seedling", 20)

def test_high_temperature():
    assert water_volume(10, "seedling", 40) == 30

def test_low_temperature():
    assert water_volume(10, "seedling", 5) == 10


# schedule()

def test_empty_schedule():
    assert schedule([], 100) == []

def test_skip_zone():
    zones = [("A", 2, 70, 0, "seedling", 20)]
    assert schedule(zones, 100) == []

def test_add_zone():
    zones = [("A", 2, 30, 0, "seedling", 20)]
    assert schedule(zones, 100) == ["A"]

def test_insufficient_budget():
    zones = [("A", 10, 30, 0, "seedling", 20)]
    assert schedule(zones, 5) == []

def test_multiple_zones():
    zones = [
        ("A", 2, 30, 0, "seedling", 20),
        ("B", 1, 40, 0, "flowering", 20)
    ]
    assert schedule(zones, 10) == ["A", "B"]

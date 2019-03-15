from unittest.mock import Mock
from main.Camera import Camera
from main.Sensor import Sensor
from main.MemoryCard import MemoryCard

import pytest

@pytest.fixture
def sensor():
    return Mock(spec=Sensor)

@pytest.fixture
def memory_card():
    return Mock(spec=MemoryCard)

@pytest.fixture
def camera(sensor, memory_card):
    return Camera(sensor, memory_card)

def test_power_on(camera, sensor):
    sensor.get_data.return_value = "picture was taken"
    camera.switch_on()
    sensor.switch_on.assert_called_once()

def test_power_off(camera, sensor, memory_card):
    memory_card.is_processing.return_value = False
    camera.switch_off()
    sensor.switch_off.assert_called_once()

def test_shutter_click(camera, sensor, memory_card):
    sensor.get_data.return_value = "picture"
    camera.switch_on()
    camera.shutter_click()
    memory_card.set_data.assert_called_once_with("picture")

def test_shutter_click_with_power_off(camera, memory_card):
    camera.shutter_click()
    memory_card.set_data.assert_not_called()

def test_power_off_with_shutter_data_processing(camera, sensor, memory_card):
    memory_card.is_processing.return_value = True

    camera.switch_on()
    camera.shutter_click()
    camera.switch_off()

    sensor.switch_off.assert_not_called()

def test_power_off_with_shutter_data_not_processing(camera, sensor, memory_card):
    memory_card.is_processing.return_value = False
    camera.switch_on()
    camera.shutter_click()
    camera.switch_off()
    sensor.switch_off.assert_called_once()

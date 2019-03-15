import unittest
from unittest.mock import Mock
from main.Camera import Camera
from main.Sensor import Sensor
from main.MemoryCard import MemoryCard


class CameraTest(unittest.TestCase):

    sensor = None
    camera = None

    def setUp(self):
        self.sensor = Mock(spec=Sensor)
        self.memory_card = Mock(spec=MemoryCard)

    def test_power_on(self):
        self.sensor.get_data.return_value = "picture was taken"
        camera = Camera(self.sensor, self.memory_card)
        camera.switch_on()

        self.sensor.switch_on.assert_called_once()

    def test_power_off(self):
        self.memory_card.is_processing.return_value = False

        camera = Camera(self.sensor, self.memory_card)
        camera.switch_off()

        self.sensor.switch_off.assert_called_once()

    def test_shutter_click(self):
        self.sensor.get_data.return_value = "picture"
        camera = Camera(self.sensor, self.memory_card)
        camera.switch_on()
        camera.shutter_click()

        self.memory_card.set_data.assert_called_once_with("picture")

    def test_shutter_click_with_power_off(self):
        camera = Camera(self.sensor, self.memory_card)
        camera.shutter_click()

        self.memory_card.set_data.assert_not_called()

    def test_power_off_with_shutter_data_processing(self):
        self.memory_card.is_processing.return_value = True

        camera = Camera(self.sensor, self.memory_card)
        camera.switch_on()
        camera.shutter_click()
        camera.switch_off()

        self.sensor.switch_off.assert_not_called()

    def test_power_off_with_shutter_data_not_processing(self):
        sensor = Mock(spec=Sensor)
        memory_card = Mock(spec=MemoryCard)
        memory_card.is_processing.return_value = False

        camera = Camera(sensor, memory_card)
        camera.switch_on()
        camera.shutter_click()
        camera.switch_off()

        sensor.switch_off.assert_called_once()


if __name__ is "__main__":
    unittest.main()

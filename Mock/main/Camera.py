class Camera():
    sensor = None
    is_on = False

    def __init__(self, sensor, memory_card):
        self.sensor = sensor
        self.memory_card = memory_card

    def switch_on(self):
        print('Switching on camera')
        self.sensor.switch_on()
        self.is_on = True
    
    def switch_off(self):
        print('Switching off the camera')

        if self.memory_card.is_processing() is False:
            self.sensor.switch_off()

        self.is_on = False

    def shutter_click(self):
        if self.is_on is True:
            data = self.sensor.get_data()
            self.memory_card.set_data(data)

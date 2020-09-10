import datetime


class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def time_input(self):
        self.hours = int(input('Hours: '))
        self.minutes = int(input('Minutes: '))
        self.seconds = int(input('Seconds: '))

    def _validate(self):
        if self.hours > 23:
            return False
        elif self.minutes > 59:
            return False
        elif self.seconds > 59:
            return False
        return True

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'
            
    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        if not self._validate(): 
            raise ValueError('Time is incorrect')

class TimeStamp(Time):
    def __init__(self, hours, minutes, seconds):
        super().__init__(hours, minutes, seconds)


time = Time(12, 34, 56)
print(time)

now = datetime.datetime.now()
time_stamp = TimeStamp(now.hour, now.minute, now.second)

print(time_stamp)

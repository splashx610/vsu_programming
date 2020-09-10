class Time:
    def __init__(self):
        self.hours = None
        self.minutes = None
        self.seconds = None

    def time_input(self):
        self.hours = int(input('Hours: '))
        self.minutes = int(input('Minutes: '))
        self.seconds = int(input('Seconds: '))

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'


t = Time()
t.time_input()
print(t)

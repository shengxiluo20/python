class Car:
    #     这是一个特殊的函数，使用两个下划线标记主要是为了跟其它的普通函数区分开来。 在java里这个叫构造函数
    # 里面有带了几个参数来填充属性，还可以添加默认参数，里面我添加了一个odometer_reading这个属性
    # 这里面我添加了两个方法get_descriptive_name 和 update_odometer 这里面必须传入self，这是对自身的一种引用，另外还可以在后面添加若干参数
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print('move ' + str(self.odometer_reading) + ' miles')
        else:
            print("you can't roll back an odometer!")


# 继承类
class ElectriCar(Car):
    def __init__(self, max_speed, make, model, year):
        super().__init__(make, model, year)
        self.max_speed = max_speed

    # 静态方法
    @staticmethod
    def fill_gas_tank():
        print("i hava a battery")

    # 新建方法
    def descript_batter(self):
        print("This car has a " + str(self.battery_size) + " kwh battery.")

    # 重写方法
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model + "我是很快的特斯拉"
        return long_name.title()


# 调用类
byd = Car('byd', 'byd tang', '2017')  # 实例化Car类
str1 = byd.get_descriptive_name()  # 调用类的方法
print(str1.title())

byd.update_odometer(100)
byd.update_odometer(70)
byd.update_odometer(120)

print("=============")

ElectriCar.fill_gas_tank()
my_tesla = ElectriCar(300, "tesla", "model s", "2018")
name = my_tesla.get_descriptive_name()
print(name.title())

# 定义函数
def describe_pet(animal_type="默认动物", pet_name="默认名字"):
    print("i have a " + animal_type)
    print("names " + pet_name)


# 函数调用方式
describe_pet("小狗", "大黄")
describe_pet(pet_name="汤姆", animal_type="猫")
describe_pet("老鼠")
describe_pet()


def describe():
    return 213123321


i = describe()
print(i)


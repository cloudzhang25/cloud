while True:
    print('又胖了不能吃了')
    w=input('瘦了吗')
    if w=='瘦了':
        break
print('随便吃')


while True:
    p=input('请用户输入密码')
    if p=='小龙女':
        break
print('输入正确')


while True:
    q1 = input('第一问：你一生之中，在什么地方最是快乐逍遥？')
    if q1 != '黑暗的冰窖':
        continue
    print('答对了，下面是第二问：')
    q2 = input('你生平最爱之人，叫什么名字？')
    if q2 != '梦姑':
        continue
    print('答对了，下面是第三问：')
    q3 = input('你最爱的这个人相貌如何？')
    if q3 == '不知道':
        break
print('都答对了，你是虚竹。')


a = int(input('请输入一个整数:'))
if a > 100:
    pass
else:
    print('你输入了一个小于100的数字')


for i in range(5):
    a = int(input('请输入0来结束循环，你有5次机会:'))
    if a == 0:
        print('你触发了break语句，循环结束，导致else语句不会生效。')
        break
else:
    print('5次循环你都错过了，else语句生效了。')


i = 0
while i<5:
    a = int(input('请输入0结束循环，你有5次机会:'))
    i = i+1
    if a == 0:
        print('你触发了break语句，导致else语句不会生效。')
        break
else:
    print('5次循环你都错过了，else语句生效了。')


secret = 24  #设定秘密数字
while True:
    guess = input('你来猜猜我的秘密数字是多少:')   #输入猜测数字
    if int(guess)==secret:  #数字对比
        print('正确！你很棒哦。')
        break
    elif int(guess)>secret:
        print('你猜的太大了，请重新猜猜~')
    else:
        print('你猜的太小了，请重新猜猜~')


secret = 24
for i in range(3):
    guess = input('guess which number is my secret:')
    if  int(guess) ==secret:
        print('正确！你很棒哦。')  #输出结果
        break
    elif int(guess)>secret:
        print('你猜的太大了，请重新猜猜~')
    else:
        print('你猜的太小了，请重新猜猜~')
else:
    print('给你3次机会都猜不到，你失败了。')


while True:
    a = input('A，你认罪吗？请回答认罪或者不认：')
    b = input('B，你认罪吗？请回答认罪或者不认：')
    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')
    elif a == '不认' and b == '认罪':
        print('A判20年，B判1年，唉')
    elif a == '认罪' and b == '不认':
        print('A判1年，B判20年')
    elif a == '不认' and b == '不认':
        print('都判3年，太棒了')
        break
    else:
        print('别捣乱，只能回答“认罪”或“不认”！')
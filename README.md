# python
#### 什么是python：Python（英国发音：/ˈpaɪθən/ 美国发音：/ˈpaɪθɑːn/）, 是一种面向对象、解释型计算机程序设计语言。
#### python程序的组成
     1.程序由模块构成
     2.模块包含语句
     3.语句包含表达式
     4.表达式建立并处理对象
#### python关键字
     循环判断
     if elif else for while break continue and or is not in
     函数模块类
     from 从某个文件当中引入模块
     import 引入某些内容
     as 当做什么 生成新的对象用
     def 定义函数
     pass 空语句占位
     lambda 定义匿名函数
     return 函数返回函数返回值
     class 定义类
     异常
     try 异常检测
     except 异常处理
     finally 最终执行 异常执行
     raise 抛出异常
     其他
     del 删除一个变量
     global 声明使用全局变量
     with 形成一个新对象
     assert 断言处理
     yield 函数的终断返回
     nonlocal 闭包
     exec 形成新的进程
#### python的核心数据类型
     数字（包含整形Int和浮点型Float） 字符串（String） 列表（List） 字典(Dict) 元组(Tuple) 集合(Set) 文件
     其他类型 ： 类类型(object) None(Nonetype) 布尔型(Boolean)
     编程单元模块类型 ： 函数(function) 模块(module) 类(class)
#### 常量与变量
     常量：不能给被改变的量
     变量：人为设定有的标识符，用来标记常量，可以被重复利用赋值
#### 标识符明明规则
     1.标识符由一个或多个字母、数字或下划线组成
     2.标识符的第一个字符必须是字母或下划线
     3.标识符不能与关键字相同
     4.python语言是严格区分大小写的
     但是在python的标识符命名中还有一些默认规则
     1.以单一下划线开头的变量名（—x）不会被from module import ×语句导入
     2.前后双下划线的变量（————x————）为系统的默认变量
     3.前面两个下划线开头的变量（————x）为类的私有变量
#### python中0为假1为真
#### ‘’‘ 原样输出
#### #coding=utf-8设置在首行或者第二行 可以在python中输出中文
#### 字符串：零个或多个字符组成的有限串行
#### a|b 与 两个数2进制进行比较 只要有一个数是1就取1
#### a&b 或 两个数2进制进行比较，只要有一个数是0就为0
#### a^b 亦或 连个数2进制进行比较，相同取0，不同取1
#### 强制转换：
     a=1.234 int（a）=1 取整数
#### import math 引用math这个数学库
     math.sqrt(a):a开方
     math.pow(a,b):a的b次方
     math.trunc(a):如果a是小数，省去小数部分，或者int（a）函数，也可以省去小数部
     math.floor(a):对a向下求整，他的值小于或等于a
     math.cell(a):对a向上求整，她的值大于或等于a
     math.factorial(a):求a的阶乘
     math.exp(a):求e的a次方
#### import random 引入random模块（随机）
     random.random():随机生成一组数
     random.choice（数据类型）：在这个数据类型中随机挑选一个
#### 转义字符
     \n 换行
     \r 回车
     \t 水平制表
#### 字符串操作
     1 字符串的拼接和重复 （+和×）
     2 repr
     a.find('a')查找字符串a，找到返回索引值，找不到返回-1
     a.replace('a','sf'):对全局进行搜索和替换
     a.split(',')把，作为分隔符把他们分割成单一的部分
     a.upper()把a的字符全部都编程大写的
     a.isalpha()检查a中是否全部是字母，是返回true，否则返回false
     切片操作
     a='asdasd'
     a[1]: 's'
     a[-1]: 'd'
     a[1:3]: 'sd'
     a[1:]: 'sdasd'
     a[0:3]: 'asd'
     a[:-1]: 'asdas'
     a[:]: 'asdasd'
     a[::-1] 'dsadsa' 逆向取值 每一个取一个
     a[::-2] 'das' 　　逆向取值　每两个取一个
     a[-1:-5:-2]  'da'
     a[2::-2] 'da' 在２前边的每两个取一个
#### 输入输出
     input 输入
     print 输出 python2中不换后加，python3中不换行后加，end“
     %d 传入整型
     %s 传入字符串
     %f 传入浮点型
     %% 输入%
#### 列表
     定义：列表表示一种容器类型，是任意对象的有序集合，通过索引访问其中的元素。
     表达符号：[]
     append 增加 append（‘a’）向列表的末端加入a
     extend 合并列表 extend（[5,6]）合并两个列表
     insert 在某个位置插入一个元素 insert(3,2)在下标为3的位置插入2
     index 定位 index(5)显示5的下标
     count 计数
     sort 排序 （默认从小到大）sort（cmp=numsort）从大到小
     reverse 反转
     del 删除
     remove 删除
     pop 弹出
#### 元组
     定义：元组是一种容器类型，是任意对象的有序集合，通过索引访问其中的元素
     长度固定，对象不可变
     表达符号：（）
     元组的操作
     元组的用法几乎与列表一致，唯一不同的是元组不可修改，这在一些特殊需求的时候有意义。只是元组的定义中用圆括号，在初始化的时候可以用括号也可以不        用。
     用途
     元组的存在看似多余但是在有些地方不可替代
     1.作为键使用的时候
     2.作为一些内建函数或者方法的返回值，不希望被修改
#### 字典：通过键值对来实现元素的存取，是一种无序的集合，容器可变，可改变的，没有运算
     键：可以是数字或字符串，值什么类型都可以，内部查找是散列查找
     d.keys() 列出所有的键
     d.values() 列出所有的值
     d.items() 列出所有的键和值，每一对形成一个元组
     d.get("a") 获取键a的值
     d.update(d2) 合并
     d.pop(key) 弹出某一个 字典中弹出的一个消失
     del d[key] 删除 用中括号
     a = dict(zip(x,y))两个元组x,y或者其他转换成字典
#### 集合：无序排列，可包含不同的数据类型，支持成员关系测试，花括号{}，只能整体使用不可以取数，不可以有重复的项
     s = {[1,2]} 定义一个集合
     s = set([]) 定义一个空集合
     s = {1,2} 定义一个集合
     s = frozenset({1,2,3}) frozenset 定义的列表不可变
#### 集合方法：
     s.add(5) 添加一个值
     s.pop() 随机弹出
     s.cleat() 清空集合
     s.remove() 删除集合中某个数
     s.diffrence(s1) 列出s中有s1没有的项
     s.union(s1) 合并s和s1 相同的只取一项
     s.update(s1) 合并s和s1 相同的只取一项
#### 集合运算：
     s - s1  减去s1中和s中重复的项
     s | s1 合并（并集）
     s & s1 相同的（交集）
     s ^ s1 不相同的|（补集）
#### 数据类型总结：
     bool：true false 逻辑运算得到的结果为bool类型
     nonetype：none用做空，占位变量
     数字类型 整型 不可变的 数学运算位运算等
     浮点型
     字符串类型  有序的  不可变的 + * 运算  属性方法 切片操作 in逻辑
     列表       有序的  可变的   + * 运算  属性方法 切片操作 in逻辑
     元组       有序的  不可变的 + * 运算  属性方法 切片操作 in逻辑
     字典       无序的  可变的            属性方法         in逻辑
     集合  set  无序的  可变的 -|^&运算   属性方法         in逻辑
     frozenset 无序的  不可变的 -|^&运算  属性方法         in逻辑
#### 继承：继承描述了基类的属性如果“遗传”给派生类。一个子类可以继承它的基类的任何属性，不管是数据属性还是方法。
     简单总结继承的意图或者好处：
     1.可以实现代码重用，但不是仅仅实现代码重用，有时候根本就没有重用。
     2.实现属性和方法继承
     3.一个类在继承父类的同时也有自己特有的方法和属性，当与父类重名的时候会覆盖掉父类的方法和属性。
#### 多重继承
#### 继承检测
     可以使用issubclass()函数来检测一个类是否继承于另一个类>>>issubclass(Class1,Class2)
#### super函数
     初始化
     函数的继承分一般方法的继承还有点不同，在子类中无法直接使用父类中的初始化函数。在子类覆盖父类的方法后如果海西哪个要使用父类中的方法就需要借组        super函数。这个函数的目的就是帮组程序员找出相应的父类，然后方便调用相关的属性。一般情况下，程序员可能仅仅采用非绑定方式调用祖先类方法。使用        super()可以简化搜索一个合适祖先的任务，并且在调用它时，替你传入实例或类型对象。 
#### super函数的参数，第一个是当前子类的类的名字，第二个self，然后是点号，点号后面是所要调用的父类的方法。
#### 封装
     继承。封装和多态被认为是面向对象编程的三个重要特征。但是封装和多态无论在理解上还是实践上都是有争议的话题。这些争议多来自于对同意现象的不同理        解，还有不同的编程语言的事项和对多态封装的诠释角度不同。不管有多少不同的理解方式，我们都药对这两个概念有所了解，这也是编程水平进阶的必须。
#### 封装和私有化
     在程序设计中，封装是对对象的一种抽象，即将某些部分隐藏起来，对程序（或者模块）外部不可见，无法调用。封装离不开“私有化”。就是将类或者函数中的某      些属性限制在某个区域之内，外部无法调用。Python中私有化的方法比较简单，就是在准备私有化的属性（方法或者数据）名字前面加上双下划线。
#### 多态
     多态是值面向对象程序执行时，相同的信息可能会送给多个不同的类别对象，系统可依据对象所属类别，引发对应类别的方法而又不同的行为。简单来说就是相同      的信息给予不同的对象会引发不同的动作。
#### 魔法方法、属性和迭代器
     在Python中，有的方法和属性名称前后都会有两个下划线，这种写法很特别，在之前我们提到过，我们跟这种方法或者属性叫做特殊方法（属性）夜叫做魔法方法      （属性）。一般这种方法都是由系统定义的，有特殊的含义，可以通过dir（）函数进行查看一个对象有什么魔法方法（属性）。
     class A（）：
     a.__doc__ 文档说明
     a.__class__ 类名
     a.__dict__ 字典
     __getattr__ 调用一个不存在的变量时会调用getattr
     __setattr__ 给一个不存在的属性赋值时会调用setattr
#### 迭代器和生成器
     迭代器
     class TestIter:
         def __init__(self,a):
             self.a = a
     def __iter__(self):
         return self
     def __next__（self）:
         self.a += 1
         return self.a ** 2
     a = TestIter(2)
     print (next(a))
     print (a.__next__()) 与上一行表达意思相同，python2，3都可以使用
     生成器
     生成器是一次生成一个值的特殊类型函数。可以将其视为可恢复函数。调用该函数将返回一个可用于生成连续x值的生成器，简单的说就是在函数的执行过程中，
     yield语句会把你需要的值返回给调用生成器的地方，然后退出函数，下一次调用生成器函数的时候又从上次中断的地方开始执行，而生成器内的素有变量参数
     都会被保存下来供下一次使用。
     def fib(max):
         a,b=0,1
         while a<max:
             yield a
             a,b = b,a+b
     for i in fib(20):
         print(i)

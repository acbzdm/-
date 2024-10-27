# 小丑牌成功概率计算器

## 项目简介

小丑牌成功概率计算器是一个用 Python 开发的应用程序，用于计算特定条件下弃牌后做成目标牌型的成功的概率。
用户输入需要牌的数量，弃牌后的获得牌数和牌剩余数量将返回成功的概率。

## 计算公式

举例示意
现有牌做顺子差一张。弃掉剩下的4张牌后至少来一张9或A才能做出顺子
需要牌的剩余总数为8，需要牌的至少数量1，弃牌后收到的牌数4，剩余牌数44。

此时做出顺子的概率计算公式为：

![公式](https://github.com/user-attachments/assets/90c54b61-d2ba-4061-9f77-ea5adfb0e9d0)



Python
使用scipy.special里的comb函数计算排列组合。使用tkinter做可视化输入输出

使用pyinstaller打包，过程中显示找不到scipy.special._ufuncs，最终打包的windows可运行程序在release中。

效果展示

![作顺子的概率为56 61%](https://github.com/user-attachments/assets/23a3be6d-26a8-4a58-a0eb-185c9cd5307a)

做顺子的概率为56.61%

![作红桃同花的概率为31 67%](https://github.com/user-attachments/assets/fe1e9de3-5cb6-4042-b4ba-416388f61959)

做红桃同花的概率为31.67%

![弃牌做红心同花后做红心同花的概率38 12%](https://github.com/user-attachments/assets/558b6b65-13c7-4ada-b4c2-60e96f1541fd)

弃牌做红心同花后做红心同花的概率38.12%，比31.67%并没有上升多少

![弃牌作红心同花后作方块同花的概率为56 28%](https://github.com/user-attachments/assets/964d13c7-929b-4092-9fd5-15981b0b5db4)

弃牌做红心同花后做方块同花的概率为56.28%

![弃牌做红心同花后做小顺子的概率56 28%](https://github.com/user-attachments/assets/39957ddc-c355-4655-9aec-79da880eb316)

弃牌做红心同花后做小顺子的概率56 28%

![弃牌做红心同花后做大顺子的概率50 25%](https://github.com/user-attachments/assets/2000128a-18b6-4b1a-9158-68c37db19fca)

弃牌做红心同花后做大顺子的概率50.25%

此时做方块同花和小顺子的概率相同，但是同花的得分会更高。

还有时会出现顺子，同花，葫芦都各差一张做成时使用该计算器计算更加快捷。


## 使用说明

1. 打开应用程序

![程序图片](https://github.com/user-attachments/assets/8a4fc1a3-9056-4d6a-a468-b8ef2713ac42)

3. 输入以下参数：
   - **需要牌的剩余总张数**：输入需要的牌剩余数量。
   - **需要牌的至少数量**：输入需要的牌的最小数量。
   - **弃牌后收到的牌数**：输入弃牌后实际得到的牌数量。
   - **剩余牌总数**：输入剩余牌的总数量。

以上参数必须都是正整数
4. 点击“开始计算”按钮查看结果。

# 小丑牌成功概率计算器

## 项目简介

小丑牌成功概率计算器是一个用 Python 开发的应用程序，用于计算特定条件下弃牌后做成目标牌型的成功的概率。
用户输入需要牌的数量，弃牌后的获得牌数和牌剩余数量将返回成功的概率。

## 计算公式

举例示意
现有牌做顺子差一张。弃掉剩下的4张牌后至少来一张9或A才能做出顺子
需要牌的剩余总数为8，需要牌的至少数量1，弃牌后收到的牌数4，剩余牌数44
$\frac{C_{8}^{1}*C_{36}^{3}}{C_{44}^{4} } +\frac{C_{8}^{2}*C_{36}^{2}}{C_{44}^{4} } +\frac{C_{8}^{3}*C_{36}^{1}}{C_{44}^{4} }+\frac{C_{8}^{4}*C_{36}^{0}}{C_{44}^{4} }$
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">  <mfrac>    <mrow>      <msubsup>        <mi>C</mi>        <mrow>          <mn>8</mn>        </mrow>        <mrow>          <mn>1</mn>        </mrow>      </msubsup>      <mo>&#x2217;</mo>      <msubsup>        <mi>C</mi>        <mrow>          <mn>36</mn>        </mrow>        <mrow>          <mn>3</mn>        </mrow>      </msubsup>    </mrow>    <msubsup>      <mi>C</mi>      <mrow>        <mn>44</mn>      </mrow>      <mrow>        <mn>4</mn>      </mrow>    </msubsup>  </mfrac>  <mo>+</mo>  <mfrac>    <mrow>      <msubsup>        <mi>C</mi>        <mrow>          <mn>8</mn>        </mrow>        <mrow>          <mn>2</mn>        </mrow>      </msubsup>      <mo>&#x2217;</mo>      <msubsup>        <mi>C</mi>        <mrow>          <mn>36</mn>        </mrow>        <mrow>          <mn>2</mn>        </mrow>      </msubsup>    </mrow>    <msubsup>      <mi>C</mi>      <mrow>        <mn>44</mn>      </mrow>      <mrow>        <mn>4</mn>      </mrow>    </msubsup>  </mfrac>  <mo>+</mo>  <mfrac>    <mrow>      <msubsup>        <mi>C</mi>        <mrow>          <mn>8</mn>        </mrow>        <mrow>          <mn>3</mn>        </mrow>      </msubsup>      <mo>&#x2217;</mo>      <msubsup>        <mi>C</mi>        <mrow>          <mn>36</mn>        </mrow>        <mrow>          <mn>1</mn>        </mrow>      </msubsup>    </mrow>    <msubsup>      <mi>C</mi>      <mrow>        <mn>44</mn>      </mrow>      <mrow>        <mn>4</mn>      </mrow>    </msubsup>  </mfrac>  <mo>+</mo>  <mfrac>    <mrow>      <msubsup>        <mi>C</mi>        <mrow>          <mn>8</mn>        </mrow>        <mrow>          <mn>4</mn>        </mrow>      </msubsup>      <mo>&#x2217;</mo>      <msubsup>        <mi>C</mi>        <mrow>          <mn>36</mn>        </mrow>        <mrow>          <mn>0</mn>        </mrow>      </msubsup>    </mrow>    <msubsup>      <mi>C</mi>      <mrow>        <mn>44</mn>      </mrow>      <mrow>        <mn>4</mn>      </mrow>    </msubsup>  </mfrac></math>
其中：
- \( P \) 是成功概率
- \( C(n, k) \) 表示组合数（从 n 中选择 k 的方式数）
- \( a \) 是剩余牌的总数
- \( b \) 是需要的至少数量
- \( c \) 是弃牌后收到的牌数
- \( d \) 是剩余牌总数

## 使用说明
![弃牌作红心同花后作方块同花的概率为56 28%](https://github.com/user-attachments/assets/964d13c7-929b-4092-9fd5-15981b0b5db4)
![弃牌做红心同花后做小顺子的概率56 28%](https://github.com/user-attachments/assets/39957ddc-c355-4655-9aec-79da880eb316)
![弃牌做红心同花后做红心同花的概率38 12%](https://github.com/user-attachments/assets/558b6b65-13c7-4ada-b4c2-60e96f1541fd)
![弃牌做红心同花后做大顺子的概率50 25%](https://github.com/user-attachments/assets/2000128a-18b6-4b1a-9158-68c37db19fca)
![作顺子的概率为56 61%](https://github.com/user-attachments/assets/23a3be6d-26a8-4a58-a0eb-185c9cd5307a)
![作红桃同花的概率为31 67%](https://github.com/user-attachments/assets/fe1e9de3-5cb6-4042-b4ba-416388f61959)


1. 打开应用程序。
2. 输入以下参数：
   - **需要牌的剩余总张数**：输入总牌数。
   - **需要牌的至少数量**：输入需要的最小牌数。
   - **弃牌后收到的牌数**：输入弃牌后实际得到的牌数。
   - **剩余牌总数**：输入剩余牌的总数。

3. 点击“开始计算”按钮查看结果。

## 界面预览

![应用程序界面](C:\Users\黄敬生\Desktop\作红桃同花的概率为31.67%.png)

## 安装与运行

### 依赖项

确保安装以下依赖：

- Python 3.x
- Kivy

### 克隆项目

```bash
git clone https://github.com/你的用户名/小丑牌成功概率计算器.git
cd 小丑牌成功概率计算器

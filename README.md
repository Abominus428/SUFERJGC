# Matrix



## 功能

### 功能函数

`function matrixAdd(A, B)` **矩阵相加**

`function matrixSubtract(A, B)` **矩阵相减**

`function matrixMultiply(A, B) `**矩阵相乘**

> 要判断A.列和B.行是否相等

`function solveAXB(A, B)` **AX = B**

> X = A^-1^B
>
> 要判断矩阵A是否为方阵和B 的维度**（行）**与 A 是否匹配。
>
> 要判断A是否可逆

`function solveXAB(A, B)` **XA = B**

> X = BA^-1^
>
> 要判断矩阵A是否为方阵和B 的维度**（列）**与 A 是否匹配。
>
> 要判断A是否可逆

`function matrixTranspose(A)` **矩阵转置**

> 3x2矩阵 --> 2x3矩阵

`function matrixInverse(A)` **矩阵求逆**

> 只有方阵才有逆矩阵！
>
> 行列式 det(A)，（特例：由于行列式为 0，矩阵 A 不可逆。）
>
> 伴随矩阵 adj(A)
>
> 通过公式 A^-1 = adj(A) / det(A)

`function matrixDeterminant(A)` **矩阵行列式**

> 行列式仅适用于方阵！
>
> **高斯消元法**，将初始矩阵 --> 上三角矩阵
>
> 对角线值相乘

`function matrixRank(A)` **矩阵的秩**

> **高斯消元法**，进入[矩阵计算器 (matrixcalc.org)](https://matrixcalc.org/zh-CN/#rank({{0,1,2},{1,2,0},{2,4,0},{0,3,6}}))，点击详细内容 (使用高斯消去法)，可以直观了解过程。

`function matrixLU(A)` **矩阵分解（LU分解）**

> LU分解仅适用于方阵！
>
> LU分解将矩阵分为下三角矩阵（L）和上三角矩阵（U）的乘积，[lu分解_百度百科 (baidu.com)](https://baike.baidu.com/item/lu分解?fromModule=lemma_search-box)

`function matrixScalarMultiply(A, scalar)` **矩阵数乘**

`function matrixPower(A, n)` **矩阵的幂**

> 只有方阵才能进行幂运算!
>
> 幂次必须为非负整数!
>
> (特例：由于幂次为 0，返回单位矩阵)

### 辅助函数

`function matrixAdjugate(A)` **伴随矩阵**

> 通过余子式计算(不好描述，[伴随矩阵_百度百科 (baidu.com)](https://baike.baidu.com/item/伴随矩阵?fromModule=lemma_search-box))

### 其他函数

function initMatrixInputs(matrixId)  //初始化

function parseFraction(value)   //返回 Fraction 形式

function switchToTwoMartixOperations()  //切换到两个矩阵运算

function switchToSingleMartixOperations()  //切换到单个矩阵运算



function insertMatrix(targetMatrix, sourceMatrix)

function insertMatrixB(targetMatrix)

function insertMatrixA(targetMatrix)

function insertMatrixANS(targetMatrix)



function restoreHistory()  //恢复历史

function clearMatrices()  //清零

> 上面两个没有测试过，不知道会不会报错



function addRow(matrixId)

function addCol(matrixId)

function removeRow(matrixId)

function removeCol(matrixId)



function calculate()  // 计算函数

function displayResult(result, process)  // 显示计算结果

function displayLUResult(result)  // 显示 LU 分解结果

function displayMatrix(matrix, title = '')  // 显示矩阵

function getMatrix(matrixId)  // 获取矩阵数据

function selectFunction(op)  // 选择功能，动态调整矩阵 B 的显示



---



## 需求产生方式

**1.** **需求来源**

- **用户需求**：目标用户主要是需要进行矩阵运算的学生、教师、工程师或研究人员。通过观察他们日常需要完成的矩阵运算任务，例如矩阵加减、乘法、求逆、求行列式等，确定具体需求。
- **自身需求**：你作为开发者对软件功能有特定设想，包括展示矩阵计算过程、可视化输入输出等，这些都构成了软件的初步功能需求。
- **技术发展需求**：当前许多软件依赖于简单易用的网页界面，你可以通过调研其他同类矩阵计算工具的不足，确定设计独特的、用户友好的界面和功能特点。

**2.** **需求获取方式**

- **竞品分析**：对比现有的矩阵计算工具， 我们的软件会展示计算过程，能够帮助用户了解计算的过程，协助其巩固和纠错。
- **功能性验证**：在开发原型的过程中，小组之间不断提建议，将产品交给室友去尝试，听取其他人的建议。根据收集到的报错和优化提议，不断调整功能和界面设计。

**3.** **需求定义与整理**

- **功能性需求**：
  - 支持基本矩阵运算，如加法、减法、乘法、求逆等。
  - 用户可以通过表格输入矩阵。
  - 支持大矩阵操作，允许行列扩展和缩减。
  - 显示完整的运算过程，帮助用户理解计算步骤。
- **非功能性需求**：
  - 简洁、直观的界面设计。
  - 结果显示要清晰，支持分数显示。
  - 响应速度快，适合处理较大规模的矩阵。

**4.** **需求文档编写**

- 编写功能需求文档，明确各项功能的输入、输出和计算细节。
- 确定界面需求，细化输入区域、功能栏、结果展示区域的布局。
- 描述用户交互需求，例如按钮操作、矩阵尺寸调整的逻辑。

**5.** **需求评审**

- **与潜在用户确认需求**：将设计与用户进行沟通，收集他们的反馈，调整功能和界面。
- **可行性分析**：对比技术可行性，评估如何实现较复杂的矩阵运算（如求逆、LU分解），确保功能可以在合理的时间内完成。
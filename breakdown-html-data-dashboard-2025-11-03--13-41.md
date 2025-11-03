# 迭代式氛围编程需求文件

**创建时间**：2025-11-03 13:41
**项目名称**：Agentic AI Performance Dashboard - HTML数据看板
**目标受众**：Python/HTML/CSS/JavaScript 初学者
**学习方式**：通过观察AI迭代式生成HTML数据看板的过程来学习编程

---

## 📋 文档说明

本文档将一个完整的数据分析可视化项目分解为 **12个原子化迭代**，每个迭代：
- ✅ **原子化**：不可再拆分，聚焦单一学习目标
- ✅ **独立上线**：可以独立运行并观察效果
- ✅ **循序渐进**：从易到难，从核心到支持性
- ✅ **技术完整**：完成所有迭代后实现业务需求的全部功能

**使用方式**：
1. 按顺序完成每个迭代
2. 每个迭代完成后观察预期成果
3. 理解该迭代引入的技术概念
4. 在理解基础上进入下一个迭代

---

## 🎯 项目概述

### 业务背景

分析 Kaggle 数据集 "Agentic AI Performance Dataset 2025"（80条记录），回答3个业务问题：

1. **问题1**：支持多模态处理的智能体类型占比Top 3是哪些？
2. **问题2**：支持多模态处理的大模型架构占比Top 3是哪些？
3. **问题3**：各任务类型的公正性中位数Top 3是哪些？

### 最终交付物

1. **analyze_data.py** - Python数据分析脚本
2. **data-dashboard.html** - HTML数据看板（214KB，完全自包含）
   - 内嵌 Chart.js 4.4.0 库
   - 3个水平柱状图
   - 温暖橙色系设计
   - 中英双语界面
   - 移动端响应式（最小375px）

---

## 🛠 技术栈总览

本项目使用以下技术（与现有项目代码一致）：

### Python 技术
- **环境管理**：venv 虚拟环境
- **数据处理**：pandas（read_excel, groupby, agg, median）
- **数据导出**：json 模块

### HTML 技术
- **文档结构**：HTML5 语义化标签（header, section, canvas）
- **响应式配置**：viewport meta 标签
- **双语支持**：lang 属性，中英双语标题

### CSS 技术
- **样式管理**：CSS 自定义属性（变量）
- **布局设计**：移动优先响应式设计
- **视觉风格**：温暖橙色系（#FFF5E6, #FF9800, #FF6F00）
- **响应式布局**：media queries（@media min-width: 768px）

### JavaScript 技术
- **图表库**：Chart.js 4.4.0（内嵌完整库）
- **图表类型**：水平柱状图（indexAxis: 'y'）
- **动画效果**：duration: 1500ms, easing: 'easeOutQuart'
- **交互功能**：tooltip 自定义回调
- **数据处理**：Array.map() 方法

---

## 📊 迭代规划总览

项目分为 **4个阶段，共12个迭代**：

| 阶段 | 迭代数 | 核心目标 | 学习重点 |
|------|--------|----------|----------|
| **第一阶段** | 1-2 | 准备与探索 | Python环境、数据理解 |
| **第二阶段** | 3-8 | 首个图表完整实现 | HTML/CSS/JS完整技能栈 |
| **第三阶段** | 9-10 | 后续图表快速复用 | 技术复用、举一反三 |
| **第四阶段** | 11-12 | 整体优化打磨 | 用户体验、国际化 |

**学习策略**：
- 阶段2最详细（首次学习完整流程）
- 阶段3快速复用（体现学习进步）
- 每个迭代都能看到可观察的成果

---

## 第一阶段：准备与探索（迭代1-2）

> **阶段目标**：搭建开发环境，理解数据集结构
> **学习重点**：Python虚拟环境、pandas基础数据探索

---

### 迭代1：虚拟环境准备

#### 🎯 学习目标

通过本迭代，您将学会：
- 理解虚拟环境的作用和必要性
- 掌握使用venv创建Python虚拟环境的方法
- 学会使用pip管理Python包依赖
- 建立项目环境隔离的良好开发习惯

#### 📚 先决知识要求

- 已安装Python 3.x（建议3.8+）
- 了解命令行基本操作（cd、ls等命令）
- 无需任何Python编程经验

#### 📝 业务需求

为Python数据分析项目搭建独立的开发环境，安装必要的依赖包（pandas和openpyxl），确保项目运行环境的隔离性和可复现性。

#### 🔧 技术选型

- **Python venv**：创建隔离的虚拟环境（目录名：venv）
- **pip**：Python包管理工具
- **pandas**：数据分析核心库
- **openpyxl**：Excel文件读取引擎

**为什么选择这些技术**：
- venv是Python官方推荐的虚拟环境工具
- pandas是数据分析的行业标准库
- openpyxl是pandas读取.xlsx文件的依赖

#### ✅ 验收标准

**必须满足以下所有条件才算完成本迭代**：

1. **环境创建验证**：
   - 项目根目录下存在 `venv/` 文件夹
   - 文件夹内包含 `bin/`（Mac/Linux）或 `Scripts/`（Windows）子目录

2. **Python版本验证**：
   - 运行命令：`./venv/bin/python --version`（Mac/Linux）或 `venv\Scripts\python --version`（Windows）
   - 终端输出显示Python版本号，例如：`Python 3.13.5` 或 `Python 3.11.x`

3. **依赖包验证**：
   - 运行命令：`./venv/bin/pip list`
   - 终端输出的包列表中包含：
     - `pandas` (版本2.0+)
     - `openpyxl` (版本3.0+)

4. **环境激活测试**（可选但推荐）：
   - 激活虚拟环境后，命令行提示符前出现 `(venv)` 标记

#### 💡 技术要点

- **虚拟环境**：为每个项目创建独立的Python环境，避免依赖冲突
- **命令**：`python3 -m venv venv` 创建虚拟环境
- **激活**：`source venv/bin/activate`（Mac/Linux）或 `venv\Scripts\activate`（Windows）
- **安装包**：`./venv/bin/pip install pandas openpyxl`

---

### 迭代2：数据探索与理解

#### 🎯 学习目标

通过本迭代，您将学会：
- 使用pandas读取Excel文件的方法
- 掌握DataFrame的基本操作（head, info, describe, value_counts）
- 理解探索性数据分析（EDA）的重要性和方法
- 学会编写Python脚本并通过虚拟环境运行

#### 📚 先决知识要求

- 已完成迭代1（虚拟环境已搭建）
- 项目根目录下有Excel数据文件：`first-80-rows-agentic_ai_performance_dataset_20250622.xlsx`
- 了解基本的数据概念（行、列、数据类型）
- 无需pandas经验，本迭代将从零开始学习

#### 📝 业务需求

读取Excel数据集文件（80条AI智能体性能记录），探索其结构和内容，理解数据列的含义、数据类型、数据分布等关键信息，为后续分析打下基础。

#### 🔧 技术选型

- **pandas.read_excel()**：读取Excel文件（注意：header=1 跳过标题行）
- **DataFrame基本操作**：
  - `df.head()`：查看前几行数据
  - `df.info()`：查看列信息和数据类型
  - `df.describe()`：查看数值列的统计信息
  - `df['column'].value_counts()`：查看分类列的分布

**为什么这样设计**：
- 先理解数据再分析是数据科学的基本流程
- 探索性数据分析（EDA）帮助发现数据特征和潜在问题

#### ✅ 验收标准

**必须满足以下所有条件才算完成本迭代**：

1. **文件创建验证**：
   - 项目根目录下存在 `explore_data.py` 文件
   - 文件包含pandas导入语句和Excel读取代码

2. **脚本运行验证**：
   - 运行命令：`./venv/bin/python explore_data.py`
   - 脚本无报错，成功执行完成

3. **数据读取验证**：
   - 终端输出显示：**总记录数：80行**
   - 终端输出显示：**总列数：26列**

4. **关键列识别验证**：
   - 输出中能看到以下5个关键列的信息：
     - `agent_type`（对象类型）
     - `multimodal_capability`（布尔类型）
     - `model_architecture`（对象类型）
     - `task_category`（对象类型）
     - `bias_detection_score`（浮点类型）

5. **数据分布验证**：
   - 输出显示 `agent_type` 有**16种**不同的类型
   - 输出显示 `multimodal_capability` 中True约有**12个**，False约有**68个**
   - 输出显示 `model_architecture` 有**10种**不同的架构
   - 输出显示 `bias_detection_score` 的数值范围在**0.69-0.83**之间

**示例终端输出**（作为参考）：
```
=== DATASET EXPLORATION ===
Total records: 80
Total columns: 26

Key columns for business questions:
- agent_type: 16 unique types
- multimodal_capability: True(12), False(68)
- model_architecture: 10 unique types
- task_category: 10 unique categories
- bias_detection_score: range 0.69-0.83
```

#### 💡 技术要点

- **header参数**：Excel文件第0行是标题，第1行才是列名，所以用 `header=1`
- **数据类型**：multimodal_capability是布尔型，bias_detection_score是浮点型
- **探索方法**：先整体（info），再细节（value_counts），最后统计（describe）

---

## 第二阶段：首个图表完整实现（迭代3-8）

> **阶段目标**：从零到一实现第一个完整的数据图表
> **学习重点**：HTML/CSS/JavaScript完整技能栈，Chart.js深度学习
> **设计理念**：首个图表实现最详细，建立完整的技术认知

---

### 迭代3：下载并理解Chart.js库

#### 🎯 学习目标

通过本迭代，您将学会：
- 理解前端图表库的作用和选型考虑
- 掌握从CDN下载JavaScript库的方法
- 了解UMD模块格式和文件压缩的概念
- 理解离线可用（无外部依赖）的重要性

#### 📚 先决知识要求

- 已完成迭代1-2（Python环境和数据探索）
- 了解基本的命令行操作（curl或浏览器下载）
- 无需JavaScript经验，本迭代只是下载文件

#### 📝 业务需求

获取专业的图表可视化工具 Chart.js，将其下载到本地，为后续在HTML中内嵌使用做准备。理解Chart.js的基本概念和版本选择。

#### 🔧 技术选型

- **Chart.js 4.4.0**：最新稳定版本的图表库
- **下载源**：jsdelivr CDN（https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js）
- **文件格式**：UMD格式的压缩版（约200KB）

**为什么选择Chart.js**：
- 开源免费，功能强大
- 文档完善，社区活跃
- 支持内嵌（满足"无外部依赖"的需求）
- API设计友好，适合初学者

#### ✅ 验收标准

**必须满足以下所有条件才算完成本迭代**：

1. **文件存在验证**：
   - 项目根目录下存在 `chartjs-4.4.0.js` 文件

2. **文件大小验证**：
   - 运行命令：`ls -lh chartjs-4.4.0.js`
   - 终端显示文件大小约为**200KB**（在190KB-210KB之间均正常）

3. **版本信息验证**：
   - 运行命令：`head -5 chartjs-4.4.0.js`
   - 输出的前几行注释中包含：`Chart.js v4.4.0`

4. **文件完整性验证**：
   - 运行命令：`wc -l chartjs-4.4.0.js`
   - 文件为压缩版，通常只有1-5行（压缩后代码在一行）
   - 文件开头应该是 `/*!` 或类似的注释标记

#### 💡 技术要点

- **CDN vs 本地**：CDN需要网络，本地内嵌实现离线可用
- **UMD格式**：Universal Module Definition，支持多种模块加载方式
- **压缩版（.min.js）**：体积小，但不易读；开发时可用未压缩版学习
- **下载命令**：`curl -o chartjs-4.4.0.js https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js`

---

### 迭代4：创建HTML基础框架

#### 🎯 学习目标

通过本迭代，您将学会：
- HTML5文档的基本结构（DOCTYPE、head、body）
- CSS变量（自定义属性）的定义和使用方法
- 响应式设计的viewport配置
- 语义化HTML标签的使用（header、section）
- 建立统一的配色体系和视觉风格

#### 📚 先决知识要求

- 已完成迭代1-3（环境、数据探索、Chart.js下载）
- 了解基本的HTML概念（标签、属性）
- 了解基本的CSS概念（选择器、属性-值）
- 无需HTML/CSS实战经验，本迭代将从零开始

#### 📝 业务需求

建立数据看板的基本HTML结构和样式体系，包括页面标题、数据概览卡片和统一的温暖橙色系配色方案。此时还不包含图表，仅搭建框架。

#### 🔧 技术选型

**HTML技术**：
- **HTML5文档结构**：`<!DOCTYPE html>`, `<html lang="zh-CN">`
- **meta标签**：charset=UTF-8, viewport（响应式配置）
- **语义化标签**：`<header>`, `<section>`, `<div>`

**CSS技术**：
- **CSS变量（自定义属性）**：`:root { --bg-primary: #FFF5E6; }`
- **温暖橙色系**：
  - 背景色：#FFF5E6（浅杏仁色）
  - 主色：#FF9800（标准橙）
  - 强调色：#FF6F00（深橙）
  - 浅色：#FFE0B2（浅橙边框）
- **基础样式**：box-sizing, 字体栈, 行高

**为什么这样设计**：
- CSS变量便于统一管理配色，后续修改方便
- 语义化标签提升代码可读性和可维护性
- 移动优先的viewport设置保证手机端显示

#### ✅ 验收标准

**必须满足以下所有条件才算完成本迭代**：

1. **文件创建验证**：
   - 项目根目录下存在 `data-dashboard.html` 文件
   - 文件包含完整的HTML5文档结构（DOCTYPE、html、head、body）

2. **浏览器显示验证**：
   - 双击打开HTML文件，浏览器能正常显示页面（无报错）

3. **标题显示验证**：
   - 页面顶部显示主标题：**"Agentic AI Performance Dashboard"**（深橙色，大字）
   - 主标题下方显示副标题：**"AI智能体性能数据看板"**（灰色，小字）

4. **数据概览卡片验证**：
   - 标题下方显示白色卡片
   - 卡片内容：**"Dataset Records | 数据集记录数: 80"**（80是粗体）
   - 卡片有圆角和淡橙色阴影效果

5. **配色方案验证**：
   - 页面整体背景为**浅杏仁色**（#FFF5E6或接近颜色）
   - 主标题颜色为**深橙色**（#FF6F00或接近颜色）
   - 视觉整体温暖、清新

6. **响应式配置验证**：
   - 查看HTML源代码，`<head>`中包含：`<meta name="viewport" content="width=device-width, initial-scale=1.0">`

7. **CSS变量验证**：
   - 查看HTML源代码，`<style>`中包含`:root`块，定义了CSS变量（如`--bg-primary`、`--orange-main`）

#### 💡 技术要点

- **CSS变量语法**：`var(--变量名)` 使用变量，如 `color: var(--orange-main);`
- **响应式viewport**：`width=device-width, initial-scale=1.0` 让页面自适应设备宽度
- **系统字体栈**：优先使用系统字体（-apple-system, BlinkMacSystemFont），加载速度快
- **box-shadow**：`0 2px 8px rgba(255, 152, 0, 0.1)` 创建橙色半透明阴影

---

### 迭代5：Python分析问题1

#### 🎯 学习目标

通过本迭代，您将学会：
- pandas的分组聚合操作（groupby + agg）
- 计算分组内的百分比统计
- 数据排序和Top N提取
- 将分析结果导出为JSON格式

#### 📚 先决知识要求

- 已完成迭代1-4（环境、数据探索、Chart.js、HTML框架）
- 熟悉迭代2中探索的数据结构
- 了解基本的Python语法（变量、函数调用）
- 了解百分比计算的基本概念

#### 📝 业务需求

使用Python分析第一个业务问题：在所有智能体类型中，支持多模态处理的智能体在该类型内的占比，找出占比最高的前三种智能体类型（Top 3）。

**具体要求**：
- 按agent_type分组
- 计算每个类型内multimodal_capability=True的占比
- 按占比从高到低排序，取前3名

#### 🔧 技术选型

- **pandas.groupby()**：按agent_type分组
- **agg()**：聚合函数，同时计算sum和count
- **百分比计算**：`(multimodal_count / total_count) * 100`
- **sort_values()**：按百分比降序排序
- **head(3)**：取前3条记录
- **json.dump()**：将结果导出为JSON格式

**为什么这样分析**：
- 用户关心的是"在该类型内的占比"（WITHIN），不是全局占比
- groupby是pandas处理分组统计的标准方法
- 导出JSON是为了后续嵌入HTML

#### ✅ 验收标准

**必须满足以下所有条件才算完成本迭代**：

1. **文件创建/更新验证**：
   - 项目根目录下存在 `analyze_data.py` 文件
   - 文件包含问题1的分析代码（groupby、agg、百分比计算）

2. **脚本运行验证**：
   - 运行命令：`./venv/bin/python analyze_data.py`
   - 脚本无报错，成功执行完成

3. **终端输出验证**：
   - 输出显示标题：**"QUESTION 1: Top 3 Agent Types by Multimodal Capability %"**
   - 输出显示Top 3结果，排名第1的是：**Research Assistant (60.00%)**
   - 输出显示排名第2的是：**Document Processor (33.33%)**
   - 输出显示排名第3的是：**Sales Assistant (28.57%)**
   - 每个结果包含"Multimodal: X out of Y"的明细信息

4. **JSON文件生成验证**：
   - 项目根目录下生成了 `question1_data.json` 文件
   - 运行命令：`cat question1_data.json | head -10`
   - 文件包含有效的JSON格式数据
   - JSON中包含"top3"键，值为包含3个对象的数组
   - 每个对象包含字段：agent_type, multimodal_count, total_count, multimodal_percentage

5. **数据准确性验证**：
   - Research Assistant的百分比为 **60.0** (3/5)
   - Document Processor的百分比为 **33.33** (2/6)
   - Sales Assistant的百分比为 **28.57** (2/7)

#### 💡 技术要点

- **groupby的聚合**：`df.groupby('agent_type').agg({'multimodal_capability': ['sum', 'count']})`
- **多层列名**：agg后会产生多层列名，需要flatten：`columns = ['agent_type', 'multimodal_count', 'total_count']`
- **布尔值的sum**：True被视为1，False为0，sum就是True的数量
- **JSON可序列化**：使用 `to_dict('records')` 转换DataFrame为字典列表

---

### 迭代6：将数据嵌入HTML并创建基础图表

#### 🎯 学习目标

通过本迭代，您将学会：
- 理解HTML中的`<canvas>`元素及其用途
- 掌握JavaScript数据对象的定义和嵌入方法
- 学会Chart.js的基础配置和初始化
- 理解水平柱状图(indexAxis: 'y')的配置方式
- 掌握从JSON数据到图表渲染的完整流程

#### 📚 先决知识要求

- 已完成迭代1-5（环境、数据探索、Chart.js、HTML框架、Python分析）
- 了解基本的JavaScript语法（对象、数组、函数）
- 了解HTML中`<script>`标签的作用
- question1_data.json文件已生成
- 能够在浏览器中打开HTML文件并查看效果

#### 📝 业务需求

将问题1的分析结果嵌入HTML文件，使用Chart.js创建第一个水平柱状图来可视化Top 3智能体类型的多模态能力占比。此时的图表是基础版本（无动画，简单样式）。

#### 🔧 技术选型

**HTML技术**：
- **`<canvas>` 元素**：Chart.js的渲染目标，`<canvas id="chart1"></canvas>`
- **图表区域结构**：section包装，包含标题和canvas

**JavaScript技术**：
- **数据内嵌**：在`<script>`标签中定义JavaScript对象
- **Chart.js基础配置**：
  - `type: 'bar'`：柱状图
  - `indexAxis: 'y'`：水平方向（横向柱状图）
  - `data.labels`：图表的标签（3个智能体类型名称）
  - `data.datasets[0].data`：图表的数值（3个百分比）
- **响应式配置**：`responsive: true, maintainAspectRatio: false`

**Chart.js内嵌**：
- 将Chart.js库代码插入HTML的`<script>`标签中

**为什么选择水平柱状图**：
- 智能体名称较长（如"Research Assistant"），水平布局更易阅读
- 手机屏幕宽度有限，水平图表更适合移动端

#### ✅ 验收标准

**必须满足以下所有条件才算完成本迭代**：

1. **文件更新验证**：
   - `data-dashboard.html` 文件已更新
   - 文件中包含Chart.js库代码（可通过搜索"Chart.js v4.4.0"确认）
   - 文件中包含question1的数据对象（JavaScript格式）

2. **浏览器显示验证**：
   - 刷新浏览器，页面能正常显示（无JavaScript错误）
   - 页面顶部的标题和数据概览卡片依然存在（迭代4的内容保留）

3. **图表区域验证**：
   - 页面新增图表区域，标题为：**"Question 1: Top 3 Agent Types by Multimodal Capability %"**
   - 图表区域包含一个`<canvas>`元素（id="chart1"）

4. **图表显示验证**：
   - 浏览器显示**水平柱状图**（柱子横向排列）
   - 显示**3根柱子**，对应3个智能体类型
   - Y轴标签（从上到下）：Research Assistant、Document Processor、Sales Assistant
   - 柱子长度正确反映百分比：60%、33.33%、28.57%

5. **基础版本确认**：
   - 柱子颜色为默认灰色或简单颜色（非橙色系）
   - 页面加载时图表直接显示（无增长动画）
   - 鼠标悬停无特殊效果（基础tooltip或无tooltip）

6. **HTML结构验证**：
   - 查看源代码，确认新增了`<section class="chart-section">`
   - section内包含标题和canvas元素
   - JavaScript代码中包含`new Chart(...)`初始化语句

#### 💡 技术要点

- **canvas的尺寸**：通过CSS设置容器高度（如280px），让Chart.js自适应
- **indexAxis**：Chart.js 3.0+的新API，`'y'`表示水平，`'x'`表示垂直
- **数据来源**：从question1_data.json复制数据，硬编码到JavaScript对象中
- **Chart初始化**：
  ```javascript
  const ctx = document.getElementById('chart1').getContext('2d');
  new Chart(ctx, { type: 'bar', data: {...}, options: {...} });
  ```

---

### 迭代7：添加样式（温暖橙色系）

#### 🎯 学习目标

通过本迭代，您将学会：
- 掌握Chart.js的颜色配置方法
- 学会统一配色方案的应用
- 理解图表视觉元素的样式控制
- 掌握CSS阴影和圆角的视觉设计技巧
- 理解半透明颜色(rgba)在视觉设计中的应用

#### 📚 先决知识要求

- 已完成迭代1-6（图表1的基础版本已创建）
- 了解CSS基础（颜色、边框、阴影）
- 了解十六进制颜色代码（如#FF9800）
- 了解rgba()半透明颜色的概念
- 能够修改JavaScript对象的属性值

#### 📝 业务需求

美化图表和页面，将图表配色改为统一的温暖橙色系，增强视觉吸引力和品牌一致性。同时优化图表区域的卡片样式、边框圆角和阴影效果。

#### 🔧 技术选型

**CSS优化**：
- **图表卡片样式**：
  - 白色背景（`--white`）
  - 圆角：`border-radius: 12px`
  - 橙色阴影：`box-shadow: 0 2px 8px rgba(255, 152, 0, 0.1)`
  - 内边距：`padding: 20px`

**Chart.js颜色配置**：
- **柱子背景色**：`backgroundColor: '#FF9800'`（标准橙）
- **柱子边框**：`borderColor: '#FF6F00'`（深橙）
- **柱子圆角**：`borderRadius: 6`
- **网格线颜色**：`grid: { color: 'rgba(255, 152, 0, 0.1)' }`（淡橙色）

**为什么这样设计**：
- 温暖橙色系传达积极、活力的视觉感受
- 浅色背景+深色强调保证可读性
- 半透明阴影和网格线保持视觉层次

#### ✅ 验收标准

**必须满足以下所有条件才算完成本迭代**：

1. **文件更新验证**：
   - `data-dashboard.html` 文件已更新
   - JavaScript代码中chart1的配置包含颜色属性（backgroundColor, borderColor）

2. **柱子颜色验证**：
   - 刷新浏览器，图表1的柱子颜色为**橙色**（#FF9800或视觉上的橙色）
   - 柱子有**深橙色边框**（#FF6F00或更深的橙色）
   - 边框宽度明显可见（约2px）

3. **柱子圆角验证**：
   - 柱子的右侧两个角为**圆角**（不是直角）
   - 圆角半径约6px，视觉上柔和自然

4. **卡片阴影验证**：
   - 图表区域的白色卡片有**淡橙色阴影**效果
   - 阴影颜色为半透明橙色（rgba(255, 152, 0, 0.1)或接近）
   - 阴影位置在卡片下方和右侧

5. **网格线颜色验证**：
   - X轴（水平方向）的网格线为**淡橙色**，不再是默认灰色
   - 网格线颜色与阴影协调统一

6. **整体视觉验证**：
   - 页面配色统一：背景浅杏仁色、柱子橙色、标题深橙色
   - 视觉感受：温暖、清新、专业
   - 与迭代6对比：从"灰色生硬"变为"橙色温暖"

#### 💡 技术要点

- **Chart.js颜色配置位置**：在 `datasets[0]` 对象中设置
  ```javascript
  datasets: [{
    backgroundColor: '#FF9800',
    borderColor: '#FF6F00',
    borderWidth: 2,
    borderRadius: 6
  }]
  ```
- **网格线配置**：在 `options.scales.x.grid` 中设置
- **CSS颜色复用**：使用CSS变量 `var(--orange-main)` 可以保持一致性
- **rgba()半透明**：`rgba(255, 152, 0, 0.1)` 中的0.1是透明度（10%）

---

### 迭代8：添加动画和交互效果

#### 🎯 学习目标

通过本迭代，您将学会：
- 掌握Chart.js动画配置（duration、easing）
- 学会自定义tooltip回调函数
- 理解缓动函数对用户体验的影响
- 掌握JavaScript函数和数组索引的使用
- 理解动画和交互对数据可视化的价值

#### 📚 先决知识要求

- 已完成迭代1-7（图表1已有橙色样式）
- 了解基本的JavaScript函数概念
- 了解动画的基本概念（时长、效果）
- 了解用户交互的重要性
- 能够修改JavaScript对象的嵌套属性

#### 📝 业务需求

增强用户体验，让图表加载时有平滑的增长动画（柱子从0增长到目标值），并且当鼠标悬停在柱子上时显示详细的数据信息（多模态数量、总数量、百分比）。

#### 🔧 技术选型

**Chart.js动画配置**：
- **animation对象**：
  - `duration: 1500`：动画时长1.5秒
  - `easing: 'easeOutQuart'`：缓动函数（先快后慢）
- **动画效果**：柱子从左侧（0%）增长到实际值

**Chart.js tooltip（提示框）配置**：
- **启用tooltip**：`plugins.tooltip.enabled: true`
- **背景色**：`backgroundColor: 'rgba(255, 152, 0, 0.9)'`（橙色半透明）
- **自定义回调**：`callbacks.label` 函数，返回自定义文本
- **显示内容**：
  - 百分比：60.00%
  - 明细：Multimodal: 3 / 5

**为什么添加这些效果**：
- 动画让数据呈现更生动，提升专业感
- Tooltip提供详细信息而不占用页面空间
- 缓动函数让动画更自然（而不是匀速）

#### ✅ 验收标准

**必须满足以下所有条件才算完成本迭代**：

1. **文件更新验证**：
   - `data-dashboard.html` 文件已更新
   - JavaScript代码中chart1的配置包含 `options.animation` 对象
   - JavaScript代码中包含 `plugins.tooltip.callbacks.label` 函数

2. **加载动画验证**：
   - **刷新浏览器**（或按Ctrl+Shift+R强制刷新）
   - 图表的柱子从**0慢慢增长到目标值**
   - 动画持续时间约**1.5秒**
   - 动画效果为**先快后慢**（不是匀速）

3. **悬停tooltip验证**：
   - 鼠标悬停在任意柱子上（如"Research Assistant"）
   - 显示**橙色tooltip框**（背景色为橙色半透明）
   - Tooltip显示**多行信息**：
     - 第1行：标签名称或说明
     - 第2行：**Percentage: 60.00%**（或对应的百分比）
     - 第3行：**Multimodal: 3 / 5**（或对应的明细）

4. **tooltip交互验证**：
   - 鼠标移开柱子时，tooltip消失
   - 鼠标移动到不同柱子时，tooltip显示对应数据
   - Tooltip文字清晰可读（字体大小合适）

5. **动画自然度验证**：
   - 观察动画效果，柱子增长速度不是恒定的
   - 开始时增长较快，接近目标值时减速
   - 整体视觉感受：流畅、自然、专业

#### 💡 技术要点

- **animation配置位置**：在Chart配置的顶层 `options.animation`
- **缓动函数类型**：
  - `linear`：匀速
  - `easeOutQuart`：先快后慢（推荐）
  - `easeInOutQuart`：两头慢中间快
- **tooltip回调函数**：
  ```javascript
  callbacks: {
    label: function(context) {
      const dataIndex = context.dataIndex;
      const item = question1Data.top3[dataIndex];
      return [
        `Percentage: ${item.multimodal_percentage.toFixed(2)}%`,
        `Multimodal: ${item.multimodal_count} / ${item.total_count}`
      ];
    }
  }
  ```
- **数组返回值**：tooltip回调返回数组，每个元素是一行文本

---

## 第三阶段：后续图表快速复用（迭代9-10）

> **阶段目标**：快速实现问题2和问题3，复用已学技术
> **学习重点**：技术迁移能力，举一反三
> **设计理念**：体现学习进步，加速开发节奏

---

### 迭代9：实现问题2（大模型架构多模态占比）

#### 🎯 学习目标

通过本迭代，您将学会：
- 学会技术复用和代码迁移
- 巩固pandas分组分析的技能
- 体会举一反三的学习方法
- 掌握多图表页面的组织方式
- 理解代码模式的抽象和应用

#### 📚 先决知识要求

- 已完成迭代1-8（问题1完整实现）
- 熟悉迭代5-8的技术流程
- 理解问题1和问题2的相似性
- 能够独立修改变量名和数据源
- 了解代码复制粘贴的最佳实践

#### 📝 业务需求

分析第二个业务问题：在所有大模型架构中，支持多模态处理的模型在该架构内的占比，找出占比最高的前三种大模型架构（Top 3），并在HTML看板中添加第二个图表展示结果。

**复用策略**：
- Python分析逻辑与问题1相同（只是分组字段从agent_type改为model_architecture）
- 图表配置与图表1相同（直接复制代码，修改数据源和标题）

#### 🔧 技术选型

**Python技术**（复用迭代5）：
- `df.groupby('model_architecture')`：按大模型架构分组
- 其余分析逻辑完全相同
- 导出 `question2_data.json`

**HTML/CSS技术**（复用迭代4、7）：
- 添加新的 `<section class="chart-section">`
- 包含 `<canvas id="chart2">`

**JavaScript技术**（复用迭代6、8）：
- 复制chart1的完整配置
- 修改：
  - canvas ID：`chart2`
  - 数据源：`question2Data.top3`
  - 标题：Question 2相关

#### ✅ 验收标准

**必须满足以下所有条件才算完成本迭代**：

1. **Python文件更新验证**：
   - `analyze_data.py` 文件已更新，包含问题2的分析代码
   - 运行命令：`./venv/bin/python analyze_data.py`
   - 脚本无报错，成功执行

2. **Python输出验证**：
   - 终端输出包含：**"QUESTION 2: Top 3 Model Architectures by Multimodal Capability %"**
   - 排名第1：**GPT-4o (37.50%)**
   - 排名第2：**CodeT5+ (33.33%)**
   - 排名第3：**Transformer-XL (20.00%)**

3. **JSON文件生成验证**：
   - 项目根目录下生成了 `question2_data.json` 文件
   - JSON中包含"top3"键和3个大模型架构的数据

4. **HTML文件更新验证**：
   - `data-dashboard.html` 文件已更新
   - 文件中包含question2的数据对象
   - 文件中包含chart2的初始化代码

5. **浏览器显示验证**：
   - 刷新浏览器，页面现在显示**2个图表**
   - 图表1（问题1）依然正常显示
   - 新增图表2，标题为：**"Question 2: Top 3 Model Architectures..."**

6. **图表2显示验证**：
   - 图表2显示**3根橙色柱子**（水平布局）
   - Y轴标签：GPT-4o、CodeT5+、Transformer-XL
   - 柱子长度正确：37.50%、33.33%、20.00%
   - 图表2有**增长动画**和**tooltip悬停效果**（与图表1一致）

7. **代码复用验证**：
   - 查看源代码，chart2的配置与chart1高度相似
   - 主要差异：canvas ID、数据源、标题文字

#### 💡 技术要点

- **代码复用**：这是软件开发的核心技能，避免重复造轮子
- **命名规范**：chart1 → chart2, question1 → question2，保持一致性
- **快速验证**：因为逻辑已验证，重点检查数据是否正确映射
- **学习体会**：体会从"学习新技术"到"应用已学技术"的转变

---

### 迭代10：实现问题3（任务类型公正性中位数）

#### 🎯 学习目标

通过本迭代，您将学会：
- 掌握pandas中位数(median)计算方法
- 学会处理不同数据类型的图表展示
- 理解Chart.js轴配置的灵活性
- 体会数据分析中不同统计指标的应用
- 掌握图表配置的微调技巧

#### 📚 先决知识要求

- 已完成迭代1-9（问题1和2已实现）
- 理解中位数与平均数的区别
- 了解问题3的数据类型（0-1的分数，而非百分比）
- 能够调整Chart.js的轴配置参数
- 熟悉迭代5-8的完整流程

#### 📝 业务需求

分析第三个业务问题：各任务类型（task_category）的智能体公正性表现（bias_detection_score）的中位数，找出中位数最高的前三种任务类型（Top 3），并在HTML看板中添加第三个图表展示结果。

**与前两个问题的差异**：
- 不是计算占比（百分比），而是计算中位数（median）
- 数值范围是0-1的分数，不是0-100的百分比
- X轴需要调整：不显示"%"符号，范围是0-1

#### 🔧 技术选型

**Python技术**：
- `df.groupby('task_category')`：按任务类型分组
- `agg({'bias_detection_score': 'median'})`：计算中位数（而非sum/count）
- 导出 `question3_data.json`

**Chart.js配置调整**：
- **X轴范围**：`scales.x.max: 1`（而非100）
- **X轴标签**：去掉 `callback: value => value + '%'`，直接显示数值
- **tooltip内容**：显示"Median Bias Score: 0.821"而非百分比

#### ✅ 验收标准

**必须满足以下所有条件才算完成本迭代**：

1. **Python文件更新验证**：
   - `analyze_data.py` 文件已更新，包含问题3的分析代码（使用median）
   - 运行命令：`./venv/bin/python analyze_data.py`
   - 脚本无报错，成功执行

2. **Python输出验证**：
   - 终端输出包含：**"QUESTION 3: Top 3 Task Categories by Median Bias Detection Score"**
   - 排名第1：**Communication (median: 0.821)**
   - 排名第2：**Research & Summarization (median: 0.785)**
   - 排名第3：**Decision Making (median: 0.782)**

3. **JSON文件生成验证**：
   - 项目根目录下生成了 `question3_data.json` 文件
   - JSON中包含"top3"键和中位数数据

4. **HTML文件更新验证**：
   - `data-dashboard.html` 文件已更新
   - 文件中包含question3的数据对象
   - 文件中包含chart3的初始化代码

5. **浏览器显示验证**：
   - 刷新浏览器，页面现在显示**3个图表**（所有业务问题完成！）
   - 图表1和2依然正常显示
   - 新增图表3，标题为：**"Question 3: Top 3 Task Categories..."**

6. **图表3显示验证**：
   - 图表3显示**3根橙色柱子**（水平布局）
   - Y轴标签：Communication、Research & Summarization、Decision Making
   - 柱子长度正确反映分数：约0.821、0.785、0.782

7. **X轴配置验证**：
   - X轴范围为**0到1**（不是0到100）
   - X轴标签显示：**0.0, 0.2, 0.4, 0.6, 0.8, 1.0**（无百分号"%"）
   - X轴标签为小数格式，不是百分比格式

8. **Tooltip显示验证**：
   - 鼠标悬停在柱子上
   - Tooltip显示："**Median Bias Score: 0.821**"（而非百分比）
   - Tooltip内容准确反映数据类型差异

**重要里程碑**：完成本迭代后，所有3个业务问题的分析和可视化全部完成！

#### 💡 技术要点

- **中位数vs平均数**：median对极端值不敏感，更能反映整体水平
- **Chart.js轴配置灵活性**：通过 `scales.x.max` 和 `ticks.callback` 可以自定义任何显示方式
- **数据类型差异处理**：百分比vs分数，需要在可视化层面做对应调整
- **学习迁移**：虽有差异，但核心流程不变（分析→导出→嵌入→渲染）

---

## 第四阶段：整体优化打磨（迭代11-12）

> **阶段目标**：提升用户体验，优化国际化和移动端显示
> **学习重点**：双语界面设计、响应式布局进阶
> **设计理念**：从"功能完成"到"用户友好"

---

### 迭代11：添加双语支持

#### 🎯 学习目标

通过本迭代，您将学会：
- 理解国际化(i18n)的基本概念
- 掌握HTML双语内容的组织方式
- 学会使用lang属性标记语言
- 理解"标题双语、数据英文"的设计策略
- 掌握CSS实现双语样式差异化

#### 📚 先决知识要求

- 已完成迭代1-10（3个图表已完整实现）
- 了解中英文双语的显示需求
- 了解HTML标签的层级关系
- 了解CSS样式对不同元素的应用
- 能够修改HTML结构和CSS样式

#### 📝 业务需求

为数据看板添加中英双语界面支持，让中文和英文用户都能理解页面内容。采用"标题双语，数据英文"的策略，即标题显示中英文，但数据标签（智能体名称、架构名称等）保持英文原样。

#### 🔧 技术选型

**HTML技术**：
- **lang属性**：`<html lang="zh-CN">` 声明主要语言为中文
- **双语标题结构**：
  - 主标题：`<h3 class="chart-title-en">`（英文，大字）
  - 副标题：`<h4 class="chart-title-cn">`（中文，小字，灰色）

**CSS技术**：
- **标题样式**：
  - 英文标题：`font-size: 1.1rem`, `color: var(--text-dark)`
  - 中文标题：`font-size: 0.95rem`, `color: var(--text-light)`, `font-weight: 400`

**文案对照表**：
| 英文 | 中文 |
|------|------|
| Agentic AI Performance Dashboard | AI智能体性能数据看板 |
| Dataset Records | 数据集记录数 |
| Question 1: Top 3 Agent Types by Multimodal Capability % | 问题1：多模态能力占比最高的前三种智能体类型 |
| Question 2: Top 3 Model Architectures by Multimodal Capability % | 问题2：多模态能力占比最高的前三种大模型架构 |
| Question 3: Top 3 Task Categories by Median Bias Detection Score | 问题3：公正性中位数最高的前三种智能体处理任务 |

**为什么这样设计**：
- 数据标签（如"Research Assistant", "GPT-4o"）是专业术语，保持英文更准确
- 双语标题兼顾可读性（中文）和专业性（英文）
- 视觉层次：英文主标题+中文副标题，清晰不混乱

#### ✅ 验收标准

**必须满足以下所有条件才算完成本迭代**：

1. **HTML文件更新验证**：
   - `data-dashboard.html` 文件已更新
   - 查看源代码，`<html>`标签包含：`lang="zh-CN"`

2. **页面主标题双语验证**：
   - 刷新浏览器，页面顶部显示**两行标题**
   - 第1行（英文，大字，深橙色）：**"Agentic AI Performance Dashboard"**
   - 第2行（中文，小字，灰色）：**"AI智能体性能数据看板"**

3. **数据概览卡片双语验证**：
   - 卡片内容包含：**"Dataset Records | 数据集记录数: 80"**
   - 英文和中文用"|"分隔，数字80为粗体

4. **图表标题双语验证**（检查所有3个图表）：
   - 每个图表都有**两行标题**
   - 第1行：英文标题（大字，深色）
   - 第2行：中文标题（小字，灰色）
   - 图表1中文：**"问题1：多模态能力占比最高的前三种智能体类型"**
   - 图表2中文：**"问题2：多模态能力占比最高的前三种大模型架构"**
   - 图表3中文：**"问题3：公正性中位数最高的前三种智能体处理任务"**

5. **数据标签语言验证**：
   - 图表中的数据标签（Y轴）**保持英文**：
     - "Research Assistant"（不是"研究助手"）
     - "GPT-4o"（保持原样）
     - "Communication"（不是"沟通"）

6. **CSS样式差异验证**：
   - 查看源代码或浏览器检查器
   - 英文标题CSS类：`chart-title-en`（字体大、深色）
   - 中文标题CSS类：`chart-title-cn`（字体小、浅色、font-weight: 400）

7. **整体效果验证**：
   - 中文用户能理解页面内容（有中文标题）
   - 英文用户能理解页面内容（有英文标题）
   - 数据专业术语保持英文（准确性）
   - 视觉层次清晰（英文主、中文辅）

#### 💡 技术要点

- **SEO优化**：`<html lang="zh-CN">` 帮助搜索引擎理解页面语言
- **字体权重**：英文标题用默认粗体，中文副标题用 `font-weight: 400`（正常）
- **颜色层次**：主标题用深色（--text-dark），副标题用浅色（--text-light）
- **国际化思维**：考虑不同文化背景用户的需求

---

### 迭代12：移动端响应式优化

#### 🎯 学习目标

通过本迭代，您将学会：
- 掌握CSS Media Queries的使用方法
- 理解移动优先设计的理念
- 学会使用相对单位(rem)进行响应式布局
- 掌握移动端触摸交互的优化技巧
- 理解响应式设计的最佳实践

#### 📚 先决知识要求

- 已完成迭代1-11（功能已全部实现）
- 了解不同设备的屏幕尺寸差异
- 了解手机浏览器的特点
- 能够在手机上测试HTML页面
- 了解CSS的@media规则

#### 📝 业务需求

确保数据看板在手机浏览器（最小屏幕宽度375px）上能完整、清晰地显示所有内容，无需横向滚动，文字和图表都易于阅读和操作，触摸交互流畅自然。

#### 🔧 技术选型

**CSS响应式技术**：
- **移动优先设计**：基础样式针对手机（375px+）
- **Media Queries**：`@media (min-width: 768px)` 为平板和桌面优化
- **弹性单位**：使用 `rem` 和百分比，避免固定像素

**具体优化点**：

1. **布局优化**：
   - 移动端：垂直堆叠，图表占满屏宽
   - 桌面端：最大宽度1200px，居中显示

2. **字体优化**：
   - 基础字体：`16px`（保证可读性）
   - 标题自适应：`1.8rem`, `1.3rem`（相对单位）

3. **图表高度**：
   - 移动端：`height: 280px`
   - 平板/桌面：`height: 320px`

4. **触摸优化**：
   - `touch-action: pan-y`：允许垂直滚动，防止图表拦截触摸事件
   - Tooltip在触摸屏上点击显示（Chart.js自动支持）

5. **内边距优化**：
   - 移动端：`padding: 20px`（紧凑）
   - 桌面端：`padding: 40px`（宽敞）

**为什么这样设计**：
- 移动端用户占比越来越高，必须优先考虑
- 垂直堆叠避免手机屏幕宽度不足的问题
- 相对单位（rem）随系统字体大小缩放，提升可访问性

#### ✅ 验收标准

**必须满足以下所有条件才算完成本迭代**：

1. **HTML文件更新验证**：
   - `data-dashboard.html` 文件已更新
   - CSS代码中包含 `@media (min-width: 768px)` 等media queries
   - CSS使用rem单位（如 `font-size: 1.8rem`）

2. **手机浏览器测试（375px宽度，如iPhone）**：
   - 在手机浏览器打开HTML文件
   - **无横向滚动条**：左右滑动无效，内容完全可见
   - **3个图表垂直排列**：图表从上到下依次显示
   - **图表占满屏宽**：每个图表宽度接近100%屏宽
   - **文字清晰可读**：16px基础字体，无需缩放即可阅读
   - **柱状图标签完整**："Research Assistant"等长文本不被截断
   - **图表高度适中**：约280px，不过高或过矮

3. **手机触摸交互验证**：
   - 用手指触摸图表柱子，显示tooltip
   - 触摸空白处可以垂直滚动页面
   - Chart.js不会阻止页面滚动

4. **平板测试（768px+宽度，如iPad）**：
   - 在iPad或调整浏览器窗口到768px以上
   - **图表高度增加**：从280px变为320px（更舒适）
   - **内边距增加**：从20px变为40px（更宽敞）
   - **布局依然垂直**：图表仍然垂直排列

5. **桌面浏览器测试（1200px+宽度）**：
   - 在桌面浏览器打开，全屏显示
   - **内容居中显示**：左右有空白margin
   - **最大宽度限制**：内容区域不超过1200px
   - **不过度拉伸**：即使屏幕很宽，内容也不会过分拉伸

6. **CSS代码验证**：
   - 查看源代码，确认使用**移动优先**策略
   - 基础样式针对小屏幕（无media query）
   - `@media (min-width: 768px)` 增强平板和桌面
   - 使用rem相对单位而非px固定单位

7. **最终完整验收**：
   - 在手机、平板、桌面三种设备上都能正常显示 ✅
   - 符合业务需求文件中**验收条件3的所有要求** ✅
   - **所有12个迭代全部完成，项目交付！** 🎉

#### 💡 技术要点

- **移动优先 vs 桌面优先**：
  - 移动优先：先写移动端样式，再用 `@media (min-width: ...)` 增强桌面端
  - 桌面优先：先写桌面端，再用 `@media (max-width: ...)` 简化移动端
  - 推荐移动优先（本项目采用）

- **rem单位**：1rem = 根元素字体大小（通常16px）
  - `1.8rem` = 28.8px（当根字体16px时）
  - 好处：用户调整系统字体时会等比缩放

- **touch-action属性**：
  ```css
  .chart-container {
    touch-action: pan-y;  /* 允许垂直滚动 */
  }
  ```
  防止Chart.js拦截触摸事件导致无法滚动

- **viewport meta的重要性**：
  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  ```
  没有这行，手机会以桌面宽度渲染，然后缩小显示

---

## 🎓 学习路径图

```
准备阶段 (迭代1-2)
    ↓
Python环境 → 数据理解
    ↓
核心实现阶段 (迭代3-8)
    ↓
Chart.js → HTML框架 → Python分析 → 图表渲染 → 样式 → 动画
    ↓
复用加速阶段 (迭代9-10)
    ↓
图表2 → 图表3
    ↓
用户体验阶段 (迭代11-12)
    ↓
双语支持 → 移动端优化
    ↓
✅ 完整的数据看板项目
```

**学习曲线设计**：
- 阶段1：平缓（环境准备）
- 阶段2：陡峭（新技能密集学习）
- 阶段3：加速（复用已学技能）
- 阶段4：平缓（细节打磨）

---

## 📚 技术概念索引

按技术分类列出所有学习要点，方便查阅：

### Python 技能

**环境管理**（迭代1）：
- 虚拟环境创建：`python3 -m venv venv`
- 包管理：`pip install pandas openpyxl`

**数据处理**（迭代2, 5, 9, 10）：
- Excel读取：`pd.read_excel(file, header=1)`
- 数据探索：`head()`, `info()`, `describe()`, `value_counts()`
- 分组聚合：`groupby().agg()`
- 排序：`sort_values()`
- JSON导出：`json.dump()`

**统计计算**（迭代5, 9, 10）：
- 布尔值统计：`sum()`（True视为1）
- 百分比计算：`(count / total) * 100`
- 中位数：`median()`

### HTML 技能

**文档结构**（迭代4）：
- HTML5：`<!DOCTYPE html>`
- 语义化标签：`<header>`, `<section>`, `<canvas>`
- meta配置：charset, viewport

**双语设计**（迭代11）：
- lang属性：`<html lang="zh-CN">`
- 标题层次：`<h3>` 英文 + `<h4>` 中文

### CSS 技能

**样式系统**（迭代4, 7）：
- CSS变量：`:root { --color: #FFF; }`
- 变量使用：`var(--color)`
- 颜色方案：温暖橙色系

**布局设计**（迭代4, 12）：
- 盒模型：`box-sizing: border-box`
- 卡片样式：`border-radius`, `box-shadow`
- 响应式：`@media (min-width: 768px)`

**排版优化**（迭代11, 12）：
- 字体栈：系统字体优先
- 相对单位：`rem`, `%`
- 行高：`line-height: 1.6`

### JavaScript 技能

**基础操作**（迭代6）：
- DOM获取：`document.getElementById()`
- Canvas上下文：`canvas.getContext('2d')`

**数据处理**（迭代6, 9, 10）：
- 数组映射：`Array.map()`
- 对象解构

**Chart.js 配置**（迭代6-10）：
- 图表类型：`type: 'bar'`, `indexAxis: 'y'`
- 数据结构：`labels`, `datasets`
- 响应式：`responsive`, `maintainAspectRatio`
- 轴配置：`scales.x`, `scales.y`
- 颜色：`backgroundColor`, `borderColor`
- 动画：`duration`, `easing`（迭代8）
- Tooltip：`callbacks.label`（迭代8）

### 集成技能

**前后端协作**（迭代5-10）：
- Python生成JSON → JavaScript嵌入HTML
- 数据流：Excel → pandas → JSON → Chart.js

**用户体验**（迭代8, 11, 12）：
- 加载动画：视觉反馈
- 交互提示：tooltip详细信息
- 双语支持：国际化
- 响应式：多设备适配

---

## ✅ 验收条件对照

### 验收条件1：Python脚本功能

**前置条件**：Excel文件准备完毕（80条记录）

**实现迭代**：迭代1, 2, 5, 9, 10

**验收结果**：
- ✅ 成功读取Excel文件的所有80行数据
- ✅ 准确计算出3个业务问题的分析结果
- ✅ 代码在venv虚拟环境中正常执行
- ✅ 无运行错误或异常

### 验收条件2：HTML数据看板

**前置条件**：完成数据分析，获得3个问题的答案

**实现迭代**：迭代3, 4, 6, 7, 8, 9, 10

**验收结果**：
- ✅ HTML文件包含完整的数据可视化看板
- ✅ 使用浅色调设计风格（温暖橙色系）
- ✅ 显示实际处理的数据集记录数（80条）
- ✅ 清晰展示3个业务问题的分析结果和相应图表
- ✅ 所有图表数据已内嵌在HTML中，无需加载外部数据源

### 验收条件3：移动端适配

**前置条件**：HTML文件已生成

**实现迭代**：迭代12

**验收结果**：
- ✅ 页面布局适配手机屏幕（最小375px）
- ✅ 所有图表能够完整显示无需横向滚动
- ✅ 文字清晰可读（16px基础字体）
- ✅ 交互元素在触摸屏上可正常操作（tooltip点击显示）

### 验收条件4：独立运行

**前置条件**：HTML文件包含所有必需元素

**实现迭代**：迭代3（Chart.js内嵌）

**验收结果**：
- ✅ 双击打开HTML文件，无需启动本地服务器
- ✅ 不依赖外部文件、CDN或网络连接
- ✅ 所有样式和脚本已内联在HTML中
- ✅ 图表数据已静态嵌入，可离线查看

---

## 📖 附录：完整文件清单

完成所有12个迭代后，项目将包含以下文件：

```
project-root/
├── venv/                          # Python虚拟环境（迭代1）
│   ├── bin/python
│   └── lib/...
├── first-80-rows-agentic_ai_performance_dataset_20250622.xlsx  # 数据源
├── explore_data.py                # 数据探索脚本（迭代2）
├── analyze_data.py                # 完整分析脚本（迭代5, 9, 10）
├── question1_data.json            # 问题1数据（迭代5）
├── question2_data.json            # 问题2数据（迭代9）
├── question3_data.json            # 问题3数据（迭代10）
├── chartjs-4.4.0.js               # Chart.js库（迭代3）
└── data-dashboard.html            # 最终看板（迭代4-12完善）
    └── [内嵌Chart.js + 数据 + 样式]
```

**最终交付的核心文件**：
1. `analyze_data.py`（约150行）
2. `data-dashboard.html`（约530行，214KB）

---

## 🎯 下一步行动

**准备开始学习？**

1. 确保已安装 Python 3.x
2. 准备好 Excel 数据文件
3. 按照迭代顺序，从迭代1开始
4. 每完成一个迭代，验证预期成果
5. 遇到问题时，参考"技术要点"部分

**学习建议**：
- 不要跳过迭代，每个都有独特的学习价值
- 理解比记忆更重要，思考"为什么这样设计"
- 动手实践，亲自运行代码观察效果
- 尝试修改参数，观察变化，加深理解

**预计学习时长**：
- 有编程基础：8-12小时
- 零基础初学者：15-20小时

---

**祝您学习愉快！通过这12个迭代，您将掌握从数据分析到Web可视化的完整技能链。** 🚀

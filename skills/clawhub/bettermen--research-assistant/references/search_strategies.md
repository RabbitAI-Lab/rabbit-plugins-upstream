# 文献检索策略参考

## 检索框架

### PICO 框架（临床/实验研究）
- **P** (Population/Problem): 研究对象/问题
- **I** (Intervention): 干预措施/处理方法
- **C** (Comparison): 对照/比较
- **O** (Outcome): 结果/结局

### SPIDER 框架（定性/混合方法研究）
- **S** (Sample): 样本
- **P** (Phenomenon of Interest): 关注现象
- **D** (Design): 研究设计
- **E** (Evaluation): 评估
- **R** (Research type): 研究类型

### PICOC 框架（计算机科学）
- **P** (Population): 系统/用户
- **I** (Intervention): 技术/方法
- **C** (Comparison): 基线/对照组
- **O** (Outcome): 性能指标
- **C** (Context): 应用场景

## 主要学术搜索引擎

| 引擎 | 优势 | 适用领域 |
|------|------|---------|
| Semantic Scholar | AI驱动的语义搜索，TL;DR摘要 | 全学科 |
| Google Scholar | 覆盖最广，引用追踪 | 全学科 |
| arXiv | 最新预印本 | CS/Math/Physics |
| PubMed | 生物医学权威 | 生物医学 |
| Web of Science | 核心期刊筛选 | 全学科（经管偏重） |
| IEEE Xplore | 工程/CS | 工程/计算机 |
| Scopus | 文献计量分析 | 全学科 |
| CNKI/知网 | 中文学术资源 | 中文全学科 |

## 检索式构建技巧

### 布尔逻辑
- AND: 缩小范围（machine learning AND drug discovery）
- OR: 扩大范围（deep learning OR neural network）
- NOT: 排除（cancer NOT lung）

### 通配符与截词
- `*`: 截词（comput* → computer/computing/computation）
- `?`: 单字符（wom?n → woman/women）

### 精准匹配
- 引号: "reinforcement learning" 精确短语
- 字段限定: title:, author:, journal:

### 时间范围
- 近3年: 2023-2026
- 经典文献: 不限时间，按引用量排序

## 文献筛选标准

### 纳入标准
1. 发表于同行评审期刊或顶会
2. 与研究问题直接相关
3. 方法论描述完整
4. 数据可获取

### 排除标准
1. 非同行评审（博客/新闻/灰色文献）
2. 重复发表
3. 方法论严重缺陷
4. 数据不可复现

## 引用网络分析

### 种子论文选择
- 领域奠基性文献（最高引用量）
- 最新综述（覆盖全面）
- 争议性论文（引发广泛讨论）

### 扩展策略
- 前向引用：谁引用了这篇→追踪后续发展
- 后向引用：这篇引用了谁→溯源基础理论
- 共被引：两篇被同一篇引用→研究聚类
- 耦合：两篇引用同一批文献→研究相似度

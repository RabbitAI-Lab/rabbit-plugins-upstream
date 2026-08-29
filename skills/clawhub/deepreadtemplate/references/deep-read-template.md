# Literature Deep-Read Report — Template & Extraction Prompts

Copy this scaffold for every paper. Fill each bracket from the paper text; mark inferences with "（推断）" and missing data with "未报告".

## Report Template

```
# [第一作者 et al., 年份] 《[论文标题]》精读报告

## 一句话贡献 (One-line Contribution)
[用一句话说明：用了什么方法，解决了什么未知，得出什么核心结论。]

## 1. 背景 (Background)
- 研究空白：[前人未解决的问题]。
- 研究问题 / 假设：[H1、H2…]。
- 理论/现实动机：[为什么重要]。
（提取提示：读 Introduction 与 General Discussion 的 gap 陈述。）

## 2. 变量 (Variables)
- 自变量 (IV)：[名称]，操作化定义：[如何操纵/测量]。
- 因变量 (DV)：[名称]，操作化定义：[如何测量，单位]。
- 调节/中介：[如有]。
- 控制变量：[人口学、基线等]。
（提取提示：读 Methods 的 Participants / Measures / Design。保留原文术语，括号加中文。）

## 3. 范式方法 (Paradigm / Method)
- 总体范式：[如强化学习 + 漂移扩散模型（RL-DDM）、fMRI、问卷、行为实验]。
- 建模/分析路径：[如 trial-by-trial 更新、参数恢复、模型比较 BIC]。
- 工具：[Python/R、psychoPy、HBayesDM 等，如文中给出]。
（提取提示：读 Methods 的 Computational Modeling / Analysis Plan。）

## 4. 任务流程 (Task Flow)
1. [被试签署知情同意 / 填写基线问卷]。
2. [学习/决策阶段：每 trial 的刺激—反馈—选择]。
3. [关键操纵：如经济困境 vs 控制条件]。
4. [测试/问卷/脑成像阶段]。
5. [ debrief ]。
（提取提示：按时间顺序重排 Methods 的 Procedure；写"被试视角"。）

## 5. 设计细节 (Design Details)
- 设计类型：[被试间/被试内/混合]，因子：[A×B]。
- 样本：[N=__，招募渠道，排除__，power 分析__]。
- 刺激与试次：[试次数、block、平衡/随机化方式]。
- 关键参数：[如学习率 α、损失厌恶 η+、η−、β、温度]。
（提取提示：Methods 的 Participants、Stimuli、Procedure、Parameters。）

## 6. 统计分析 (Statistical Analysis)
- 主要检验：[如 mixed-effects model、ANOVA、t-test、贝叶斯因子]。
- 模型比较：[如 DDM 参数贝叶斯估计、BIC/AIC、留一法]。
- 校正：[多重比较、FDR、先验设定]。
- 每个检验回答的问题：[检验 → 对应假设]。
（提取提示：Analysis / Results 的统计段落；抄写精确统计量。）

## 7. 主要结果 (Main Results)
- 结果 1：[估计/效应量，95% CI，p=__，对应假设]。
- 结果 2：[…]。
- 调节/脑相关：[如有]。
- 解释：[结果如何支持/反驳假设]。
（提取提示：Results + Discussion；务必抄原文数字，标注章节/页码。）

## 局限与可复现性 (Limitations & Reproducibility)
- 局限：[样本代表性、因果方向、测量误差等]。
- 可复现：[是否公开数据/代码，OSF/ preprint 链接]。
```

## Worked Example (skeleton — fill with the real paper at run time)

Paper: 一篇使用 RL-DDM 研究"经济困境下晚期青少年损失敏感性"的计算建模论文。
- 一句话贡献：用强化学习 + 漂移扩散模型证明经济困难背景会显著提升晚期青少年的损失敏感性参数。
- 背景：经济困境与风险决策的关系尚缺计算层面的机制证据。
- 变量：IV=经济困境条件；DV=损失厌恶参数 η−、学习率 α、决策阈值 β（DDM）。
- 范式方法：trial-by-trial RL 更新 + DDM 参数贝叶斯估计 + 模型比较。
- 任务流程：基线问卷 → 赌博/决策任务（带反馈）→ 参数估计 → 组间比较。
- 设计细节：被试间（困境 vs 控制），N=__，试次=__，平衡=__。
- 统计分析：组间 t-test / 混合模型 + 参数恢复检验 + BIC 模型比较。
- 主要结果：困境组 η− 显著更高（p=__），α/β 无差异（填真实值）。
- 局限：横断面、样本地域局限；代码/数据是否公开见文末。

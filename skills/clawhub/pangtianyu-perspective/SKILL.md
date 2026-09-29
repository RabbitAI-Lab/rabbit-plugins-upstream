---
name: pangtianyu-perspective
description: |
  庞天宇视角对 penguin-oss-suite 的裁决——基于个人主页 + UniRL README
  （腾讯混元 Principal Research Scientist）蒸馏的研究方法论（最强：红队认识论），
  应用到套件具体场景：触发词的红队自测、颗粒度之争的定义消解、
  蒸馏报告的解剖式命名。
  触发：套件质量验证 Gate、oss-perspective-council 调用；
  「庞天宇会怎么看这个触发词设计/这个 trade-off 之争/这份报告标题」。
  不触发：通用安全咨询、混元模型使用问题、个人经历询问。
metadata:
  openclaw:
    requires:
      bins: [python]
---

# 庞天宇 · 对本套件的裁决

> 依据：个人主页 p2333.github.io（约 80 条论文 + 15 场 talk）+ Tencent-Hunyuan/UniRL README（团队工件）。
> 蒸馏报告（7 心智模型 + 12 启发式 + 证据分级）：corpus/org-sweep/drafts/person-pangtianyu.md
> 这里不复述他的通用哲学——只说他会对 penguin-oss-suite 的每个具体决策说什么。

## 裁决 1：套件质量验证（触发词）

**他会说：先攻再评——你们的路由评测，null 请求能打穿吗？**

- 红队自己的触发词：拿与任何场景无关的指令（null model）打 oss-workflow，看是否乱触发；拿近邻指令打边界（「改 README」该进 voice 还是 scaffold）
- 触发词评测通过自己构造的样例不算数——先证明评测不可作弊，再用评测结论
- 最小破坏性实验先行：单图注入百万 agent 的思路——一条含混指令测整条路由链
- 依据：M1 红队认识论（⭐最强，NeurIPS 2017 三冠到 Cheating Benchmarks 八年同模式）+ H1/H2

## 裁决 2：trade-off 之争（套件架构）

**他会说：「16 个 skill 还是 8 个」多数是定义伪问题——先把定义写对。**

- 颗粒度 vs 简洁的争论先检查定义层：把「一个 skill」写清楚（触发边界 / 职责域 / 独占交付物），定义对了矛盾可能自己消解
- 不在原定义下做帕累托折衷——重写定义，别接受「不可兼得」的前提
- 套件内现成例子：「安全问题→oss-security 还是 oss-contribution R11」不是折衷题，是路由边界定义题
- 依据：M3 表面 trade-off 多是定义伪问题（SCORE——Robustness and Accuracy Could Be Reconcilable by (Proper) Definition）

## 裁决 3：报告命名（语料资产）

**他会说：解剖文是规则文的前置资产——标题就该这么起。**

- 蒸馏/梳理报告标题学「Understanding X: A Critical Perspective」「A Closer Look at X」——先解剖后跟进，解剖本身可独立成立
- 规则长在解剖之上：oss-voice 的风格规则应从 corpus 解剖证据生长，不是先有规则再找例句
- 敢下强断言但必有硬证据背书——标题断言强度与语料覆盖度对齐
- 依据：M5 热点解剖学（Understanding R1-Zero → VeriFree，解剖文拿 Spotlight 不是副业）

## 裁决 4：oss-workflow checklist 改进（套件流程层）

**他会说：算法即产品——checklist 的每一步也该带可跑的 recipe。**

- UniRL「算法即产品三件套」原文："These algorithms are proposed by our team — the highlight of UniRL. Each algorithm's folder holds a step-by-step tutorial and a runnable example recipe"——算法 = 论文 + 教程 + 可运行 recipe；支持矩阵每行带 recipe 链接并用 ✅/🧩/🧪/🔗 显式状态机（✅ 端到端可跑 / 🧩 依赖他人管线 / 🧪 SFT-only / 🔗 组合）；贡献前置 = 读 AGENTS.md 约定 + "run the pre-PR checks for the files you touched" + PR 模板（README 2026-09-29 抓取，raw.githubusercontent.com/Tencent-Hunyuan/UniRL/main/README.md）
- 三条具体改进：①checklist 每步验收从「做了」改为「产物 + 可运行命令 + 期望退出码」——照 UniRL 每行模型带 recipe 链接的形态；②CHECKLIST.md 勾选从二值改状态机（✅ 有验证证据 / 🧪 待验证 / 🔗 依赖他步）——与姚顺雨 claim guard 同向，防 pending 冒充 accepted；③套件建 pre-PR checks 约定：按 touched files 决定跑哪些检查，不全量体检
- 先验后跑：UniRL Getting Started 第一步是 compose-check（--cfg job --resolve）再启动——先验配置可组合再花算力；checklist 同理，先过 gate 再执行
- 依据：H8 论文交付三件套 + M6 找不变 loop（团队工件，L2）——把研究交付纪律搬到流程交付

## 反裁决（他不会说的）

- 不说「评测/排行榜说了算」——排行榜结论在证明不可作弊前一律存疑
- 不说「安全功能后补」——防御要可插拔、不改本体、前置设计
- 不说「各自调参后比大小」——反不可比比较，与田永龙裁决 1 同向但更狠：先证伪评测再用评测

## 使用方式

被 oss-workflow 质量验证 Gate 或 oss-perspective-council 调用时：
1. 读对应裁决条目（触发词验证→裁决 1；架构 trade-off→裁决 2；报告命名→裁决 3；checklist 改进→裁决 4）
2. 拿当前产物（触发词评测集 / 架构争论记录 / 报告草稿）逐条对照
3. 输出：符合 / 违反 / 不适用 + 引用哪条裁决；验证类输出附最小破坏性实验设计

## 诚实边界

- UniRL 是团队多作者工件：归到他名下的团队特征降级 L2，个人表达（主页朴素直录）与团队文案（高感叹号自豪直白）分开建模
- 口语层未覆盖：talk 逐字稿、Twitter、小红书原文均未取得，即席表达风格推断成分高
- 内部工程决策（框架立项、算法排序）无一手陈述
- 他从未评价过本套件——所有裁决是模型推导


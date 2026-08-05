# JD QuickLearn

> 把一份陌生岗位 JD，转化为零基础也能读懂的岗位学习指南。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Codex Skill](https://img.shields.io/badge/Codex-Skill-3157D5)

`jd-quicklearn` 是一个面向求职准备的 Codex Skill。用户提供 JD 文件、JD 文本或明确岗位名称后，它会解析岗位职责与任职要求，研究公司、部门、业务和行业背景，建立岗位知识体系，并给出有优先级的学习路径。

它专注于“理解岗位和补齐知识”，不生成或收集面试题库、历史真题、预测题或答题框架。

## 能做什么

- 解析公司与团队介绍、岗位职责和任职要求
- 识别岗位级别、协作对象、业务阶段和考核方式等隐含信息
- 将 JD 术语翻译成新人可理解的实际工作内容
- 核验公司、产品、团队与行业的最新公开信息
- 拆解岗位所需的硬技能、分析方法和软技能
- 根据可用时间生成优先级明确的学习路径

## 输入示例

可以直接粘贴 JD，也可以提供 `.docx`、Markdown 或纯文本文件。

<p align="center">
  <img src="assets/input-example.png" alt="JD QuickLearn 输入示例" width="820">
</p>

## 默认输出

报告固定包含五部分：

1. **岗位基础介绍**：岗位解决的问题、价值链位置、常见产出及相邻岗位区别
2. **公司、部门及业务背景**：公司与产品背景、团队目标、行业现状和竞争格局
3. **核心知识体系**：关键框架、模型、术语及其关联
4. **技能拆解**：硬技能、分析方法、软技能、重要程度和对应 JD 条目
5. **学习路径**：按时间安排学习顺序、资料方向和阶段目标

需要文件交付时，默认生成：

```text
{岗位名称}完整学习指南.md
```

### 完整输出示例

<img src="assets/output-example.png" alt="JD QuickLearn 完整输出示例">

## 使用方式

将仓库放入 Codex Skills 目录：

```text
~/.codex/skills/jd-quicklearn/
├── SKILL.md
├── README.md
├── LICENSE
└── assets/
```

然后在 Codex 中提供 JD，例如：

```text
使用 jd-quicklearn 分析这份 JD，帮我从零理解岗位、部门业务、核心知识和需要补齐的技能。
```

也可以直接说：

```text
我对用户增长产品经理完全不了解，请根据这份 JD 生成学习指南。
```

## 信息质量

- 关键知识和技能必须对应到具体 JD 条目
- 最新业务事实优先使用可靠公开来源，并注明日期
- 区分公开事实、合理推断和信息缺口
- 无法核验的内部组织信息明确标注为“公开信息不足”
- 不编造业务数据、部门情况或岗位要求

## License

[MIT License](LICENSE) © 2026 yangming1768-alt

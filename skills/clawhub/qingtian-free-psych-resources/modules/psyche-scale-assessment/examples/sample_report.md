# 测评报告示例（HTML）

本技能的测评报告现以**自包含 HTML** 形式生成：CSS 内联，浏览器双击即开，无需任何外部依赖，也不再使用 Markdown。

## 报告结构

- 渐变头部：量表名称、简介、适用人群、预计用时
- 🆘 紧急求助资源（危机题触发时**严格前置**于任何分数）
- 缺失题提示（若有漏答）
- 一、得分概览（维度 / 原始分 / 标准分 / 分级彩色徽章）
- 分数可视化（CSS 进度条）
- 二、结果解读（按分级给出释义）
- 三、行动建议（立即行动 / 日常调节 / 何时就医）
- 四、重要声明（不诊断、来源与授权）

## 如何生成一份示例

```bash
python scripts/scoring_engine.py PHQ-9 answers.json    # 仅计分
python scripts/report_generator.py PHQ-9 answers.json  # 计分 + 保存 HTML 到 reports/
```

或在技能对话中触发：说「启动」→ 选择量表 → 逐题作答 → 自动生成并打开 HTML 报告。

> 实际生成的示例见 `reports/` 目录下 `*.html` 文件（每份报告以 `量表id_report_时间戳.html` 命名）。

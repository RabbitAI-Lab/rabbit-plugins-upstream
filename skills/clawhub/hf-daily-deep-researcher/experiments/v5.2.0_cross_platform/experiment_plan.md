# v5.2.0 跨平台兼容性对比实验方案

**实验日期**: 2026-07-29
**实验目的**: 验证 `web_fetch` 降级方案（非 Kimi 平台）与 `kimi_search` 完整方案（Kimi 平台）在全链路质量上的差异
**Skill 版本**: hf-daily-deep-researcher v5.2.0

---

## 1. 实验设计

### 1.1 对照组 vs 实验组

| 维度 | 方案 A（对照组） | 方案 B（实验组） |
|------|-----------------|-----------------|
| **名称** | 完整方案 | 降级方案 |
| **搜索工具** | `kimi_search` 主力 + `web_fetch` 补充 | `web_fetch` 唯一 |
| **精读工具** | `kimi_fetch` 主力 | `web_fetch` 唯一 |
| **模拟环境** | Kimi / OpenClaw | 开源 OpenClaw / Claude Code |
| **核心理念** | 语义搜索 + 精准获取 | API 搜索 + 标准获取 |

### 1.2 控制变量

| 变量 | 固定值 | 说明 |
|------|--------|------|
| 研究方向 | Credit Assignment | config.json 中已配置 |
| 关键词集合 | 相同 | multi-agent credit assignment, hindsight credit, stepwise reward, turn-level advantage, hierarchical credit, credit decomposition, advantage estimation, process reward model |
| 时间窗口 | 2026-07-22 至 2026-07-29（过去7天） | 固定，确保两方案搜索同一批论文 |
| 工作模式 | 轻量扫描（Light Scan） | ≤30天，自动判断 |
| 精读策略 | 最多精读 3 篇 P0 | 相同 |
| 报告模板 | `templates/report_template.md` | 相同 |

### 1.3 评价指标

#### Phase 1 — 搜索质量（权重 40%）

| 指标 | 计算方法 | 目标 |
|------|---------|------|
| 论文总数 | 去重后的论文数量 | ≥20 篇 |
| P0 数量 | priority ≥ 0.8 | ≥1 篇 |
| P1 数量 | 0.6 ≤ priority < 0.8 | ≥3 篇 |
| 覆盖率 | 与另一方案找到的论文交集比例 | 交集 ≥ 60% |
| 遗漏率 | 对方案找到但本方案遗漏的重要论文数 | ≤2 篇 |
| 搜索耗时 | 从第一组查询到最后输出的时间 | 记录 |

#### Phase 2 — 精读质量（权重 35%）

| 指标 | 计算方法 | 目标 |
|------|---------|------|
| ar5iv 获取成功率 | 成功获取全文的论文数 / 尝试获取数 | 100% |
| 分析报告字数 | 每篇精读报告的字数 | ≥800 字 |
| 关键信息完整度 | 是否包含：动机、方法、实验、批判分析 | 4/4 |
| 数据准确性 | 实验数据是否与论文原文一致 | 0 错误 |

#### Phase 3 — 报告质量（权重 25%）

| 指标 | 计算方法 | 目标 |
|------|---------|------|
| 报告总字数 | 最终报告字数 | ≥3000 字 |
| 结构完整度 | 是否包含：执行摘要、论文列表、趋势分析、下周重点 | 4/4 |
| 信息密度 | 每篇论文的平均分析深度 | 有实质性分析 |
| 格式规范性 | Markdown 格式、表格、链接是否正确 | 无格式错误 |

---

## 2. 执行流程

### 2.1 准备工作

```bash
# 创建实验目录
mkdir -p experiments/v5.2.0_cross_platform/{plan_a,plan_b}

# 备份当前配置
cp config.json experiments/v5.2.0_cross_platform/config_backup.json
```

### 2.2 方案 A 执行（完整方案）

1. 主 Agent 直接调用 `kimi_search` 执行搜索
2. 并行 Deep Readers 使用 `kimi_fetch` 获取论文
3. 正常执行 Analyst → Writer → Checker
4. 保存所有中间文件和最终报告到 `plan_a/`

### 2.3 方案 B 执行（降级方案）

1. **禁用 kimi_search**：主 Agent 不调用 `kimi_search`，只调用 `web_fetch`
2. **禁用 kimi_fetch**：Deep Reader 不调用 `kimi_fetch`，只调用 `web_fetch`
3. 其余流程与方案 A 完全一致
4. 保存所有中间文件和最终报告到 `plan_b/`

### 2.4 对比分析

1. 读取两方案的中间文件（papers_raw.json, paper_analysis_*.md）
2. 计算上述评价指标
3. 输出对比报告

---

## 3. 预期结果

### 3.1 搜索阶段预期

| 场景 | 预期结果 |
|------|---------|
| 理想情况 | 两方案找到高度重叠的论文集，覆盖率 ≥ 80% |
| 可接受 | kimi_search 找到更多边缘论文，web_fetch 覆盖核心论文 |
| 需要修复 | web_fetch 遗漏大量重要论文，或获取的论文质量明显更低 |

### 3.2 精读阶段预期

| 场景 | 预期结果 |
|------|---------|
| 理想情况 | kimi_fetch 和 web_fetch 获取的 ar5iv HTML 内容完全一致 |
| 可接受 | web_fetch 获取的 HTML 需要更多解析工作，但内容完整 |
| 需要修复 | web_fetch 无法获取完整 HTML，或内容有截断/乱码 |

### 3.3 报告阶段预期

| 场景 | 预期结果 |
|------|---------|
| 理想情况 | 两方案报告质量相当，差异在可接受范围内 |
| 可接受 | 方案 B 报告信息密度略低，但结构完整 |
| 需要修复 | 方案 B 报告质量显著低于方案 A |

---

## 4. 判定标准

### 实验通过（Skill 跨平台可用）

所有以下指标必须满足：
- [ ] 方案 B 论文总数 ≥ 方案 A 的 70%
- [ ] 方案 B P0 + P1 论文数 ≥ 方案 A 的 60%
- [ ] 两方案 P0 论文交集 ≥ 50%（至少一半的核心论文被双方找到）
- [ ] 方案 B ar5iv 获取成功率 = 100%
- [ ] 方案 B 报告结构完整度 = 4/4

### 实验不通过（需要继续优化降级方案）

任一指标不满足，则需要：
1. 分析具体失败原因
2. 优化 web_fetch 搜索策略（增加查询组数、改进关键词组合）
3. 优化 arXiv API 解析逻辑
4. 重新测试

---

## 5. 风险与应对

| 风险 | 可能性 | 应对 |
|------|--------|------|
| 过去7天论文太少（假期等） | 中 | 延长到10天或选择固定日期范围 |
| arXiv API 返回 XML 解析失败 | 低 | web_fetch 返回的是原始文本，手动提取关键字段 |
| 单篇论文精读超时 | 中 | 控制超时为15分钟，超时后标记为"部分完成" |
| 两方案找到完全不同的论文集 | 低 | 扩展关键词范围，增加搜索组数 |

---

## 6. 输出物

1. `experiments/v5.2.0_cross_platform/experiment_plan.md` — 本文件
2. `experiments/v5.2.0_cross_platform/plan_a/` — 方案 A 所有中间文件和报告
3. `experiments/v5.2.0_cross_platform/plan_b/` — 方案 B 所有中间文件和报告
4. `experiments/v5.2.0_cross_platform/comparison_report.md` — 对比分析报告

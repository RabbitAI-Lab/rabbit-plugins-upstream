---
name: tdd
version: 2.1.0
description: "Apply test-driven development with Red-Green-Refactor cycle and vertical slice tracer bullet method"
tags: [coding, general, iterative, template-based, api-integration]
metadata:
  author: yindb2 (adapted from community skill)
  category: coding
  triggers:
    - TDD
    - 测试驱动
    - red-green-refactor
    - 测试优先
    - 单元测试
    - 集成测试
    - 写测�?    - 覆盖�?  dependencies:
    - coding-framework (>=10.0.0) �?安全守卫、代理审�?  integration:
    - daily-agent 调度入口，匹�?测试/覆盖�?类任�?    - coding-framework 模式2（代理审查）�?test-engineer 代理调用本技�?    - iterative-loop (>=1.0.0) 配合进行迭代式测试修�?    - diagnose (>=2.1.0) 在修复阶段调用本技能构建回归测�?---

# TDD �?测试驱动开�?
Red-Green-Refactor循环，采用垂直切片（tracer bullet）方法，避免水平切片的常见陷阱�?
---

## 核心警告：避�?垃圾测试"

以下做法会产�?*垃圾测试**�?- 批量写测试测�?*想象�?*行为，而非**实际�?*行为
- 测试数据结构�?*形状**而非用户可见的行�?- 测试对真实变更不敏感——行为坏了测试还过，行为好了测试还挂
-  outrun your headlights——在理解实现之前就承诺了测试结构

**正确方法**：垂直切片，tracer bullet。一个测�?�?一个实�?�?重复。每个测试响应上一个循环学到的东西。因为你刚写了代码，你知道什么行为重要、怎么验证�?
```
错误（水平切片）�?  RED:   test1, test2, test3, test4, test5
  GREEN: impl1, impl2, impl3, impl4, impl5

正确（垂直切片）�?  RED→GREEN: test1→impl1
  RED→GREEN: test2→impl2
  RED→GREEN: test3→impl3
  ...
```

---

## 工作�?
### 1. 规划

探索代码库时，使用项目的领域术语，让测试名和接口词汇匹配项目语言，尊重相关ADR�?
写任何代码之前：
- [ ] 与用户确认需要什么接口变�?- [ ] 与用户确认哪些行为需要测试（排优先级�?- [ ] 识别深模块机会（小接口、深实现�?- [ ] 为可测试性设计接�?- [ ] 列出要测试的行为（不是实现步骤）
- [ ] 获得用户对计划的认可

**�?*�?公共接口应该长什么样？哪些行为最重要需要测试？"

**你不能测试所有东西�?* 与用户确认哪些行为最重要。把测试精力集中在关键路径和复杂逻辑上，不是每个可能的边界情况�?
### 2. Tracer Bullet

�?*一�?*测试确认系统�?*一件事**�?```
RED:   写第一个行为的测试 �?测试失败
GREEN: 写最小代码让它通过 �?测试通过
```

这是你的tracer bullet——证明路径端到端通了�?
### 3. 增量循环

对每个剩余行为：
```
RED:   写下一个测�?�?失败
GREEN: 最小代码让它通过 �?通过
```

规则�?- 一次一个测�?- 只写够通过当前测试的代�?- 不要预判未来的测�?- 测试聚焦于可观测行为

### 4. 重构

所有测试通过后，寻找重构机会�?- [ ] 提取重复代码
- [ ] 深化模块（把复杂性移到简单接口后面）
- [ ] 自然应用SOLID原则
- [ ] 考虑新代码揭示了旧代码的什么信�?- [ ] 每次重构后运行测�?
**永远不要在RED状态重构�?* 先回到GREEN�?
---

## 每个循环的检查清�?
```
[ ] 测试描述行为，不是实�?[ ] 测试只使用公共接�?[ ] 测试能在内部重构后存�?[ ] 代码对当前测试来说是最小的
[ ] 没有添加投机性功�?```

---

## 测试分层策略

### 测试金字�?
```
        /  E2E  \          �?少量：关键用户路�?       /--------\
      / 集成测试  \        �?中量：模块间交互
     /------------\
    /   单元测试    \      �?大量：纯函数/纯逻辑
   /----------------\
```

### 各层职责

| 层级 | 测试什�?| 速度 | 数量 |
|------|---------|------|------|
| 单元 | 纯函数、算法、数据转�?| 毫秒�?| �?|
| 集成 | 模块间交互、API调用、数据库操作 | 秒级 | �?|
| E2E | 关键用户路径、业务流�?| 分钟�?| �?|

### 测试选择原则

1. **优先测试行为**，不是实现细�?2. **优先测试关键路径**，不是边角情�?3. **优先测试复杂逻辑**，不是简单映�?4. **测试成本与风险成正比** �?出bug代价高的地方多测

---

## 常见测试模式

### Mock vs 不Mock

**应该Mock**�?- 外部服务调用（HTTP、数据库�?- 时间依赖（`Date.now()`�?- 随机数生�?- 文件系统操作（在单元测试中）

**不应该Mock**�?- 被测模块内部的纯函数
- 值对�?数据结构
- 测试中不需要隔离的协作�?
### 测试数据管理

**原则**�?- 每个测试自带数据，不依赖其他测试的状�?- 使用factory/builder模式创建测试数据
- 测试数据要有意义的命名（`userWithNameAlice` 而非 `testData1`�?
### 断言最佳实�?
```
# 好：断言具体行为
assert result.status == "success"
assert result.items.length == 3
assert result.items[0].name == "expected"

# 差：断言形状
assert result != null
assert typeof result === "object"
```

---

## 语言特定指南

### JavaScript / TypeScript
- 测试框架：Jest / Vitest
- 断言库：内置expect / chai
- Mock：jest.mock() / vi.mock()
- 覆盖率：`--coverage` 标志

### Python
- 测试框架：pytest
- 断言：内置assert
- Mock：unittest.mock
- 覆盖率：pytest-cov

### Go
- 测试框架：内置testing
- 断言：testify（第三方�?- 表驱动测试：Go的标准模�?- 覆盖率：`go test -cover`

---

## 测试覆盖率检�?
### 覆盖率目标（按层级）

| 层级 | 最低覆盖率 | 推荐覆盖�?| 说明 |
|------|------------|------------|------|
| 单元测试 | 80% | 90%+ | 纯函�?算法必须高覆�?|
| 集成测试 | 60% | 75%+ | 关键路径覆盖 |
| E2E 测试 | 关键路径100% | - | 只覆盖核心用户路�?|

### 覆盖率检查流�?
```
1. 运行测试 + 覆盖率收�?   - JS/TS: npx vitest --coverage / npx jest --coverage
   - Python: pytest --cov=src --cov-report=term-missing
   - Go: go test -coverprofile=coverage.out && go tool cover -func=coverage.out

2. 检查未覆盖�?   - 识别 uncovered lines
   - 判断是否是关键路径（关键路径必须覆盖�?   - 非关键路径可标记�?acceptable gap

3. 补充测试
   - 对关键路径的 uncovered lines 补充测试
   - 使用 tracer-bullet 方法：一�?uncovered 分支 �?一个测�?```

### 覆盖率降级策�?
| 场景 | 降级方案 |
|------|----------|
| 覆盖率工具不可用 | 手动检查：列出所有分支，确认每个分支有对应测�?|
| 覆盖率低于目�?| 列出 uncovered 关键路径，优先补�?|
| 遗留代码无法测试 | 记录为技术债务，标记需要重构的接缝 |

---

## 错误处理与降级策�?
### 测试构建失败

| 场景 | 降级方案 |
|------|----------|
| 无法 Mock 外部依赖 | 使用集成测试替代单元测试，在真实环境中验�?|
| 测试框架不兼�?| 退回到语言内置�?assert + 脚本驱动 |
| 测试执行太慢 | 缩小测试范围，只运行相关测试文件 |

### Red-Green 循环卡住

| 场景 | 降级方案 |
|------|----------|
| RED 后无�?GREEN | 回退到上一�?GREEN 状态，重新分析 |
| GREEN 后测试仍失败 | 检查是否有测试间状态泄�?|
| 重构后测试失�?| 回退重构，先确保 GREEN，再小步重构 |

---

## �?iterative-loop 集成

### 迭代式测试修�?
当测试失败数量较多时，使�?iterative-loop 管理修复循环�?
```
iterative-loop init --mode max --max 20 --condition "regex:All tests passed"
  �?每轮迭代�?  1. 运行测试，获取失败列�?  2. 选择最高优先级的失�?  3. 使用 tracer-bullet 方法修复
  4. 运行测试验证
  �?iterative-loop update --result pass/fail
  �?满足完成条件 �?iterative-loop complete
```

### 覆盖率迭代提�?
```
iterative-loop init --mode adaptive --max 10 --patience 3
  --condition "regex:coverage.*90%"
  �?每轮迭代�?  1. 运行覆盖率检�?  2. 识别最�?uncovered 分支
  3. 补充测试
  4. 重新检查覆盖率
  �?连续3轮改�?< 阈�?�?停止
```

---

## �?coding-framework 集成

### 调度入口

tdd 作为 daily-agent 的独立子技能，当任务分类为"测试/覆盖�?时自动加载�?
### 与代理审查配�?
coding-framework 模式2（代理审查）中的 test-engineer 代理使用本技能的方法论：
- 评估测试覆盖�?- 检查测试质�?- 生成测试用例建议

### 与安全守卫配�?
运行测试命令时，coding-framework 模式4（安全守卫）自动生效�?
---

## 相关参�?
- `references/tdd-patterns.md` �?TDD高级模式与重构技�?- `references/testing-anti-patterns.md` �?测试反模式与避坑指南

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v2.1.0 | 2026-06-29 | 增加覆盖率检查流程、iterative-loop 集成、错误处理与降级策略 |
| v2.0.0 | 2026-06-20 | 从mp-tdd重组织，补充references和分层策略，适配daily-agent v2.0 |
| v1.0.0 | 社区版本 | Red-Green-Refactor原始方法 |

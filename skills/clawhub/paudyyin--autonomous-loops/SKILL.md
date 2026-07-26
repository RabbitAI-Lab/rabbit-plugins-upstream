---
name: autonomous-loops
description: "Run autonomous execution loops with de-sloppify cleanup and complexity-tiered pipelines. Use when implementing self-directed task execution with automatic code quality cleanup."
metadata:
  origin: ECC autonomous-loops (partial: De-Sloppify + Complexity Tiers)
---

# Autonomous Loops �?自主循环模式

自主编码循环的模式和架构。聚焦两个核心模式：**De-Sloppify 清理**�?*复杂度分�?*�?
## 触发条件

- 执行迭代编码循环
- LLM 编码产出冗余（过度测试、过度防御）
- 需要根据任务复杂度选择审查深度
- 多步骤编码工作流

## 模式 1: De-Sloppify（清理模式）

### 问题

当要�?LLM �?TDD 实现时，它过于字面理�?写测�?�?
- 测试验证 TypeScript 类型系统工作（测�?`typeof x === 'string'`�?- 对类型系统已保证的内容进行过度防御的运行时检�?- 测试框架行为而不是业务逻辑
- 过多错误处理掩盖实际代码

### 为什么不用否定指令？

添加"不要测试类型系统"�?不要添加不必要检�?到实�?prompt 有下游影响：

- 模型�?*所�?*测试变得犹豫
- 跳过合法的边界情况测�?- 质量不可预测地下�?
### 解决方案：独立清理步�?
不要约束实现者，让它彻底。然后添加专注的清理 agent�?
```bash
# Step 1: 实现（让它彻底）
"Implement the feature with full TDD. Be thorough with tests."

# Step 2: De-Sloppify（独立上下文，专注清理）
"Review all changes in the working tree. Remove:
- Tests that verify language/framework behavior rather than business logic
- Redundant type checks that the type system already enforces
- Over-defensive error handling for impossible states
- Console.log statements
- Commented-out code

Keep all business logic tests. Run the test suite after cleanup to ensure nothing breaks."
```

### 在循环上下文�?
```bash
for feature in "${features[@]}"; do
  # 实现
  "Implement $feature with TDD."

  # De-Sloppify
  "Cleanup pass: review changes, remove test/code slop, run tests."

  # 验证
  "Run build + lint + tests. Fix any failures."

  # 提交
  "Commit with message: feat: add $feature"
done
```

### 核心洞察

> **"两个专注�?Agent 优于一个受约束�?Agent�?**

不要添加否定指令（有下游质量影响），添加独立 de-sloppify 步骤�?
### De-Sloppify 检查清�?
**移除**�?- [ ] 验证语言/框架行为而不是业务逻辑的测�?- [ ] 类型系统已强制的冗余类型检�?- [ ] 对不可能状态的过度防御错误处理
- [ ] Console.log 语句
- [ ] 注释掉的代码
- [ ] 测试语言特性的测试（如测试 TypeScript 泛型工作�?
**保留**�?- [ ] 所有业务逻辑测试
- [ ] 边界情况测试
- [ ] 错误路径测试（真实的错误路径，不是不可能的）
- [ ] 集成测试

**验证**�?- [ ] 运行测试套件确保没有破坏
- [ ] 运行 lint 确保代码风格一�?- [ ] 运行类型检查确保类型安�?
## 模式 2: 复杂度分�?
### 问题

对所有任务使用相同管道深度：
- 简单任务过度审查（浪费 token�?- 复杂任务审查不足（遗漏问题）

### 解决方案：按复杂度分�?
| 复杂�?| 管道阶段 | 示例 |
|--------|---------|------|
| **trivial** | 实现 �?测试 | 修复拼写错误、调整样式、添加注�?|
| **small** | 实现 �?测试 �?代码审查 | 添加简单功能、修�?bug、重构小模块 |
| **medium** | 研究 �?计划 �?实现 �?测试 �?PRD审查 + 代码审查 �?审查修复 | 添加中等功能、跨模块重构、API 变更 |
| **large** | 研究 �?计划 �?实现 �?测试 �?PRD审查 + 代码审查 �?审查修复 �?最终审�?| 架构变更、新功能模块、性能优化 |

### 复杂度检�?
根据以下信号自动检测：

| 信号 | 复杂�?|
|------|--------|
| 单文件修�?< 50 �?| trivial |
| 单文件修�?50-200 �?| small |
| 多文件修�?< 5 文件 | medium |
| 多文件修�?>= 5 文件 | large |
| 涉及架构变更 | large |
| 涉及 API 契约变更 | medium+ |
| 涉及性能关键路径 | large |

### 分层管道示例

#### Trivial（简单）

```bash
# 直接实现 + 测试
"Fix the typo in README.md"
"Run tests to ensure nothing broke"
"Commit"
```

#### Small（小�?
```bash
# 实现 + 测试 + 代码审查
"Add unit tests for utils/calculateTotal()"
"Run tests"
"Code review: check for edge cases, error handling"
"Commit"
```

#### Medium（中�?
```bash
# 研究 + 计划 + 实现 + 测试 + 审查
"Research: analyze current auth flow"
"Plan: design OAuth2 integration"
"Implement: add OAuth2 login"
"Test: run full test suite"
"PRD review: verify against spec"
"Code review: security, error handling"
"Fix review issues"
"Commit"
```

#### Large（大�?
```bash
# 完整管道
"Research: analyze codebase architecture"
"Plan: design caching layer"
"Implement: add Redis caching"
"Test: run full test suite + load tests"
"PRD review: verify against spec"
"Code review: performance, security, edge cases"
"Fix review issues"
"Final review: overall quality gate"
"Commit"
```

### �?coding-framework 集成

�?coding-framework Step 1（任务分析）后，检测复杂度并选择管道�?
```markdown
## Step 1.5: 复杂度分层（新增�?
1. 检测复杂度信号（文件数、行数、架构影响）
2. 分配复杂度等级（trivial/small/medium/large�?3. 选择对应管道深度
4. 执行管道
```

### 模型路由（可选）

不同复杂度可以用不同模型�?
```bash
# Trivial: 快速模�?"Fix the typo" --model haiku

# Small: 中等模型
"Add tests" --model sonnet

# Medium/Large: 强模�?"Refactor auth" --model opus
```

�?OpenClaw 中，可以通过 spawn 子代理时指定 model 参数实现�?
## 循环模式组合

这些模式可以良好组合�?
### 组合 1: 顺序管道 + De-Sloppify

最常见组合。每个实现步骤都有清理步骤�?
```bash
for feature in "${features[@]}"; do
  "Implement $feature with TDD."
  "De-sloppify: remove test/code slop."
  "Verify: run build + tests."
  "Commit."
done
```

### 组合 2: 复杂度分�?+ De-Sloppify

根据复杂度选择管道，每个实现步骤后都有清理�?
```bash
if [ "$complexity" = "large" ]; then
  "Research."
  "Plan."
  "Implement."
  "De-sloppify."  # 清理步骤
  "Test."
  "PRD review."
  "Code review."
  "Fix."
  "Final review."
else
  "Implement."
  "De-sloppify."  # 清理步骤
  "Test."
  "Commit."
fi
```

### 组合 3: 迭代循环 + De-Sloppify

�?ralph-orchestrator 迭代循环中，每次迭代都有清理�?
```bash
for iteration in 1 2 3; do
  "Implement improvements."
  "De-sloppify: remove slop."
  "Verify: run tests."
  "Review: check quality."
done
```

## 反模�?
### 1. 无退出条件的无限循环

**错误**�?```bash
while true; do
  "Improve code."
done
```

**正确**�?```bash
for i in {1..10}; do  # 最�?10 次迭�?  "Improve code."
  if quality_check_passed; then
    break
  fi
done
```

### 2. 迭代间无上下文桥�?
**错误**：每次迭代都从零开始�?
**正确**：使用文件系统状态或 SHARED_TASK_NOTES.md 桥接上下文�?
```markdown
## Progress
- [x] Added tests for auth module (iteration 1)
- [x] Fixed edge case in token refresh (iteration 2)
- [ ] Still need: rate limiting tests

## Next Steps
- Focus on rate limiting module next
```

### 3. 重试相同失败

**错误**：失败后盲目重试�?
**正确**：捕获错误上下文并反馈给下次尝试�?
```markdown
## Previous Failure
- Error: Connection timeout
- Attempted: retry 3 times
- Root cause: Missing connection pool

## Next Attempt
- Fix: Add connection pool configuration
- Verify: Test with load simulation
```

### 4. 否定指令代替清理步骤

**错误**�?```
"Implement with TDD. Don't test type systems. Don't add unnecessary checks."
```

**正确**�?```bash
"Implement with TDD. Be thorough."
"De-sloppify: remove test slop."
```

### 5. 所�?Agent 在一个上下文窗口

**错误**：实现者和审查者在同一上下文�?
**正确**：分离上下文窗口，消除作者偏见�?
```bash
# 实现者上下文
"Implement the feature."

# 审查者上下文（独立）
"Review the implementation. Check for security, performance, edge cases."
```

## 与现有技能的关系

| 技�?| 关系 |
|------|------|
| `coding-framework` | 本技能提供循环模式，coding-framework 提供实现流程 |
| `ralph-orchestrator` | 本技能的 De-Sloppify 可集成到 ralph 迭代循环 |
| `code-review` | 复杂度分层决定审查深�?|
| `agent-introspection-debugging` | 循环失败时触发调�?|

## 使用示例

### 示例 1: 简单功能（Small�?
```bash
# 检测复杂度：单文件�? 100 �?�?small

# 管道
"Add retry logic to HTTP client"
"Write tests for retry logic"
"De-sloppify: remove test slop, keep business logic tests"
"Run tests"
"Code review: check error handling, edge cases"
"Commit"
```

### 示例 2: 中等功能（Medium�?
```bash
# 检测复杂度：多文件，涉�?API 变更 �?medium

# 管道
"Research: analyze current API structure"
"Plan: design new endpoint"
"Implement: add new endpoint"
"De-sloppify: remove slop"
"Test: run full test suite"
"PRD review: verify against spec"
"Code review: security, error handling"
"Fix review issues"
"Commit"
```

### 示例 3: 大型重构（Large�?
```bash
# 检测复杂度：多文件，架构变�?�?large

# 管道
"Research: analyze codebase architecture"
"Plan: design refactoring strategy"
"Implement: refactor module"
"De-sloppify: remove slop"
"Test: run full test suite + integration tests"
"PRD review: verify against spec"
"Code review: performance, security, edge cases"
"Fix review issues"
"Final review: overall quality gate"
"Commit"
```

---

*自主循环：De-Sloppify 清理冗余，复杂度分层优化审查深度�?

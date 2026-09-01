# 置信度评分详细指南

> 本文件是 code-review skill 的参考文档，供置信度验证步骤使用。
> 借鉴 Anthropic 官方 Code Review Plugin 的评分体系。

## 评分量表（逐条给分，附理由）

### 0分 — 完全不确信
- 经不起-light-scrutiny 的假阳性
- 预存在的问题（PR未引入）
- 代码看起来有问题但实际是有意设计

**示例**：
- "这个变量名不够好" — 主观判断，无客观依据
- "这个函数太长了" — 200行的数据处理函数可能是合理的

### 25分 —  somewhat confident
- 可能是真的，但无法验证
- 风格问题但项目规范未明确要求
- 需要更多上下文才能确认

**示例**：
- "这里可能有竞态条件" — 但没有证据证明会并发访问
- "这个错误处理可能不够" — 但当前场景下可能不会触发

### 50分 — moderately confident
- 确认是真实问题
- 但属于nitpick或不太重要
- 相对于PR的其他问题，优先级低

**示例**：
- "这个循环可以用 map 简化" — 确实可以，但不改也不会出bug
- "这里缺少类型注解" — 确实缺少，但运行时不会出错

### 75分 — highly confident
- 反复验证，确认很可能在实际中触发
- PR中的现有方案不充分
- 问题会直接影响代码功能，或规范中有明确要求

**示例**：
- "OAuth回调缺少错误处理" — 规范明确要求 "Always handle OAuth errors"
- "这个SQL有注入风险" — 直接拼接用户输入，无参数化

### 100分 — absolutely certain
- 反复验证，确认在实际中会频繁触发
- 证据直接支持
- 无法辩驳

**示例**：
- "这个除以零会崩溃" — 分母可能为0，无guard
- "这个内存泄漏" — 资源分配后未在finally中释放

## 验证流程

### 对每个 issue 执行以下检查：

```
1. [ ] 这个 issue 是 PR 引入的吗？（不是 → -30分）
2. [ ] 这个 issue 是真实 bug 吗？（不确定 → -25分）
3. [ ] lint/typechecker/compiler 能捕获吗？（能 → -50分）
4. [ ] 代码中有 lint-ignore 注释吗？（有 → -50分）
5. [ ] 这个 issue 在用户修改的行上吗？（不是 → -30分）
6. [ ] 有具体的规范条款支持吗？（没有 → -25分）
7. [ ] 高级工程师会指出这个问题吗？（不会 → -20分）
```

### 初始分数计算：
- 基础分 = 审查代理给出的原始置信度（0-100）
- 逐项扣分，最低为0

### 最终决策：
- 最终分 ≥ 80 → 输出
- 最终分 < 80 → 过滤

## 假阳性案例库

### 案例1：预存在问题
```diff
  function oldCode() {
-   return x + y;
+   return x + y + z;  // PR只改了这行
  }
  
  function otherOldCode() {
    // 这里有个bug，但PR没改这里
  }
```
**判定**：`otherOldCode` 中的bug是预存在的，过滤。

### 案例2：有意设计
```diff
+ const data = JSON.parse(rawInput);  // 看起来没try-catch
```
**审查**：如果上游已保证 `rawInput` 是合法JSON（如来自内部API），则不是bug。
**判定**：需确认上下文。如果无法确认，给50分（moderately confident）。

### 案例3：lint可捕获
```diff
+ import { foo } from './bar';  // foo 未使用
```
**判定**：ESLint `no-unused-vars` 会捕获，过滤（-50分）。

### 案例4：被显式静默
```diff
+ // eslint-disable-next-line no-eval
+ const result = eval(expression);
```
**判定**：开发者已知风险并显式忽略，过滤（-50分）。

### 案例5：未修改行
```diff
  function process(data) {
-   return transform(data);
+   return transform(data, options);
    
    // 第10行有个问题，但PR没改
  }
```
**判定**：第10行的问题不是PR引入的，过滤（-30分）。

## 特殊情况处理

### 安全问题的置信度调整
- 安全问题的阈值可以降低到 70（因为安全问题的代价更高）
- 但仍然需要排除明显的假阳性

### 性能问题的置信度调整
- 性能问题通常需要量化证据（如Big-O分析、基准测试）
- 没有量化证据的性能建议，最高给 50分

### 风格问题的置信度调整
- 如果项目有明确的风格规范（如 .eslintrc、.prettierrc），违反规范的问题给 75分
- 如果没有明确规范，纯主观的风格建议给 25分

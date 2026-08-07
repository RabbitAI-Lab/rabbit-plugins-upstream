# TDD 高级模式与重构技巧

## 高级TDD模式

### 1. Outside-In TDD
从最外层（用户接口）开始，逐步向内驱动实现。

**流程**：
1. 写一个端到端测试（Controller/API层）
2. 运行失败（因为内部还没实现）
3. 用mock/stub让外层通过
4. 对mock的内部重复TDD循环
5. 逐步替换mock为真实实现

**适用场景**：需要明确整体架构时、多人协作时

### 2. Triangulation
当不确定如何实现时，用两个极端测试"三角定位"正确实现。

**流程**：
1. 写一个最简单的测试（如输入0返回0）
2. 写一个稍复杂的测试（如输入[1,2,3]返回6）
3. 从两个具体案例中归纳出通用实现

**适用场景**：算法实现、复杂转换

### 3. Transformation Priority Premise (TPP)
按固定优先级顺序应用代码变换，避免过早引入复杂性。

**优先级（从低到高）**：
1. 常量 → 字面量
2. 字面量 → 变量
3. 变量 → 条件语句
4. 条件语句 → 循环
5. 循环 → 集合操作
6. 集合操作 → 多态

**原则**：每次测试失败时，选择优先级最低的变换让测试通过。

### 4. 接口发现
通过TDD发现自然的接口边界。

**信号**：
- 你在mock某个东西 → 那里可能有一个接口
- 测试setup很复杂 → 接口可能需要简化
- 同一个mock在多个测试中出现 → 它可能应该是独立组件

## 重构技巧

### 重构时机
- **所有测试GREEN后** — 唯一安全的重构时机
- **有代码异味时** — 重复、过长函数、过深嵌套

### 安全重构清单

| 重构 | 前提条件 | 验证方式 |
|------|---------|---------|
| 提取函数 | 一段代码有明确意图 | 提取后测试仍通过 |
| 提取接口 | 多个实现共享行为 | 所有实现者的测试通过 |
| 消除重复 | 两处以上相同逻辑 | 合并后测试通过 |
| 内联临时变量 | 变量只用了一次 | 内联后测试通过 |
| 替换条件为多态 | switch/if-else链 | 多态后测试通过 |

### 重构中的安全网
- **小步前进** — 每次只做一个小重构
- **频繁运行测试** — 每步之后都运行
- **可逆操作** — 如果测试挂了，能立即回退
- **Git checkpoint** — 重构前commit，挂了可以reset

## 测试设计原则

### FIRST原则
- **Fast** — 测试要快，慢了就不想跑
- **Isolated** — 测试间不互相依赖
- **Repeatable** — 任何环境、任何顺序都能跑
- **Self-validating** — 测试自己判断pass/fail，不需人工检查
- **Timely** — 及时写，不要拖到代码写完

### 测试命名
```
# 好：描述行为和场景
test_should_return_empty_when_input_is_null
test_login_fails_with_wrong_password
test_calculate_total_applies_discount_for_premium_users

# 差：无意义
test_1
test_function_a
test_something
```

### 测试结构（AAA模式）
```
# Arrange - 准备
user = create_user(name="Alice", role="admin")

# Act - 执行
result = authorize(user, resource)

# Assert - 断言
assert result.granted == True
```

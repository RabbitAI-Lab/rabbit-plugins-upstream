# 测试反模式与避坑指南

## 常见反模式

### 1. 测试实现而非行为 ❌

```python
# 坏：测试内部实现
def test_process_calls_validate():
    validator = Mock()
    processor = DataProcessor(validator)
    processor.process(data)
    validator.validate.assert_called_once()  # 测试了调用关系

# 好：测试可见行为
def test_process_rejects_invalid_data():
    processor = DataProcessor()
    result = processor.process(invalid_data)
    assert result.status == "rejected"
    assert "invalid field" in result.errors
```

**问题**：实现变了测试就挂，即使行为没变。

### 2. 测试间共享状态 ❌

```python
# 坏：共享全局状态
shared_db = Database()

def test_create_user():
    shared_db.create_user("alice")
    assert shared_db.count() == 1

def test_delete_user():
    # 依赖上一个测试的状态！
    shared_db.delete_user("alice")
    assert shared_db.count() == 0
```

**修复**：每个测试独立setup/teardown。

### 3. 过度Mock ❌

```python
# 坏：mock了所有东西，测试的只是mock
def test_order_total():
    order = Mock()
    order.items = [Mock(price=10), Mock(price=20)]
    order.get_total = lambda: sum(i.price for i in order.items)
    assert order.get_total() == 30  # 测试了什么？
```

**修复**：只mock外部依赖，不mock被测代码内部逻辑。

### 4. 断言太少 ❌

```python
# 坏：只断言不崩溃
def test_create_user():
    create_user("alice", "admin")
    # 没有断言！

# 好：断言具体结果
def test_create_user():
    user = create_user("alice", "admin")
    assert user.name == "alice"
    assert user.role == "admin"
    assert user.id is not None
```

### 5. 测试不稳定（Flaky Test）❌

**常见原因**：
- 依赖系统时间
- 依赖随机数（无种子）
- 依赖网络/外部服务
- 测试顺序敏感
- 竞态条件

**修复**：
- 注入时间源（`clock.now()` 而非 `Date.now()`）
- 固定随机种子
- Mock外部服务
- 每个测试独立可运行

### 6. 测试太慢 ❌

**症状**：
- 测试套件跑超过1分钟
- 开发者不想在本地跑测试
- CI经常超时

**修复**：
- 单元测试不碰数据库/网络
- 集成测试用内存数据库
- E2E测试只覆盖关键路径
- 并行运行独立测试

### 7. 巨型测试函数 ❌

```python
# 坏：一个测试函数测所有东西
def test_user_management():
    # 创建用户
    # 修改用户
    # 删除用户
    # 权限检查
    # ... 200行 ...
```

**修复**：一个测试函数只测一个行为。

## 覆盖率陷阱

### 高覆盖率 ≠ 好测试

```python
# 100%覆盖率但没用的测试
def test_add():
    add(1, 2)  # 执行了所有代码行，但没有断言
```

### 覆盖率的使用方式
- **低覆盖率** → 肯定有问题，需要加测试
- **高覆盖率** → 不一定好，但至少没漏测
- **覆盖率变化** → 新代码是否有测试覆盖

## 何时不写测试

不是所有代码都值得测试：
- **一次性脚本** — 跑完就删
- **纯配置** — 没有逻辑
- **简单getter/setter** — 测试成本 > 价值
- **原型/探索代码** — 验证后可能丢弃

**判断标准**：如果这段代码出bug代价高，就值得测试。

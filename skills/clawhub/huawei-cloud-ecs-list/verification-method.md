# 验证方法

## 验证 skill 输出正确性

### 1. 列表查询验证

```bash
# 设置 AK/SK 环境变量
export HUAWEI_AK="您的AK"
export HUAWEI_SK="您的SK"

# 执行列表查询
python3 scripts/huawei-cloud-ecs-list.py list --region cn-north-4
```

**预期输出**：

```json
{
  "count": 0,
  "servers": []
}
```

- 有实例时 `count > 0`，`servers` 数组含实例对象
- 无实例时 `count=0`，`servers` 为空数组（非报错）

### 2. 过滤查询验证

```bash
python3 scripts/huawei-cloud-ecs-list.py list --region cn-north-4 --status ACTIVE --name web
```

**验证**：返回结果中实例状态均为 ACTIVE，名称包含 "web"。

### 3. 详情查询验证

```bash
# 先通过列表获取一个实例 ID
python3 scripts/huawei-cloud-ecs-list.py list --region cn-north-4

# 用实例 ID 查询详情
python3 scripts/huawei-cloud-ecs-list.py show --server-id <实际实例ID> --region cn-north-4
```

**预期输出**：`{"server": {...}}`，包含实例全部字段。

### 4. 错误处理验证

```bash
# AK/SK 缺失
unset HUAWEI_AK HUAWEI_SK
python3 scripts/huawei-cloud-ecs-list.py list
# 预期：stderr 输出 {"error": "AK/SK credentials missing..."}，退出码 3

# 无效实例 ID
python3 scripts/huawei-cloud-ecs-list.py show --server-id invalid-id-12345
# 预期：stderr 输出 {"error": "Instance not found..."}，退出码 2
```

### 5. 退出码验证

| 场景 | 退出码 |
|------|--------|
| 查询成功 | 0 |
| 参数/ID 无效 | 2 |
| AK/SK 缺失/无效 | 3 |
| API 调用失败 | 4 |

```bash
python3 scripts/huawei-cloud-ecs-list.py list; echo "exit: $?"
```

### 6. 与控制台交叉验证

将 skill 输出的实例列表与华为云控制台 → ECS 控制台 → 实例列表对比，确认实例数量、ID、名称、状态一致。

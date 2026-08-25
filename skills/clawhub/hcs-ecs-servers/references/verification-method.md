# 验证方法

## 如何确认 skill 输出正确

### 1. capability-list 验证

```bash
cd skills/hcs-ecs-servers/
python3 scripts/hcs-ecs-servers.py capability-list
```

Expected: 输出 JSON 格式的能力清单，包含 `list-servers` 和 `capability-list` 两个能力项。

### 2. --help 验证

```bash
python3 scripts/hcs-ecs-servers.py --help
python3 scripts/hcs-ecs-servers.py list-servers --help
```

Expected: 无语法错误，显示所有子命令和参数说明。

### 3. list-servers 验证

```bash
python3 scripts/hcs-ecs-servers.py list-servers
```

Expected:
- 退出码 0
- 输出表格格式（实例名称/ID/状态/规格/私有IP/公网IP）
- 如果该区域有 ECS 实例，显示实例信息
- 如果该区域无 ECS 实例，显示"（该区域无 ECS 实例）"

### 4. --json 验证

```bash
python3 scripts/hcs-ecs-servers.py list-servers --json
```

Expected: 输出 JSON 格式，包含 `count`、`region`、`servers` 字段。

### 5. --region 验证

```bash
python3 scripts/hcs-ecs-servers.py list-servers --region cn-north-4
```

Expected: 查询指定区域的 ECS 实例。

### 6. --status 验证

```bash
python3 scripts/hcs-ecs-servers.py list-servers --status ACTIVE
```

Expected: 只返回状态为 ACTIVE 的实例。

### 7. 退出码验证

| 场景 | 退出码 |
|------|--------|
| 成功 | 0 |
| 参数错误 | 2 |
| 缺少 AK/SK | 3 |
| API 调用失败 | 4 |

验证方法：

```bash
python3 scripts/hcs-ecs-servers.py list-servers; echo "exit: $?"
# 无 AK/SK 时
env -u HUAWEI_AK -u HUAWEI_SK python3 scripts/hcs-ecs-servers.py list-servers; echo "exit: $?"
```

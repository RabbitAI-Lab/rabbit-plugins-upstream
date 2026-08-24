# 数据流图

## Skill 请求/响应流程

```mermaid
flowchart TD
    A[用户执行命令] --> B[Python 脚本启动]
    B --> C[动态扫描环境变量获取 AK/SK]
    C --> D{AK/SK 非空?}
    D -->|否| E[输出 JSON 错误到 stderr\n退出码 3]
    D -->|是| F[解析子命令与参数]
    F --> G{子命令类型}
    G -->|list| H[组装 ListServersDetails 命令]
    G -->|show| I[组装 ShowServer 命令]
    G -->|capability-list| J[输出能力列表 JSON]
    H --> K[执行 hcloud CLI\n注入 --cli-access-key/--cli-secret-key\n30s 超时]
    I --> K
    K --> L{调用成功?}
    L -->|是| M[解析 JSON 响应]
    L -->|超时| N[输出超时错误\n退出码 4]
    L -->|404| O[输出实例不存在错误\n退出码 2]
    L -->|401/403| P[输出认证失败错误\n退出码 3]
    L -->|其他错误| Q[输出 API 错误\n退出码 4]
    M --> R[输出 JSON 到 stdout\n保留全部字段]
    R --> S[退出码 0]
```

## 数据结构

### list 请求 → 响应

```
请求: hcloud ECS ListServersDetails --cli-region=cn-north-4 [--status] [--name] [--flavor] [--ip] [--limit]
响应: {"count": N, "servers": [{实例全部字段}, ...]}
```

### show 请求 → 响应

```
请求: hcloud ECS ShowServer --cli-region=cn-north-4 --server_id=<UUID>
响应: {"server": {实例全部字段}}
```

### 实例字段（API 返回全部字段）

- `id`：实例 ID
- `name`：实例名称
- `status`：实例状态
- `addresses`：公网/私网 IP
- `flavor`：规格（vCPU/内存）
- `OS-EXT-AZ:availability_zone`：可用区
- `created`：创建时间
- `image`：镜像信息
- `vpc_id`：VPC ID
- `subnet_id`：子网 ID
- `security_groups`：安全组
- `volumes_attached`：磁盘信息
- 其他 API 返回字段

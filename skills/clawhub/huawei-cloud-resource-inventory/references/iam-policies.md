# IAM 权限策略

## 该 Skill 需要的华为云权限

| 操作 | IAM 权限 | 说明 |
|------|---------|------|
| 查询 ECS 列表 | ecs:servers:list | 获取云服务器列表及详情 |
| 查询 BMS 列表 | bms:servers:list | 获取裸金属服务器列表 |
| 查询 RDS 实例 | rds:instances:list | 获取 RDS 数据库实例列表 |
| 查询 EVS 卷 | evs:volumes:list | 获取云硬盘列表 |
| 查询 DCS 实例 | dcs:instance:list | 获取分布式缓存实例列表 |
| 查询 CCE 集群 | cce:cluster:list | 获取 CCE 集群及节点列表 |
| 查询 VPC | vpc:vpcs:list | 获取 VPC 列表 |
| 查询子网 | vpc:subnets:list | 获取子网列表 |
| 查询 EIP | eip:publicips:list | 获取弹性公网 IP 列表 |
| 查询 ELB | elb:loadbalancers:list | 获取负载均衡器列表 |
| 查询 NAT | nat:natGateways:list | 获取 NAT 网关列表 |
| 查询 DNS | dns:zones:list | 获取 DNS zone 列表 |
| 查询 IAM 项目 | iam:projects:list | 获取项目列表用于跨 region 查询 |

## 最小权限策略

```json
{
  "Version": "1.1",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecs:servers:list",
        "bms:servers:list",
        "rds:instances:list",
        "evs:volumes:list",
        "dcs:instance:list",
        "cce:cluster:list",
        "cce:node:list",
        "vpc:vpcs:list",
        "vpc:subnets:list",
        "eip:publicips:list",
        "elb:loadbalancers:list",
        "nat:natGateways:list",
        "dns:zones:list",
        "iam:projects:list"
      ],
      "Resource": ["*"]
    }
  ]
}
```

## 权限说明

- 该 skill 只需要上述列出的权限（最小权限原则）
- 不需要管理员权限
- 不需要写权限（只读查询类 skill）
- 所有操作均为 List/Show/Get 只读操作

# IAM 权限策略

## 该 Skill 需要的华为云权限

| 操作 | IAM 权限 | 说明 |
|------|---------|------|
| 查询集群列表 | `cce:cluster:list` | 调用 CCE ListClusters API 获取集群列表 |

## 最小权限策略

```json
{
  "Version": "1.1",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cce:cluster:list"
      ],
      "Resource": ["*"]
    }
  ]
}
```

## 权限说明

- 该 skill 只需要 `cce:cluster:list` 一个只读权限
- 不需要管理员权限
- 不需要写权限
- 不需要其他 CCE 子资源的权限（如节点、存储等）
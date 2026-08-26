# IAM 权限策略

## 该 Skill 需要的华为云权限

| 操作 | IAM 权限 | 说明 |
|------|---------|------|
| 查询 ECS 实例列表 | ECS:cloudServers:list | 查询云服务器详情列表 |
| 获取 project_id | IAM:projects:list | 通过 IAM API 获取区域项目 ID |

## 最小权限策略

```json
{
  "Version": "1.1",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ECS:cloudServers:list",
        "IAM:projects:list"
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
- `ECS:cloudServers:list` 对应 `GET /v1/{project_id}/cloudservers/detail` API
- `IAM:projects:list` 对应 `GET /v3/projects?name={region}` API（用于获取 project_id）

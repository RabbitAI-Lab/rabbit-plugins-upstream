# 华为云 ECS API Reference

> API 端点通过 huaweicloudsdkecs SDK `_http_info` 确认，非猜测。
> 认证方式：AK/SK 签名（SDK-HMAC-SHA256）。

## 基本信息

- **API 名称**：华为云 ECS（弹性云服务器）
- **SDK 包**：huaweicloudsdkecs v2
- **认证方式**：AK/SK 签名（SDK-HMAC-SHA256）
- **响应格式**：JSON

## 端点列表

### 查询 ECS 实例列表详情

#### GET /v1/{project_id}/cloudservers/detail

查询云服务器详情列表。

**API 来源**：`huaweicloudsdkecs.v2.EcsClient.list_servers_details` 的 `_http_info`：

```python
http_info = {
    "method": "GET",
    "resource_path": "/v1/{project_id}/cloudservers/detail",
    "request_type": "ListServersDetailsRequest",
    "response_type": "ListServersDetailsResponse"
}
```

**路径参数**：

| 参数 | 位置 | 类型 | 必填 | 说明 |
|------|------|------|------|------|
| project_id | path | string | 是 | 项目 ID（通过 IAM API 获取） |

**查询参数**：

| 参数 | 位置 | 类型 | 必填 | 说明 |
|------|------|------|------|------|
| enterprise_project_id | query | string | 否 | 企业项目 ID |
| flavor | query | string | 否 | 规格 ID |
| ip | query | string | 否 | IPv4 地址模糊匹配 |
| ip_eq | query | string | 否 | IPv4 地址精确匹配 |
| limit | query | integer | 否 | 每页最大返回数（默认 25，最大 1000） |
| name | query | string | 否 | 实例名称模糊匹配 |
| not-tags | query | string | 否 | 排除指定标签 |
| offset | query | integer | 否 | 页码偏移（从 1 开始） |
| reservation_id | query | string | 否 | 预留 ID |
| status | query | string | 否 | 实例状态筛选 |
| tags | query | string | 否 | 标签筛选 |
| server_id | query | string | 否 | 实例 ID |
| marker | query | string | 否 | 分页标记 |

**status 支持的值**：

| 状态 | 说明 |
|------|------|
| ACTIVE | 运行中 |
| SHUTOFF | 关机 |
| BUILD | 创建中 |
| ERROR | 异常 |
| REBOOT | 重启中 |
| HARD_REBOOT | 硬重启中 |
| MIGRATING | 迁移中 |

**响应**：

```json
{
  "count": 1,
  "servers": [
    {
      "name": "test-ecs-01",
      "id": "1234abcd-5678-efgh-...",
      "status": "ACTIVE",
      "created": "2026-01-01T00:00:00Z",
      "flavor": {
        "id": "s6.large.2",
        "name": "s6.large.2",
        "vcpus": "2",
        "ram": 2048
      },
      "addresses": {
        "vpc-network": [
          {
            "version": 4,
            "addr": "192.168.1.10",
            "OS-EXT-IPS:type": "fixed"
          },
          {
            "version": 4,
            "addr": "1.2.3.4",
            "OS-EXT-IPS:type": "floating"
          }
        ]
      },
      "OS-EXT-AZ:availability_zone": "cn-north-4a"
    }
  ]
}
```

## 签名方式

使用 `huaweicloudsdkcore.signer.signer.Signer` 生成 SDK-HMAC-SHA256 签名：

1. 构建 `SdkRequest` 对象（method/host/resource_path/query_params/header_params）
2. 调用 `Signer.sign(sdk_req)` 自动生成 `Authorization` / `X-Sdk-Date` / `Host` 头
3. 使用 `requests` 发送签名后的请求

## project_id 获取

通过 IAM API 获取：

```
GET https://iam.myhuaweicloud.com/v3/projects?name={region}
```

返回 JSON 中 `projects[0].id` 即为该区域的 project_id。

## 子命令映射表

| 子命令 | HTTP 方法 | API 路径 | 说明 |
|--------|-----------|----------|------|
| list-servers | GET | /v1/{project_id}/cloudservers/detail | 查询 ECS 实例列表 |
| capability-list | - | - | 列出本 skill 所有能力项 |

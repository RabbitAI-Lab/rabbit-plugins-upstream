# 华为云 ECS 云服务器实例相关 API（文档摘录）

> 依据华为云 ECS 服务 API 文档整理。真实调用使用官方 Python SDK `huaweicloudsdkecs`（V2 客户端 `EcsClient`），等价 REST 接口如下。

## 1. 查询 ECS 实例列表（能力 A）

```
GET /v1/{project_id}/cloudservers/detail
```

- 分页参数：`limit`（默认 25，最大 1000）、`marker`（上一页最后一条实例 ID）。
- 过滤参数：
  - `name`：按实例名称模糊匹配
  - `status`：按实例状态过滤（ACTIVE / SHUTOFF / ERROR / BUILD 等）
  - `flavor`：按实例类型过滤
  - `ip`：按 IP 地址过滤
  - `enterprise_project_id`：按企业项目过滤
- 返回 `servers` 数组 + `count`（总数），每项含：
  - `id`：实例 ID
  - `name`：实例名称
  - `status`：实例状态
  - `OS-EXT-AZ:availability_zone`：可用区
  - `flavor`：实例类型（ServerFlavor 对象，含 id/name/vcpus/ram/disk）
  - `addresses`：网络地址（dict，key 为网络名，value 为 ServerAddress 列表）
  - `created`：创建时间
  - `updated`：更新时间
- SDK：`ListServersDetailsRequest` / `client.list_servers_details`

## ServerAddress 结构

| 字段 | JSON key | 说明 |
|---|---|---|
| `addr` | `addr` | IP 地址 |
| `version` | `version` | IP 版本（4 / 6） |
| `os_ext_ip_stype` | `OS-EXT-IPS:type` | 地址类型（fixed / floating） |
| `os_ext_ips_ma_cmac_addr` | `OS-EXT-IPS-MAC:mac_addr` | MAC 地址 |
| `os_ext_ip_sport_id` | `OS-EXT-IPS:port_id` | 端口 ID |

## ServerFlavor 结构

| 字段 | 说明 |
|---|---|
| `id` | 实例类型 ID（如 s6.large.2） |
| `name` | 实例类型名称 |
| `vcpus` | vCPU 数 |
| `ram` | 内存（MB） |
| `disk` | 系统盘大小（GB） |

## 区域域名

- 北京四（cn-north-4，默认）：`https://ecs.cn-north-4.myhuaweicloud.com`
- 其他区域：`https://ecs.{region}.myhuaweicloud.com`

## 认证

- AK/SK 方式（环境变量 `HWCLOUD_AK` / `HWCLOUD_SK`），由 `huaweicloudsdkcore.auth.credentials.BasicCredentials` 构造。
- 项目 ID：`BasicCredentials.with_project_id()` 显式指定；缺省由 AK/SK 自动解析默认项目。

## 常见实例状态

| 状态 | 说明 |
|---|---|
| `ACTIVE` | 运行中 |
| `BUILD` | 创建中 |
| `SHUTOFF` | 已关机 |
| `REBOOT` | 重启中 |
| `ERROR` | 异常 |
| `HARD_REBOOT` | 硬重启中 |
| `REBUILD` | 重建中 |

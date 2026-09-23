---
name: alist
version: "1.0.0"
description: "统一网盘管理,30+存储后端文件上传分享下载,百度/阿里/夸克网盘。触发:文件上传/网盘分享/素材管理"
tools: [read]
dependencies: []
metadata:
  layer: infrastructure
  priority: P1
  category: infra
  openclaw:
    emoji: "⚙️"
    os: ["win32", "linux", "darwin"]
    requires:
      bins: ["python"]
      env: ["ALIST_BASE_URL", "ALIST_USERNAME", "ALIST_PASSWORD"]
      config: ["mcp.servers.alist-mcp"]
---

<!-- 纯MCP调用型Skill,无exec脚本 -->

# AList 统一网盘管理

基于alist(45k+星)的统一网盘管理服务，支持百度网盘/阿里云盘/夸克网盘/115网盘等30+种存储后端。通过alist REST API v3实现文件上传、下载、分享、删除等操作。内置Token自动刷新(48小时有效期，过期前5分钟自动续期)、熔断器保护(3次重试+指数退避)和发货安全机制(自动密码+有效期+客户跟踪+重发限制)。替代原baidu-pan-mcp和quark-promote-mcp。

## 使用场景

1. 虚拟商品自动发货生成安全分享链接（EP-02）
2. 多平台网盘资源统一管理与同步
3. 闲置资源分享管理（带密码+有效期保护）
4. 云端素材库维护（商品图/视频/文案模板）
5. 企业文件集中管理（跨网盘统一操作）
6. 发货链接过期提醒与自动重发
7. 虚拟商品自动发货：买家付款后自动生成网盘分享链接+提取码发送给买家
8. 资料包分发：批量生成分享链接，用于闲鱼商品描述中的下载指引

## 工作流

### 主流程: 文件上传与分享

1. 调用list_drives确认可用的存储后端
2. 调用upload_file将本地文件上传到指定网盘目录
3. 调用create_share_link生成分享链接(设置密码+有效期)
4. 输出分享URL+密码+有效期信息

### 安全发货流程(虚拟商品专用)

1. 根据商品类型确定网盘文件路径
2. 调用create_secure_share生成安全分享链接(自动6位密码(小写字母+数字)+默认3天有效期)
3. delivery_tracker记录客户跟踪信息(买家ID+商品+链接+过期时间)
4. 输出安全分享结果(share_url+password+period_days+expires_at)

### 文件浏览与下载

1. 调用list_files列出指定目录下的文件
2. 调用get_file_info获取文件详细信息(大小/类型/修改时间)
3. 调用download_url获取文件下载链接
4. 输出文件列表或下载URL

### 发货跟踪管理

1. 调用redelivery_status查询买家发货记录(过期状态/重发次数/剩余次数)
2. 调用check_expiring_links检查即将过期的分享链接
3. 调用delivery_stats获取发货统计信息
4. 输出跟踪状态或统计结果

## 输入格式

### 文件上传
```json
{
  "local_path": "d:/output/product_image.png",
  "remote_dir": "/JueJin/products/",
  "drive": ""
}
```

### 安全分享
```json
{
  "file_path": "/JueJin/products/tutorial.zip",
  "drive": "",
  "period_days": 3
}
```

### 发货跟踪查询
```json
{
  "buyer_id": "buyer_123",
  "product_name": "OpenClaw部署教程"
}
```

## 输出格式

### 分享链接输出
```json
{
  "success": true,
  "data": {
    "share_url": "http://localhost:5244/s/abc123",
    "password": "a3b7",
    "file_path": "/JueJin/products/tutorial.zip",
    "drive": "",
    "period_days": 3
  },
  "error": null,
  "code": null
}
```

### 安全分享输出(含跟踪)
```json
{
  "success": true,
  "data": {
    "share_url": "http://localhost:5244/s/abc123",
    "password": "k9m2",
    "file_path": "/JueJin/products/tutorial.zip",
    "period_days": 3,
    "expires_at": 1747358400.0
  },
  "error": null,
  "code": null
}
```

## MCP工具清单

| 工具 | 参数 | 说明 |
|:-----|:-----|:-----|
| list_files | path, drive | 列出网盘目录文件 |
| upload_file | local_path, remote_dir, drive | 上传文件到网盘 |
| create_share_link | file_path, drive, period, password | 生成分享链接 |
| create_secure_share | file_path, drive, period_days | 生成安全分享链接(自动密码+跟踪) |
| delete_file | file_path, drive | 删除网盘文件 |
| get_file_info | file_path, drive | 获取文件详细信息 |
| download_url | file_path, drive | 获取文件下载链接 |
| list_drives | 无 | 列出所有存储后端 |
| healthcheck | 无 | 检查服务健康状态 |
| redelivery_status | buyer_id, product_name | 查询发货跟踪记录 |
| delivery_stats | 无 | 获取发货统计信息 |
| check_expiring_links | 无 | 检查即将过期的链接 |

## Token管理

| 项目 | 值 | 说明 |
|:-----|:---|:-----|
| Token有效期 | 48小时 | 与alist服务端config.json一致 |
| 自动刷新 | 过期前5分钟 | token_manager自动续期 |
| 刷新失败 | CRITICAL告警 | alert_manager推送告警 |
| 401处理 | 清空Token重登录 | 自动重试1次 |

## 异常处理

| 错误代码 | 场景 | 处理方式 |
|:---------|:-----|:---------|
| LIST_ERROR | 文件列表获取失败 | 返回错误信息 |
| UPLOAD_ERROR | 文件上传失败 | 检查文件路径和网络，重试3次 |
| SHARE_ERROR | 分享链接生成失败 | 检查文件路径和权限 |
| DELETE_ERROR | 文件删除失败 | 检查文件路径和权限 |
| INFO_ERROR | 文件信息获取失败 | 检查文件路径 |
| DOWNLOAD_ERROR | 下载链接获取失败 | 检查文件路径和权限 |
| DRIVE_ERROR | 存储后端列表获取失败 | 检查alist服务状态 |
| FILE_NOT_FOUND | 本地文件不存在 | 确认local_path路径正确 |
| RECORD_NOT_FOUND | 发货记录不存在 | 确认buyer_id和product_name |
| REDELIVERY_ERROR | 重发状态查询失败 | 检查delivery_tracker |
| EXPIRY_CHECK_ERROR | 过期检查失败 | 检查delivery_tracker |
| MAX_RETRIES_EXCEEDED | 重试3次均失败 | 检查alist服务+网络+Token |
| HEALTH_ERROR | 健康检查失败 | 检查alist服务是否运行 |

## 三省六部归口

- **部门**: 吏部 (libu_hr)
- **职责**: 统一网盘存储与资产管理
- **关联Agent**: libu_hr

## 示例

### 示例1: 上传文件并生成安全分享链接

输入:
```json
{"local_path": "d:/output/tutorial.zip", "remote_dir": "/JueJin/products/", "drive": ""}
```

执行:
1. 调用upload_file(local_path="d:/output/tutorial.zip", remote_dir="/JueJin/products/")
2. 调用create_secure_share(file_path="/JueJin/products/tutorial.zip", period_days=3)
3. delivery_tracker自动记录客户跟踪信息

输出:
```json
{
  "success": true,
  "data": {
    "share_url": "http://localhost:5244/s/abc123",
    "password": "k9m2",
    "file_path": "/JueJin/products/tutorial.zip",
    "period_days": 3,
    "expires_at": 1747358400.0
  }
}
```

### 示例2: 查询买家发货记录

输入:
```json
{"buyer_id": "buyer_123", "product_name": "OpenClaw部署教程"}
```

执行:
1. 调用redelivery_status(buyer_id="buyer_123", product_name="OpenClaw部署教程")
2. 返回链接状态+重发次数+剩余次数

输出:
```json
{
  "success": true,
  "data": {
    "buyer_id": "buyer_123",
    "product_name": "OpenClaw部署教程",
    "share_url": "http://localhost:5244/s/abc123",
    "is_expired": false,
    "remaining_hours": 48.5,
    "delivery_count": 1,
    "can_redeliver": true,
    "remaining_redeliveries": 2,
    "status": "active"
  }
}
```

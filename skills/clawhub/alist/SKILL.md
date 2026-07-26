---
name: alist
version: 1.2.0
description: alist 全功能 API 客户端：文件系统（列表/搜索/创建/重命名/移动/复制/删除/上传/下载/目录扫描/离线下载）、存储管理、驱动管理、用户管理、元信息管理、设置管理、任务管理、索引管理、备份恢复、SSH/SFTP、审计日志、公告、2FA、SSO、刮削诊断。支持 token 自动管理和重试。
---

# alist 全功能管理

基于 alist REST API 的 Python 客户端，覆盖 alist 全部核心管理功能。

---

## 1) 快速开始

```bash
python scripts/alist_client.py --base-url http://localhost:80 --username admin --password xxx ping
python scripts/alist_client.py --base-url http://localhost:80 --api-key "your-key" list /mnt/sda2
```

配置优先级：命令行参数 > 环境变量 (`ALIST_BASE_URL`, `ALIST_USERNAME`, `ALIST_PASSWORD`, `ALIST_API_KEY`)

Token 自动管理：首次调用自动登录并缓存 token（48h 有效），后续请求自动携带。

---

## 2) 全部命令

### 认证
| 命令 | 说明 |
|------|------|
| `login` | 登录并缓存 token |
| `ping` | 测试连接（调用 /api/public/settings） |

### 文件系统
| 命令 | 参数 | 说明 |
|------|------|------|
| `list [path]` / `ls [path]` | `--password` `--page` | 列出目录内容 |
| `get <path>` | `--password` | 获取文件/目录详情 |
| `search <keyword>` | `--scope 0/1/2` | 搜索文件 |
| `mkdir <path>` | — | 创建目录 |
| `rename <path> <name>` | — | 重命名（name 不含路径） |
| `move <src> <dst> <names...>` | `--no-verify` | 批量移动，默认查任务列表，status=4 成功则自动清理任务 |
| `recursive-move <src> <dst>` | `--no-verify` | 递归移动，同上：查任务列表 + 自动清理 |
| `copy <src> <dst> <names...>` | `--no-verify` | 批量复制，同上：查任务列表 + 自动清理 |
| `remove <dir> <names...>` / `rm <dir> <names...>` | — | 批量删除文件/目录 |
| `tree [path]` | `--depth` | 树形展示目录结构 |

### 存储管理
| 命令 | 参数 | 说明 |
|------|------|------|
| `storage-list` | — | 列出所有存储 |
| `storage-get <id>` | — | 获取存储详情 |
| `storage-refresh` | — | 刷新所有存储缓存 |
| `storage-enable <id>` | — | 启用存储 |
| `storage-disable <id>` | — | 禁用存储 |
| `storage-delete <id>` | — | 删除存储 |
| `driver-list` | — | 驱动配置模板列表 |
| `driver-names` | — | 驱动名称列表 |

### 用户管理
| 命令 | 参数 | 说明 |
|------|------|------|
| `user-list` | — | 用户列表 |
| `user-get <id>` | — | 用户详情 |
| `user-delete <id>` | — | 删除用户 |

### 元信息
| 命令 | 说明 |
|------|------|
| `meta-list` | 元信息列表 |

### 设置
| 命令 | 说明 |
|------|------|
| `setting-list` | 设置列表 |
| `diagnose-scrape <path>` | 刮削诊断 |

### 任务管理
| 命令 | 说明 |
|------|------|
| `task-upload` | 上传任务列表 |
| `task-download` | 下载任务列表 |
| `task-copy` | 复制任务列表 |
| `task-clear-done` | 清除已完成任务 |
| `task-clear-succeeded` | 清除已成功任务 |
| `task-clear` | 清除全部任务 |

---

## 3) Python API 调用

```python
from alist_client import AlistClient

# 方式一：用户名密码
client = AlistClient("http://localhost:80", "admin", "password")

# 方式二：API Key（无需登录）
client = AlistClient("http://localhost:80", api_key="alist-xxx")

# 文件操作
client.list_files("/mnt/sda2/Downloads")
client.search_files("movie", scope=0)
client.mkdir("/mnt/sda2/电影")
client.rename("/mnt/sda2/test.mp4", "new_name.mp4")
client.move("/mnt/sda2", "/mnt/sda2/电影", ["movie.mp4"])
# 跨存储大文件：增加 timeout（默认查 alist 任务列表验证，避免预占空间误判）
client.move("/mnt/sda2", "/mnt/sdb1/movie", ["movie.mp4"], timeout=3600)
# 跳过验证（不推荐）
client.move("/mnt/sda2", "/mnt/sdb1/", ["x.mp4"], verify=False)
client.remove("/mnt/sda2", ["old_file.mp4"])

# 存储管理
client.storage_list()
client.storage_refresh()
client.storage_enable(1)

# 用户管理
client.user_list()
client.user_create("guest", "pass", role=1)

# 任务管理
client.task_download_list()
client.task_clear_succeeded()

# 树形展示
print(client.tree("/mnt/sda2", depth=2))

# 刮削诊断
diagnosis = client.diagnose_scrape("/电影库NO1/Scream 7 (2026)")
print(diagnosis["verdict"])  # OK / SKIPPED / NOT_SCRAPED / MISCONFIGURED
```

---

## 4) 完整 API 方法列表

| 方法 | HTTP | 路径 | 说明 |
|------|------|------|------|
| `login()` | POST | /api/auth/login/hash | 密码哈希登录 |
| `list_files()` | POST | /api/fs/list | 列出目录 |
| `get_file()` | POST | /api/fs/get | 文件详情 |
| `search_files()` | POST | /api/fs/search | 搜索文件 |
| `mkdir()` | POST | /api/fs/mkdir | 创建目录 |
| `rename()` | POST | /api/fs/rename | 重命名 |
| `move()` | POST | /api/fs/move | 移动，查任务列表验证 + 自动清理已完成任务 |
| `recursive_move()` | POST | /api/fs/recursive_move | 递归移动，同上 |
| `copy()` | POST | /api/fs/copy | 复制，同上 |
| `remove()` | POST | /api/fs/remove | 删除文件 |
| `dirs()` | POST | /api/fs/dirs | 子目录列表（含计数，刮削扫描） |
| `add_offline_download()` | POST | /api/fs/add_offline_download | 离线下载 |
| `add_aria2()` | POST | /api/fs/add_aria2 | aria2 下载 |
| `upload_file()` | PUT | /api/fs/form | 上传，查任务列表验证 + 自动清理 |
| `download_file()` | GET | /d/{path} | 下载，查任务列表验证 + 自动清理 |
| `storage_list()` | GET | /api/admin/storage/list | 存储列表 |
| `storage_get()` | GET | /api/admin/storage/get | 存储详情 |
| `storage_create()` | POST | /api/admin/storage/create | 创建存储 |
| `storage_update()` | POST | /api/admin/storage/update | 更新存储 |
| `storage_delete()` | POST | /api/admin/storage/delete | 删除存储 |
| `storage_enable()` | POST | /api/admin/storage/enable | 启用 |
| `storage_disable()` | POST | /api/admin/storage/disable | 禁用 |
| `storage_refresh()` | POST | /api/admin/storage/refresh | 刷新缓存 |
| `driver_list()` | GET | /api/admin/driver/list | 驱动模板 |
| `driver_names()` | GET | /api/admin/driver/names | 驱动名称 |
| `driver_info()` | POST | /api/admin/driver/info | 驱动配置字段 |
| `user_list()` | GET | /api/admin/user/list | 用户列表 |
| `user_get()` | GET | /api/admin/user/get | 用户详情 |
| `user_create()` | POST | /api/admin/user/create | 创建用户 |
| `user_update()` | POST | /api/admin/user/update | 更新用户 |
| `user_delete()` | POST | /api/admin/user/delete | 删除用户 |
| `meta_list()` | GET | /api/admin/meta/list | 元信息列表 |
| `meta_create()` | POST | /api/admin/meta/create | 创建元信息 |
| `meta_update()` | POST | /api/admin/meta/update | 更新元信息 |
| `meta_delete()` | POST | /api/admin/meta/delete | 删除元信息 |
| `setting_list()` | GET | /api/admin/setting/list | 设置列表 |
| `setting_get()` | GET | /api/admin/setting/get | 获取设置 |
| `setting_save()` | POST | /api/admin/setting/save | 保存设置 |
| `setting_delete()` | POST | /api/admin/setting/delete | 删除设置 |
| `setting_reset()` | POST | /api/admin/setting/reset | 重置设置 |
| `task_upload_list()` | GET | /api/admin/task/upload | 上传任务 |
| `task_download_list()` | GET | /api/admin/task/download | 下载任务 |
| `task_copy_list()` | GET | /api/admin/task/copy | 复制任务 |
| `task_delete()` | POST | /api/admin/task/delete | 删除任务 |
| `task_cancel()` | POST | /api/admin/task/cancel | 取消任务 |
| `task_retry()` | POST | /api/admin/task/retry | 重试任务 |
| `task_clear_done()` | POST | /api/admin/task/clear_done | 清除已完成 |
| `task_clear_succeeded()` | POST | /api/admin/task/clear_succeeded | 清除已成功 |
| `task_clear()` | POST | /api/admin/task/clear | 清除全部 |
| `index_build()` | POST | /api/admin/index/build | 构建索引 |
| `index_update()` | POST | /api/admin/index/update | 更新索引 |
| `index_stop()` | POST | /api/admin/index/stop | 停止索引 |
| `index_clear()` | POST | /api/admin/index/clear | 清除索引 |
| `index_progress()` | GET | /api/admin/index/progress | 索引进度 |
| `backup_list()` | GET | /api/admin/backup/list | 备份列表 |
| `backup_backup()` | POST | /api/admin/backup/backup | 创建备份 |
| `backup_restore()` | POST | /api/admin/backup/restore | 恢复备份 |
| `backup_delete()` | POST | /api/admin/backup/delete | 删除备份 |
| `ssh_list()` | GET | /api/admin/ssh/list | SSH 列表 |
| `ssh_create()` | POST | /api/admin/ssh/create | 创建 SSH |
| `ssh_update()` | POST | /api/admin/ssh/update | 更新 SSH |
| `ssh_delete()` | POST | /api/admin/ssh/delete | 删除 SSH |
| `audit_list()` | GET | /api/admin/audit/list | 审计日志 |
| `audit_clear()` | POST | /api/admin/audit/clear | 清除审计 |
| `announcement_list()` | GET | /api/admin/announcement/list | 公告列表 |
| `announcement_update()` | POST | /api/admin/announcement/update | 更新公告 |
| `twofa_list()` | GET | /api/admin/2fa/list | 2FA 配置列表 |
| `twofa_delete()` | POST | /api/admin/2fa/delete | 删除 2FA |
| `sso_list()` | GET | /api/admin/sso/list | SSO 列表 |
| `sso_create()` | POST | /api/admin/sso/create | 创建 SSO |
| `sso_update()` | POST | /api/admin/sso/update | 更新 SSO |
| `sso_delete()` | POST | /api/admin/sso/delete | 删除 SSO |
| `ping()` | GET | /api/public/settings | 连接测试 |
| `tree()` | — | 组合调用 | 树形展示 |
| `diagnose_scrape()` | — | 组合调用 | 刮削诊断：检查目录刮削状态 |

---

## 5) 代理与 TMDB 刮削

### 刮削机制

alist 刮削是**前端驱动**的：用户浏览包含媒体文件的目录时，alist-web（React 前端）从 `/api/public/settings` 读取 `tmdb_api_key`，直接构造 TMDB API 请求（POST /api/fs/get 返回文件列表时附带刮削结果）。

关键配置项：

| 设置项 | Key | 用途 | 常见错误 |
|--------|-----|------|----------|
| TMDB API Key | `tmdb_api_key` | 前端调用 TMDB 的认证密钥 | 无感知（前端调用） |
| TMDB API URL | `tmdb_api_url` | **前端构造 TMDB 请求的基地址** | 误设为代理地址（如 `http://192.168.51.15:7897`），会导致构造出错误 URL |
| HTTP 代理 | `http_proxy` | **后端**出站请求的代理地址 | 仅设置此项不足以让 Docker 容器使用代理 |
| 外部预览 | `external_previews` | 对象值，含 `nfo`, `open_api_url` 等 | - |

### 代理配置分层

三层代理配置，**互不替代**：

```
┌─────────────────────────────────────────┐
│ 浏览器（用户端）                          │
│ → 直接根据 tmdb_api_url 构造 URL 访问 TMDB │
│ → 需要用户网络能直连 TMDB                 │
├─────────────────────────────────────────┤
│ alist 后端 (Docker 容器)                  │
│ → 通过 http_proxy 设置项 → 宿主机代理      │
│ → Docker 容器必须注入环境变量：             │
│   HTTP_PROXY / HTTPS_PROXY               │
│   http_proxy / https_proxy               │
├─────────────────────────────────────────┤
│ 宿主机代理 (192.168.51.15:7897)           │
│ → 实际出站到 TMDB                         │
└─────────────────────────────────────────┘
```

**Docker 代理注入** (docker-compose.yml)：
```yaml
environment:
  - HTTP_PROXY=http://192.168.51.15:7897
  - HTTPS_PROXY=http://192.168.51.15:7897
  - http_proxy=http://192.168.51.15:7897
  - https_proxy=http://192.168.51.15:7897
```

### Docker Bridge 网络 HTTPS 502 问题

Docker bridge 网络下，容器通过宿主机代理发起 **HTTPS** 请求时可能返回 502 Bad Gateway，但 **HTTP** 请求正常。

**解决方案**：
1. **HTTP 降级**（推荐）：`tmdb_api_url` 设为 `http://api.themoviedb.org`，走 HTTP 通路
2. **host 网络模式**：`docker-compose.yml` 设 `network_mode: host`，容器直接使用宿主机网络栈

> 当前环境采用方案 1（HTTP 降级），TMDB HTTP API 功能完整。

### setting_save API 调用格式

```python
# 错误（单个对象，设置不生效）
data = {"key": "tmdb_api_url", "value": "http://api.themoviedb.org"}

# 正确（数组）
data = [{"key": "tmdb_api_url", "value": "http://api.themoviedb.org"}]

client.setting_save(data)  # data 必须是 list[dict]
```

### 刮削不生效诊断流程

1. **检查 tmdb_api_key**：`setting_list()` → 确认 key 存在且正确
2. **检查 tmdb_api_url**：`setting_list()` → 确认值为 `http://api.themoviedb.org`（非代理地址）
3. **测试 TMDB 连通性**：宿主机 `curl http://api.themoviedb.org` 确认通
4. **检查 Docker 容器代理**：`docker exec alist curl -x http://192.168.51.15:7897 http://api.themoviedb.org`
5. **检查 NFO 产物**：用 `get_file()` 查看目录下是否有 `.nfo` 文件，检查修改时间
6. **已有海报跳过问题**：若目录已存在 `poster.jpg`，alist 可能跳过刮削。临时重命名 poster.jpg 后重新访问目录可触发完整刮削过程

### 重新触发刮削

- **新影片入库**：目录无任何元数据文件时，前端浏览目录会自动触发刮削
- **已有海报无 NFO**：手动删除/重命名 poster.jpg → 重新访问目录 → 触发完整刮削
- **批量刷新**：暂不支持通过 API 批量触发刮削

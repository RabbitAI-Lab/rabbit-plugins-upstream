---
name: blog-mini-yaw-kit
version: 0.1.0
description: |
  管理 Blog System API (FastAPI) 全部 32 个端点：文章/标签/用户/评论/留言/说说/文件上传/前端页面/后台管理/健康检查。
  无认证公开 API，子命令驱动，支持 JSON/Markdown 输出。
triggers:
  - 博客管理
  - 文章发布
  - 博客API
  - blog system
  - FastAPI博客
tags:
  - blog
  - fastapi
  - rest-api
  - content-management
  - no-auth
tools:
  - curl
  - python3
---

# blog-mini-yaw-kit

Blog System API (FastAPI) 管理 skill — 覆盖全部 32 个端点，无认证公开 API。

## 安全硬约束（必须遵守）

**通用约束（所有 skill 必含）**：

1. 严禁读取 data/、configs/、sessions.db、user_accounts 等 Grape 内部数据。
2. API 返回 403/无权限时：立即停止该操作并回复用户，严禁尝试其他 token 或绕行手段。
3. 所有 curl / API 调用设 30s 超时——超时判定失败，不 hang。
4. 严禁 mock 模式/假数据：所有 API 调用必须真实访问目标系统。
5. 调用目标 API 一律以 `references/api-reference.md` 为准：严禁根据经验/记忆/猜测自行拼写 API 路径。

**动态约束（无认证）**：

- 本 skill 为无认证公开 API，仅需配置 base_url，不需要凭据环境变量。
- 后台管理端点（/admin/*）需要 session cookie（通过 admin-login 获取），cookie 由脚本内部 session 自动持久化，不写入文件。

## 评论规范

- 所有 Issue/PR 评论 body 必须以 `[blog-mini-yaw-kit]` 开头
- 引用用户原文：`> {用户评论}\n\n[blog-mini-yaw-kit] {回复}`

## Configuration

目标系统 API 地址必须在使用前确定。所有命令中的 `{base_url}` 替换为实际地址（格式 `http://<host>:<port>`）（示例）。

`{base_url}` 解析优先级：

1. **项目知识** — 检查 `.project-info/` 目录下 JSON 配置文件（`config.BLOG_MINI_YAW_KIT_BASE_URL`）
2. **环境变量** — `BLOG_MINI_YAW_KIT_BASE_URL`
3. **当前上下文** — 用户直接提供或 A2A context 中已包含
4. **交互输入** — 以上都无时提示用户输入

### 配置指导

**方式一：环境变量（临时，推荐快速测试）**

```bash
export BLOG_MINI_YAW_KIT_BASE_URL="http://<host>:<port>"  # (示例)
```

**方式二：项目知识 JSON 文件（持久化，推荐生产使用）**

在项目根目录下创建 `.project-info/` 目录，放入任意名称的 `.json` 文件（脚本会递归扫描所有 JSON 文件）：

```json
{
  "config": {
    "BLOG_MINI_YAW_KIT_BASE_URL": "http://<host>:<port>"
  }
}
```

> key 必须按 `BLOG_MINI_YAW_KIT_` 前缀命名（由 skill name 推导），避免与其他系统凭据冲突。
> ⚠️ `.project-info/` 含敏感配置，不提交到 git 仓库（加入 .gitignore）。

## 场景 / When to Use

- 用户要求查询/发布/编辑/删除博客文章
- 用户要求管理博客标签、用户、评论
- 用户要求管理留言板（留言/回复）
- 用户要求管理说说（mood）
- 用户要求上传/管理文件
- 用户要求管理员登录并批量删除文章
- 用户要求检查博客系统 API 健康状态

Don't use for: 非 Blog System API 的操作 / 数据库直连操作 / 前端页面渲染（HTML 端点仅供文档参考，不生成子命令）

## 知识 / Knowledge

### API Base URL

```
{base_url}
```

All endpoints below are relative to this base. 无认证（公开 API），不需要 header。
后台管理端点（/admin/*）需要 session cookie（通过 admin-login 获取）。

### Endpoints（32 个，按业务域分组）

#### 文章 Articles（7）

| Subcommand | Method | Path | Description |
|------------|--------|------|-------------|
| list-articles | GET | /api/articles | 文章列表（分页/筛选） |
| create-article | POST | /api/articles | 创建文章 |
| get-article | GET | /api/articles/{article_id} | 获取单篇文章 |
| update-article | PUT | /api/articles/{article_id} | 更新文章 |
| delete-article | DELETE | /api/articles/{article_id} | 删除文章（软/硬） |
| restore-article | POST | /api/articles/{article_id}/restore | 恢复软删文章 |
| top-articles | GET | /api/articles/heat/top | 热度排行 |

#### 标签 Labels（2）

| Subcommand | Method | Path | Description |
|------------|--------|------|-------------|
| list-labels | GET | /api/lables | 标签列表（API 路径为 lables） |
| create-label | POST | /api/lables | 创建标签（API 路径为 lables） |

#### 用户 Users（2）

| Subcommand | Method | Path | Description |
|------------|--------|------|-------------|
| list-users | GET | /api/users | 用户列表 |
| create-user | POST | /api/users | 创建用户 |

#### 评论 Comments（3）

| Subcommand | Method | Path | Description |
|------------|--------|------|-------------|
| create-comment | POST | /api/comments | 创建评论 |
| list-comments | GET | /api/comments/{aid} | 文章评论列表 |
| delete-comment | DELETE | /api/comments/{comment_id} | 删除评论 |

#### 留言 Messages（4）

| Subcommand | Method | Path | Description |
|------------|--------|------|-------------|
| list-messages | GET | /api/messages | 留言列表 |
| create-message | POST | /api/messages | 创建留言 |
| reply-message | POST | /api/messages/reply | 回复留言 |
| delete-message | DELETE | /api/messages/{message_id} | 删除留言 |

#### 说说 Moods（3）

| Subcommand | Method | Path | Description |
|------------|--------|------|-------------|
| list-moods | GET | /api/moods | 说说列表 |
| create-mood | POST | /api/moods | 创建说说 |
| delete-mood | DELETE | /api/moods/{mood_id} | 删除说说 |

#### 文件上传 File Upload（4）

| Subcommand | Method | Path | Description |
|------------|--------|------|-------------|
| upload-file | POST | /api/upload | 上传单文件（multipart） |
| upload-files | POST | /api/upload/multiple | 批量上传（multipart） |
| list-uploads | GET | /api/uploads/list | 已上传文件列表 |
| delete-upload | DELETE | /api/uploads/{filename} | 删除已上传文件 |

#### 前端页面 Frontend Pages（2，HTML 页面，无子命令）

| Method | Path | Description |
|--------|------|-------------|
| GET | / | 博客首页（HTML） |
| GET | /article/{article_id} | 文章详情页（HTML） |

#### 后台管理 Admin（4）

| Subcommand | Method | Path | Description |
|------------|--------|------|-------------|
| — | GET | /admin | 管理后台页面（HTML，无子命令） |
| admin-login | POST | /admin/login | 管理员登录（form-data，设 session cookie） |
| admin-logout | GET | /admin/logout | 管理员登出 |
| admin-delete-articles | POST | /admin/api/delete | 批量删除文章（需 session） |

#### 健康检查 Health（1）

| Subcommand | Method | Path | Description |
|------------|--------|------|-------------|
| health-check | GET | /health | API 健康检查 |

### 认证方式

- **无认证**：公开 API，不需要凭据
- **API 地址**：`BLOG_MINI_YAW_KIT_BASE_URL`
- **凭据前缀**：由 skill name 推导（`blog-mini-yaw-kit` → `BLOG_MINI_YAW_KIT`）
- **后台管理**：admin-login 通过 form-data 登录获取 session cookie，后续 admin-* 命令自动携带（脚本内部 requests.Session 持久化）

### Common Pitfalls

1. **API 路径拼写「lables」**（非 labels）。子命令用正确拼写 list-labels/create-label，但脚本内部请求 /api/lables。
2. **delete-article 的 soft 参数**：soft=true 软删除（可 restore），soft=false 硬删除（不可恢复）。参数为 query string。
3. **admin 端点需先登录**：admin-login 返回 302 + Set-Cookie。未登录时 admin-delete-articles 返回 `{"code":401,"message":"未登录或登录已过期"}`（HTTP 200）。
4. **文件上传用 multipart**：upload-file 用 `files={'file': f}`，upload-files 用 `files=[('files', f) for f in files]`（元组列表，不能用 dict value 为列表）。
5. **响应包裹格式**：列表类端点返回 `{"code":200,"data":[...],"total":N,"page":N,"size":N}`，非列表返回 `{"code":200,"data":{...}}`，health 返回 `{"status":"ok"}`。

### 字段说明

| 字段 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| title | string | 是（create） | — | 文章标题 |
| content | string | 是（create/article/mood） | — | 内容 |
| uid | integer | 否 | — | 用户 ID |
| lid | integer | 否 | — | 标签 ID |
| img | string | 否 | — | 图片 URL |
| heat | integer | 否 | — | 热度值 |
| uname | string | 是（create-user） | — | 用户名 |
| phone | string | 否 | — | 手机号 |
| pwd | string | 否 | — | 密码 |
| email | string | 否 | — | 邮箱 |
| lname | string | 是（create-label） | — | 标签名 |
| aid | integer | 是（comment） | — | 文章 ID |
| mid | integer | 是（reply） | — | 被回复留言 ID |
| src | string | 否 | — | 配图 URL |
| soft | boolean | 否 | — | 软删除标记 |
| limit | integer | 否 | — | 返回条数限制 |

## 步骤 / Steps

### 1. 检查 API 可达性

```bash
python3 scripts/blog-mini-yaw-kit.py health-check
```
Expected: `{"status":"ok","service":"blog-api","version":"1.0.0"}`

### 2. 查询可用资源

#### list-articles
```bash
python3 scripts/blog-mini-yaw-kit.py list-articles --page 1 --size 10
```
Expected: `{"code":200,"data":[...],"total":N,"page":1,"size":10}`

参数：`--page`（页码）`--size`（每页条数）`--lid`（标签筛选）`--keyword`（关键词）

#### list-labels
```bash
python3 scripts/blog-mini-yaw-kit.py list-labels
```
Expected: `{"code":200,"data":[{"id":1,"lname":"技术"},...]}`

#### list-users
```bash
python3 scripts/blog-mini-yaw-kit.py list-users
```
Expected: `{"code":200,"data":[{"id":1,"uname":"admin",...}]}`

#### list-messages / list-moods / list-uploads
```bash
python3 scripts/blog-mini-yaw-kit.py list-messages
python3 scripts/blog-mini-yaw-kit.py list-moods
python3 scripts/blog-mini-yaw-kit.py list-uploads
```
Expected: `{"code":200,"data":[...]}`

#### top-articles
```bash
python3 scripts/blog-mini-yaw-kit.py top-articles --limit 5
```
Expected: `{"code":200,"data":[...]}`

### 3. 执行操作

#### create-article
```bash
python3 scripts/blog-mini-yaw-kit.py create-article --title "标题" --content "内容" --uid 1 --lid 1
```
Expected: `{"code":200,"data":{"id":N,...}}`
参数：`--title`（必填）`--content`（必填）`--uid` `--lid` `--img` `--heat`

#### get-article
```bash
python3 scripts/blog-mini-yaw-kit.py get-article --article-id 1
```
Expected: `{"code":200,"data":{"id":1,...}}`

#### update-article
```bash
python3 scripts/blog-mini-yaw-kit.py update-article --article-id 1 --title "新标题"
```
Expected: `{"code":200,"data":{"id":1,...}}`
参数：`--article-id`（必填）`--title` `--content` `--lid` `--img` `--heat`（均可选）

#### delete-article
```bash
python3 scripts/blog-mini-yaw-kit.py delete-article --article-id 1 --soft true
```
Expected: `{"code":200,"message":"删除成功"}`
参数：`--soft`（true 软删/false 硬删）

#### restore-article
```bash
python3 scripts/blog-mini-yaw-kit.py restore-article --article-id 1
```
Expected: `{"code":200,"message":"恢复成功"}`

#### create-label
```bash
python3 scripts/blog-mini-yaw-kit.py create-label --lname "新标签"
```
Expected: `{"code":200,"data":{"id":N,"lname":"新标签"}}`

#### create-user
```bash
python3 scripts/blog-mini-yaw-kit.py create-user --uname "user1" --phone "13800000000" --pwd "pass" --email "u@e.com"
```
Expected: `{"code":200,"data":{"id":N,...}}`

#### create-comment
```bash
python3 scripts/blog-mini-yaw-kit.py create-comment --uid 1 --aid 1 --content "好文"
```
Expected: `{"code":200,"data":{"id":N,...}}`

#### list-comments
```bash
python3 scripts/blog-mini-yaw-kit.py list-comments --aid 1
```
Expected: `{"code":200,"data":[...]}`

#### delete-comment
```bash
python3 scripts/blog-mini-yaw-kit.py delete-comment --comment-id 1
```
Expected: `{"code":200,"message":"删除成功"}`

#### create-message
```bash
python3 scripts/blog-mini-yaw-kit.py create-message --uid 1 --content "留言内容"
```
Expected: `{"code":200,"data":{"id":N,...}}`

#### reply-message
```bash
python3 scripts/blog-mini-yaw-kit.py reply-message --uid 1 --mid 1 --content "回复内容"
```
Expected: `{"code":200,"data":{"id":N,...}}`

#### delete-message
```bash
python3 scripts/blog-mini-yaw-kit.py delete-message --message-id 1
```
Expected: `{"code":200,"message":"删除成功"}`

#### create-mood
```bash
python3 scripts/blog-mini-yaw-kit.py create-mood --content "今天心情不错" --title "日记"
```
Expected: `{"code":200,"data":{"id":N,...}}`

#### delete-mood
```bash
python3 scripts/blog-mini-yaw-kit.py delete-mood --mood-id 1
```
Expected: `{"code":200,"message":"删除成功"}`

#### upload-file
```bash
python3 scripts/blog-mini-yaw-kit.py upload-file --file /path/to/image.png
```
Expected: `{"code":200,"data":{"url":"...","filename":"..."}}`

#### upload-files
```bash
python3 scripts/blog-mini-yaw-kit.py upload-files --files /path/a.png /path/b.png
```
Expected: `{"code":200,"data":[{"url":"...",...},...]}`

#### delete-upload
```bash
python3 scripts/blog-mini-yaw-kit.py delete-upload --filename image.png
```
Expected: `{"code":200,"message":"删除成功"}`

#### admin-login
```bash
python3 scripts/blog-mini-yaw-kit.py admin-login --username admin --password admin
```
Expected: `{"status_code":302,"cookies_set":{"session":"..."}}`

#### admin-logout
```bash
python3 scripts/blog-mini-yaw-kit.py admin-logout
```
Expected: `{"status_code":302,...}`

#### admin-delete-articles
```bash
python3 scripts/blog-mini-yaw-kit.py admin-delete-articles --ids 1 2 3
```
Expected: `{"code":200,"message":"删除成功"}`（需先 admin-login）

#### capability-list
```bash
python3 scripts/blog-mini-yaw-kit.py capability-list
```
Expected: `{"capability":"capability-list","subcommand_count":29,"endpoint_count":32,...}`

## 判断标准 / Verification

- [ ] API 可达（health-check 返回 `{"status":"ok"}`）
- [ ] 只读操作返回有效数据（list-articles/list-labels/list-users 返回 code 200）
- [ ] 脚本 --help 无语法错误（30 个子命令全部列出）
- [ ] 退出码正确（0=成功/2=参数错误/3=缺少配置/4=API失败）
- [ ] 文件上传 multipart 正确（upload-file/upload-files 返回 url）
- [ ] admin-login 获取 session cookie（302 + cookies_set）
- [ ] --format md 输出 Markdown 表格

## 输出规范 / Output Format

### 脚本输出

- 默认输出：JSON
- 可选输出：Markdown 表格（`--format md`）
- 使用示例：`cd skills/blog-mini-yaw-kit/ && python3 scripts/blog-mini-yaw-kit.py list-articles --format md`

### Issue 评论格式

```
[blog-mini-yaw-kit] ✅ {操作名称}完成

## 操作结果

| 操作 | 状态 | 资源 ID | 详情 |
|------|------|---------|------|
| {操作名} | ✅ 成功 / 🔴 失败 | {id} | {简要说明} |

**API 地址**：{base_url}
**执行时间**：{UTC ISO}
```

失败时：

```
[blog-mini-yaw-kit] 🔴 {操作名称}失败

## 错误分析

- **操作**：{操作名}
- **错误**：{API 返回的错误信息}
- **HTTP 状态码**：{code}
- **原因**：{分析原因}

### 修复建议
{修复步骤}
```

## 参考文档 / References

- [API 端点文档](references/api-reference.md) — 32 端点完整文档（方法/路径/参数/请求体/curl 示例/响应说明）
- [测试用例](templates/test-vars.json) — 10 个测试用例（9 只读 + 1 变更含 cleanup）

## 分析结论示例

成功时：

```
分析结论：
- 场景：博客 API 操作（A2A 触发，Issue Agent 交棒 Coding Agent）
- Skill：blog-mini-yaw-kit v0.1.0
- 操作：list-articles --page 1 --size 10
- 结果：✅ 成功（返回 0 篇文章，total=0）
- 必须执行：创建 PR → A2A 交棒 QA
```

失败时：

```
分析结论：
- 场景：博客 API 操作
- Skill：blog-mini-yaw-kit v0.1.0
- 操作：get-article --article-id 999
- 结果：🔴 失败（文章不存在）
- 必须执行：Issue 评论报告错误 → 任务结束
```

## 任务结束

完成所有业务动作后，在最终答复末尾输出以下 JSON 块并结束任务：

```json
{
  "actions": ["{具体执行的操作，如 list-articles: 返回 N 篇文章}"],
  "conclusion": "{处理结论，如 查询成功，返回 N 篇文章}",
  "artifacts": ["{产生的产物：写操作返回资源 ID 或操作结果 / 只读查询无产物填空数组}"],
  "next_step": "{下一步建议，如 无 / 等待用户下一步指令}",
  "issue_summary": "{Issue 最新聚合结论，紧凑文本，用 | 分隔}"
}
```

注意：只输出一个 JSON 块，放在答复末尾。

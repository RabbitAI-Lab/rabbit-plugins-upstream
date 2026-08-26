# Blog System API — 端点参考文档

> Blog System API (FastAPI) v1.0.0 — 全部 32 个端点完整文档。
> 认证方式：无认证（公开 API）。后台管理端点（/admin/*）需 session cookie。
> 所有 curl 示例中 `{base_url}` 替换为实际 API 地址（格式 `http://<host>:<port>`）（示例）。

## 目录

| 分组 | 端点数 | 说明 |
|------|--------|------|
| [文章 Articles](#文章-articles7) | 7 | 文章 CRUD + 恢复 + 热度排行 |
| [标签 Labels](#标签-labels2) | 2 | 标签列表 + 创建（API 路径 lables） |
| [用户 Users](#用户-users2) | 2 | 用户列表 + 创建 |
| [评论 Comments](#评论-comments3) | 3 | 评论创建 + 列表 + 删除 |
| [留言 Messages](#留言-messages4) | 4 | 留言 CRUD + 回复 |
| [说说 Moods](#说说-moods3) | 3 | 说说 CRUD（无更新） |
| [文件上传 File Upload](#文件上传-file-upload4) | 4 | 上传 + 列表 + 删除 |
| [前端页面 Frontend Pages](#前端页面-frontend-pages2) | 2 | HTML 页面（无子命令） |
| [后台管理 Admin](#后台管理-admin4) | 4 | 管理后台页面 + 登录/登出 + 批量删除 |
| [健康检查 Health](#健康检查-health1) | 1 | API 健康状态 |

**合计：32 个端点**

---

## 文章 Articles（7）

### 1. GET /api/articles — 文章列表

分页查询文章列表，支持按标签和关键词筛选。

**Query 参数**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| page | integer | 否 | 1 | 页码 |
| size | integer | 否 | 10 | 每页条数 |
| lid | integer | 否 | — | 标签 ID 筛选 |
| keyword | string | 否 | — | 关键词搜索 |

**curl 示例**

```bash
curl -s --max-time 30 "{base_url}/api/articles?page=1&size=10&lid=1&keyword=技术"
```

**响应说明**

```json
{
  "code": 200,
  "data": [
    {"id": 1, "title": "文章标题", "content": "...", "uid": 1, "lid": 1, "img": "...", "heat": 0, "createtime": "2026-08-24T23:14:07"}
  ],
  "total": 100,
  "page": 1,
  "size": 10
}
```

### 2. POST /api/articles — 创建文章

**请求体**（`application/json`，Schema: ArticleCreate）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| title | string | 是 | 文章标题 |
| content | string | 是 | 文章内容 |
| uid | integer | 否 | 作者用户 ID |
| lid | integer | 否 | 标签 ID |
| img | string | 否 | 封面图 URL |
| heat | integer | 否 | 热度值 |

**curl 示例**

```bash
curl -s --max-time 30 -X POST "{base_url}/api/articles" \
  -H "Content-Type: application/json" \
  -d '{"title":"我的文章","content":"正文内容","uid":1,"lid":1,"img":"img/cover.jpg","heat":0}'
```

**响应说明**

```json
{"code": 200, "data": {"id": 5, "title": "我的文章", "content": "正文内容", ...}}
```

### 3. GET /api/articles/{article_id} — 获取单篇文章

**Path 参数**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| article_id | integer | 是 | 文章 ID |

**curl 示例**

```bash
curl -s --max-time 30 "{base_url}/api/articles/1"
```

**响应说明**

```json
{"code": 200, "data": {"id": 1, "title": "...", "content": "...", "uid": 1, "lid": 1, "img": "...", "heat": 10, "createtime": "..."}}
```

文章不存在时：`{"detail": "文章不存在"}`

### 4. PUT /api/articles/{article_id} — 更新文章

**Path 参数**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| article_id | integer | 是 | 文章 ID |

**请求体**（`application/json`，Schema: ArticleUpdate，所有字段可选）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| title | string | 否 | 文章标题 |
| content | string | 否 | 文章内容 |
| lid | integer | 否 | 标签 ID |
| img | string | 否 | 封面图 URL |
| heat | integer | 否 | 热度值 |

**curl 示例**

```bash
curl -s --max-time 30 -X PUT "{base_url}/api/articles/1" \
  -H "Content-Type: application/json" \
  -d '{"title":"更新标题","heat":100}'
```

**响应说明**

```json
{"code": 200, "data": {"id": 1, "title": "更新标题", ...}}
```

### 5. DELETE /api/articles/{article_id} — 删除文章

支持软删除（可恢复）和硬删除（不可恢复）。

**Path 参数**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| article_id | integer | 是 | 文章 ID |

**Query 参数**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| soft | boolean | 否 | — | true=软删除（可 restore），false=硬删除 |

**curl 示例**

```bash
# 软删除
curl -s --max-time 30 -X DELETE "{base_url}/api/articles/1?soft=true"

# 硬删除
curl -s --max-time 30 -X DELETE "{base_url}/api/articles/1?soft=false"
```

**响应说明**

```json
{"code": 200, "message": "删除成功"}
```

### 6. POST /api/articles/{article_id}/restore — 恢复软删文章

恢复被软删除的文章。

**Path 参数**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| article_id | integer | 是 | 文章 ID |

**curl 示例**

```bash
curl -s --max-time 30 -X POST "{base_url}/api/articles/1/restore"
```

**响应说明**

```json
{"code": 200, "message": "恢复成功"}
```

### 7. GET /api/articles/heat/top — 热度排行

按热度（heat）降序返回热门文章。

**Query 参数**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| limit | integer | 否 | — | 返回条数 |

**curl 示例**

```bash
curl -s --max-time 30 "{base_url}/api/articles/heat/top?limit=10"
```

**响应说明**

```json
{"code": 200, "data": [{"id": 1, "title": "...", "heat": 100, ...}]}
```

---

## 标签 Labels（2）

> ⚠️ API 路径使用「lables」（拼写错误），子命令使用正确拼写 labels。

### 8. GET /api/lables — 标签列表

**curl 示例**

```bash
curl -s --max-time 30 "{base_url}/api/lables"
```

**响应说明**

```json
{
  "code": 200,
  "data": [
    {"id": 1, "lname": "技术"},
    {"id": 2, "lname": "生活"},
    {"id": 3, "lname": "随笔"},
    {"id": 4, "lname": "教程"}
  ]
}
```

### 9. POST /api/lables — 创建标签

**请求体**（`application/json`，Schema: LableCreate）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| lname | string | 是 | 标签名称 |

**curl 示例**

```bash
curl -s --max-time 30 -X POST "{base_url}/api/lables" \
  -H "Content-Type: application/json" \
  -d '{"lname":"新标签"}'
```

**响应说明**

```json
{"code": 200, "data": {"id": 5, "lname": "新标签"}}
```

---

## 用户 Users（2）

### 10. GET /api/users — 用户列表

**curl 示例**

```bash
curl -s --max-time 30 "{base_url}/api/users"
```

**响应说明**

```json
{
  "code": 200,
  "data": [
    {"id": 1, "uname": "admin", "phone": "admin", "img": "img/moren.jpg", "email": "admin@blog.com", "address": "", "profession": "", "createtime": "2026-08-24T23:14:07"}
  ]
}
```

### 11. POST /api/users — 创建用户

**请求体**（`application/json`，Schema: UserCreate）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| uname | string | 是 | 用户名 |
| phone | string | 否 | 手机号 |
| pwd | string | 否 | 密码 |
| email | string | 否 | 邮箱 |
| img | string | 否 | 头像 URL |

**curl 示例**

```bash
curl -s --max-time 30 -X POST "{base_url}/api/users" \
  -H "Content-Type: application/json" \
  -d '{"uname":"newuser","phone":"13800000000","pwd":"pass123","email":"user@e.com","img":"img/moren.jpg"}'
```

**响应说明**

```json
{"code": 200, "data": {"id": 2, "uname": "newuser", ...}}
```

---

## 评论 Comments（3）

### 12. POST /api/comments — 创建评论

**请求体**（`application/json`，Schema: CommentCreate）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| uid | integer | 是 | 用户 ID |
| aid | integer | 是 | 文章 ID |
| content | string | 是 | 评论内容 |

**curl 示例**

```bash
curl -s --max-time 30 -X POST "{base_url}/api/comments" \
  -H "Content-Type: application/json" \
  -d '{"uid":1,"aid":1,"content":"好文章！"}'
```

**响应说明**

```json
{"code": 200, "data": {"id": 1, "uid": 1, "aid": 1, "content": "好文章！", "createtime": "..."}}
```

### 13. GET /api/comments/{aid} — 文章评论列表

获取指定文章的评论列表。

**Path 参数**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| aid | integer | 是 | 文章 ID |

**curl 示例**

```bash
curl -s --max-time 30 "{base_url}/api/comments/1"
```

**响应说明**

```json
{"code": 200, "data": [{"id": 1, "uid": 1, "aid": 1, "content": "好文章！", "createtime": "..."}]}
```

### 14. DELETE /api/comments/{comment_id} — 删除评论

**Path 参数**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| comment_id | integer | 是 | 评论 ID |

**curl 示例**

```bash
curl -s --max-time 30 -X DELETE "{base_url}/api/comments/1"
```

**响应说明**

```json
{"code": 200, "message": "删除成功"}
```

---

## 留言 Messages（4）

### 15. GET /api/messages — 留言列表

**curl 示例**

```bash
curl -s --max-time 30 "{base_url}/api/messages"
```

**响应说明**

```json
{"code": 200, "data": [{"id": 1, "uid": 1, "content": "留言内容", "createtime": "...", "replies": [...]}]}
```

### 16. POST /api/messages — 创建留言

**请求体**（`application/json`，Schema: MessageCreate）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| uid | integer | 是 | 用户 ID |
| content | string | 是 | 留言内容 |

**curl 示例**

```bash
curl -s --max-time 30 -X POST "{base_url}/api/messages" \
  -H "Content-Type: application/json" \
  -d '{"uid":1,"content":"你好，留言板！"}'
```

**响应说明**

```json
{"code": 200, "data": {"id": 1, "uid": 1, "content": "你好，留言板！", "createtime": "..."}}
```

### 17. POST /api/messages/reply — 回复留言

回复指定的留言。

**请求体**（`application/json`，Schema: Message2Create）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| uid | integer | 是 | 用户 ID |
| mid | integer | 是 | 被回复留言 ID |
| content | string | 是 | 回复内容 |

**curl 示例**

```bash
curl -s --max-time 30 -X POST "{base_url}/api/messages/reply" \
  -H "Content-Type: application/json" \
  -d '{"uid":2,"mid":1,"content":"回复你了！"}'
```

**响应说明**

```json
{"code": 200, "data": {"id": 2, "uid": 2, "mid": 1, "content": "回复你了！", "createtime": "..."}}
```

### 18. DELETE /api/messages/{message_id} — 删除留言

**Path 参数**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| message_id | integer | 是 | 留言 ID |

**curl 示例**

```bash
curl -s --max-time 30 -X DELETE "{base_url}/api/messages/1"
```

**响应说明**

```json
{"code": 200, "message": "删除成功"}
```

---

## 说说 Moods（3）

### 19. GET /api/moods — 说说列表

**curl 示例**

```bash
curl -s --max-time 30 "{base_url}/api/moods"
```

**响应说明**

```json
{"code": 200, "data": [{"id": 1, "title": "日记", "content": "今天心情不错", "src": "img/mood.jpg", "createtime": "..."}]}
```

### 20. POST /api/moods — 创建说说

**请求体**（`application/json`，Schema: MoodCreate）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| title | string | 否 | 标题 |
| content | string | 是 | 内容 |
| src | string | 否 | 配图 URL |

**curl 示例**

```bash
curl -s --max-time 30 -X POST "{base_url}/api/moods" \
  -H "Content-Type: application/json" \
  -d '{"title":"日记","content":"今天心情不错","src":"img/mood.jpg"}'
```

**响应说明**

```json
{"code": 200, "data": {"id": 1, "title": "日记", "content": "今天心情不错", "src": "img/mood.jpg", "createtime": "..."}}
```

### 21. DELETE /api/moods/{mood_id} — 删除说说

**Path 参数**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| mood_id | integer | 是 | 说说 ID |

**curl 示例**

```bash
curl -s --max-time 30 -X DELETE "{base_url}/api/moods/1"
```

**响应说明**

```json
{"code": 200, "message": "删除成功"}
```

---

## 文件上传 File Upload（4）

### 22. POST /api/upload — 上传单文件

上传单个文件（图片/视频），返回文件 URL。

**请求体**（`multipart/form-data`，Schema: Body_upload_file_api_upload_post）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| file | string (binary) | 是 | 文件内容 |

**curl 示例**

```bash
curl -s --max-time 30 -X POST "{base_url}/api/upload" \
  -F "file=@/path/to/image.png"
```

**响应说明**

```json
{"code": 200, "data": {"url": "uploads/2026/08/24/uuid-image.png", "filename": "image.png"}}
```

### 23. POST /api/upload/multiple — 批量上传

批量上传多个文件。

**请求体**（`multipart/form-data`，Schema: Body_upload_files_api_upload_multiple_post）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| files | array (binary) | 是 | 文件列表 |

**curl 示例**

```bash
curl -s --max-time 30 -X POST "{base_url}/api/upload/multiple" \
  -F "files=@/path/to/a.png" \
  -F "files=@/path/to/b.png"
```

**响应说明**

```json
{"code": 200, "data": [{"url": "uploads/.../a.png", ...}, {"url": "uploads/.../b.png", ...}]}
```

### 24. GET /api/uploads/list — 已上传文件列表

**curl 示例**

```bash
curl -s --max-time 30 "{base_url}/api/uploads/list"
```

**响应说明**

```json
{"code": 200, "data": [{"filename": "image.png", "url": "uploads/.../image.png", "size": 102400}]}
```

### 25. DELETE /api/uploads/{filename} — 删除已上传文件

**Path 参数**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| filename | string | 是 | 文件名 |

**curl 示例**

```bash
curl -s --max-time 30 -X DELETE "{base_url}/api/uploads/image.png"
```

**响应说明**

```json
{"code": 200, "message": "删除成功"}
```

---

## 前端页面 Frontend Pages（2）

> HTML 页面端点，不生成子命令。仅供文档参考。

### 26. GET / — 博客首页

渲染博客首页 HTML，支持分页和标签筛选。

**Query 参数**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| page | integer | 否 | 页码 |
| lid | integer | 否 | 标签 ID 筛选 |
| keyword | string | 否 | 关键词搜索 |

**curl 示例**

```bash
curl -s --max-time 30 "{base_url}/?page=1&lid=1"
```

**响应说明**

返回 HTML 页面（`text/html`）。

### 27. GET /article/{article_id} — 文章详情页

渲染单篇文章详情页 HTML。

**Path 参数**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| article_id | integer | 是 | 文章 ID |

**curl 示例**

```bash
curl -s --max-time 30 "{base_url}/article/1"
```

**响应说明**

返回 HTML 页面（`text/html`）。

---

## 后台管理 Admin（4）

> 后台管理端点需要 session cookie。先调用 admin-login 获取 cookie，后续 admin-* 请求自动携带。

### 28. GET /admin — 管理后台页面

渲染管理后台 HTML 页面（需登录）。

**curl 示例**

```bash
curl -s --max-time 30 "{base_url}/admin"
```

**响应说明**

返回 HTML 页面（`text/html`）。未登录时重定向到登录页。

### 29. POST /admin/login — 管理员登录

使用表单数据登录，成功后返回 302 重定向并设置 session cookie。

**请求体**（`application/x-www-form-urlencoded`）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| username | string | 是 | 管理员用户名 |
| password | string | 是 | 管理员密码 |

**curl 示例**

```bash
curl -s --max-time 30 -X POST "{base_url}/admin/login" \
  -d "username=admin&password=admin" \
  -c cookies.txt -L
```

**响应说明**

- 成功：HTTP 302 重定向到 /admin，设置 Set-Cookie（session）
- 失败：HTTP 401 或重定向回登录页

### 30. GET /admin/logout — 管理员登出

清除 session cookie，登出管理后台。

**Query 参数**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| t | string | 否 | 可选 token 参数 |

**curl 示例**

```bash
curl -s --max-time 30 "{base_url}/admin/logout" -b cookies.txt
```

**响应说明**

HTTP 302 重定向到登录页，清除 session cookie。

### 31. POST /admin/api/delete — 批量删除文章

管理员批量删除文章（需登录 session）。

**请求体**（`application/json`）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| ids | array (integer) | 是 | 文章 ID 列表 |

**curl 示例**

```bash
curl -s --max-time 30 -X POST "{base_url}/admin/api/delete" \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d '{"ids":[1,2,3]}'
```

**响应说明**

- 已登录：`{"code":200,"message":"删除成功"}`
- 未登录：`{"code":401,"message":"未登录或登录已过期"}`（HTTP 200，body 中 code=401）

---

## 健康检查 Health（1）

### 32. GET /health — API 健康检查

检查 API 服务是否正常运行。

**curl 示例**

```bash
curl -s --max-time 30 "{base_url}/health"
```

**响应说明**

```json
{"status": "ok", "service": "blog-api", "version": "1.0.0"}
```

---

## Schema 定义（12 个）

### ArticleCreate

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| title | string | 是 | 文章标题 |
| content | string | 是 | 文章内容 |
| uid | integer | 否 | 作者用户 ID |
| lid | integer | 否 | 标签 ID |
| img | string \| null | 否 | 封面图 URL |
| heat | integer | 否 | 热度值 |

### ArticleUpdate

所有字段可选（部分更新）。

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| title | string \| null | 否 | 文章标题 |
| content | string \| null | 否 | 文章内容 |
| lid | integer \| null | 否 | 标签 ID |
| img | string \| null | 否 | 封面图 URL |
| heat | integer \| null | 否 | 热度值 |

### CommentCreate

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| uid | integer | 是 | 用户 ID |
| aid | integer | 是 | 文章 ID |
| content | string | 是 | 评论内容 |

### LableCreate

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| lname | string | 是 | 标签名称 |

### MessageCreate

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| uid | integer | 是 | 用户 ID |
| content | string | 是 | 留言内容 |

### Message2Create

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| uid | integer | 是 | 用户 ID |
| mid | integer | 是 | 被回复留言 ID |
| content | string | 是 | 回复内容 |

### MoodCreate

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| title | string | 否 | 标题 |
| content | string | 是 | 内容 |
| src | string | 否 | 配图 URL |

### UserCreate

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| uname | string | 是 | 用户名 |
| phone | string | 否 | 手机号 |
| pwd | string | 否 | 密码 |
| email | string | 否 | 邮箱 |
| img | string | 否 | 头像 URL |

### Body_upload_file_api_upload_post

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| file | string (binary) | 是 | 单文件内容 |

### Body_upload_files_api_upload_multiple_post

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| files | array (binary) | 是 | 多文件列表 |

### HTTPValidationError

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| detail | array | 否 | 验证错误详情 |

### ValidationError

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| loc | array | 是 | 错误位置 |
| msg | string | 是 | 错误消息 |
| type | string | 是 | 错误类型 |

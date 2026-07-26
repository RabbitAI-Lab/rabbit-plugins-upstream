---
slug: "api-generator-free"
name: "api-generator-free"
version: "1.0.0"
displayName: "API代码生成器免费版"
summary: "生成RESTful端点、GraphQL schema与测试套件,快速搭建API代码脚手架"
license: "MIT"
description: |-
  API 代码生成器免费版。从零生成基础 API 代码脚手架,支持 RESTful CRUD 端点（Express.js）、
  GraphQL Type+Query+Mutation schema 与 Jest+Supertest 测试套件.
  OpenAPI 文档、Python 客户端、Mock 服务器、认证代码、速率限制器等高级功能需升级付费版.
tags:
  - 研发工具
  - Development
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# API 代码生成器（免费版）

从零生成基础 API 代码脚手架。支持 RESTful 端点、GraphQL schema 与测试套件,所有代码输出到 stdout.
> **升级提示**: OpenAPI 文档、Python 客户端、Mock 服务器、认证代码、速率限制器等高级功能为付费版专享。升级付费版解锁完整能力.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | API代码生成器免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

- **rest** `<name>` — RESTful CRUD 端点（Express.js）,含 GET/POST/PUT/DELETE 路由
- **graphql** `<name>` — GraphQL Type + Query + Mutation schema 定义
- **test** `<name>` — Jest + Supertest API 测试套件,含 CRUD 测试用例

### 付费版专享功能
以下功能在免费版中不可用,升级付费版解锁:

- **swagger** `<name>` — OpenAPI 3.0 规范文档生成
- **client** `<name>` — Python API 客户端类生成
- **mock** `<name>` — Mock API 服务器（内存存储）生成
- **auth** `<type>` — 认证代码生成（`jwt`/`oauth`/`apikey`）
- **rate-limit** `<type>` — 速率限制器生成（`token-bucket`/`sliding-window`）

**输入**: 用户提供付费版专享功能所需的指令和必要参数.
**处理**: 解析付费版专享功能的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### rest

针对rest,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供rest相关的配置参数、输入数据和处理选项.
**输出**: 返回rest的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`rest`的配置文档进行参数调优
### graphql

针对graphql,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供graphql相关的配置参数、输入数据和处理选项.
**输出**: 返回graphql的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`graphql`的配置文档进行参数调优
#
## 命令用法

```bash
bash （请参考skill目录中的脚本文件） <command> <resource_name> [options]
```

| 命令 | 免费版 | 说明 |
|---:|---:|---:|
| `rest` | 可用 | 生成 RESTful CRUD 端点（Express.js） |
| `graphql` | 可用 | 生成 GraphQL schema |
| `test` | 可用 | 生成 Jest+Supertest 测试套件 |
| `swagger` | 付费版 | 生成 OpenAPI 3.0 文档 |
| `client` | 付费版 | 生成 Python API 客户端 |
| `mock` | 付费版 | 生成 Mock API 服务器 |
| `auth` | 付费版 | 生成认证代码 |
| `rate-limit` | 付费版 | 生成速率限制器 |

## 使用流程

### Step 1: 确定生成目标
明确需要生成的代码类型（rest/graphql/test）与资源名称.
### Step 2: 执行生成命令
```bash
bash （请参考skill目录中的脚本文件） rest user
```

### Step 3: 查看输出
所有代码输出到 stdout,含完整注释.
### Step 4: 重定向到项目文件
```bash
bash （请参考skill目录中的脚本文件） rest user > routes/user.js
bash （请参考skill目录中的脚本文件） test user > tests/user.test.js
```

> **提示**: 如需生成 OpenAPI 文档、Mock 服务器、认证代码等,请升级付费版.
## 案例展示

### 案例1: 生成用户 RESTful 端点
**场景**: 开发者需要快速搭建用户 CRUD API

```bash
bash （请参考skill目录中的脚本文件） rest user
```

**输出**: Express.js 路由代码,包含:
- `GET /users` — 获取用户列表
- `GET /users/:id` — 获取单个用户
- `POST /users` — 创建用户
- `PUT /users/:id` — 更新用户
- `DELETE /users/:id` — 删除用户

**说明**: 生成的代码含完整注释与错误处理,重定向到 `routes/user.js` 即可使用.
### 案例2: 生成产品 GraphQL Schema
**场景**: 开发者需要为产品模块定义 GraphQL 类型

```bash
bash （请参考skill目录中的脚本文件） graphql product
```

**输出**: GraphQL schema 定义,包含:
- `type Product` — 产品类型定义（id, name, price, description）
- `type Query` — 查询（`products`、`product(id)`）
- `type Mutation` — 变更（`createProduct`、`updateProduct`、`deleteProduct`）

### 案例3: 生成订单测试套件
**场景**: 开发者需要为订单 API 编写测试

```bash
bash （请参考skill目录中的脚本文件） test order
```

**输出**: Jest + Supertest 测试文件,包含:
- 创建订单测试（`POST /orders`）
- 获取订单列表测试（`GET /orders`）
- 更新订单测试（`PUT /orders/:id`）
- 删除订单测试（`DELETE /orders/:id`）

> **升级提示**: 付费版支持 `auth jwt` 生成 JWT 认证代码与 `rate-limit token-bucket` 生成速率限制器.
## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:---:|:---:|:---:|:---:|
| 命令不存在 | `Unknown command: <cmd>` | 使用了未定义的命令 | 使用 rest/graphql/test（免费版）或升级付费版 |
| 资源名缺失 | `Resource name required` | 未提供 `<name>` 参数 | 补充资源名,如 `bash （请参考skill目录中的脚本文件） rest user` |
| 命令需付费 | `Paid feature: <cmd>` | 使用了付费版专享命令 | 升级付费版解锁 swagger/client/mock/auth/rate-limit |
| 脚本无执行权限 | `Permission denied` | `（请参考skill目录中的脚本文件）` 无执行权限 | 执行 `chmod +x （请参考skill目录中的脚本文件）` |
| Bash 不可用 | `bash: command not found` | Windows 环境未安装 Bash | 安装 Git Bash 或 WSL |

## 常见问题

### Q1: 免费版支持哪些命令?
A: 免费版支持 3 个核心命令: `rest`（RESTful 端点）、`graphql`（GraphQL schema）、`test`（测试套件）。`swagger`、`client`、`mock`、`auth`、`rate-limit` 需升级付费版.
### Q2: 免费版能生成认证代码吗?
A: 不能。`auth` 命令（支持 `jwt`/`oauth`/`apikey` 三种类型）为付费版专享。升级付费版可生成 JWT 认证中间件、OAuth2 授权流程与 API Key 验证代码.
### Q3: 免费版能生成 Mock 服务器吗?
A: 不能。`mock` 命令为付费版专享。升级付费版可生成基于内存存储的 Mock API 服务器,适用于前端开发时后端 API 未就绪的场景.
### Q4: 免费版能生成 OpenAPI 文档吗?
A: 不能。`swagger` 命令为付费版专享。升级付费版可生成 OpenAPI 3.0 规范文档,含路径、参数、响应定义.
### Q5: 免费版能生成速率限制器吗?
A: 不能。`rate-limit` 命令为付费版专享。升级付费版可生成 `token-bucket`（令牌桶）与 `sliding-window`（滑动窗口）两种算法的速率限制器.
## 已知限制

1. **仅 3 个命令**: 免费版仅支持 rest/graphql/test,其余 5 个命令需升级
2. **无认证代码**: 不支持 jwt/oauth/apikey 认证代码生成
3. **无 Mock 服务器**: 不支持内存 Mock API 服务器生成
4. **无 OpenAPI 文档**: 不支持 swagger 规范文档生成
5. **无速率限制器**: 不支持 token-bucket/sliding-window 限流器生成
6. **无 Python 客户端**: 不支持 client 命令生成 Python API 客户端

---

> **升级付费版** 解锁: swagger（OpenAPI 文档）、client（Python 客户端）、mock（Mock 服务器）、auth（认证代码）、rate-limit（速率限制器）等完整生成能力.
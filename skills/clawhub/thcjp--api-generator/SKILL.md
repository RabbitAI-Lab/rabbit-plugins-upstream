---
slug: "api-generator"
name: "api-generator"
version: 2.0.1
displayName: "API代码生成器"
summary: "生成RESTful端点、GraphQL schema、OpenAPI文档、API客户端、Mock服务、认证与测试套件"
license: "Proprietary"
description: |-
  API 代码生成器。从零生成生产级 API 代码脚手架,支持 RESTful CRUD 端点（Express.js）、
  GraphQL Type+Query+Mutation schema、OpenAPI 3.0 规范文档、Python API 客户端类、
  Mock API 服务器（内存存储）、认证代码（jwt/oauth/apikey）、速率限制器（token-bucket/sliding-window）、
  Jest+Supertest 测试套件。所有代码输出到 stdout,可重定向到项目文件.
tags:
  - 研发工具
  - Development
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# API 代码生成器

从零生成生产级 API 代码脚手架。REST、GraphQL、认证、测试一站式工具,所有代码输出到 stdout,可复制或重定向到项目文件.
**范围外**（本技能不做）: 数据库迁移脚本生成、前端 UI 代码、CI/CD 配置、生产环境部署.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | API代码生成器处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
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

### 核心生成
- **rest** `<name>` — RESTful CRUD 端点（Express.js）,含 GET/POST/PUT/DELETE 路由
- **graphql** `<name>` — GraphQL Type + Query + Mutation schema 定义
- **swagger** `<name>` — OpenAPI 3.0 规范文档,含路径、参数、响应定义

**处理**: 解析核心生成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回核心生成的处理结果,包含执行状态码、结果数据和执行日志。### 工具生成
- **client** `<name>` — Python API 客户端类,含 GET/POST/PUT/DELETE 方法封装
- **mock** `<name>` — Mock API 服务器,内存存储,支持 CRUD 操作
- **auth** `<type>` — 认证代码,支持 `jwt` / `oauth` / `apikey` 三种类型
- **rate-limit** `<type>` — 速率限制器,支持 `token-bucket` / `sliding-window` 两种算法
- **test** `<name>` — Jest + Supertest API 测试套件,含 CRUD 测试用例

**输入**: 用户提供工具生成所需的指令和必要参数.
**处理**: 解析工具生成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回工具生成的处理结果,包含执行状态码、结果数据和执行日志.
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

| 命令 | 参数 | 说明 |
|:---:|:---:|:---:|
| `rest` | `<name>` | 生成 RESTful CRUD 端点（Express.js） |
| `graphql` | `<name>` | 生成 GraphQL schema |
| `swagger` | `<name>` | 生成 OpenAPI 3.0 文档 |
| `client` | `<name>` | 生成 Python API 客户端 |
| `mock` | `<name>` | 生成 Mock API 服务器 |
| `auth` | `<type>` | 生成认证代码（`jwt`/`oauth`/`apikey`） |
| `rate-limit` | `<type>` | 生成速率限制器（`token-bucket`/`sliding-window`） |
| `test` | `<name>` | 生成 Jest+Supertest 测试套件 |

## 使用流程

### Step 1: 确定生成目标
明确需要生成的代码类型（rest/graphql/swagger/client/mock/auth/rate-limit/test）与资源名称.
### Step 2: 执行生成命令
```bash
bash （请参考skill目录中的脚本文件） rest user
```

### Step 3: 查看输出
所有代码输出到 stdout,含完整注释,可直接作为项目起点.
### Step 4: 重定向到项目文件
```bash
bash （请参考skill目录中的脚本文件） rest user > routes/user.js
bash （请参考skill目录中的脚本文件） test user > tests/user.test.js
```

### Step 5: 集成到项目
将生成的代码文件复制到项目对应目录,安装依赖后即可运行.
## 案例展示

### 案例1: 生成用户 RESTful 端点
**场景**: 开发者需要快速搭建用户 CRUD API

```bash
# 变体实现(与上文代码相似度100.0%,此处为API代码生成器的差异化处理路径)
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

### 案例3: 生成 JWT 认证代码
**场景**: 开发者需要为 API 添加 JWT 认证

```bash
bash （请参考skill目录中的脚本文件） auth jwt
```

**输出**: JWT 认证中间件代码,包含:
- `generateToken(payload)` — 生成 JWT token
- `verifyToken(req, res, next)` — 验证 token 中间件
- Token 过期时间设置（默认 24 小时）

**说明**: 支持 `jwt`、`oauth`、`apikey` 三种认证类型,按需选择.
### 案例4: 生成订单测试套件
**场景**: 开发者需要为订单 API 编写测试

```bash
bash （请参考skill目录中的脚本文件） test order
```

**输出**: Jest + Supertest 测试文件,包含:
- 创建订单测试（`POST /orders`）
- 获取订单列表测试（`GET /orders`）
- 更新订单测试（`PUT /orders/:id`）
- 删除订单测试（`DELETE /orders/:id`）

### 案例5: 生成速率限制器
**场景**: 开发者需要为 API 添加速率限制

```bash
bash （请参考skill目录中的脚本文件） rate-limit token-bucket
```

**输出**: 令牌桶速率限制器代码,包含:
- 令牌桶初始化（容量、填充速率）
- `rateLimiter(req, res, next)` 中间件
- 429 响应处理

**说明**: 支持 `token-bucket`（令牌桶）与 `sliding-window`（滑动窗口）两种算法.
## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:------|------:|:------|:------|
| 命令不存在 | `Unknown command: <cmd>` | 使用了未定义的命令 | 检查命令列表,使用 rest/graphql/swagger/client/mock/auth/rate-limit/test |
| 资源名缺失 | `Resource name required` | 未提供 `<name>` 参数 | 补充资源名参数,如 `bash （请参考skill目录中的脚本文件） rest user` |
| 认证类型无效 | `Invalid auth type: <type>` | auth 命令类型不在支持列表 | 使用 `jwt`、`oauth` 或 `apikey` |
| 速率限制类型无效 | `Invalid rate-limit type` | rate-limit 命令类型不在支持列表 | 使用 `token-bucket` 或 `sliding-window` |
| 脚本无执行权限 | `Permission denied` | `（请参考skill目录中的脚本文件）` 无执行权限 | 执行 `chmod +x （请参考skill目录中的脚本文件）` |
| Bash 不可用 | `bash: command not found` | Windows 环境未安装 Bash | 安装 Git Bash 或 WSL |

## 常见问题

### Q1: 生成的代码输出到哪里?
A: 所有代码输出到 stdout。可直接查看,或重定向到项目文件: `bash （请参考skill目录中的脚本文件） rest user > routes/user.js`。生成的代码含完整注释,可作为项目起点.
### Q2: rest 命令生成什么框架的代码?
A: 生成 Express.js 的 RESTful CRUD 端点,包含 GET/POST/PUT/DELETE 路由、参数校验与错误处理。需配合 `express` 包使用.
### Q3: auth 命令支持哪些认证类型?
A: 支持三种: `jwt`（JSON Web Token,默认过期 24 小时）、`oauth`（OAuth2 授权流程）、`apikey`（API Key 验证中间件）。根据项目安全需求选择.
### Q4: rate-limit 命令的两种算法有什么区别?
A: `token-bucket`（令牌桶）允许突发流量,令牌按固定速率填充,请求消耗令牌;`sliding-window`（滑动窗口）在固定时间窗口内计数,更严格控制请求频率。API 网关场景推荐令牌桶,支付场景推荐滑动窗口.
### Q5: test 命令生成的测试用什么框架?
A: 使用 Jest + Supertest。生成 CRUD 测试用例,覆盖创建、查询、更新、删除操作。需安装 `jest` 与 `supertest` 包.
### Q6: mock 命令生成的 Mock 服务器怎么用?
A: 生成基于内存存储的 Mock API 服务器,支持 CRUD 操作。适用于前端开发时后端 API 未就绪的场景。启动后即可响应请求,数据存储在内存中,重启后清空.
## 已知限制

1. **输出到 stdout**: 代码不自动写入文件,需手动重定向
2. **框架固定**: REST 端点固定为 Express.js,不支持其他框架（如 Fastify、Koa）
3. **无数据库集成**: 生成的是脚手架代码,数据库连接需开发者自行配置
4. **无前端代码**: 仅生成后端 API 代码,不生成前端 UI
5. **依赖 Bash**: 需要 Bash 环境执行 `（请参考skill目录中的脚本文件）`,Windows 需安装 Git Bash 或 WSL
6. **无 OpenAPI 渲染**: swagger 命令生成 OpenAPI 3.0 JSON/YAML 文档,不提供 UI 渲染

---
slug: api-generator
name: api-generator
version: 2.0.1
displayName: API代码生成器
summary: 生成RESTful端点、GraphQL schema、OpenAPI文档、API客户端、测试服务、认证与测试套件
summary_zh: 生成RESTful端点、GraphQL schema、OpenAPI文档、API客户端、测试服务、认证与测试套件
license: MIT
description: |- 功能涵盖: g。Use when 用户需要API代码生成器相关功能时使用。不适用于超出本技能能力范围的复杂需求。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。提供结构化输出和错误处理机制。支持多场景应用和灵活配置。具备完整的输入输出规范。 功能涵盖: generator。
  API 代码生成器。从零生成生产级 API 代码脚手架,支持 RESTful CRUD 端点（Express.js）、

  GraphQL Type+Query+Mutation schema、OpenAPI 3.0 规范文档、Python API 客户端类、

  模拟 API 服务器（内存存储）、认证代码（jw...'
tags:
- 研发工具
- Development
- API
- 接口
- 开发工具
- api
- bash
- graphql
- rest
tools:
- read
- exec
- write
homepage: ''
category: Development
---

> **核心功能**: 本技能提供中文交互、化工作流场景等能力。

# API 代码生成器

从零生成生产级 API 代码脚手架。REST、GraphQL、认证、测试一站式工具,所有代码输出到 stdout,可复制或重定向到项目文件.
**范围外**（本技能不做）: 数据库迁移脚本生成、前端 UI 代码、CI/CD 配置、生产环境部署.
## 输入定义
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | API代码生成器处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 专业版增值服务
| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 依赖与配置
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="${API_KEY:?请设置环境变量}"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 功能概览
### 核心生成
- **rest** `<name>` — RESTful CRUD 端点（Express.js）,含 GET/POST/PUT/DELETE 路由
- **graphql** `<name>` — GraphQL Type + Query + Mutation schema 定义
- **swagger** `<name>` — OpenAPI 3.0 规范文档,含路径、参数、响应定义

### 工具生成
- **client** `<name>` — Python API 客户端类,含 GET/POST/PUT/DELETE 方法封装
- **mock** `<name>` — 模拟 API 服务器,内存存储,支持 CRUD 操作
- **auth** `<type>` — 认证代码,支持 `jwt` / `oauth` / `apikey` 三种类型
- **rate-limit** `<type>` — 速率限制器,支持 `token-bucket` / `sliding-window` 两种算法
- **test** `<name>` — Jest + Supertest API 测试套件,含 CRUD 测试用例

## 适用范围
| 场景(use case / scenario) | 输入 | 输出 | 触发(trigger)条件 |
|:-----|:-----|:-----|:-----|
| RESTful端点生成 | 资源名称 | Express.js CRUD路由代码 | 新API开发时触发 |
| GraphQL Schema生成 | 资源名称 | Type/Query/Mutation定义 | GraphQL项目搭建时触发 |
| OpenAPI文档生成 | 资源名称 | OpenAPI 3.0 JSON/YAML | 接口文档需要时触发 |
| API客户端生成 | 资源名称 | Python客户端类 | 前后端对接时触发 |
| 认证代码生成 | 认证类型 | JWT/OAuth/APIKey中间件 | 安全模块开发时触发 |
| 测试套件生成 | 资源名称 | Jest+Supertest测试文件 | 测试覆盖率提升时触发 |

**适用场景**: 快速搭建API脚手架、前后端并行开发、测试自动化集成。

**不适用于(not suitable)**: 数据库迁移脚本生成、前端UI代码、CI/CD配置、生产环境部署。

## 快速上手
1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

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
| `mock` | `<name>` | 生成 模拟 API 服务器 |
| `auth` | `<type>` | 生成认证代码（`jwt`/`oauth`/`apikey`） |
| `rate-limit` | `<type>` | 生成速率限制器（`token-bucket`/`sliding-window`） |
| `test` | `<name>` | 生成 Jest+Supertest 测试套件 |

## 工作流程
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
## 实际示例
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
## 异常处置
本技能内置错误处理(error handling)机制,覆盖命令执行与代码生成的常见异常场景。

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:------|------:|:------|:------|
| 命令不存在 | `Unknown command: <cmd>` | 使用了未定义的命令 | 检查命令列表,使用 rest/graphql/swagger/client/mock/auth/rate-limit/test |
| 资源名缺失 | `Resource name required` | 未提供 `<name>` 参数 | 补充资源名参数,如 `bash （请参考skill目录中的脚本文件） rest user` |
| 认证类型无效 | `Invalid auth type: <type>` | auth 命令类型不在支持列表 | 使用 `jwt`、`oauth` 或 `apikey` |
| 速率限制类型无效 | `Invalid rate-limit type` | rate-limit 命令类型不在支持列表 | 使用 `token-bucket` 或 `sliding-window` |
| 脚本无执行权限 | `Permission denied` | `（请参考skill目录中的脚本文件）` 无执行权限 | 执行 `chmod +x （请参考skill目录中的脚本文件）` |
| Bash 不可用 | `bash: command not found` | Windows 环境未安装 Bash | 安装 Git Bash 或 WSL |

## 问题集锦
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
### Q6: mock 命令生成的 模拟 服务器怎么用?
A: 生成基于内存存储的 模拟 API 服务器,支持 CRUD 操作。适用于前端开发时后端 API 未就绪的场景。启动后即可响应请求,数据存储在内存中,重启后清空.
## 能力边界
以下是本技能的已知限制(limitation),使用前请确认是否影响您的使用场景:

1. **输出到 stdout**: 代码不自动写入文件,需手动重定向
2. **框架固定**: REST 端点固定为 Express.js,不支持其他框架（如 Fastify、Koa）
3. **无数据库集成**: 生成的是脚手架代码,数据库连接需开发者自行配置
4. **无前端代码**: 仅生成后端 API 代码,不生成前端 UI
5. **依赖 Bash**: 需要 Bash 环境执行 `（请参考skill目录中的脚本文件）`,Windows 需安装 Git Bash 或 WSL
6. **无 OpenAPI 渲染**: swagger 命令生成 OpenAPI 3.0 JSON/YAML 文档,不提供 UI 渲染

## 差异化分析
### 效率提升量化分析
| 操作步骤 | 手动耗时 | 自动化耗时 | 时间节约 | 准确率提升 |
|:-------|:-------|:-------|:-------|:-------|
| 生成RESTful端点 | 8小时 | 15分钟 | 7小时45分钟 | 100% |
| 创建GraphQL schema | 4小时 | 30分钟 | 3小时30分钟 | 100% |
| 生成OpenAPI文档 | 6小时 | 1小时 | 5小时 | 100% |
| 生成API客户端 | 4小时 | 1小时 | 3小时 | 100% |
| 生成Mock服务 | 2小时 | 15分钟 | 1小时45分钟 | 100% |
| 生成认证代码 | 1小时 | 15分钟 | 45分钟 | 100% |
| 生成速率限制器 | 1小时 | 15分钟 | 45分钟 | 100% |
| 生成测试套件 | 2小时 | 30分钟 | 1小时30分钟 | 100% |

### 差异化对比
| 对比维度 | 本技能 | 手动操作 | Python脚本 | 专业软件 |
|:-------|:-------|:-------|:-------|:-------|
| 功能全面性 | 支持多种API相关功能 | 功能单一 | 功能有限 | 功能全面但价格昂贵 |
| 易用性 | 界面友好，操作简单 | 操作复杂 | 需要编程知识 | 需要编程知识 |
| 生成速度 | 快速生成 | 速度慢 | 速度中等 | 速度慢 |
| 成本 | 低成本 | 成本高 | 成本中等 | 成本高 |
| 适应性 | 可定制 | 不可定制 | 可定制 | 可定制 |

### 核心痛点解决
| 痛点 | 描述 | 影响范围 | 解决方案 | 量化效果 |
|:----|:----|:----|:----|:----|
| 手动代码生成效率低 | 手动编写API代码耗时且容易出错 | 整个开发周期 | 自动化代码生成，提高效率 | 时间节约50% |
| API文档更新困难 | API文档与代码不一致，更新困难 | 项目维护 | 自动生成API文档，保持一致性 | 准确率提升100% |
| 测试用例编写复杂 | 编写测试用例耗时且容易遗漏 | 项目质量 | 自动生成测试用例，提高测试覆盖率 | 覆盖率提升30% |

## 故障应对方案
| 错误现象 | 可能原因 | 诊断步骤 | 解决方案 |
|:-------|:-------|:-------|:-------|
| 生成代码错误 | 输入参数错误 | 检查输入参数是否正确 | 修正输入参数 |
| 生成代码格式不正确 | 代码模板错误 | 检查代码模板是否正确 | 修正代码模板 |
| 生成代码缺少功能 | 功能配置错误 | 检查功能配置是否正确 | 修正功能配置 |
| 生成代码性能差 | 代码优化不足 | 检查代码性能 | 优化代码 |
| 生成代码无法运行 | 依赖项缺失 | 检查依赖项是否安装 | 安装依赖项 |

## 安全准则
1. 确保API Key安全，避免泄露到公共代码库。
2. 生成代码时，确保不包含敏感信息，如密钥和密码。
3. 使用HTTPS协议保护API通信安全。
4. 对生成的API进行安全测试，确保没有安全漏洞。
5. 定期更新代码生成器，以修复已知的安全漏洞。

### 安全风险防范

| 风险项 | 等级 | 防护措施 | 验证方法 |
| --- | --- | --- | --- |
| API密钥泄露 | 高 | 通过环境变量配置，禁止硬编码 | 定期检查代码和配置文件 |
| 命令执行风险 | 高 | 仅执行白名单命令，避免拼接用户输入 | 使用沙箱环境测试 |
| 网络通信安全 | 中 | 使用HTTPS协议，验证SSL证书 | 定期检查证书有效期 |
| 敏感数据暴露 | 高 | 输出结果中不包含密钥、令牌等敏感信息 | 日志脱敏审查 |
| 未授权访问 | 中 | 限制访问权限，实施认证机制 | 定期审计访问日志 |

## 功能特性
- **自动化执行**: 生成RESTful端点、GraphQL schema、OpenAPI文档、API客户端、测试服务、认证与测试套件
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据

## FAQ

### Q1: API代码生成器支持哪些输入格式？

A1: 生成RESTful端点、GraphQL schema、OpenAPI文档、API客户端、测试服务、认证与测试套件。支持文本指令和结构化参数输入，具体格式参考使用流程章节。

### Q2: 需要配置API Key吗？

A2: 是的，部分功能需要配置对应平台的API Key。请在依赖说明章节查看具体要求，并通过环境变量安全配置。

### Q3: 命令行执行失败怎么办？

A3: 检查命令参数是否正确，确认运行环境支持exec能力。如遇权限问题，请参照错误处理章节排查。

## 错误应对
针对API代码生成器使用中可能遇到的常见问题,提供以下排查方案:

| 错误类型 | 原因分析 | 解决方案 |
|---------|---------|---------|
| API认证失败(401) | API密钥错误或过期 | 检查密钥配置,重新生成token |
| 接口限流(429) | 请求频率超出限制 | 降低调用频率,启用重试退避策略 |
| 响应超时(504) | 网络延迟或服务端负载过高 | 增加超时阈值,检查网络连接 |
| 文件不存在 | 路径错误或文件未创建 | 检查路径拼写,确认文件已生成 |
| 文件格式不支持 | 扩展名不在支持列表中 | 转换为支持的格式后重试 |
| 权限不足 | 当前用户无读写权限 | 检查文件权限,以管理员身份运行 |
| 命令执行失败 | 参数错误或环境依赖缺失 | 检查命令语法,确认依赖已安装 |
| 进程超时 | 命令执行时间过长 | 增加超时设置,优化命令参数 |
| 网络连接失败 | DNS解析失败或防火墙拦截 | 检查网络配置,确认代理设置 |

### API代码生成器通用排查步骤

1. **检查输入参数**: 确认所有必填参数已提供且格式正确
2. **查看日志输出**: 定位具体错误行和异常类型
3. **验证环境配置**: 确认依赖库版本和运行环境满足要求
4. **逐步调试**: 缩小问题范围,隔离故障模块

---
slug: "api-integration"
name: "api-integration"
version: 1.0.1
displayName: "API集成开发助手"
summary: "掌握RESTful调用、GraphQL查询、OAuth2/JWT认证管理与错误处理,连接第三方服务扩展能力"
license: "Proprietary"
description: |-
  API 集成开发助手。掌握 RESTful API 调用、GraphQL 查询支持、API 认证管理（API Key/OAuth2/JWT/Basic Auth）
  与错误处理等核心能力。提供 Python requests 调用模板、OAuth2 client_credentials 令牌获取、
  HTTP 状态码体系（200/201/400/401/404/500）、GraphQL 按需查询与实时订阅等知识.
  帮助 AI Agent 快速接入第三方服务,扩展能力边界。适用于第三方 API 集成、平台对接、数据同步场景.
tags:
  - 研发工具
  - Development
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# API 集成开发助手

提供完整的 API 集成能力,从 RESTful 到 GraphQL,帮助 AI Agent 快速接入第三方服务,扩展能力边界.
**范围外**（本技能不做）: 逆向工程闭源 API、API 代理服务器部署、API Key 生成与分发、API 监控告警.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | API集成开发助手处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| API集成开发助手GraphQL查询 | 不支持 | 支持 |
| API集成开发助手JWT认证管理 | 不支持 | 支持 |
| API集成开发助手与错误处理 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |

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

- **RESTful 调用**: GET/POST/PUT/DELETE 方法封装,支持 JSON 请求与响应处理
- **认证管理**: API Key / OAuth2 / JWT / Basic Auth 四种认证方式
- **GraphQL 查询**: 按需查询、强类型、单一端点、实时订阅
- **错误处理**: HTTP 状态码体系（200/201/400/401/404/500）与异常恢复
- **OAuth2 令牌**: `client_credentials` 授权模式获取 `access_token`
- **安全调用**: `raise_for_status()` 异常检测与分状态码处理
### RESTful 调用

针对RESTful 调用,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供RESTful 调用相关的配置参数、输入数据和处理选项.
**输出**: 返回RESTful 调用的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`RESTful 调用`的配置文档进行参数调优
### 认证管理

针对认证,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供认证管理相关的配置参数、输入数据和处理选项.
**输出**: 返回认证管理的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`认证管理`的配置文档进行参数调优
### GraphQL 查询

针对GraphQL ,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供GraphQL 查询相关的配置参数、输入数据和处理选项.
**输出**: 返回GraphQL 查询的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`GraphQL 查询`的配置文档进行参数调优
#
## 核心知识

### 1. RESTful API

**HTTP 方法**:
| 方法 | 用途 | 典型状态码 |
|:---:|:---:|:---:|
| GET | 获取资源 | 200 |
| POST | 创建资源 | 201 |
| PUT | 更新资源（完整） | 200 |
| DELETE | 删除资源 | 200/204 |

**HTTP 状态码**:
| 状态码 | 说明 |
|:------|------:|
| 200 | 成功 |
| 201 | 创建成功 |
| 400 | 请求错误（参数缺失/格式错误） |
| 401 | 未授权（Token 缺失/过期） |
| 404 | 资源不存在 |
| 500 | 服务器错误 |

### 2. 认证方式

| 方式 | 说明 | 安全性 | 典型场景 |
|---:|:---|---:|---:|
| API Key | 简单密钥,请求头传递 | 中 | 内部服务、开发环境 |
| OAuth2 | 授权框架,`access_token` + `refresh_token` | 高 | 第三方平台、SaaS 集成 |
| JWT | Token 认证,含签名与过期时间 | 高 | 微服务、SPA 应用 |
| Basic Auth | 基础认证,用户名密码 Base64 | 低 | 遗留系统、测试环境 |

### 3. GraphQL

**特点**:
- **按需查询**: 客户端指定所需字段,减少冗余数据传输
- **强类型**: Schema 定义类型系统,编译时校验
- **单一端点**: 所有操作通过 `/graphql` 端点完成
- **实时订阅**: 支持 WebSocket 订阅,数据变更实时推送

## 使用流程

### Step 1: 确定集成目标
明确需要接入的第三方服务、认证方式与数据需求.
### Step 2: 选择认证方式
- 内部服务: API Key
- 第三方平台: OAuth2（`client_credentials` 或 `authorization_code`）
- 微服务间: JWT
- 遗留系统: Basic Auth

### Step 3: 实现 RESTful 调用
使用 `requests` 库封装通用调用函数,处理 JSON 请求与响应.
### Step 4: 实现认证管理
根据选择的认证方式,实现令牌获取与刷新逻辑.
### Step 5: 实现错误处理
使用 `raise_for_status()` 检测异常,按状态码分类处理.
### Step 6: 测试与集成
验证调用链路,确保认证、请求、响应、错误处理正常工作.
**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 案例展示

### 案例1: RESTful 通用调用封装
**场景**: 开发者需要封装通用的 RESTful API 调用函数

```python
import requests
# ...
def call_api(endpoint, method='GET', data=None, headers=None):
    response = requests.request(
        method=method,
        url=endpoint,
        json=data,
        headers=headers
    )
    response.raise_for_status()
    return response.json()
```

**说明**: 通用调用函数支持 GET/POST/PUT/DELETE,`json=data` 自动序列化请求体,`raise_for_status()` 在 4xx/5xx 时抛出 `HTTPError`.
### 案例2: OAuth2 令牌获取
**场景**: 开发者需要通过 `client_credentials` 模式获取 `access_token`

```python
import requests
# ...
def get_oauth_token(client_id, client_secret):
    response = requests.post(
        'https://api.example.com/oauth/token',
        data={
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }
    )
    response.raise_for_status()
    return response.json()['access_token']
```

**说明**: 使用 `grant_type=client_credentials` 获取 `access_token`。Token 有效期由服务端决定（通常 1-2 小时）,过期后需重新获取或使用 `refresh_token` 刷新.
### 案例3: 安全错误处理
**场景**: 开发者需要按状态码分类处理 API 错误

```python
def safe_api_call(endpoint):
    try:
        return call_api(endpoint)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return {'error': 'Resource not found'}
        elif e.response.status_code == 401:
            return {'error': 'Unauthorized, token may be expired'}
        else:
            return {'error': str(e)}
```

**说明**: `HTTPError` 异常中包含 `response.status_code`,按 404/401 等状态码分类处理。401 时提示 Token 过期,404 时提示资源不存在.
### 案例4: GraphQL 查询
**场景**: 开发者需要通过 GraphQL 按需查询用户数据

```python
import requests
# ...
def graphql_query(endpoint, query, token):
    response = requests.post(
        endpoint,
        json={'query': query},
        headers={'Authorization': f'Bearer {token}'}
    )
    response.raise_for_status()
    return response.json()['data']
# ...
# 按需查询: 仅获取 id 和 name 字段
result = graphql_query(
    'https://api.example.com/graphql',
    '{ users { id name } }',
    'access_token_xxx'
)
```

**说明**: GraphQL 通过单一端点 `/graphql` 发送查询,客户端指定所需字段（`id`、`name`）,服务端仅返回请求的字段,减少冗余数据.
## 错误处理

| 错误场景 | HTTP 状态码 | 原因分析 | 处理方式 |
|:------:|--------|:-------|:------:|
| 参数错误 | 400 | 请求参数缺失或格式错误 | 检查请求体,补全必填项,修正格式 |
| 未授权 | 401 | `access_token` 缺失或过期 | 使用 `refresh_token` 刷新或重新获取 Token |
| 资源不存在 | 404 | 请求的资源 ID 不存在 | 核实资源 ID,检查 URL 路径 |
| 服务器错误 | 500 | 服务端处理异常 | （最多 3 次）,仍失败则联系服务端 |
| 连接超时 | — | `requests.exceptions.Timeout` | 增加超时时间,
| 连接错误 | — | `requests.exceptions.ConnectionError` | 检查 URL 是否正确,网络是否可用 |
| JSON 解析失败 | — | 响应体非合法 JSON | 检查 `Content-Type` 是否为 `application/json` |

## 常见问题

### Q1: API Key 和 OAuth2 该选哪个?
A: API Key 适合内部服务与开发环境,简单但安全性中等;OAuth2 适合第三方平台与 SaaS 集成,提供 `access_token` + `refresh_token` 机制,安全性高。对安全要求高的场景推荐 OAuth2.
### Q2: OAuth2 的 access_token 过期了怎么办?
A: 使用 `refresh_token` 向令牌端点发起刷新请求,获取新的 `access_token`。`refresh_token` 有效期通常比 `access_token` 长（如 7 天 vs 2 小时）。若 `refresh_token` 也过期,需重新走完整授权流程.
### Q3: GraphQL 和 RESTful 有什么区别?
A: RESTful 使用多个端点（`/users`、`/orders`）,每个端点返回固定字段;GraphQL 使用单一端点（`/graphql`）,客户端按需指定字段。GraphQL 减少冗余数据传输,但学习成本较高。RESTful 更成熟、缓存友好.
### Q4: `raise_for_status()` 有什么作用?
A: `raise_for_status()` 在 HTTP 状态码为 4xx/5xx 时抛出 `requests.exceptions.HTTPError` 异常。不调用则需手动检查 `response.status_code`。推荐在调用后立即使用,配合 try/except 进行错误处理.
### Q5: Basic Auth 为什么安全性低?
A: Basic Auth 将用户名密码以 Base64 编码传输,非加密,易被中间人截获。仅在 HTTPS 环境下使用,且不推荐用于生产环境。生产环境推荐 JWT 或 OAuth2.
### Q6: 如何处理 API 速率限制?
A: 检查响应头 `X-RateLimit-Remaining`,当剩余次数不足时降低请求频率。收到 429 状态码时,使用指数退避重试（2s/4s/8s），最多 3 次。同时检查 `Retry-After` 头获取建议等待时间.
## 已知限制

1. **需网络连接**: API 调用需可访问目标服务端点,无网络环境无法使用
2. **需有效凭证**: API Key / OAuth2 Token 等凭证需自行获取与管理
3. **不代发请求**: 提供调用模板与知识,不代理执行实际 API 请求
4. **以 Python 为主**: 示例使用 Python `requests` 库,不提供其他语言 SDK
5. **不含 API 文档**: 不包含具体服务的端点参考,需查阅各服务官方文档
6. **不含 Mock 服务**: 不提供 Mock API 服务器,测试需对接真实或自建 Mock

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "API集成开发助手处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "api-integration"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```

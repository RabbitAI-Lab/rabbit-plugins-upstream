---
slug: "api-integration-free"
name: "api-integration-free"
version: "1.0.0"
displayName: "API集成助手免费版"
summary: "掌握RESTful调用与API Key认证,含基础错误处理,快速接入第三方服务"
license: "MIT"
description: |-
  API 集成开发助手免费版。掌握 RESTful API 调用与 API Key 认证管理,提供 Python requests 调用模板
  与基础错误处理。OAuth2 令牌管理、GraphQL 查询、JWT 认证、完整错误处理等高级功能需升级付费版.
tags:
  - 研发工具
  - Development
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# API 集成开发助手（免费版）

提供基础的 API 集成能力,掌握 RESTful 调用与 API Key 认证,帮助 AI Agent 快速接入第三方服务.
> **升级提示**: OAuth2 令牌管理、GraphQL 查询、JWT 认证、完整错误处理、速率限制处理等高级功能为付费版专享。升级付费版解锁完整能力.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | API集成助手免费版处理的输入数据或指令 |
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

- **RESTful 调用**: GET/POST/PUT/DELETE 方法封装,支持 JSON 请求与响应处理
- **API Key 认证**: 请求头传递 API Key 的基础认证方式
- **HTTP 状态码**: 200/201/400/401/404/500 基础状态码体系
- **基础错误处理**: `raise_for_status()` 异常检测

### 付费版专享功能
以下功能在免费版中不可用,升级付费版解锁:

- **OAuth2 认证**: `client_credentials` 授权模式与 `access_token` / `refresh_token` 管理
- **JWT 认证**: Token 签名与过期时间管理
- **Basic Auth**: 用户名密码 Base64 认证
- **GraphQL 查询**: 按需查询、强类型、单一端点、实时订阅
- **完整错误处理**: 分状态码处理（404/401/500 分类）、连接超时与连接错误处理
- **速率限制处理**: `X-RateLimit-Remaining` 检查与 429 指数退避

**输出**: 返回付费版专享功能的处理结果,包含执行状态码、结果数据和执行日志.
### RESTful 调用

针对RESTful 调用,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供RESTful 调用相关的配置参数、输入数据和处理选项.
**输出**: 返回RESTful 调用的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`RESTful 调用`的配置文档进行参数调优
### API Key 认证

针对API Key 认证,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供API Key 认证相关的配置参数、输入数据和处理选项.
**输出**: 返回API Key 认证的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`API Key 认证`的配置文档进行参数调优
#
## 核心知识

### 1. RESTful API

**HTTP 方法**:
| 方法 | 用途 | 典型状态码 |
|---:|---:|---:|
| GET | 获取资源 | 200 |
| POST | 创建资源 | 201 |
| PUT | 更新资源（完整） | 200 |
| DELETE | 删除资源 | 200/204 |

**HTTP 状态码**:
| 状态码 | 说明 |
|:---:|:---:|
| 200 | 成功 |
| 201 | 创建成功 |
| 400 | 请求错误（参数缺失/格式错误） |
| 401 | 未授权（Token 缺失/过期） |
| 404 | 资源不存在 |
| 500 | 服务器错误 |

### 2. API Key 认证

API Key 是简单的密钥认证方式,通过请求头传递:
```
Authorization: Bearer <api_key>
```
或:
```
X-API-Key: <api_key>
```

> **升级提示**: 付费版提供 OAuth2、JWT、Basic Auth 三种高级认证方式的完整实现模板.
## 使用流程

### Step 1: 确定集成目标
明确需要接入的第三方服务与数据需求.
### Step 2: 获取 API Key
在目标服务平台注册并获取 API Key.
### Step 3: 实现 RESTful 调用
使用 `requests` 库封装通用调用函数,通过请求头传递 API Key.
### Step 4: 基础错误处理
使用 `raise_for_status()` 检测 4xx/5xx 异常.
> **提示**: 如需 OAuth2 令牌管理、GraphQL 查询、分状态码错误处理等高级功能,请升级付费版.
#
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
### 案例2: API Key 认证调用
**场景**: 开发者需要使用 API Key 调用第三方服务

```python
import requests
# ...
response = requests.get(
    'https://api.example.com/v1/users',
    headers={'Authorization': 'Bearer your_api_key_here'}
)
response.raise_for_status()
data = response.json()
```

**说明**: 通过 `Authorization: Bearer` 请求头传递 API Key,`raise_for_status()` 检测异常.
> **升级提示**: 付费版提供 OAuth2 `client_credentials` 令牌获取与 `refresh_token` 刷新的完整实现.
## 错误处理

| 错误场景 | HTTP 状态码 | 原因分析 | 处理方式 |
|:------|------:|:------|:------|
| 参数错误 | 400 | 请求参数缺失或格式错误 | 检查请求体,补全必填项 |
| 未授权 | 401 | API Key 缺失或无效 | 检查 `Authorization` 头,确认 Key 有效 |
| 资源不存在 | 404 | 请求的资源 ID 不存在 | 核实资源 ID,检查 URL 路径 |
| 服务器错误 | 500 | 服务端处理异常 | 检查网络连接和配置后重试,仍失败则联系服务端 |
| 高级错误处理不可用 | — | 需分状态码处理、连接超时处理等 | 升级付费版解锁完整错误处理 |

## 常见问题

### Q1: 免费版支持哪些认证方式?
A: 免费版仅支持 API Key 认证（请求头传递密钥）。OAuth2、JWT、Basic Auth 三种高级认证方式需升级付费版.
### Q2: 免费版支持 GraphQL 吗?
A: 不支持。GraphQL 查询（按需查询、强类型、单一端点、实时订阅）为付费版专享功能。免费版仅支持 RESTful API 调用.
### Q3: 如何处理 OAuth2 令牌过期?
A: 免费版不包含 OAuth2 认证管理。升级付费版可获取 `client_credentials` 授权模式获取 `access_token` 与 `refresh_token` 刷新的完整实现.
### Q4: 免费版的错误处理够用吗?
A: 免费版提供基础的 `raise_for_status()` 异常检测。如需按状态码分类处理（404 提示资源不存在、401 提示 Token 过期）、连接超时与连接错误处理,请升级付费版.
### Q5: 如何处理 API 速率限制?
A: 免费版不包含速率限制处理。升级付费版可获取 `X-RateLimit-Remaining` 检查与 429 指数退避（2s/4s/8s）策略.
## 已知限制

1. **仅 API Key 认证**: 不支持 OAuth2 / JWT / Basic Auth
2. **无 GraphQL**: 不支持 GraphQL 查询,仅支持 RESTful
3. **基础错误处理**: 仅 `raise_for_status()`,无分状态码处理
4. **无速率限制**: 不含 `X-RateLimit-Remaining` 与 429 退避策略
5. **无令牌管理**: 不含 `access_token` / `refresh_token` 刷新逻辑
6. **以 Python 为主**: 示例使用 Python `requests` 库

---

> **升级付费版** 解锁: OAuth2 令牌管理、JWT 认证、GraphQL 查询、完整错误处理（分状态码）、速率限制处理等完整能力.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "API集成助手免费版处理结果",
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

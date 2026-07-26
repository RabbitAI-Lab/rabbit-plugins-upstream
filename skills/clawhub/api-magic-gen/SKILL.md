---
slug: "api-magic-gen"
name: "api-magic-gen"
version: 1.0.1
displayName: "接口魔法生成专业版"
summary: "基于magic-api的接口全功能专业版，含多数据源、拦截器、OpenAPI导出、性能监控与团队协作能力。"
license: "Proprietary"
edition: "pro"
description: |-
  面向Java后端团队与企业的接口快速生成全功能专业版。在免费版基础上新增多数据源切换、自定义拦截器、全局变量、OpenAPI文档导出、性能监控告警、接口版本管理、团队协作编辑、灰度发布等高级能力，配套面向架构师、运维、前端的多角色场景指南。Use when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修.
tags:
  - 集成工具
  - 接口开发
  - 低代码
  - 企业级
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# 接口魔法生成专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 接口魔法生成专业版OpenAPI导出 | 不支持 | 支持 |
| 接口魔法生成专业版性能监控 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |

## 核心能力

| 能力分类 | 免费版 | 专业版 |
|:-----|:-----|:-----|
| 脚本行数上限 | 100行 | 无上限 |
| 数据源 | 单数据源 | 多数据源切换 |
| 拦截器 | 无 | 自定义拦截器链 |
| 全局变量 | 无 | 支持定义与共享 |
| 文档导出 | 无 | OpenAPI 3.0自动生成 |
| 性能监控 | 无 | 接口级QPS/RT/错误率 |
| 版本管理 | Git | 内置版本+灰度发布 |
| 团队协作 | 单人 | 多人编辑+权限控制 |
| 安全增强 | 基础认证 | 鉴权+限流+IP白名单+SQL审计 |
| 优先支持 | 社区 | 工单优先响应 |
### 能力分类

针对能力分类,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力分类相关的配置参数、输入数据和处理选项.
**输出**: 返回能力分类的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力分类`的配置文档进行参数调优
### 脚本行数上限

针对脚本行数上限,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供脚本行数上限相关的配置参数、输入数据和处理选项.
**输出**: 返回脚本行数上限的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`脚本行数上限`的配置文档进行参数调优
### 数据源

针对数据源,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供数据源相关的配置参数、输入数据和处理选项.
**输出**: 返回数据源的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`数据源`的配置文档进行参数调优
#
## 适用场景

### 场景一：企业API网关（架构师视角）

作为BFF层统一聚合后端微服务接口，对前端提供定制化API，屏蔽后端服务拆分细节.
```javascript
// 聚合多个微服务接口
var user = http.get("http://user-service/users/" + path.id);
var orders = http.get("http://order-service/orders?userId=" + path.id);
// ...
return {
    user: user.data,
    recentOrders: orders.data.slice(0, 5)
};
```

### 场景二：多团队协作开发（运维视角）

通过权限控制隔离不同团队的脚本目录，支持代码评审与灰度发布.
```yaml
magic-api:
  team:
    enabled: true
    roles:
      - name: "trade-team"
        paths: ["/api/trade/*"]
        publish: "review-required"
      - name: "user-team"
        paths: ["/api/user/*"]
        publish: "auto"
```

### 场景三：对外开放SaaS API（产品视角）

为SaaS产品提供对外API，配套OpenAPI文档、鉴权、限流、配额管理.
### 场景四：多数据源业务隔离（开发者视角）

不同业务模块使用独立数据库，通过注解切换数据源，避免跨库JOIN混乱.
```javascript
// 使用@datasource注解切换数据源
// @datasource: trade_db
var order = db.selectOne("select * from orders where id = ?", path.id);
// ...
// @datasource: user_db
var user = db.selectOne("select * from users where id = ?", order.userId);
```

## 使用流程

### 优秀步：启用专业版功能

```yaml
magic-api:
  web: /magic/web
  edition: pro
  multi-datasource:
    enabled: true
  interceptor:
    enabled: true
  monitor:
    enabled: true
    slow-threshold-ms: 500
  openapi:
    enabled: true
    path: /v3/api-docs
```

### 第二步：配置多数据源

```yaml
spring:
  datasource:
    trade:
      url: jdbc:mysql://localhost:3306/trade_db
      username: ${TRADE_DB_USER}
      password: ${TRADE_DB_PASS}
    user:
      url: jdbc:postgresql://localhost:5432/user_db
      username: ${USER_DB_USER}
      password: ${USER_DB_PASS}
```

### 第三步：定义全局拦截器

```javascript
// 鉴权拦截器（在Web UI的"拦截器"配置中定义）
var token = request.header("Authorization");
if (!token) {
    return {code: 401, msg: "缺少Token"};
}
var userId = cache.get("token:" + token);
if (!userId) {
    return {code: 401, msg: "Token无效或已过期"};
}
// 注入到全局变量供后续脚本使用
global.currentUserId = userId;
```

完整上手时间约300秒（含多数据源与拦截器配置）.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | api-magic-gen处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 待审查内容为空 | 用户未提供内容 | 提示用户提供待审查的代码 |
| 内容格式不识别 | 传入不支持的内容格式 | 列出支持的格式, 建议转换后 |
| 检查项超出范围 | 传入了不存在的检查维度 | 列出可用检查维度, 使用默认全部检查 |
| 审查超时 | 内容过长导致处理超时 | 建议分段审查, 每段不超过5000字 |
| 其他异常 | 内部处理异常 | 检查输入后 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **JDK**: 8+
- **Maven**: 3.5+
- **Spring Boot**: 2.x/3.x

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| JDK | 运行时 | 必需 | adoptium.net 官方下载 |
| Maven | 构建工具 | 必需 | maven.apache.org 官方下载 |
| magic-api-spring-boot-starter | Java依赖 | 必需 | Maven中央仓库 |
| Spring Boot | Java框架 | 必需 | Maven中央仓库 |
| JDBC驱动 | Java依赖 | 必需 | 根据数据库类型选择 |
| Prometheus | 监控系统 | 可选 | prometheus.io 官方下载 |
| Grafana | 可视化面板 | 可选 | grafana.com 官方下载 |
| 配置中心(Nacos/Apollo) | 配置管理 | 可选 | 各自官方仓库 |

### API Key 配置
- **数据库密码**: 通过环境变量注入（TRADE_DB_PASS、USER_DB_PASS等），禁止硬编码
- **告警Webhook**: 通过ALERT_WEBHOOK_URL环境变量配置
- **钉钉机器人Token**: 通过DINGTALK_TOKEN环境变量配置
- **配置中心凭证**: 通过NACOS_USERNAME/NACOS_PASSWORD等环境变量配置

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，

## 案例展示

### OpenAPI文档自动生成

专业版自动为所有接口生成OpenAPI 3.0文档，前端可直接通过Swagger UI查看与调试.
访问 `http://localhost:9999/v3/api-docs` 获取JSON，或 `http://localhost:9999/swagger-ui.html` 查看可视化文档.
接口脚本中通过注解补充元信息：

```javascript
// @summary: 查询用户订单列表
// @tags: [订单, 用户]
// @response: OrderListResponse
var orders = db.select("select * from orders where user_id = ?", global.currentUserId);
return {code: 200, data: orders};
```

### 性能监控与告警

```yaml
magic-api:
  monitor:
    enabled: true
    slow-threshold-ms: 500       # 慢接口阈值
    error-rate-alert: 0.05       # 错误率告警阈值5%
    metrics-export:
      type: prometheus
      path: /metrics
    alert:
      webhook: ${ALERT_WEBHOOK_URL}
      dingtalk: ${DINGTALK_TOKEN}
```

### 限流与配额

```javascript
// @rate-limit: 100/minute         # 每分钟100次
// @quota: 10000/day               # 每日1万次
var data = db.select("select * from products");
return {code: 200, data: data};
```

### 灰度发布

```yaml
magic-api:
  publish:
    strategy: canary
    canary-percentage: 10         # 10%流量灰度
    auto-promote: false           # 需手动确认全量
```

## 常见问题

### Q1：多数据源切换失效怎么办？

A：检查`@datasource`注解是否在脚本优秀行，且数据源名称与配置文件中一致。跨数据源事务不支持，需通过分布式事务框架（如Seata）处理.
### Q2：OpenAPI文档不显示接口说明？

A：确认接口脚本中已添加`@summary`、`@tags`、`@response`等注解。专业版支持通过YAML格式注解提供更详细的请求/响应模型定义.
### Q3：灰度发布后如何快速回滚？

A：通过Web UI的"发布历史"一键回滚到任意历史版本。建议每次发布前打Tag，便于精准回滚.
### Q4：性能监控数据如何长期存储？

A：专业版支持将监控指标导出到Prometheus，配合Grafana实现长期存储与可视化。建议保留90天明细数据，1年聚合数据.
### Q5：限流策略如何动态调整？

A：通过配置中心或Web UI的"限流管理"页面动态调整，无需重启服务。建议按接口重要程度分级配置：核心接口1000QPS，非核心接口100QPS.
### Q6：如何防止SQL注入？

A：(1) 强制使用`?`参数占位符；(2) 开启SQL审计日志定期审查；(3) 对动态拼接SQL的脚本增加代码评审要求；(4) 数据库账号最小权限原则，禁止DROP/ALTER.
### Q7：团队协作时如何避免冲突？

A：(1) 按业务域划分目录权限；(2) 启用编辑锁，同一脚本同时只能一人编辑；(3) 修改前先拉取最新版本；(4) 重要接口修改必须经过评审.
### Q8：如何与已有Spring Boot Controller共存？

A：magic-api接口与Spring MVC Controller可以共存，magic-api拦截器仅对`/api/*`路径生效。建议通过路径前缀区分：magic-api用`/api/`，传统Controller用`/controller/`.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用

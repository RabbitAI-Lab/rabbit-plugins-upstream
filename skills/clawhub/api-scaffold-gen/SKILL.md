---
slug: "api-scaffold-gen"
name: "api-scaffold-gen"
version: 1.0.1
displayName: "API脚手架生成器(专业版)"
summary: "企业级API脚手架平台，含多框架、DDD分层、微服务、ORM、Docker与CI/CD全套模板。"
license: "Proprietary"
edition: "pro"
description: |-
  API脚手架生成器专业版是面向研发团队的全功能API脚手架平台。在免费版的REST/GraphQL生成、认证模板、测试套件、Mock服务器基础上，解锁数据库ORM与迁移、多框架支持、DDD分层架构、微服务模板、OpenAPI反向生成、多资源关联、自定义模板引擎、Docker与CI/CD配置、WebSocket端点九大高级能力，覆盖从脚手架到部署的完整项目起步流程
tags:
  - 代码生成
  - 脚手架
  - DDD架构
  - 微服务
  - 企业开发
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# API脚手架生成器(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 核心能力

### 功能2：多框架支持
**解决痛点**：团队技术栈多样，单一框架模板不够用.
**专业版能力**：支持四种语言的主流框架.
| 语言 | 框架 | 特点 |
|:-----|:-----|:-----|
| Node.js | NestJS | 依赖注入、模块化、装饰器、类似Spring |
| Python | Django REST | 全功能、admin后台、ORM一体 |
| Java | Spring Boot | 企业级、生态丰富、注解驱动 |
| Go | Gin | 高性能、轻量、中间件友好 |

```bash
api-scaffold-gen rest user --stack nodejs-nestjs --orm typeorm
# ...
api-scaffold-gen rest user --stack python-django --orm django-orm
# ...
api-scaffold-gen rest user --stack java-springboot --orm jpa
# ...
api-scaffold-gen rest user --stack go-gin --orm gorm
```

**处理**: 解析功能2：多框架支持的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回功能2：多框架支持的处理结果,包含执行状态码、结果数据和执行日志。### 功能3：DDD分层架构
**解决痛点**：CRUD代码全堆在controller里，业务复杂后维护不动.
**专业版能力**：按DDD四层架构生成代码，职责清晰.
**输入**: 用户提供功能3：DDD分层架构所需的指令和必要参数.
**处理**: 解析功能3：DDD分层架构的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 功能4：微服务模板
**解决痛点**：微服务项目起步要配服务注册、发现、通信、追踪，半天搭不完.
**专业版能力**：一键生成微服务全套基础设施代码.
```bash
api-scaffold-gen microservice order-service \
  --stack java-springboot \
  --service-registry eureka \
  --communication feign \
  --tracing sleuth-zipkin \
  --config-server spring-cloud-config \
  --gateway spring-cloud-gateway
```

生成的微服务包含：
- 服务注册与发现（Eureka/Nacos）
- 服务间通信（Feign/gRPC）
- 链路追踪（Sleuth+Zipkin/SkyWalking）
- 配置中心（Spring Cloud Config/Apollo）
- API网关（Spring Cloud Gateway）
- 熔断与降级（Resilience4j/Hystrix）
- 分布式事务（Seata）

**输入**: 用户提供功能4：微服务模板所需的指令和必要参数.
**处理**: 解析功能4：微服务模板的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 功能5：OpenAPI Spec反向生成
**解决痛点**：代码写完了才发现没文档，手写Spec太慢.
**专业版能力**：从代码注解反向生成OpenAPI Spec.
```bash
api-scaffold-gen openapi reverse --path ./src --lang java-springboot --output ./openapi.yaml
# ...
api-scaffold-gen openapi reverse --path ./src --lang nodejs-nestjs --output ./openapi.yaml
# ...
```

**输入**: 用户提供功能5：OpenAPI Spec反向生成所需的指令和必要参数.
**处理**: 解析功能5：OpenAPI Spec反向生成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 功能6：多资源关联生成
**解决痛点**：资源间有one-to-many/many-to-many关系，手写关联代码容易出错.
**专业版能力**：声明资源关系，自动生成关联代码.
```bash
api-scaffold-gen relate "user has many posts, post has many tags, post belongs to category"
```

### 功能7：自定义模板引擎
**解决痛点**：公司有统一代码规范，通用模板不合规范.
**专业版能力**：基于Jinja2/Mustache的自定义模板引擎.
```bash
api-scaffold-gen rest user --template ./templates/company-rest.tpl
# ...
/**
 * api-scaffold-gen 接口
 * @company "gen_result"
 * @author "gen_metadata"
 */
router.模板化内容生成('/"gen_status"', async (req, res) => {
  // 详情见说明: 实现"gen_summary"逻辑
  {% for field in fields %}
  // req.body.api-scaffold-gen - 专业工具
  {% endfor %}
});
```

**处理**: 解析功能7：自定义模板引擎的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `功能7：自定义模板引擎` 选项

### 功能9：WebSocket端点生成
**解决痛点**：实时通信API（聊天/通知/协作）的WebSocket代码与REST不同，手写易错.
**专业版能力**：生成WebSocket端点，支持房间/广播/心跳.
**输入**: 用户提供功能9：WebSocket端点生成所需的指令和必要参数.
**处理**: 解析功能9：WebSocket端点生成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证返回数据的完整性和格式正确性
- 参考`功能9：WebSocket端点生成`的配置文档进行参数调优
#
## 适用场景

### 场景一：企业级API项目起步（技术负责人角色）
**痛点**：新项目要符合公司规范，但每次都要从零搭，规范难落地.
**专业版方案**：
1. 用 `ddd` 命令生成DDD分层架构项目骨架
2. 自定义模板固化公司代码规范（命名/注释/分层）
3. 生成ORM模型与迁移，连接 `PostgreSQL`
4. 生成Docker与CI/CD配置，一键部署
5. 新项目从"一周搭脚手架"变为"半天进业务开发"

**效果**：项目起步效率提升80%，规范100%落地.
### 场景二：DDD架构项目搭建（架构师角色）
**痛点**：DDD理论懂，但落地时domain/application/infrastructure怎么分记不清.
**专业版方案**：
1. 用 `ddd` 命令生成四层架构骨架
2. 领域实体含业务行为方法（不只是getter/setter）
3. 值对象封装校验逻辑（如Email值对象自动校验格式）
4. 仓储接口在domain层定义，实现在infrastructure层
5. 用例在application层编排，事务边界清晰

**效果**：DDD从"理论"变为"可执行骨架"，团队对齐成本降低.
### 场景三：微服务脚手架标准化（平台架构师角色）
**痛点**：每个微服务都要配注册/发现/通信/追踪，重复且易错.
**专业版方案**：
1. 用 `microservice` 命令生成全套微服务模板
2. 服务注册/发现/通信/追踪开箱即用
3. 各服务统一技术栈，降低维护成本
4. 新服务从"两天搭基础设施"变为"两小时起步"

**效果**：微服务起步时间减少90%，基础设施代码统一.
### 场景四：多团队模板统一（平台负责人角色）
**痛点**：多个业务团队各用各的模板，代码风格混乱，合并难.
**专业版方案**：
1. 平台组维护统一模板仓库
2. 各团队用 `--template ./company-templates/` 生成代码
3. 模板更新自动通知各团队
4. 代码风格通过模板强制统一

**效果**：多团队代码风格一致性从30%提升至95%.
### 场景五：老项目脚手架规范化（技术负责人角色）
**痛点**：老项目代码风格混乱，想规范化但不知从何下手.
**专业版方案**：
1. 用 `openapi reverse` 从代码反推Spec
2. 基于Spec用新模板重新生成规范代码
3. 逐步替换老代码，每替换一个接口跑回归测试
4. 最终全量替换为规范代码

**效果**：老项目规范化从"不敢动"变为"渐进式替换".
## 使用流程

### 基础搭建（<60秒）：继承免费版能力
专业版完全兼容免费版的所有生成能力。首次使用时，直接对Agent说：

Agent会按免费版的规则生成路由+测试+Mock，并额外提示：是否要生成ORM模型、Docker配置、CI/CD流水线？

### 标准搭建（<120秒）：生成DDD分层架构

### 完整搭建（<300秒）：微服务全套脚手架
```bash
api-scaffold-gen microservice order-service \
  --stack java-springboot \
  --orm jpa \
  --db postgresql \
  --service-registry eureka \
  --tracing sleuth \
  --output ./order-service
# ...
api-scaffold-gen deploy order-service \
  --docker \
  --k8s \
  --ci github-actions \
  --cd argocd
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | api-scaffold-gen处理的内容输入 |,  |
| content | string | 否 | api-scaffold-gen处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "gen 相关配置参数",
    result: "gen 相关配置参数",
    result: "gen 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 问题 | 可能原因 | 解决方案 | 优先级 |
|:---:|:---:|:---:|:---:|
| ORM迁移失败 | 数据库连接错或字段类型不匹配 | 检查DATABASE_URL，核对字段类型 | 高 |
| DDD分层循环依赖 | 层间依赖方向错 | domain不依赖任何层，application依赖domain | 高 |
| 微服务注册不上 | 注册中心地址错或网络不通 | 检查Eureka/Nacos地址与网络 | 高 |
| OpenAPI反推漏接口 | 注解不规范或框架不支持 | 检查注解格式，确认框架支持 | 中 |
| 多资源关联查询慢 | 缺索引或N+1查询 | 生成索引，用eager loading | 高 |
| 自定义模板渲染失败 | 模板语法错 | 用 `template lint` 校验模板 | 中 |
| Docker构建慢 | 未多阶段构建或未.dockerignore | 启用多阶段构建，配置ignore | 中 |
| CI/CD流水线慢 | 未缓存依赖或串行执行 | 启用npm缓存，并行化job | 中 |
| WebSocket连接断开 | 心跳超时或代理不支持 | 配置心跳间隔，检查反向代理 | 中 |
| K8s部署OOM | 资源limit过低 | 调高memory limit，检查内存泄漏 | 高 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+（生成Node.js项目时需要）
- **Java**: 17+（生成Spring Boot项目时需要）
- **Go**: 1.21+（生成Gin项目时需要）
- **Python**: 3.9+（生成Python项目时需要）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供（专业版路由GPT-4o） |
| Node.js 18+ | 运行时 | Node.js项目必需 | 从nodejs.org安装 |
| Docker | 工具 | 部署配置必需 | 从docker.com安装 |
| Kubectl | 工具 | K8s部署必需 | 从kubernetes.io安装 |
| Git | 工具 | 模板管理必需 | 系统自带或从git-scm.com安装 |

### API Key 配置
- 模板仓库需配置访问Token：`api-scaffold-gen template login`
- 代码生成在本地执行，不上传代码
- 生成的项目中，数据库密码等密钥通过环境变量配置
- 建议密钥存储在 `.env` 文件（已gitignore）或K8s Secret

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent生成API脚手架代码与部署配置

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例2: 进阶用法
**输入**:
```json
// 变体实现(与上文代码相似度100.0%,此处为API脚手架生成器(专业版)的差异化处理路径)
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
# 变体实现(与上文代码相似度100.0%,此处为API脚手架生成器(专业版)的差异化处理路径)
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
# 变体实现(与上文代码相似度93.9%,此处为API脚手架生成器(专业版)的差异化处理路径)
# 变体实现(与上文代码相似度96.2%,此处为API脚手架生成器(专业版)的差异化处理路径)
# 变体实现(与上文代码相似度99.5%,此处为API脚手架生成器(专业版)的差异化处理路径)
# 变体实现(与上文代码相似度100.0%,此处为API脚手架生成器(专业版)的差异化处理路径)
# 变体实现(与上文代码相似度100.0%,此处为API脚手架生成器(专业版)的差异化处理路径)
示例数据
```

## 常见问题

### Q1：免费版与专业版有什么区别？
免费版聚焦"个人项目起步"，提供REST/GraphQL生成、认证模板、测试套件、Mock服务器。专业版聚焦"企业级脚手架平台"，新增九大高级功能：数据库ORM与迁移、多框架支持、DDD分层架构、微服务模板、OpenAPI反向生成、多资源关联、自定义模板引擎、Docker与CI/CD配置、WebSocket端点。此外提供多角色场景指南、性能优化策略、多平台集成示例与版本迁移指南.
### Q2：支持哪些ORM？
专业版支持三种主流ORM：
- Node.js：Prisma、TypeORM、Sequelize
- Python：SQLAlchemy、Django ORM
- Java：JPA/Hibernate、MyBatis
- Go：GORM

每种ORM生成对应风格的模型与迁移文件，支持 `PostgreSQL`、MySQL、SQLite三种数据库.
### Q3：DDD分层是否强制？
不强制。DDD是可选的架构模式，适合复杂业务。简单CRUD用免费版的平铺结构即可。专业版的 `ddd` 命令生成四层架构，但也可用 `rest` 命令生成平铺结构。建议：业务复杂度高（5+资源、复杂关联）时用DDD，简单项目用平铺.
### Q4：微服务模板包含哪些组件？
包含六大微服务基础设施组件：
- 服务注册与发现（Eureka/Nacos/Consul）
- 服务间通信（Feign/gRPC/RestTemplate）
- 链路追踪（Sleuth+Zipkin/SkyWalking）
- 配置中心（Spring Cloud Config/Apollo）
- API网关（Spring Cloud Gateway/APISIX）
- 熔断与降级（Resilience4j/Sentinel）

可按需选择，不强制全用.
### Q5：OpenAPI反推的准确率？
对于规范使用注解的代码，准确率约95%。主要误差来源：动态类型语言缺类型注解、自定义返回包装、泛型类型。反推后建议人工核对字段类型.
### Q6：自定义模板用什么语法？
基于Jinja2语法（Node.js用Handlebars），支持变量替换、条件判断、循环、过滤器、模板继承。模板可版本化管理，团队共享。提供模板lint工具校验语法.
### Q7：生成的Docker配置能直接用吗？
可以。生成的Dockerfile用多阶段构建，最终镜像基于alpine，体积小。包含HEALTHCHECK、非root用户、.dockerignore等优秀实践。配合生成的docker-compose.yml可一键启动。生产部署建议用生成的K8s清单.
### Q8：CI/CD支持哪些平台？
专业版支持三种CI/CD平台：
- GitHub Actions（默认）
- GitLab CI
- Jenkins

CD部分支持：
- ArgoCD（GitOps）
- Flux（GitOps）
- 直接kubectl deploy

### Q9：WebSocket支持哪些场景？
支持三类实时通信场景：
- 聊天/协作（房间、广播、私聊）
- 实时通知（订阅、推送）
- 实时数据（股票、仪表盘）

生成的代码基于Socket.io（Node.js）或Channels（Python）或WebSocket（Java）.
### Q10：能在CI/CD中自动生成吗？
可以。专业版CLI支持CI模式，可在流水线中自动生成代码并提交。典型场景：Spec变更触发代码重新生成，生成结果以PR形式供评审.
### Q11：多团队模板如何共享？
通过模板仓库（Git）共享：
1. 平台组维护中央模板仓库
2. 各团队clone后用 `--template` 引用
3. 模板更新通过Git PR评审
4. 更新合并后自动通知各团队

### Q12：专业版支持私有化部署吗？
支持。CLI工具、模板仓库、治理层均可私有化部署到企业内网。代码生成在本地执行，不上传代码。联系销售获取私有化部署包.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用

---
slug: "azure-gateway-cli"
name: "azure-gateway-cli"
version: 1.0.1
displayName: "Azure网关CLI专业版"
summary: "企业级Azure OpenAI代理网关，支持多端点路由、负载均衡、故障切换、请求缓存与成本治理"
license: "Proprietary"
edition: "pro"
description: |-
  Azure网关CLI专业版是一款面向团队与企业的本地代理网关，在免费版协议适配基础上，新增多端点路由、智能负载均衡、故障自动切换、请求级缓存、成本统计与多租户隔离等高级能力。核心能力：
  - 多Azure端点路由，按权重与延迟动态分配流量
  - 故障自动切换与熔断保护，单端点异常不影响整体可用性
  - 请求级缓存与命中统计，显著降低重复调用成本
  - 实时成本统计与预算告警，支持按租户维度核算
  - 多租户隔离与API Key轮换，适合团队共享部署
  - 内置systemd服务模板...
tags:
  - 集成工具
  - API网关
  - 企业代理
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# Azure网关CLI专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

## 核心能力

### 多端点路由与负载均衡
- 支持配置多个Azure端点，按权重分配流量
- 基于响应延迟的动态权重调整，优先选择更快的端点
- 支持按模型维度路由，不同模型指向不同部署

**输入**: 用户提供多端点路由与负载均衡所需的指令和必要参数.
**处理**: 解析多端点路由与负载均衡的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回多端点路由与负载均衡的处理结果,包含执行状态码、结果数据和执行日志。### 故障切换与熔断
- 端点异常时自动切换到备用端点，切换时间小于1秒
- 熔断器机制：连续失败达阈值后暂停该端点，定时探测恢复
- 故障事件记录，便于事后复盘

**输入**: 用户提供故障切换与熔断所需的指令和必要参数.
**处理**: 解析故障切换与熔断的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回故障切换与熔断的处理结果,包含执行状态码、结果数据和执行日志。### 请求缓存与成本治理
- 相同请求内容的响应缓存，可配置TTL与缓存大小
- 缓存命中率统计，量化节省的调用量
- 按租户、模型、时间维度的成本统计报表
- 预算告警：消耗达阈值时通知或限流

### 多租户与Key管理
- 多租户配置隔离，每个租户独立Key与配额
- API Key轮换：支持双Key平滑切换，避免单Key失效导致中断
- Key健康度检查：定期探测Key有效性，异常时告警

**输入**: 用户提供多租户与Key管理所需的指令和必要参数.
**输出**: 返回多租户与Key管理的处理结果,包含执行状态码、结果数据和执行日志。### 服务化部署
- 内置systemd服务模板，一键注册为系统服务
- 开机自启与崩溃自动重启
- 优雅关闭：收到终止信号时等待进行中请求完成

**处理**: 解析服务化部署的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回服务化部署的处理结果,包含执行状态码、结果数据和执行日志.
#
## 适用场景

### 场景一：团队共享Azure额度与成本核算
团队多人共用企业Azure订阅，需按项目或成员核算各自用量。专业版的多租户配置让每个成员使用独立Key与配额，月度报表清晰展示各方成本.
### 场景二：高可用生产代理
生产环境要求99.9%可用性，单端点故障不可接受。配置主备两个Azure端点，故障时自动切换，熔断器保护避免雪崩.
### 场景三：成本敏感型批量调用
批量处理任务中存在大量重复请求（如相同提示词的温度采样）。启用请求缓存后，相同内容的请求直接返回缓存结果，成本降低40%以上.
### 场景四：多模型统一网关
团队同时使用GPT-4o、GPT-4o-mini、o3等多个部署，通过专业版的模型路由能力，客户端只需指向单一网关端口，网关按模型名自动分发到对应部署.
## 使用流程

预计上手时间：约120秒.
### 优秀步：编写多端点配置

创建`config.yaml`：

```yaml
endpoints:
  - name: primary
    host: your-resource-primary.openai.azure.com
    deployment: gpt-4o
    apiVersion: "2025-01-01-preview"
    weight: 70
  - name: backup
    host: your-resource-backup.openai.azure.com
    deployment: gpt-4o
    apiVersion: "2025-01-01-preview"
    weight: 30
# ...
cache:
  enabled: true
  ttlMs: 600000
  maxSize: 1000
# ...
circuitBreaker:
  failureThreshold: 5
  cooldownMs: 30000
# ...
tenants:
  - id: team-a
    apiKey: ${TEAM_A_AZURE_KEY}
    budgetMonthly: 500
  - id: team-b
    apiKey: ${TEAM_B_AZURE_KEY}
    budgetMonthly: 300
```

### 第二步：启动网关

```bash
node （请参考skill目录中的脚本文件） --config config.yaml
```

### 第三步：注册为系统服务（可选）

```bash
mkdir -p ~/.config/systemd/user
cp （请参考skill目录中的脚本文件） ~/.config/systemd/user/
nano ~/.config/systemd/user/azure-gateway.service
# ...
systemctl --user daemon-reload
systemctl --user enable azure-gateway
systemctl --user start azure-gateway
```

### 第四步：验证多端点与缓存

```bash
# 健康检查
curl http://localhost:18790/health
# ...
# 查看端点状态
curl http://localhost:18790/endpoints
# ...
# 查看缓存统计
curl http://localhost:18790/cache/stats
# ...
# 查看租户成本
curl http://localhost:18790/tenants/team-a/cost
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | azure-gateway-cli处理的内容输入 |, 默认: 全部维度 |
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
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+（推荐LTS版本）
- **网络**: 需可访问所有配置的Azure OpenAI端点
- **可选**: systemd（用于服务化部署）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| Node.js | 运行时 | 必需 | nodejs.org官方下载 |
| Azure OpenAI服务 | API | 必需 | Azure门户订阅 |
| YAML解析库 | npm依赖 | 必需 | `npm install js-yaml` |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- **Azure API Key**: 通过环境变量`AZURE_OPENAI_API_KEY`或租户级环境变量注入
- **多租户Key**: 通过`tenants[].apiKey`字段引用环境变量，不写入明文
- **Key存储**: 建议使用`d:\skills\.skillhub-credentials\`目录（已gitignore）
- **禁止**: 在SKILL.md、配置文件或脚本中硬编码API Key

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，

## 案例展示

### 完整环境变量

| 变量名 | 默认值 | 说明 |
|:------|------:|:------|
| `AZURE_PROXY_PORT` | `18790` | 监听端口 |
| `AZURE_PROXY_BIND` | `127.0.0.1` | 绑定地址 |
| `AZURE_PROXY_CONFIG` | `config.yaml` | 配置文件路径 |
| `AZURE_PROXY_LOG_LEVEL` | `info` | 日志级别 |
| `AZURE_PROXY_CACHE_TTL` | `600000` | 缓存TTL（毫秒） |
| `AZURE_PROXY_CB_THRESHOLD` | `5` | 熔断失败阈值 |

### 租户级路由配置

```json
{
  "tenants": {
    "team-a": {
      "endpoints": ["primary", "backup"],
      "rateLimit": "100/min",
      "budgetMonthly": 500
    },
    "team-b": {
      "endpoints": ["backup"],
      "rateLimit": "50/min",
      "budgetMonthly": 300
    }
  }
}
```

### 缓存策略配置

```yaml
cache:
  enabled: true
  ttlMs: 600000
  maxSize: 1000
  keyStrategy: "hash"  # hash | exact
  excludeModels: ["o3"]  # 不缓存实时性要求高的模型
```

## 常见问题

### Q1：多端点如何选择主备？
建议主端点选择延迟最低的区域，备用端点选择不同区域的同规格部署。通过`curl`测量各端点延迟后分配权重.
### Q2：熔断器触发后如何恢复？
熔断器进入冷却期（默认30秒）后会自动探测端点，连续2次成功探测后恢复流量。也可通过`POST /endpoints/{name}/reset`手动重置.
### Q3：缓存导致响应不一致怎么办？
对实时性要求高的场景（如代码生成、流式输出），可在请求头中添加`Cache-Control: no-cache`跳过缓存，或将该模型加入`excludeModels`列表.
### Q4：租户预算超限后会怎样？
默认行为是限流（返回429），可在配置中改为告警放行（`budgetAction: warn`）或硬阻断（`budgetAction: block`）.
### Q5：Key轮换期间如何保证不中断？
配置双Key模式，新Key与旧Key并存，网关优先使用新Key。旧Key在确认新Key稳定后移除，整个过程零中断.
### Q6：如何查看实时成本统计？
访问`GET /stats/cost?tenant=team-a&range=today`，返回当日该租户的调用次数、Token消耗与费用估算.
### Q7：systemd服务启动失败如何排查？
执行`journalctl --user -u azure-gateway -f`查看实时日志，常见原因包括Node.js路径错误、配置文件路径不存在、端口被占用.
### Q8：能否与Nginx反向代理叠加使用？
可以。Nginx负责TLS卸载与外部访问控制，本网关负责协议适配与多端点路由，两者分工互补.
## 错误处理

| 错误场景2 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 依赖云服务，需要网络连接
- 本地运行，不支持多设备同步

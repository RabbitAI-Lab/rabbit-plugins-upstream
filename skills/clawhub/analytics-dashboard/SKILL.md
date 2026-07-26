---
slug: "analytics-dashboard"
name: "analytics-dashboard"
version: 1.0.1
displayName: "数据分析面板(专业版)"
summary: "全功能数据可视化系统，含widget构建器、高级分析、多通道告警、报表导出与团队协作，支撑企业级监控。"
license: "Proprietary"
edition: "pro"
description: |-
  数据分析面板专业版是面向团队与企业的全功能数据可视化与监控系统。在免费版基础上解锁自定义widget构建器、高级分析（趋势/异常/预测）、多通道告警、报表导出、团队协作与分享、自定义数据源、主题定制、实时数据推送八大高级能力。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理.
tags:
  - 数据可视化
  - 企业仪表盘
  - 高级分析
  - 实时告警
  - 团队协作
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# 数据分析面板(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 数据分析面板(专业版)高级分析 | 不支持 | 支持 |
| 数据分析面板(专业版)报表导出 | 不支持 | 支持 |
| 数据分析面板(专业版)支撑企业级监控 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |

## 核心能力

### 功能一：自定义widget构建器
支持拖拽式创建多种widget类型：

| Widget类型 | 适用场景 | 配置参数 |
|:---------|:---------|:---------|
| 折线图 | 趋势分析 | data_source, x_field, y_field, time_range |
| 柱状图 | 对比分析 | data_source, dimension, metric |
| 饼图 | 占比分析 | data_source, dimension, metric |
| 指标卡 | KPI展示 | data_source, metric, target |
| 数据表 | 明细查看 | data_source, columns, page_size |
| 热力图 | 时段分析 | data_source, x_dimension, y_dimension |
| 甘特图 | 任务进度 | data_source, tasks, timeline |
| 状态卡片 | 实时状态 | data_source, status_field |

> 详细代码示例已移至 `references/detail.md`

**构建器能力**：
- 拖拽布局，自由调整widget位置与大小
- 多数据源关联（同一widget可聚合多个数据源）
- 条件样式（如指标超阈值变红）
- 联动筛选（点击一个widget筛选其他widget）

> 详细内容已移至 `references/detail.md` - ### 功能二：高级分析
### 功能三：多通道告警
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供功能三：多通道告警所需的指令和必要参数.
**处理**: 解析功能三：多通道告警的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回功能三：多通道告警的处理结果,包含执行状态码、结果数据和执行日志。### 功能四：报表导出
```bash
agent dashboard export --format pdf --output report.pdf
agent dashboard export --format csv --output data.csv
agent dashboard export --format excel --output report.xlsx
# ...
```

**输入**: 用户提供功能四：报表导出所需的指令和必要参数.
**处理**: 解析功能四：报表导出的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 功能五：团队协作与分享
> 详细代码示例已移至 `references/detail.md`

**协作能力**：
- 多用户登录（本地/LDAP/OAuth）
- 角色权限管理（admin/editor/viewer）
- 共享面板（团队可访问）
- 评论与标注（针对widget数据点）
- 操作审计日志

**处理**: 解析功能五：团队协作与分享的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回功能五：团队协作与分享的处理结果,包含执行状态码、结果数据和执行日志。### 功能六：自定义数据源
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供功能六：自定义数据源所需的指令和必要参数.
**处理**: 解析功能六：自定义数据源的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回功能六：自定义数据源的处理结果,包含执行状态码、结果数据和执行日志。### 功能七：主题定制
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供功能七：主题定制所需的指令和必要参数.
**处理**: 解析功能七：主题定制的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回功能七：主题定制的处理结果,包含执行状态码、结果数据和执行日志。### 功能八：实时数据推送
```javascript
// WebSocket实时推送
const ws = new WebSocket('ws://localhost:19195/ws?token=详情见说明');
// ...
ws.onmessage = function(event) {
  const data = JSON.parse(event.data);
  // 数据更新时自动推送，无需轮询
  updateWidget(data.widget_id, data.payload);
};
// ...
// 推送事件类型
// {type: "widget_update", widget_id: "详情见说明", payload: {...}}
// {type: "alert", rule: "详情见说明", message: "..."}
// {type: "anomaly", source: "详情见说明", data: {...}}
```

**输入**: 用户提供功能八：实时数据推送所需的指令和必要参数.
**输出**: 返回功能八：实时数据推送的处理结果,包含执行状态码、结果数据和执行日志.
### Widget类型

针对Widget类型,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Widget类型相关的配置参数、输入数据和处理选项.
**输出**: 返回Widget类型的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Widget类型`的配置文档进行参数调优
#
## 适用场景

**痛点**：运营总监需要实时掌握邮件处理、任务执行、SLA达标情况，但数据分散在多个系统.
**配置**：
```text
1. 创建运营大屏，含6个widget：
   - 邮件趋势折线图（近30天）
   - 任务状态饼图
   - SLA达标率指标卡
   - 异常告警热力图
   - 团队负载柱状图
   - 实时事件流
2. 配置多通道告警（邮件量异常、SLA违规、任务失败率）
3. 每日9点自动生成PDF报告发送邮件
4. WebSocket实时推送，无需刷新
```

**效果**：一屏掌握运营全貌，异常即时告警，每日报告自动生成，决策效率提升50%.
## 使用流程

### 60秒上手（升级激活）
专业版完全兼容免费版的目录结构与配置格式：

```bash
ls ~/workspace/dashboard/
# ...
cat ~/workspace/dashboard/config.json | grep edition
```

### 120秒上手（自定义widget）
```text
用户："帮我创建一个widget，展示近7天每日邮件数量趋势图"
# ...
Agent："已创建widget：
  类型：折线图
  数据源：inbox.jsonl
  维度：按日聚合（近7天）
  指标：邮件数量
  刷新：5分钟
  已添加到面板首页
  🆔 widget_email_trend_7d"
```

### 300秒上手（完整企业配置）

以下是数据分析面板(专业版)的快速搭建流程，从初始化到完整配置的步骤说明.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | analytics-dashboard处理的内容输入 |, 默认: 全部维度 |
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

| 问题 | 可能原因 | 解决方案 | 优先级 |
|:---:|:---:|:---:|:---:|
| 面板无法访问 | 端口被占用或token错误 | 检查端口占用；确认URL中token正确 | 高 |
| widget无数据 | 数据源文件不存在或格式错误 | 检查数据源路径；验证文件格式 | 高 |
| 实时推送不工作 | WebSocket连接失败 | 检查WebSocket端口；确认网络允许WS | 中 |
| 告警未触发 | 规则条件配置错误或窗口不足 | 验证条件表达式；检查时间窗口配置 | 高 |
| 报表导出失败 | 依赖未安装或权限不足 | 安装puppeteer（PDF）依赖；检查写权限 | 中 |
| 分析结果异常 | 数据量不足或数据质量差 | 确保30+数据点；清洗异常数据 | 中 |
| 团队登录失败 | 认证配置错误或用户不存在 | 检查auth_provider配置；确认用户已创建 | 高 |
| 自定义数据源超时 | 查询过慢或连接不稳定 | 优化查询；增加超时配置；启用缓存 | 中 |
| 面板加载缓慢 | widget过多或数据量大 | 减少widget数量；启用懒加载；增加刷新间隔 | 中 |
| 主题不生效 | 配置缓存或路径错误 | 清除浏览器缓存；检查主题配置路径 | 低 |
| 共享面板无法访问 | 权限配置错误或URL错误 | 检查共享面板access配置；确认URL正确 | 高 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+（用于Web服务器与WebSocket）
- **Python**: 3.8+（用于高级分析与报表生成）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| Express | npm包 | 必需 | `npm install express` |
| ws | npm包 | 实时推送必需 | `npm install ws` |
| Puppeteer | npm包 | PDF导出必需 | `npm install puppeteer` |
| Chart.js | 前端库 | 图表必需 | CDN引入或本地安装 |
| scikit-learn | Python库 | 异常检测必需 | `pip install scikit-learn` |
| Prophet | Python库 | 预测必需 | `pip install prophet` |

### API Key 配置
- 面板token：通过环境变量`DASHBOARD_TOKEN`配置或自动生成
- 数据库连接串：通过环境变量`DB_CONNECTION`配置
- 外部API token：通过环境变量传入
- 告警webhook：通过环境变量`DINGTALK_WEBHOOK`/`FEISHU_WEBHOOK`配置
- OAuth凭证：通过环境变量`OAUTH_CLIENT_ID`/`OAUTH_CLIENT_SECRET`配置
- 所有敏感信息通过环境变量传入，禁止硬编码在配置文件中

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，

## 案例展示

### 场景二：SLA实时监控（SRE角色）
**痛点**：SRE需要实时监控SLA达标情况，SLA违规需要立即告警并升级.
**配置**：

**效果**：SLA达标率实时可视，低于99.9%立即钉钉+电话告警，5分钟未处理自动升级.
### 场景三：定期报表自动分发（数据分析师角色）
**痛点**：每周需要手动整理数据生成报表并分发给管理层，耗时且容易遗漏.
**配置**：
```json
{
  "scheduled_reports": [
    {
      "name": "周度运营报告",
      "schedule": "0 10 * * 1",
      "format": "pdf",
      "widgets": ["email_trend", "task_completion", "sla_summary"],
      "recipients": ["ceo@company.com", "cto@company.com"],
      "include_analysis": true
    }
  ]
}
```

**效果**：每周一10点自动生成含趋势分析的PDF报告，自动分发给管理层，无需手动整理.
### 场景四：跨部门数据共享（产品经理角色）
**痛点**：产品数据需要与运营、技术团队共享，但各团队工具不同，数据孤岛严重.
**配置**：
```text
1. 创建共享面板"产品运营大屏"
2. 配置viewer权限给运营与技术团队
3. 部署在内网，团队通过SSO登录
4. 各团队可查看但不能修改
```

**效果**：跨部门数据共享透明化，减少沟通成本，各团队对产品状态有统一认知.
## 常见问题

### Q1：免费版与专业版有什么区别？
免费版提供3个固定数据源、基础图表、token保护、5秒刷新。专业版新增8大功能：widget构建器、高级分析（趋势/异常/预测）、多通道告警、报表导出、团队协作、自定义数据源、主题定制、实时推送。此外提供多角色场景指南、性能优化策略和多平台集成示例.
### Q2：widget构建器支持哪些图表类型？
支持8种widget：折线图、柱状图、饼图、指标卡、数据表、热力图、甘特图、状态卡片。每种widget可自定义数据源、聚合方式、样式、刷新频率。支持拖拽布局与联动筛选.
### Q3：高级分析的准确率如何？
趋势分析基于线性回归，准确率取决于数据量（建议30+数据点）。异常检测基于Isolation Forest，对突增/突降检测准确率约90%。预测基于Prophet模型，短期（7天）预测准确率约80-85%，长期预测准确率递减.
### Q4：告警如何避免误报？
三种机制减少误报：
- **窗口聚合**：基于时间窗口（如1小时）而非瞬时值判断
- **灵敏度调节**：anomaly_detection的sensitivity参数可调（0.9-0.99）
- **冷却期**：同一规则触发后5分钟内不重复告警

### Q5：报表导出支持哪些格式？
支持PDF（适合正式报告）、CSV（适合数据分析）、JSON（适合系统集成）、Excel（适合业务人员）。报表可包含widget截图、数据表格、分析结论。支持定时自动生成与分发.
### Q6：团队协作如何管理权限？
三级角色：admin（全权限）、editor（查看+编辑+导出）、viewer（仅查看）。支持本地账号、LDAP、OAuth三种认证方式。共享面板可设置团队可见或指定用户可见。所有操作记录审计日志.
### Q7：自定义数据源支持哪些类型？
支持4种：文件（JSONL/JSON/CSV）、数据库（PostgreSQL/MySQL/SQLite）、API（REST GET/POST）、实时流（Webhook/MQTT）。每种数据源可配置刷新频率与查询语句。敏感连接信息通过环境变量传入.
### Q8：实时推送与5秒刷新有什么区别？
5秒刷新是前端轮询（每5秒请求一次），实时推送是WebSocket服务端主动推送。实时推送延迟更低（毫秒级），服务器负载更低（无空轮询），但需要WebSocket支持。建议关键指标用实时推送，非关键指标用轮询.
### Q9：主题定制能做什么？
支持亮色/暗色/自动三种模式，可自定义品牌Logo、主色、辅色、字体。支持侧边栏开关、布局密度（舒适/紧凑）、网格列数。暗黑模式适合监控大屏夜间展示，品牌定制适合企业内部使用.
### Q10：面板能承载多少个widget？
技术上无硬性限制，但建议单个面板不超过20个widget，避免性能下降与信息过载。大量widget建议分多个面板（如"运营面板"、"技术面板"、"财务面板"），通过导航切换。每个widget可独立配置刷新频率.
### Q11：数据源连接断开会怎样？
数据源连接断开时，对应widget显示"数据源不可用"提示，但不影响其他widget。系统每30秒尝试重连，重连成功后自动恢复。可配置告警规则，在数据源断开超5分钟时通知运维.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用

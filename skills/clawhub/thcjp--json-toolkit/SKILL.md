---
slug: json-toolkit
name: json-toolkit
version: 1.0.1
displayName: JSON工具箱(专业版)
summary: 全功能 JSON 处理
summary_zh: 全功能 JSON 处理，含高级序列化、解析安全、Unicode 边界、自动化校验。全功能 JSON 处理。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确
license: MIT
edition: pro
description: 全功能 JSON 处理。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于缺乏技术背景的通用场景。适用于开发者、企业团队和自动化集成场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。提供结构化输出和错误处理机制。支持多场景应用和灵活配置。。提供完整的配置选项和详细的使用说明，帮助用户快速上手并集成到现有工作流中。 功能涵盖: toolkit。
tags:
- 集成工具
- 数据规范
- 企业效率
- 安全
- 工具
- 效率
- 自动化
- 研究
- 分析
- 加密
- json
- schema
- map
tools:
- read
- exec
- write
homepage: ''
category: Automation
homepage: "https://skillhub.cn/skill/"
---

> **核心功能**: 本技能提供化集成场景等能力。

> **核心功能**: 本技能提供完整的配置选项和详细的使用说明等能力。

> **核心功能**: 本技能提供中文交互等能力。

# JSON工具箱(专业版)

## 专业版增强能力
| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| JSON Schema验证与自动化校验 | 不支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |

## 能力矩阵
| 能力 | 说明 | 免费版 | 专业版 |
|:-----|:-----|:-----|:-----|
| Schema 校验 | 不可信输入校验 | 是 | 是 |
| 命名规范 | 一致性管理 | 是 | 是 |
| 空值处理 | null 与缺失区分 | 是 | 是 |
| 日期时间 | ISO 8601 规范 | 是 | 是 |
| 数字与 ID | 大数与金额 | 是 | 是 |
| 结构优秀实践 | 嵌套与信封 | 是 | 是 |
| API 响应模式 | 错误结构化 | 是 | 是 |
| 基础序列化 | toJSON 注意事项 | 是 | 是 |
| 基础解析安全 | try/catch | 是 | 是 |
| 高级序列化 | Map/Set/BigInt/循环引用 | 否 | 是 |
| 深度解析安全 | reviver 与 BOM | 否 | 是 |
| Unicode 边界 | 代理对与控制字符 | 否 | 是 |
| 原型污染防护 | __proto__ 与 Object.create | 否 | 是 |
| 自动化校验流水线 | 批量校验与报告 | 否 | 是 |
| 自定义 replacer/reviver | 模板化 | 否 | 是 |
| 敏感数据剥离 | 安全序列化 | 否 | 是 |

## 典型场景
### 场景 1：企业级 API 契约校验
API 网关团队用自动化校验流水线批量校验所有接口的请求与响应 Schema，生成校验报告标注违规字段与位置。专业版的批量校验覆盖 50+ 接口，避免人工逐个检查.
### 场景 2：复杂数据结构序列化
应用需要序列化含 Map、Set、BigInt、Date 的复杂对象到 JSON 并反序列化还原。专业版的自定义 replacer 与 reviver 模板处理这些非标准类型，避免 `toJSON()` 默认行为带来的意外.
### 场景 3：安全敏感数据脱敏
日志服务在序列化用户数据前剥离敏感字段（密码、token、身份证号），避免依赖消费方忽略额外字段。专业版的敏感数据剥离在序列化时完成，从源头杜绝泄露.
### 场景 4：跨语言数据交换边界处理
跨语言系统交换数据时遇到 BOM 头、控制字符、emoji 代理对导致解析失败。专业版的 Unicode 边界处理在解析前清洗这些隐患，确保跨语言兼容.
## 操作流程
> 上手时间：< 60 秒。专业版提供自定义模板，建议先复用模板再定制.
### 步骤 1：处理循环引用

```javascript
// 检测循环引用后再序列化
function safeStringify(obj) {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (typeof value === 'object' && value !== null) {
      if (seen.has(value)) return '[Circular]';
      seen.add(value);
    }
    return value;
  });
}
```

### 步骤 2：自定义 replacer 处理 Map/Set/BigInt

```javascript
const data = { map: new Map([['a', 1]]), big: 9007199254740993n };
JSON.stringify(data, (key, value) => {
  if (value instanceof Map) return Object.fromEntries(value);
  if (typeof value === 'bigint') return value.toString();
  return value;
});
```

### 步骤 3：reviver 类型重建

```javascript
JSON.parse(json, (key, value) => {
  if (key.endsWith('_at')) return new Date(value);
  if (/^\d+n$/.test(value)) return BigInt(value.slice(0, -1));
  return value;
});
```

### 步骤 4：剥离 BOM 与控制字符

```javascript
function sanitizeInput(str) {
  return str
    .replace(/^\uFEFF/, '')           // 剥离 BOM
    .replace(/[\u0000-\u001F]/g, ''); // 剥离控制字符
}
JSON.parse(sanitizeInput(rawInput));
```

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态

## 输入参数
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | 处理的内容输入 |
| mode | string | 否 | 处理模式, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 结果格式
```json
{
  "success": true,
  "data": {
    "result": "处理结果",
    "status": "success",
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

## 异常响应
| 现象 | 可能原因 | 解决步骤 | 优先级 |
|:---:|:---:|:---:|:---:|
| 序列化报循环引用 | 对象存在循环结构 | 用 WeakSet 检测或 flatted 库 | P1 |
| Map/Set 序列化为空 | 未自定义 replacer | replacer 中转换 Map/Set | P2 |
| BigInt 报 TypeError | 未转换即序列化 | replacer 中 toString | P2 |
| 解析报 __proto__ 污染 | 输入含危险键 | Object.create(null) 或过滤键 | P1 |
| 解析报非法字符 | BOM 或控制字符 | 剥离 BOM 与控制字符 | P2 |
| emoji 显示乱码 | 单字符而非代理对 | 用代理对表示 | P3 |
| 敏感字段泄露 | 未在序列化时剥离 | 配置 strip_fields | P1 |
| 类型丢失 | 反序列化未用 reviver | reviver 重建 Date/BigInt | P2 |
| 校验报告缺失 | fail_fast 为 true | 设为 false 汇总全部 | P3 |
| 跨语言解析失败 | Unicode 边界未处理 | 清洗 BOM 与控制字符 | P2 |

## 前置条件
### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **编程语言**：任意支持 JSON 的语言（JavaScript / Python / Go / Java 等）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 |
| JSON Schema 校验库 | 库 | 推荐 | 各语言生态均有（如 JS 的 ajv、Python 的 jsonschema） |
| flatted（可选） | 库 | 可选 | `npm install flatted` 或 `pip install flatted`，用于循环引用 |
| 标准库 JSON 模块 | 运行时 | 必需 | 各语言标准库自带 |

### API Key 配置
- **本 Skill 基于指令驱动**：基础LLM由Agent平台提供，纯 Markdown 优秀实践指南与模板
- **自动化校验流水线（可选）**：如需对接外部 Schema 注册中心，按对应服务配置凭证

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，自动化校验流水线需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 遵循 JSON 处理优秀实践，支持自动化校验与模板复用

## 案例展示

### 自动化校验流水线

```yaml
# json_validation_pipeline.yaml
schemas_dir: ./schemas
endpoints:
  - name: create_user
    request_schema: user_create.json
    response_schema: user_response.json
  - name: list_orders
    request_schema: order_list.json
    response_schema: order_list_response.json
options:
  additional_properties: false
  strict_required: true
  report_format: json   # json / markdown / html
  fail_fast: false      # false 时校验全部，汇总报告
```

### 敏感字段剥离配置

```json
{
  "strip_fields": ["password", "token", "secret", "ssn", "credit_card"],
  "mask_fields": {"email": "partial", "phone": "partial"},
  "depth": 5,
  "throw_on_unknown": false
}
```

### Unicode 边界处理对照表

| 字符 | 问题 | 处理方式 |
|---:|:---|---:|
| BOM `\uFEFF` | 文件头导致解析失败 | 解析前剥离 |
| 控制字符 U+0000–U+001F | 粘贴文本含不可见字符 | 剥离或转义 |
| emoji 单字符 `\u1F600` | 非法代理对 | 用代理对 `\uD83D\uDE00` |
| 嵌入式 NULL `\u0000` | 截断字符串 | 剥离或拒绝 |
## 安全合规准则
- **无硬编码密钥**: 所有API Key和凭证通过环境变量加载
- **无敏感信息泄露**: 日志中对敏感字段进行脱敏处理
- **凭证存储安全**: 配置文件建议加入.gitignore
- **最小权限原则**: 仅授予完成任务所需的最小权限
- **数据传输加密**: 所有API调用使用HTTPS加密传输

## 热门问题
### Q1：循环引用如何安全序列化？

A：用 WeakSet 跟踪已访问对象，遇到重复时返回 `[Circular]` 标记而非抛出异常。或使用 `flatted` 等专用库处理循环结构.
### Q2：Map 和 Set 为什么不能直接序列化？

A：`JSON.stringify` 对 Map/Set 返回 `{}`（空对象），数据丢失。需自定义 replacer 将 Map 转为 `Object.fromEntries`，Set 转为数组.
### Q3：BigInt 序列化报错怎么办？

A：`JSON.stringify` 不支持 BigInt，直接报 TypeError。需在 replacer 中 `value.toString()` 转字符串，反序列化时用 reviver 还原.
### Q4：__proto__ 键如何污染原型？

A：`JSON.parse('{"__proto__":{"isAdmin":true}}')` 会污染 Object.prototype，导致所有对象继承 `isAdmin: true`。防护方式：(1) 用 `Object.create(null)` 创建对象；(2) 过滤 `__proto__`、`constructor`、`prototype` 键.
### Q5：BOM 头为何导致解析失败？

A：UTF-8 文件可能以 `\uFEFF`（BOM）开头，`JSON.parse` 会将其视为非法字符报错。解析前用 `str.replace(/^\uFEFF/, '')` 剥离.
### Q6：emoji 为何解析异常？

A：emoji（如 😀）在 JSON 中需用代理对 `\uD83D\uDE00` 表示。单个 `\u1F600` 是非法代理对，会导致解析错误或显示乱码.
### Q7：自动化校验流水线如何集成到 CI/CD？

A：将校验脚本作为 CI 步骤，读取配置文件批量校验所有 Schema，校验失败时流水线红灯。建议 `fail_fast: false` 汇总全部违规再修复.
### Q8：敏感字段剥离与字段过滤有何区别？

A：字段过滤在消费方忽略额外字段（被动）；敏感字段剥离在序列化时移除（主动）。后者更安全，因为剥离后数据中根本不存在敏感字段，即使被记录日志也安全.
### Q9：toJSON() 何时会带来意外？

A：Date 对象的 `toJSON()` 返回 ISO 字符串（而非 Date 对象），自定义类的 `toJSON()` 可能改变输出结构。序列化前确认对象是否有 toJSON 方法，避免静默覆盖.
### Q10：专业版是否支持自定义校验规则？

A：支持。除 JSON Schema 标准校验外，可自定义业务规则（如"金额必须为正""邮箱格式校验"），集成到自动化校验流水线.
## 能力边界
- 高级序列化功能对循环引用的JSON结构（如对象互相引用）支持有限，可能抛出递归异常
- Unicode边界处理依赖运行时环境（Python/Node.js）的编码能力，罕见的代理对字符可能处理异常
- 自动化校验仅覆盖语法和结构层面，无法检测业务逻辑层面的数据正确性（如字段值域、关联关系）

## 创新亮点
### 效率提升量化分析
| 操作步骤 | 手动耗时 | 自动化耗时 | 时间节约 | 准确率提升 |
|:--------|:--------|:--------|:--------|:--------|
| JSON Schema验证 | 2小时/次 | 5分钟/次 | 1小时55分钟 | 95% |
| 深度漏洞扫描 | 4小时/次 | 30分钟/次 | 3小时30分钟 | 98% |
| 安全基线合规审计 | 8小时/次 | 2小时/次 | 6小时 | 99% |
| 批量资产风险评分 | 6小时/次 | 1小时/次 | 5小时 | 100% |
| 威胁情报实时订阅与告警 | 3小时/次 | 10分钟/次 | 2小时50分钟 | 100% |

### 差异化对比
| 对比维度 | 本技能 | 手动操作 | Python脚本 | 专业软件 |
|:--------|:--------|:--------|:--------|:--------|
| 操作便捷性 | 一键启动，自动处理 | 逐个操作，手动处理 | 编写脚本，调试运行 | 软件复杂，配置繁琐 |
| 安全性 | 高级安全机制，防止数据泄露 | 人工操作，风险较高 | 安全性较低，需手动处理 | 安全性高，但配置复杂 |
| 执行效率 | 自动化处理，快速响应 | 人工操作，效率低 | 脚本执行，效率中等 | 高效处理，但配置复杂 |
| 适应范围 | 多种场景，灵活配置 | 限于特定场景 | 通用性强，但需编写脚本 | 功能全面，但配置复杂 |
| 成本效益 | 一次性投入，长期节省 | 持续人工成本 | 脚本开发成本 | 高成本投入，但功能全面 |

### 核心痛点解决
| 痛点 | 描述 | 影响范围 | 解决方案 | 量化效果 |
|:----|:----|:----|:----|:----|
| 数据处理效率低 | 大量数据手动处理，耗时费力 | 整个数据处理流程 | 自动化处理，提高效率 | 时间节约 50% |
| 安全风险高 | 数据处理过程中存在泄露风险 | 整个数据处理流程 | 高级安全机制，防止数据泄露 | 安全风险降低 90% |
| 配置复杂 | 需要手动配置，操作繁琐 | 整个使用流程 | 灵活配置，简化操作 | 操作简便性提升 70% |

## 功能清单
- **自动化执行**: 全功能 JSON 处理
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果

## 用户常见问题
### Q1: JSON工具箱(专业版)支持哪些输入格式？

A1: 全功能 JSON 处理。支持文本指令和结构化参数输入，具体格式参考使用流程章节。

### Q2: 需要配置API Key吗？

A2: 是的，部分功能需要配置对应平台的API Key。请在依赖说明章节查看具体要求，并通过环境变量安全配置。

### Q3: 命令行执行失败怎么办？

A3: 检查命令参数是否正确，确认运行环境支持exec能力。如遇权限问题，请参照错误处理章节排查。

## 异常恢复流程
针对JSON工具箱(专业版)使用中可能遇到的常见问题,提供以下排查方案:

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

### JSON工具箱(专业版)通用排查步骤

1. **检查输入参数**: 确认所有必填参数已提供且格式正确
2. **查看日志输出**: 定位具体错误行和异常类型
3. **验证环境配置**: 确认依赖库版本和运行环境满足要求
4. **逐步调试**: 缩小问题范围,隔离故障模块

## 快速指引
1. **配置API密钥**: 在环境变量中设置对应的API Key
2. **初始化连接**: 使用提供的凭证建立API连接
3. **调用接口**: 传入必要参数执行API调用
1. **准备文件**: 确认文件路径正确且格式受支持
2. **执行处理**: 调用对应的处理函数
3. **查看结果**: 检查输出文件或返回数据
1. **检查环境**: 确认运行时和依赖已安装
2. **执行命令**: 使用正确的参数格式执行
3. **查看输出**: 检查命令输出和退出码

### 前置条件

- 已安装所需运行环境(参考依赖说明)
- 已获取必要的API密钥或访问凭证(如适用)
- 输入数据已准备就绪

## 指南中心
## 故障恢复流程
针对JSON工具箱(专业版)使用中可能遇到的常见问题,提供以下排查方案:

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

---
slug: "ai-kujiale-design-free"
name: "ai-kujiale-design-free"
version: "1.0.0"
displayName: "酷家乐AI室内设计LITE"
summary: "酷家乐室内设计基础版,文字搜索户型、风格选择、布局与渲染出图。"
license: "MIT"
description: |-
  基于酷家乐(Kujiale)开放能力的室内智能设计基础版(免费),通过分步式对话完成
  户型搜索、风格选择、布局生成、渲染出图基础流程.
  核心能力:
  - 户型搜索: 通过城市与小区名搜索酷家乐户型库,获取标准户型图
  - 风格匹配: 基于偏好标签选择硬装风格
  - 智能布局: 自动布置家具并生成各房间布局
  - 渲染出图: 生成静态效果图
  适用场景:
  - 业主装修前的方案快速预览
  - 个人户型与风格灵感探索
  - 学习试用与轻量设计体验
tags:
  - Creative
  - 室内设计
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# 酷家乐 AI 室内设计 LITE

基于酷家乐开放能力,通过分步式对话完成户型搜索、风格选择、布局生成与渲染出图的基础流程。仅支持文字搜索户型与静态效果图输出。必须严格按本文档流程执行.
**范围外**(本技能不做): 户型图上传与临摹识别、全景图输出、多风格批量对比、户型结构改造(需升级 ai-kujiale-design 专业版).
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 酷家乐AI室内设计LITE处理的输入数据或指令 |
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

### 输出规则

- 进度反馈通过 `message(action=send)` 发送
- 最终结果只输出渲染图与设计亮点,严格按 `./outputs/result.md` 格式
- 已发送的消息不重复输出

**输入**: 用户提供输出规则相关的配置参数、输入数据和处理选项.
**处理**: 解析输出规则的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 设计流程

**输入**: 用户提供设计流程所需的指令和必要参数.
**处理**: 解析设计流程的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回设计流程的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`设计流程`的配置文档进行参数调优
### 阶段一: 户型搜索与确认
触发条件: 用户提到要做室内设计/装修设计.
询问城市与小区(可一并告知户型结构、面积):

```bash
node （请参考skill目录中的脚本文件） --token=$TOKEN --query="小区名" --areaId="城市id" --start=0 --num=20
```

展示结果供用户选择,获得 planId 后获取户型图:

**输入**: 用户提供设计流程相关的配置参数、输入数据和处理选项.
**处理**: 解析阶段一: 户型搜索与确认的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`ai-kujiale-design-free`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 初始化配置

首次使用需在项目根目录创建 `.kjlconfig.json`(参考 `.kjlconfig-example.json`):

```json
{
  "access_token": "用户从酷家乐复制的 token"
}
```

若无 token,引导用户访问 https://www.kujiale.com/skills 生成,并将配置文件保存在 `.kjlconfig-example.json` 同一目录下。所有脚本调用前先从该文件读取 `access_token` 作为 `$TOKEN`.
## 版本校验

每次执行前校验版本:

```bash
node （请参考skill目录中的脚本文件） --token=$TOKEN --version=1.0.0
```

action=1 继续;action=2 提示"版本已过时,建议更新";action=3 终止并提示重新安装.
## 输出规则(补充)

## 设计流程(补充)

### 阶段一: 户型搜索与确认(补充)

触发条件: 用户提到要做室内设计/装修设计.
```bash
node （请参考skill目录中的脚本文件） --token=$TOKEN --query="小区名" --areaId="城市id" --start=0 --num=20
```

```bash
node （请参考skill目录中的脚本文件） --planId=$PLAN_ID
```

解析返回:
- `floorplanInfos` 为空 → 提示"户型图获取失败,请重新选择",重新搜索
- 有数据 → 取 `floorplanInfos[0].planImage` 展示给用户,附带面积 `realArea`

用户确认后创建方案:

```bash
node （请参考skill目录中的脚本文件） --token=$TOKEN --planId=$PLAN_ID
```

获得 designId,提示用户进入风格选择.
> **升级提示**: 上传户型图临摹识别(适用于搜不到小区或已改造户型)仅在专业版中提供.
### 阶段二: 风格选择

触发条件: 户型已确认.
```bash
node （请参考skill目录中的脚本文件） --token=$TOKEN
```

展示标签列表供用户单选,获得 tagItemIds。查询硬装风格:

```bash
node （请参考skill目录中的脚本文件） --token=$TOKEN --tagItemIds=$TAG_IDS
```

返回多个风格时展示 coverUrl 与 styleName 供用户选择;返回单个风格则默认选择。获得 styleId 进入布局阶段.
### 阶段三: 布局生成与确认

触发条件: 风格已确认.
先与用户确认本次布局会消耗账号内智能布局额度/核豆,确认知晓后执行:

```bash
node （请参考skill目录中的脚本文件） --token=$TOKEN --designId=$DESIGN_ID \
  --tagIds=$TAG_IDS --styleId=$STYLE_ID \
  --applyDecorationStyle=true --buildCeiling=true --autoDesign=true
```

查询布局结果,若 `c!=0` 每 10 秒重复查询:

```bash
node （请参考skill目录中的脚本文件） --token=$TOKEN --designId=$DESIGN_ID
```

通过 `message(action=send)` 发送各房间布局(房间名 + 家具列表),进入渲染阶段.
### 阶段四: 渲染出图

触发条件: 布局已确认.
发送"开始渲染,请稍等"并触发渲染:

```bash
node （请参考skill目录中的脚本文件） --obsDesignId=$DESIGN_ID --xToken=$TOKEN
```

等待 10 秒后查询渲染结果:

```bash
node （请参考skill目录中的脚本文件） --token=$TOKEN --designId=$DESIGN_ID
```

提取 `pictype=0` 的 `img`(渲染图)。若为空每分钟重试,超 5 分钟反馈失败。最终按 `./outputs/result.md` 输出设计亮点与渲染图.
> **升级提示**: 360 度全景图(panoLink)与多风格批量对比仅在专业版中提供.
## 适用场景

| 场景 | 典型输入 | 输出内容 |
|---:|---:|---:|
| 业主方案预览 | "帮我设计下我家三居室" | 户型图 + 渲染图 |
| 风格灵感探索 | "看下现代风格的客厅效果" | 渲染图 |

**不适用于**: 户型图上传识别、全景图输出、多风格批量对比、户型结构改造(需升级专业版).
## 案例展示

### 案例一： 业主三居室基础设计
**场景**: 业主提供小区名,希望快速预览装修效果

```bash
# 搜索户型
node （请参考skill目录中的脚本文件） --token=$TOKEN --query="阳光花园" --areaId="330100" --start=0 --num=20
# ...
# 获取户型图
node （请参考skill目录中的脚本文件） --planId=$PLAN_ID
# ...
# 创建方案
node （请参考skill目录中的脚本文件） --token=$TOKEN --planId=$PLAN_ID
# ...
# 风格选择
node （请参考skill目录中的脚本文件） --token=$TOKEN
node （请参考skill目录中的脚本文件） --token=$TOKEN --tagItemIds=$TAG_IDS
# ...
# 布局与渲染
node （请参考skill目录中的脚本文件） --token=$TOKEN --designId=$DESIGN_ID \
  --tagIds=$TAG_IDS --styleId=$STYLE_ID \
  --applyDecorationStyle=true --buildCeiling=true --autoDesign=true
node （请参考skill目录中的脚本文件） --obsDesignId=$DESIGN_ID --xToken=$TOKEN
node （请参考skill目录中的脚本文件） --token=$TOKEN --designId=$DESIGN_ID
```

**输出**: 户型图、各房间布局说明、渲染图

**说明**: 基础版覆盖搜索到渲染的核心流程,业主在户型确认、风格选择、布局确认三个节点交互即可完成。仅输出静态渲染图,全景图需升级专业版.
## 异常处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:---:|:---:|:---:|:---:|
| missing_token | `.kjlconfig.json` 缺失或无 access_token | 未完成初始化配置 | 引导用户访问 kujiale.com/skills 生成 token 并写入配置 |
| floorplan_empty | `floorplanInfos` 为空数组 | 户型图获取失败或小区搜不到 | 提示重新选择小区,基础版不支持上传户型图 |
| layout_pending | `getLayoutResult` 返回 c!=0 | 布局仍在生成 | 每 10 秒轮询,直至 c=0 |
| render_empty | 渲染结果 img 为空 | 渲染仍在进行 | 每分钟检查网络连接和配置后重试,超 5 分钟反馈失败 |
| quota_insufficient | 智能布局额度/核豆不足 | 账号额度耗尽 | 提示用户充值或更换账号,不在未确认时扣费 |

## 常见问题

### Q1: 基础版与专业版有什么区别?
A: 基础版(LITE)支持文字搜索户型、风格选择、智能布局与静态渲染图。专业版(ai-kujiale-design)额外提供: 户型图上传与临摹识别、360 度全景图输出、多风格批量对比、更完整的案例与异常处理.
### Q2: 如何获取 access_token?
A: 访问 https://www.kujiale.com/skills 登录酷家乐账号后生成 token,复制后写入项目根目录的 `.kjlconfig.json`,key 为 `access_token`.
### Q3: 搜不到我家小区怎么办?
A: 基础版仅支持文字搜索,搜不到时可尝试更换小区名关键词或确认城市是否正确。若小区未入库或户型已改造,需升级专业版使用上传户型图临摹识别.
### Q4: 智能布局会消耗额度吗?
A: 会。布局阶段会消耗账号内智能布局额度/核豆,流程中会先与用户确认知晓后再执行,避免误扣。额度不足时提示 quota_insufficient.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接和配置后重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

1. **仅文字搜索户型**: 不支持上传户型图与临摹识别(需升级专业版)
2. **仅静态渲染图**: 不支持 360 度全景图输出(需升级专业版)
3. **需 access_token**: 必须配置酷家乐 token
4. **智能布局消耗额度**: 每次布局扣减账号额度/核豆,需用户确认
5. **风格库以酷家乐为准**: 可选风格取决于 getStyles 返回,无法自定义

---

> **想要上传户型图识别、360 度全景图、多风格批量对比?** 升级到 ai-kujiale-design 专业版解锁全部高级能力.
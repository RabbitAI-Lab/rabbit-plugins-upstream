---
slug: ai-video-studio-pro
name: ai-video-studio-pro
version: "1.0.1"
displayName: "AI视频导演"
summary: "一个人就是一支视频团队,脚本到成片一站式+智能路由+营销策略注入"
license: Proprietary
description: |-
  AI视频导演是一款从脚本到成片一站式视频制作工具。一个人就是一支视频团队,支持热点短视频生成、
  口型同步数字人、智能路由决策树、多引擎降级。营销策略自动注入,三层TTS降级链保证配音可用性。

  核心能力:
  - 智能路由决策树:5步自动选择最优视频引擎,支持角色一致性/画质/风格化/通用/口型同步多引擎
  - 口型同步数字人:VG-07全流程,人设配置→图片生成→情感语音→口型同步→下载验证
  - 营销策略注入:卖点提炼+情绪钩子+CTA话术,注入脚本关键帧
  - 三层TTS降级链:高质量TTS→备用TTS→静默+字幕,保证交付不中断
  - 场景路由+配额管理:7场景+5卡片+降级链+成本预估+日/月配额检查
homepage: "https://skillhub.cn"
tags: [视频创作, AI视频, 短视频, 数字人, 内容自动化]
tools:
  - read
  - exec
suggested_price: "19.90"
pricing_tier: "business"
pricing_rationale: "视频音频类, medium市场, enterprise复杂度, monthly频次, business层 → 算力消耗大,参考Coze 0.5元/次"
---
# AI视频导演

> 定位: 脚本到成片一站式视频制作
> 设计: 热点短视频生成 + 口型同步视频 + 智能路由决策树 + 多引擎降级

## 核心能力

1. **智能路由决策树**:按5步决策树(硬约束过滤→一致性需求判断→内容类型判断→成本预算过滤→风格偏好注入)自动选择最优视频引擎,支持角色一致性引擎/画质引擎/风格化引擎/通用引擎/口型同步引擎多引擎路由
2. **口型同步数字人**:VG-07口型同步流程,支持agent_id人设出镜,从人设配置→图片生成→情感语音合成→口型同步→下载验证全流程,超时600秒轮询机制
3. **营销策略自动注入**:调用营销文案接口,从脚本+商品信息提炼卖点(selling_points)+选择情绪钩子(emotional_hook)+生成CTA话术,注入脚本关键帧(开头钩子/中段卖点/结尾CTA)
4. **三层TTS降级链**:Layer1高质量TTS引擎(免费,85%场景)→Layer2备用TTS(本地,10%)→Layer3静默+字幕(5%),保证配音可用性
5. **场景路由+配额管理**:scene参数场景路由模式(scene_1~scene_7),7场景+5卡片+降级链+成本预估+配额管理,渲染前检查日/月配额
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`结果验证与输出`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`结果验证与输出`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

## 适用场景

| 场景 | 输入 | 输出 | 是否适用 |
|:-----|:-----|:-----|:---------|
| 热点短视频生成 | topic主题+duration时长+platform平台 | 带配音字幕的短视频文件 | 适用 |
| 口型同步数字人视频 | agent_id人设+text文本+resolution分辨率 | 数字人口型同步视频 | 适用 |
| 连续剧角色一致性视频 | agent_id+series_id+脚本 | 角色一致性75-90%的视频 | 适用 |
| 多平台内容分发 | 已生成视频+多平台列表 | 多平台适配视频+发布结果 | 适用 |
| 营销带货视频制作 | 商品信息+脚本+CTA需求 | 含卖点钩子CTA的营销视频 | 适用 |
| 专业影视级长片制作 | 90分钟以上院线级需求 | 不适用(单次时长上限300秒) | 不适用 |
| 实时直播推流 | RTMP推流地址+实时画面 | 不适用(本Skill为离线生成) | 不适用 |
| 纯音频播客制作 | 音频-only输出需求 | 不适用(本Skill主输出视频) | 不适用 |

## 使用流程

### Step 1: 接收视频生成请求
- 解析输入参数:action(generate/lip_sync_video)、topic、duration(15-300秒)、platform、agent_id、scene
- 参数校验:topic非空、duration在15-300范围、platform在支持列表内
- 校验失败处理:返回VG-ERR-01,提示正确参数格式

### Step 2: 内容准备(仅generate流程)
- 如未指定topic→调用趋势发现接口获取TOP3热点,失败→使用默认话题"日常生活"
- 生成视频脚本→调用内容模板接口,失败→VG-ERR-02使用默认脚本模板

### Step 3: 营销策略注入(仅generate流程)
- 调用营销文案接口,输入脚本内容+商品信息
- 提炼卖点(selling_points)+选择情绪钩子(emotional_hook)+生成CTA话术
- 注入脚本关键帧(开头钩子/中段卖点/结尾CTA)
- 失败→跳过营销注入,使用原始脚本

### Step 4: 钩子结尾图检查
- 调用配置接口获取钩子结尾卡配置
- status=unset→提示用户设置 / status=configured→修改分镜最后帧 / status=dismissed→跳过
- 配置接口不可用→跳过,不阻塞主流程

### Step 5: 生成配音
- 调用TTS引擎(从配置获取voice_config)
- 三层降级:Layer1高质量TTS→Layer2备用TTS→Layer3静默+字幕
- 失败→VG-ERR-03重试3次降级默认音色

### Step 6: 视频生成(智能路由)
- 按智能路由决策树选择引擎
- 调用视频生成接口
- 失败→VG-ERR-04重试3次(间隔2分钟)

### Step 7: 字幕烧录与结尾帧注入
- 生成字幕→ffmpeg烧录SRT,失败→VG-ERR-05跳过字幕返回无字幕视频
- 钩子结尾帧注入→image_source="custom"时ffmpeg拼接结尾帧(3秒),失败→跳过不阻塞

### Step 8: 质量检查与交付
- 视频时长≈配音时长(误差<2秒),失败→重新生成
- 保存到输出目录+记录日志,失败→VG-ERR-06
- (可选)调用发布接口发布

## 智能路由决策树

```
视频生成请求到达
│
├─ Step1: 硬约束过滤 → API Key可用性检查 → available_engines
├─ Step2: 一致性需求判断 → agent_id出镜=HIGH / series_id=MEDIUM / 独立=NONE
├─ Step3: 内容类型判断
│   ├─ 数字人出镜 → VG-07口型同步(主引擎→降级引擎)
│   ├─ 角色一致性HIGH → 角色一致性引擎(75-90%) → 降级I2V引擎(70-85%)
│   ├─ AI原创画面 → 画质引擎(1.2元/5秒) → 降级通用引擎
│   ├─ AI风格化 → 风格化引擎 → 降级通用引擎
│   ├─ 真实素材 → 通用引擎(免费) → 降级风格化引擎
│   └─ 不确定 → 默认通用引擎(免费+字幕)
├─ Step4: 成本预算过滤 → free=仅免费引擎 / low=+角色一致性 / unlimited=全部
└─ Step5: 风格偏好注入 → 读取风格配置 → prompt_prefix+video_style+品牌叠加注入
```

| 场景 | 首选引擎 | 理由 | 降级路径 |
|:-----|:---------|:-----|:---------|
| 连续剧(角色一致性) | 角色一致性引擎 | 75-90%一致性 | I2V引擎→通用引擎 |
| AI原创画面 | 画质引擎 | 画质最好 | 通用引擎→免费引擎 |
| AI风格化 | 风格化引擎 | 模板+一键合成 | 免费引擎 |
| 真实素材 | 通用引擎 | 免费+字幕 | 风格化引擎 |
| 不确定/默认 | 通用引擎 | 免费+降级风险最低 | 无 |
| 预算受限 | 免费引擎 | 均免费 | 无 |
| 数字人出镜 | 口型同步引擎 | 口型同步 | 本地GPU降级 |

## 输入格式

### 生成短视频

```json
{"action": "generate", "agent_id": "agent_001", "topic": "春季穿搭", "duration": 60, "platform": "douyin", "with_subtitle": true}
```

### 生成短视频(场景路由模式)

```json
{"action": "generate", "topic": "春季穿搭", "duration": 60, "platform": "douyin", "scene": "scene_1", "with_subtitle": true}
```

> `scene` 参数: 场景ID(scene_1~scene_7),存在时走场景路由+渲染引擎; 不存在时走legacy路径(直接调通用引擎,向后兼容)。
> `duration` 参数: 视频时长(秒),15-300,默认60。
> 配额管理: scene路径会在渲染前检查日/月配额,渲染成功后记录用量。配额用尽返回 VG-ERR-QUOTA。

### 口型同步视频

```json
{"action": "lip_sync_video", "agent_id": "mengyao", "text": "嗨,今天想我了没?", "resolution": "480P", "scene": "咖啡厅"}
```

## 输出格式

```json
{"success": true, "data": {"video_url": "...", "duration": 58, "with_subtitle": true}, "error": null, "code": "VG-SUCCESS-01"}
```

### 输出格式(场景路由模式)

```json
{"success": true, "data": {"video_url": "...", "duration": 58, "with_subtitle": true, "route_metadata": {"scene": "scene_1", "engine_used": "universal_engine", "fallback_applied": false, "fallback_chain_used": [], "cost_estimate": 0}}, "error": null, "code": "VG-SUCCESS-01"}
```

## 异常处理


| 异常场景 | 原因 | 处理方式 | 错误码 |
|:---------|:-----|:---------|:-------|
| 参数无效 | topic空/duration超范围 | 返回错误,提示正确参数 | VG-ERR-01 |
| 脚本生成失败 | 内容模板接口失败 | 降级使用默认脚本模板 | VG-ERR-02 |
| TTS配音失败 | TTS引擎返回错误 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令3次→降级默认音色→备用TTS→静默+字幕 | VG-ERR-03 |
| 视频生成失败 | 视频接口返回失败 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令3次(间隔2分钟)→3次失败告警 | VG-ERR-04 |
| 字幕烧录失败 | ffmpeg未安装或执行失败 | 跳过字幕,返回无字幕视频 | VG-ERR-05 |
| 记录失败 | 日志写入失败 | 记录日志稍后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令,3次失败告警 | VG-ERR-06 |
| 素材缺失 | 源视频不存在 | 跳过缺失素材,提示补充 | VG-ERR-07 |
| 人设未找到 | agent_id无档案 | 返回错误,提示先初始化人设 | VG-ERR-08 |
| 口型同步失败 | 口型同步接口失败 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令2次→告警→检查API额度 | VG-ERR-09 |
| 视频下载失败 | 口型同步视频下载失败 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令3次 | VG-ERR-10 |
| 引擎权限不足 | 权限校验失败 | 降级到允许的最高级引擎,记录告警 | VG-ERR-11 |
| 风格配置缺失 | 风格配置未找到 | 使用默认风格(default),不阻塞主流程 | VG-ERR-12 |
| 视频配额已用尽 | 日/月配额达到上限 | 返回配额状态数据,提示升级或等待配额重置 | VG-ERR-QUOTA |
| 场景路由失败 | scene_id无效 | 返回错误,提示检查scene_id | VG-ERR-ROUTE |
| 视频渲染失败 | 所有引擎(含降级链)均失败 | 返回错误,记录降级链日志,提示执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令或更换场景 | VG-ERR-RENDER |

## TTS降级策略

```
Layer1: 高质量TTS引擎(免费,85%场景) → Layer2: 备用TTS(本地,免费,10%) → Layer3: 静默+字幕(5%)
```

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:-------|:-----|:---------|:---------|:-------------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 | DeepSeek/通义千问/文心一言/Kimi等国内模型 |
| TTS引擎 | API | 必需 | 高质量TTS/备用TTS/Edge-TTS三层降级 | CosyVoice2/鱼声Fish-Speech/Edge-TTS(免费) |
| 视频生成API | API | 必需 | 按智能路由决策树选择引擎 | 可灵AI/即梦AI/腾讯智影等国内视频生成 |
| ffmpeg | 工具 | 可选 | 字幕烧录(ffmpeg未安装时跳过字幕) | 系统包管理器安装,无海外依赖 |

### API Key 配置与安全要求
- **LLM_API_KEY**: 必需(通常由Agent内置) - 脚本生成/营销策略注入
- **TTS_API_KEY**: 可选 - TTS引擎(Edge-TTS免费可用)
- **VIDEO_API_KEY**: 可选 - 视频生成引擎
- 配置方式: 在Agent的环境变量中设置
- **零暴露原则**: API Key必须通过环境变量注入(如`$env:VIDEO_API_KEY`),严禁硬编码在SKILL.md或脚本源码中;所有示例代码中Key位置使用环境变量占位符;禁止在日志、错误信息、输出JSON中打印Key明文

### 使用流程
TTS降级链最终方案为静默+字幕。通用视频引擎免费。ffmpeg用于字幕烧录,未安装时返回无字幕视频。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 热点短视频生成

**输入**:
```json
{"action": "generate", "agent_id": "agent_001", "topic": "春季穿搭", "duration": 60, "platform": "douyin", "with_subtitle": true}
```

**执行流程**: 接收请求→验证参数→生成脚本→营销策略注入(卖点+钩子+CTA)→TTS配音→视频生成(智能路由选画质引擎)→字幕烧录→质量检查→保存交付

**输出**:
```json
{
  "success": true,
  "data": {
    "video_url": "output/videos/20260701_spring_outfit.mp4",
    "duration": 58,
    "with_subtitle": true,
    "engine_used": "quality_engine",
    "voice_used": "default_voice"
  },
  "error": null,
  "code": "VG-SUCCESS-01"
}
```

### 示例2: 口型同步视频(VG-07)

**输入**:
```json
{"action": "lip_sync_video", "agent_id": "mengyao", "text": "嗨,今天想我了没?", "resolution": "480P", "scene": "咖啡厅"}
```

**执行流程**: 接收请求→验证agent_id→获取人设外观→生成人设图片→生成情感语音→提交口型同步→轮询等待(每30秒,超时600秒)→下载验证

**输出**:
```json
{
  "success": true,
  "data": {
    "video_url": "output/videos/20260701_mengyao_lipsync.mp4",
    "duration": 5.2,
    "engine_used": "lip_sync_engine",
    "agent_id": "mengyao"
  },
  "error": null,
  "code": "VG-SUCCESS-01"
}
```

### 示例3: 引擎权限不足降级(VG-ERR-11)

**输入**: 基础套餐用户请求高级引擎
```json
{"action": "generate", "topic": "产品介绍", "duration": 30, "platform": "xhs"}
```

**输出**: 降级到免费引擎
```json
{
  "success": true,
  "data": {
    "video_url": "output/videos/20260701_product.mp4",
    "duration": 30,
    "engine_used": "universal_engine",
    "downgraded_from": "quality_engine",
    "downgrade_reason": "PERMISSION_DENIED"
  },
  "error": null,
  "code": "VG-SUCCESS-01"
}
```

### 示例4: 场景路由模式

**输入**: 选择"真实素材视频"场景(scene_1)
```json
{"action": "generate", "topic": "产品介绍", "duration": 30, "platform": "douyin", "scene": "scene_1"}
```

**输出**: 走场景路由+配额管理
```json
{
  "success": true,
  "data": {
    "video_url": "output/videos/20260707_product.mp4",
    "duration": 30,
    "with_subtitle": true,
    "route_metadata": {
      "scene": "scene_1",
      "engine_used": "universal_engine",
      "fallback_applied": false,
      "fallback_chain_used": [],
      "cost_estimate": 0
    }
  },
  "error": null,
  "code": "VG-SUCCESS-01"
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 抖音热点短视频生成(60秒,含配音字幕)

**输入**:
```json
{
  "action": "generate",
  "topic": "春季穿搭3个显瘦技巧",
  "duration": 60,
  "platform": "douyin",
  "with_subtitle": true
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "video_url": "https://cdn.videostudio.com/output/spring_outfit_001.mp4",
    "duration": 58,
    "with_subtitle": true,
    "route_metadata": {
      "scene": null,
      "engine_used": "universal_engine",
      "fallback_applied": false,
      "fallback_chain_used": [],
      "cost_estimate": 0
    }
  },
  "error": null,
  "code": "VG-SUCCESS-01"
}
```

**效果验证**: ✓视频时长58秒(误差<2秒) ✓通用引擎免费路由 ✓字幕烧录成功 ✓TTS配音正常 ✓输出格式合规

### 案例2: 口型同步数字人视频(480P)

**输入**:
```json
{
  "action": "lip_sync_video",
  "agent_id": "mengyao",
  "text": "嗨,今天想我了没?春季新款到店啦,快来看看吧!",
  "resolution": "480P",
  "scene": "咖啡厅"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "video_url": "https://cdn.videostudio.com/output/lip_sync_mengyao_001.mp4",
    "duration": 12,
    "with_subtitle": false,
    "route_metadata": {
      "scene": "咖啡厅",
      "engine_used": "lip_sync_engine",
      "fallback_applied": false,
      "fallback_chain_used": [],
      "cost_estimate": 0.5
    }
  },
  "error": null,
  "code": "VG-SUCCESS-01"
}
```

**效果验证**: ✓口型同步引擎正确路由 ✓agent_id人设加载成功 ✓情感语音合成完成 ✓480P分辨率输出 ✓输出格式合规

### 案例3: 场景路由模式生成(scene_1,含配额管理)

**输入**:
```json
{
  "action": "generate",
  "topic": "AI工具推荐:3款效率神器",
  "duration": 30,
  "platform": "xiaohongshu",
  "scene": "scene_1",
  "with_subtitle": true
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "video_url": "https://cdn.videostudio.com/output/ai_tools_scene1_001.mp4",
    "duration": 30,
    "with_subtitle": true,
    "route_metadata": {
      "scene": "scene_1",
      "engine_used": "universal_engine",
      "fallback_applied": false,
      "fallback_chain_used": [],
      "cost_estimate": 0
    }
  },
  "error": null,
  "code": "VG-SUCCESS-01"
}
```

**效果验证**: ✓场景路由scene_1正确匹配 ✓配额检查通过(日/月配额充足) ✓30秒短视频生成 ✓小红书平台适配 ✓route_metadata完整返回

### 案例4: TTS降级场景(高质量TTS不可用,降级到备用TTS)

**输入**:
```json
{
  "action": "generate",
  "topic": "职场新人避坑指南",
  "duration": 45,
  "platform": "douyin",
  "with_subtitle": true
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "video_url": "https://cdn.videostudio.com/output/workplace_tips_001.mp4",
    "duration": 44,
    "with_subtitle": true,
    "route_metadata": {
      "scene": null,
      "engine_used": "universal_engine",
      "fallback_applied": true,
      "fallback_chain_used": ["tts_layer1_failed", "tts_layer2_backup"],
      "cost_estimate": 0
    }
  },
  "error": "高质量TTS引擎不可用,已降级到备用TTS引擎",
  "code": "VG-ERR-03"
}
```

**效果验证**: ✓TTS三层降级链正确触发(Layer1→Layer2) ✓降级原因在error字段标注 ✓视频时长44秒(误差<2秒) ✓字幕烧录成功 ✓服务可用性保证(降级而非失败)

### 案例5: 营销策略注入(带货视频,含卖点钩子CTA)

**输入**:
```json
{
  "action": "generate",
  "topic": "新品保湿面霜评测",
  "duration": 60,
  "platform": "douyin",
  "with_subtitle": true,
  "product_info": {
    "name": "水润保湿面霜",
    "price": "99元",
    "selling_points": ["24小时长效保湿", "敏感肌可用", "烟酰胺提亮"]
  }
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "video_url": "https://cdn.videostudio.com/output/moisturizer_review_001.mp4",
    "duration": 60,
    "with_subtitle": true,
    "route_metadata": {
      "scene": null,
      "engine_used": "universal_engine",
      "fallback_applied": false,
      "fallback_chain_used": [],
      "cost_estimate": 0
    },
    "marketing_injected": {
      "emotional_hook": "换季皮肤干到起皮?这瓶面霜救了我的脸",
      "selling_points": ["24小时长效保湿", "敏感肌可用", "烟酰胺提亮"],
      "cta": "点击下方链接,限时99元带走,前100名额外送小样!"
    }
  },
  "error": null,
  "code": "VG-SUCCESS-01"
}
```

**效果验证**: ✓营销策略注入成功(卖点+钩子+CTA) ✓情绪钩子自动生成 ✓CTA话术含价格+限时+赠品 ✓视频时长60秒(精确匹配) ✓输出格式合规

## 常见问题

### Q1: 智能路由决策树如何选择视频引擎?
A: 决策树按5步执行:1)硬约束过滤(API Key可用性);2)一致性需求判断(agent_id出镜=HIGH/series_id=MEDIUM/独立=NONE);3)内容类型判断(数字人→口型同步/角色一致性HIGH→一致性引擎/AI原创→画质引擎等);4)成本预算过滤(free/low/unlimited);5)风格偏好注入。最终选择满足所有约束的最优引擎,不可用时走降级链。

### Q2: TTS配音失败时视频还能生成吗?
A: 可以。TTS采用三层降级链:Layer1高质量TTS引擎(免费,85%场景)→Layer2备用TTS(本地,10%)→Layer3静默+字幕(5%)。即使所有TTS引擎都不可用,也会生成静默视频+烧录字幕,保证视频交付不中断。

### Q3: 口型同步视频对agent_id有什么要求?
A: agent_id必须在人设配置中存在(VG-ERR-08),需提前初始化人设(含外观描述/参考图片)。口型同步流程会:1)获取人设外观;2)生成/获取人设图片(检查缓存);3)生成情感语音;4)提交口型同步引擎;5)轮询等待(每30秒,超时600秒)。超时或失败返回VG-ERR-09。

### Q4: scene参数和legacy路径有什么区别?
A: scene参数(scene_1~scene_7)走场景路由模式,支持7场景+5卡片+降级链+成本预估+配额管理,返回route_metadata元数据。不传scene走legacy路径,直接调通用引擎,向后兼容。建议新接入使用scene路由模式以获得更精细的引擎选择和配额控制。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

1. **单次视频时长上限300秒**:duration参数范围为15-300秒,不支持90分钟以上院线级长片制作,长视频需分段生成后合并
2. **口型同步依赖agent_id人设**:VG-07口型同步必须提供有效agent_id,无人设配置无法生成数字人视频(VG-ERR-08)
3. **角色一致性上限90%**:角色一致性引擎最高75-90%一致性,无法达到100%跨镜头完全一致,降级到I2V引擎降至70-85%
4. **ffmpeg未安装无法烧录字幕**:字幕烧录依赖ffmpeg,未安装时返回无字幕视频(VG-ERR-05),需用户自行安装ffmpeg
5. **配额用尽无法生成**:scene路由模式下日/月配额用尽返回VG-ERR-QUOTA,需等待配额重置或升级套餐

## 变更历史

| 版本 | 日期 | 变更说明 |
|:-----|:-----|:---------|
| v1.0.0 | 2026-07-17 | 初版创建,智能路由决策树+口型同步+营销注入+三层TTS降级+场景路由配额管理 |

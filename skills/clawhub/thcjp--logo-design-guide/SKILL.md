---
name: logo-design-guide
slug: logo-design-guide
displayName: "Logo Design Guide"
version: "0.2.0"
summary: "logo设计原则与AI图像生成实用指南,产出专业logo"
description: "logo设计原则与AI图像生成实用指南,帮助用户产出专业logo。覆盖字标、字母标、图形、抽象、吉祥物、组合型等logo类型,讲解提示词结构、色彩心理学、尺寸适配规范、文件格式交付全流程,并提供通义万相、文心一格等国内AI平台适配方案与错误码体系。当用户请求设计logo、品牌标志、AI生成图标、企业徽标时触发本技能。"
license: "MIT"
tools:
  - Read
  - Write
  - Edit
  - Bash
---

# Logo Design Guide

借助AI图像生成工具设计专业logo的实用指南,覆盖类型选择、提示词、配色、尺寸、交付与国内平台适配。

## 触发条件

当用户表达以下意图时触发本技能:

- "设计一个logo" / "帮我设计logo" / "做个logo"
- "品牌标志" / "企业徽标" / "品牌图标"
- "AI生成图标" / "AI画logo" / "AI设计标志"
- "logo设计原则" / "logo配色" / "logo尺寸规范"
- 包含"logo""标志""徽标""图标设计"等关键词的设计请求

触发后,Agent应先确认logo用途、品牌调性与目标尺寸,再进入提示词生成环节。

## 快速开始

以下为通用AI图像生成工具调用示意,实际命令请替换为所选平台的CLI或SDK:

```bash
# 通用调用格式(以通义万相为例)
ai-image generate --model wanx-v1 \
  --prompt "flat vector logo of a mountain peak with a sunrise, minimal geometric style, single color, clean lines, white background" \
  --width 1024 --height 1024
```

以通义万相(Wanx)为例的真实HTTP调用:

```bash
# 需先配置环境变量 DASHSCOPE_API_KEY
curl -X POST 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "wanx-v1",
    "input": {
      "prompt": "flat vector logo of a mountain peak with a sunrise, minimal geometric style, single color, white background"
    },
    "parameters": {"size": "1024*1024", "n": 1}
  }'
```

> 安装说明:各AI图像生成平台的CLI仅识别本机操作系统与架构,下载对应二进制并校验哈希,无需管理员权限或后台进程。

## AI平台适配

| 平台 | 模型示例 | 调用方式 | 适用场景 |
| --- | --- | --- | --- |
| 通义万相(阿里) | wanx-v1 / wanx2.1 | DashScope API / SDK | 国内首选,中文提示词友好 |
| 文心一格(百度) | ernie-vilg | Qianfan API | 中文品牌命名场景 |
| 豆包(字节) | seedream-4-5 | 火山引擎API | 高清写实与插画风格 |
| 通用Flux | flux-dev-lora | 各推理平台CLI | 矢量扁平风格表现佳 |
| 其他 | grok-imagine-image-pro | 对应平台CLI | 抽象线条风格 |

> 海外平台访问不稳定时,优先选用通义万相或文心一格等国内服务,降低网络与合规风险。

## Logo类型

| 类型 | 说明 | 适用场景 | 示例 |
| --- | --- | --- | --- |
| **字标(Wordmark)** | 公司名称作为logo | 品牌名简短(<10字符)且强 | Google, Coca-Cola |
| **字母标(Lettermark)** | 仅首字母缩写 | 公司名长、偏正式 | IBM, HBO, CNN |
| **图形标(Pictorial)** | 可识别的图标/符号 | 通用品牌,脱离文字仍可辨识 | Apple, Twitter bird |
| **抽象标(Abstract)** | 几何/非具象图形 | 科技公司、概念品牌 | Nike swoosh, Pepsi |
| **吉祥物(Mascot)** | 角色插画 | 亲切品牌、餐饮/体育 | KFC Colonel, Pringles |
| **组合标(Combination)** | 图标+字标 | 新品牌需同时建立识别与名称 | Burger King, Adidas |

## AI文字渲染限制(关键)

**AI图像生成工具无法可靠渲染文字。** 生成的字母会扭曲、错拼或乱码。

应对策略:

1. 仅用AI生成**图标/符号部分**
2. 文字/字标在设计工具(Figma、Canva、Illustrator)中手动添加
3. 或采用组合方式:AI图标 + 手动排版字体

## Logo提示词

### 有效关键词

```text
flat vector logo, simple minimal icon, single color silhouette,
geometric logo mark, clean lines, negative space design,
line art logo, flat design icon, minimalist symbol
```

### 失败关键词

```text
photorealistic logo (矛盾——logo不是照片)
3D rendered logo (过于复杂,缩小后失真)
gradient logo (结果不稳定,难以复现)
logo with text "Company Name" (文字渲染失败)
```

### 提示词结构

```text
flat vector logo of [主体], [风格], [颜色约束], [背景], [附加细节]
```

### 示例

```bash
# 抽象字母S标
ai-image generate --model wanx-v1 --prompt 'flat vector abstract logo, interlocking hexagonal shapes forming a letter S, minimal geometric style, single navy blue color, white background, clean sharp edges'

# 几何狐狸头
ai-image generate --model flux-dev-lora --prompt 'flat vector logo of a fox head in profile, geometric faceted style, orange and white, minimal clean lines, white background, negative space design'

# 吉祥物猫头鹰
ai-image generate --model seedream-4-5 --prompt 'friendly cartoon owl mascot logo, simple flat illustration, wearing graduation cap, purple and gold colors, white background, clean vector style'

# 抽象大脑节点
ai-image generate --model grok-imagine-image-pro --prompt 'minimal abstract logo mark, interconnected nodes forming a brain shape, line art style, single teal color, white background, tech startup aesthetic'
```

## 尺寸适配规则

logo必须在所有尺寸下都可用:

| 场景 | 尺寸 | 必须满足 |
| --- | --- | --- |
| 网站favicon | 16x16 px | 轮廓可辨识 |
| App图标 | 1024x1024 px | 细节完整 |
| 社交头像 | 400x400 px | 一眼清晰 |
| 名片 | 约1英寸 | 印刷清晰复现 |
| 户外广告牌 | 10英尺+ | 无锯齿,足够简洁 |

### 尺寸自检清单

- 缩到16px favicon仍可辨识(眯眼测试)
- 单色可用(黑底白字、白底黑字)
- 反色可用
- 无缩小后消失的细小细节
- 无缩细后断掉的细线
- 去掉颜色后轮廓仍清晰

## 配色指南

- 主logo**最多2-3种颜色**
- 必须支持**单色**呈现(黑、白或品牌主色)
- 参考**色彩心理学**:
  - 蓝:信任、专业(金融、科技、医疗)
  - 红:活力、紧迫(餐饮、娱乐、零售)
  - 绿:成长、自然(健康、可持续、金融)
  - 橙:亲和、创意(初创、年轻品牌)
  - 紫:奢华、智慧(美妆、教育)
  - 黑:高端、优雅(时尚、奢侈、科技)
- 在浅色与深色背景下均需测试

## 迭代工作流

```bash
# 批量生成候选(5张)
for i in 1 2 3 4 5; do
  ai-image generate --model flux-dev-lora \
    --prompt 'flat vector logo of a lighthouse, minimal geometric, single color, white background' \
    --no-wait
done

# 选定方向后细化
ai-image generate --model flux-dev-lora --prompt 'flat vector logo of a geometric lighthouse with light beam rays, minimal line art, navy blue, white background, negative space design'

# 高清放大(2K)
ai-image generate --model seedream-4-5 --prompt 'flat vector logo of a geometric lighthouse with radiating light beams, minimal clean design, navy blue single color, pure white background' --size 2K

# 超分辨率放大
ai-image upscale --input best-logo.png --scale 4
```

## 常见错误

| 错误 | 问题 | 修复 |
| --- | --- | --- |
| 细节过多 | 小尺寸丢失清晰度 | 简化为核心形状 |
| 依赖颜色 | 黑白场景失效 | 先用黑色设计 |
| AI生成含文字 | 字母乱码/错拼 | 仅生成图标,文字手动添加 |
| 滥用特效(发光/阴影) | 易过时、难复现 | 采用扁平、长青设计 |
| 颜色过多 | 难复现、印刷成本高 | 最多2-3种颜色 |
| 无目的的不对称 | 显得未完成 | 有意不对称或保持平衡 |

## 文件格式交付

| 格式 | 用途 |
| --- | --- |
| SVG | 矢量缩放、网页、编辑 |
| PNG(透明) | 数字应用、演示 |
| PNG(白底) | 文档、邮件签名 |
| ICO / Favicon | 网站favicon(16、32、48px) |
| 高清PNG(4096px+) | 印刷、广告牌 |

说明:AI生成的是位图(PNG)。若需真正的矢量SVG,应将AI输出作为参考在矢量工具中描摹,或使用AI转SVG工具。

## 错误处理

本技能采用结构化错误码体系,覆盖AI生成、网络、权限等场景:

| 错误码 | 场景 | 原因 | 处理方式 |
| --- | --- | --- | --- |
| ERR-001 | AI图像生成失败 | 模型服务不可用或配额耗尽 | 切换备用模型(通义万相↔文心一格),确认账户配额后重试 |
| ERR-002 | 网络请求超时 | 连接不稳定或服务端响应慢 | 检查网络,增加超时阈值至60s,优先使用国内平台 |
| ERR-003 | 提示词被安全策略拦截 | 内容触发平台审核 | 移除敏感词,改用中性描述,重写提示词 |
| ERR-004 | API密钥或权限校验失败 | Key失效、过期或权限不足 | 重新生成密钥,确认调用权限与计费开通状态 |
| ERR-005 | 输出尺寸/比例不符 | 模型不支持该分辨率 | 改用支持的尺寸(如1024x1024),再用裁剪/缩放调整 |
| ERR-006 | 生成结果文字乱码 | AI文字渲染固有限制 | 仅生成图标,文字在设计工具中手动添加 |

错误处理原则:遇到ERR-001至ERR-003优先重试(最多3次)并切换平台;ERR-004需人工介入更新凭证;ERR-005与ERR-006属业务约束,调整参数或流程即可解决。

## 常见问题

### Q1: AI生成的logo里文字总是乱码怎么办?
A: 这是AI图像生成工具的固有限制(见错误码ERR-006)。建议仅用AI生成图标/符号部分,品牌名称、标语等文字在Figma、Illustrator等设计工具中手动排版,既保证拼写正确,也便于后期统一字体。

### Q2: logo应该用几种颜色?
A: 主logo建议最多2-3种颜色,并必须支持单色(纯黑或纯白)呈现,以适配传真、印章、单色印刷等场景。设计时先用黑色定稿,再上色,可有效避免过度依赖颜色。

### Q3: logo最小可以缩到多大还保持清晰?
A: 需通过16px favicon的"眯眼测试":在16x16像素下轮廓仍可辨识。若失效,应简化为更纯粹的剪影,去除细线与碎细节。详见"尺寸适配规则"章节。

### Q4: 生成logo时提示词怎么写效果更佳?
A: 采用"flat vector logo of [主体], [风格], [颜色约束], [背景], [附加细节]"结构,多用 flat vector、minimal、single color、clean lines、negative space 等关键词;避免 photorealistic、3D、gradient、含具体文字等会劣化结果的词。

### Q5: 如何把AI生成的PNG转成矢量SVG?
A: AI输出本质是位图。可将其作为参考底图,在Illustrator、Inkscape中用钢笔工具描摹重绘为SVG,或使用矢量描摹(Image Trace)功能;也可借助AI转SVG工具,但需人工校验节点与曲线。

### Q6: 国内用户用哪个AI平台生成logo比较好?
A: 推荐通义万相(wanx-v1)作为首选,中文提示词理解好、访问稳定;文心一格适合含中文品牌命名场景;若需扁平矢量风格且可访问海外服务,Flux系列表现较佳。详见"AI平台适配"章节。

## 能力边界

本技能明确以下边界,超出范围需人工或专业工具介入:

- **文字渲染**:AI无法可靠生成正确文字,品牌名/标语必须人工添加
- **矢量输出**:AI生成位图(PNG),非真正矢量SVG,需手动描摹
- **色彩精确**:无法保证Pantone专色精确匹配,印刷级色彩需人工校准
- **复杂效果**:渐变、光影、3D等效果难以稳定复现,不推荐用于logo
- **一致性保证**:多版本/多场景的视觉一致性需人工后期统一
- **商标合规**:商标查重、侵权检索必须由人工或专业商标服务完成,AI不承担法律判断
- **品牌策略**:logo背后的品牌定位、命名策略属战略决策,需人工主导

## Related Skills

与本技能相关的其他技能方向(在SkillHub平台检索对应名称):

- **brand-guidelines**: 品牌视觉规范制定,logo落地后的色彩/字体/间距体系
- **color-theory**: 色彩理论与配色方案生成,辅助logo配色决策
- **vector-illustration**: 矢量插画与图标绘制,AI位图转SVG的描摹技巧
- **icon-design**: 图标设计规范,App图标与UI图标的尺寸/栅格体系
- **figma-basics**: Figma操作基础,logo文字排版与多格式导出

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Trae Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| AI图像生成平台 | API | 必需 | 通义万相 / 文心一格 / Flux等,按需选用 |
| 设计工具 | 软件 | 可选 | Figma / Illustrator / Inkscape,用于文字排版与SVG描摹 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key
- 调用AI图像生成平台时,需自行配置对应平台的API Key(如通义万相的 DASHSCOPE_API_KEY)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- logo设计原则与AI图像生成全流程指导
- 覆盖字标、字母标、图形、抽象、吉祥物、组合型等logo类型
- 提示词结构、色彩心理学、尺寸适配、文件格式交付
- 通义万相、文心一格等国内AI平台适配方案
- 结构化错误码体系(ERR-001至ERR-006)与运行时异常预防
- AI文字渲染限制识别与应对策略

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| logo从零设计 | 品牌名+行业+调性 | 提示词+候选logo+交付格式建议 |
| 已有logo优化 | 现有logo+改进诉求 | 问题诊断+迭代提示词 |
| 多平台适配 | 单一logo源文件 | 各尺寸/格式输出方案 |

## 运行时异常预防

为提升稳定性,执行过程中应遵循以下预防措施:

- **平台降级**:主用平台失败时自动切换备用(通义万相↔文心一格↔Flux),避免单点依赖
- **重试控制**:网络与生成类错误(ERR-001至ERR-003)最多重试3次,每次间隔递增
- **输入校验**:提交前校验提示词长度(建议<500字符)、尺寸参数为模型支持值
- **凭证隔离**:API Key通过环境变量注入,不硬编码在提示词或脚本中
- **结果校验**:生成后检查图片是否为空、尺寸是否匹配、是否含明显乱码区域
- **资源回收**:批量生成任务及时清理临时文件,避免磁盘占满导致后续失败

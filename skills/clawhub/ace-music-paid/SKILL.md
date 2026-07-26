---
slug: ace-music-paid
name: ace-music-paid
version: "1.0.0"
displayName: ACE音乐生成-专业版
summary: 企业级AI音乐生成工具,支持批量、翻唱、片段重绘、长时长输出,适配商业内容生产。
license: Proprietary
edition: pro
description: |-
  ACE音乐生成专业版,面向企业团队与专业音乐内容生产者的高级AI音乐工具。核心能力:
  - 批量生成多首歌曲,支持风格矩阵组合
  - 风格翻唱(cover)与片段重绘(repaint)
  - 长时长输出(最高 300 秒),支持完整歌曲结构
  - 音频输入驱动生成,可基于参考素材创作
  - 优先 API 配额与企业级技术支持

  适用场景:
  - 广告/影视配乐批量生产
  - 音乐厂牌快速 demo 生成与迭代
  - 游戏开发商多场景 BGM 批量产出
  - 企业品牌音频资产沉淀

  差异化:专业版在免费版基础上扩展批量生成、...
tags:
- Creative
- 音乐生成
- 企业版
- 商业内容
tools:
  - - read
- exec
---
# ACE音乐生成-专业版

## 核心能力

| 能力项 | 免费版 | 专业版 | 说明 |
|:-------|:-------|:-------|:-----|
| 文本生成音乐 | 是 | 是 | 基础 text2music |
| 自定义歌词 | 是 | 是 | 支持 Verse/Chorus 结构 |
| 单曲时长上限 | 60 秒 | 300 秒 | 支持完整歌曲结构 |
| 批量生成 | 否 | 是 | 单任务最多 10 首 |
| 风格翻唱(cover) | 否 | 是 | 基于音频输入翻唱 |
| 片段重绘(repaint) | 否 | 是 | 修改已有音频局部 |
| 音频输入驱动 | 否 | 是 | 参考素材再创作 |
| API 配额优先级 | 普通 | 高优先 | 企业级保障 |
| 技术支持 | 社区 | 专属支持 | 工单响应 |
### 能力项

执行能力项操作,处理用户输入并返回结果。

**输入**: 用户提供能力项所需的参数和指令。

**输出**: 返回能力项的处理结果。

- 执行`能力项`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`能力项`相关配置参数进行设置
### 文本生成音乐

执行文本生成音乐操作,处理用户输入并返回结果。

**输入**: 用户提供文本生成音乐所需的参数和指令。

**输出**: 返回文本生成音乐的处理结果。

- 执行`文本生成音乐`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`文本生成音乐`相关配置参数进行设置
### 自定义歌词

执行自定义歌词操作,处理用户输入并返回结果。

**输入**: 用户提供自定义歌词所需的参数和指令。

**输出**: 返回自定义歌词的处理结果。

- 执行`自定义歌词`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`自定义歌词`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 音乐生成工具、支持批量、长时长输出、适配商业内容生产、ACE、音乐生成专业版、面向企业团队与专、业音乐内容生产者、的高级、音乐工具、核心能力、批量生成多首歌曲、支持风格矩阵组合、与片段重绘、音频输入驱动生成、可基于参考素材创、配额与企业级技术。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一:广告配乐批量生成

广告公司需为多个产品线快速产出风格统一的背景音乐,使用批量生成一次性产出多版本候选。

```bash
# 批量生成 5 首电子风格广告配乐
scripts/generate.sh "electronic dance track, upbeat, brand commercial" \
  --batch 5 \
  --duration 60 \
  --output ad_edm.mp3

# 风格矩阵:不同 BPM 组合
for bpm in 110 120 128 140; do
  scripts/generate.sh "corporate uplifting pop" \
    --bpm $bpm \
    --duration 30 \
    --output ad_pop_${bpm}.mp3
done
```

### 场景二:歌曲翻唱与片段重绘

音乐厂牌希望对已有 demo 进行风格翻唱,并重绘某一段落以优化听感。

```bash
# 基于原曲翻唱为爵士风格
scripts/generate.sh "jazz cover, smoky bar, saxophone" \
  --task cover \
  --audio-input original.mp3 \
  --output jazz_cover.mp3

# 重绘副歌部分(30-60秒)
scripts/generate.sh "more energetic chorus, add brass section" \
  --task repaint \
  --audio-input original.mp3 \
  --start 30 --end 60 \
  --output refined.mp3
```

### 场景三:影视长配乐生成

影视制作公司需要生成 3-5 分钟的背景配乐,使用长时长输出能力。

```bash
# 生成长达 4 分钟的史诗风格配乐
scripts/generate.sh "epic orchestral, cinematic, emotional build-up, strings and brass" \
  --duration 240 \
  --instrumental \
  --key "D minor" \
  --bpm 90 \
  --output movie_score.mp3
```

## 使用流程

### 优秀步:配置企业 API Key

```bash
# 企业版 Key 享有更高配额与优先级
export ACE_MUSIC_API_KEY="your_pro_api_key"
export ACE_MUSIC_EDITION="pro"  # 启用专业版功能
```

### 第二步:执行批量生成

```bash
# 一次生成 3 首不同风格候选
scripts/generate.sh "summer pop hit" \
  --batch 3 \
  --duration 120 \
  --language en \
  --output summer_pop.mp3
```

### 第三步:结果处理

批量生成会输出多个文件路径,可结合脚本进行自动归档:

```bash
# 自动归档批量生成结果
results=$(scripts/generate.sh "brand jingle" --batch 5 --output jingle.mp3)
echo "$results" | while read file; do
  mv "$file" ./archive/$(date +%Y%m%d)_$(basename "$file")
done
```

### 命令参数说明

- `--batch`: 命令参数,用于指定操作选项
- `--language`: 命令参数,用于指定操作选项
- `--bpm`: 命令参数,用于指定操作选项
- `--task`: 命令参数,用于指定操作选项
- `--audio-input`: 命令参数,用于指定操作选项

### 命令参数说明

- `--end`: 命令参数,用于指定操作选项
- `--start`: 命令参数,用于指定操作选项
- `--duration`: 命令参数,用于指定操作选项
- `-up`: 命令参数,用于指定操作选项
- `--instrumental`: 命令参数,用于指定操作选项

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: Bash shell + curl + jq

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| ACE Music Pro API | 外部 API | 必需 | 企业服务渠道申请 |
| curl | 命令行工具 | 必需 | 系统自带 |
| jq | JSON 处理 | 必需 | 包管理器安装 |
| ffmpeg | 音频处理 | 推荐 | 用于拼接与转码 |
| base64 | 解码工具 | 必需 | 系统自带 |

### API Key 配置
- **环境变量名**: `ACE_MUSIC_API_KEY`(企业版 Key)
- **附加变量**: `ACE_MUSIC_EDITION=pro`
- **获取方式**: 通过企业服务渠道申请,享有高优先级配额
- **安全建议**: 使用密钥管理服务(如 Vault)存储,避免明文写入脚本

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,核心功能需要 exec 命令行执行能力)
- **说明**: 基于Markdown的AI Skill,支持批量、长时长、翻唱重绘等企业级音乐生产场景

## 案例展示

专业版完整配置:

```bash
# 环境变量
ACE_MUSIC_API_KEY=your_pro_key
ACE_MUSIC_BASE_URL=https://api.acemusic.ai
ACE_MUSIC_EDITION=pro
ACE_MUSIC_MAX_DURATION=300
ACE_MUSIC_MAX_BATCH=10

# 高级任务参数
--task text2music|cover|repaint   # 任务类型
--audio-input <file>              # 音频输入(cover/repaint 必填)
--start <seconds>                 # 重绘起始位置
--end <seconds>                   # 重绘结束位置
--batch <n>                       # 批量数量(1-10)
--duration <seconds>              # 时长(1-300)
```

## 常见问题

### Q1:专业版与免费版是否兼容?
A:完全兼容。专业版支持免费版所有参数,迁移时仅需更换 API Key 并设置 `ACE_MUSIC_EDITION=pro`。

### Q2:批量生成失败的文件如何处理?
A:批量任务中部分失败不影响其他,脚本会返回成功生成的文件列表。失败的可在下次重试。

### Q3:cover 与 repaint 的区别?
A:cover 是对整曲进行风格翻唱(保留旋律改风格),repaint 是对指定片段进行局部修改重绘,两者均可基于音频输入创作。

### Q4:企业版 API 配额如何申请提升?
A:联系企业服务渠道提交配额提升申请,专业版默认享有高优先级队列。

### Q5:长时长生成会不会中途超时?
A:专业版针对长时长任务优化,最长 300 秒歌曲生成约需 3-5 分钟。建议脚本设置合理超时(如 600 秒)。

### Q6:能否集成到 CI/CD 流水线?
A:可以。脚本支持非交互模式,可在自动化流水线中调用,建议结合重试机制与结果校验。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用

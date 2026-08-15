---
slug: music-gen
name: music-gen
version: 1.0.1
displayName: 音乐生成工具专业版
summary: 企业级AI音乐生成系统,支持批量生成、版权管理、多平台调度与CI/CD集成,适合团队与商业项目。音乐生成工具专业版为企业与内容团队提供系统化的AI音乐生成解决方案。在免费版基础生成能力之上
summary_zh: 企业级AI音乐生成系统,支持批量生成、版权管理、多平台调度与CI/CD集成,适合团队与商业项目。音乐生成工具专业版为企业与内容团队提供系统化的AI音乐生成解决方案。在免费版基础生成能力之上
license: MIT
edition: pro
description: |- 功能涵盖:。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。提供结构化输出和错误处理机制。支持多场景应用和灵活配置。具备完整的输入输出规范。 功能涵盖: gen。
  音乐生成工具专业版为企业与内容团队提供系统化的AI音乐生成解决方案。在免费版基础生成能力之上,增加批量生成、版权资产管理、多平台智能调度、
  音乐质量审计与CI/CD集成能力。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。'
tags:
- 音乐生成
- 企业级
- 批量处理
- 版权管理
- CI/CD
- 自动化
- 音频
- 创意
- true
- platform
- output
tools:
- read
- exec
- write
homepage: ''
category: Creative
homepage: "https://skillhub.cn/skill/"
---

> **核心功能**: 本技能提供化流程等能力。

> **核心功能**: 本技能提供时使用、、工作流优化时使用等能力。

> **核心功能**: 本技能提供中文交互等能力。

# 音乐生成工具专业版
## 专业版增强能力
| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 音乐生成工具专业版企业级AI音乐生成 | 不支持 | 支持 |
| 音乐生成工具专业版支持批量生成 | 不支持 | 支持 |
| 音乐生成工具专业版版权管理 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
## 能力矩阵
### 批量音乐生成
```python
batch_config = {
    "project": "电商配乐批量生产",
    "tasks": [
        {
            "id": "bgm_001",
            "platform": "stable_audio",
            "prompt": "upbeat electronic, 128 BPM, instrumental, 2 minutes",
            "output": "./output/bgm_001.mp3",
            "license": "commercial"
        },
        {
            "id": "bgm_002",
            "platform": "mubert",
            "prompt": "lo-fi hip hop, relaxed, 80 BPM, 3 minutes",
/output/bgm_002.mp3",
            "license": "commercial"
        },
        {
            "id": "song_001",
            "platform": "suno",
            "prompt": "pop song with vocals, uplifting, 120 BPM",
            "lyrics": "lyrics/song_001.txt",
/output/song_001.mp3",
            "license": "commercial"
        }
    ],
    "parallel": 3,
    "auto_validate": True,
    "license_tracking": True
}
python3 batch_music_gen.py --config batch_config
```- 验证返回数据的完整性和格式正确性
### 多平台智能调度
```python
platform_scheduler = {
    "platforms": {
        "suno": {
            "strength": "vocal_songs",
            "rate_limit": "50/day",
            "cost": "medium",
            "quality": "high"
        },
        "udio": {
            "strength": "high_quality_vocals",
            "rate_limit": "100/month",
            "cost": "high",
            "quality": "excellent"
        },
        "stable_audio": {
            "strength": "instrumental",
            "rate_limit": "500/month",
            "cost": "low",
            "quality": "good"
        },
        "mubert": {
            "strength": "realtime_electronic",
            "rate_limit": "1000/month",
            "cost": "low",
            "quality": "good"
        }
    },
    "auto_select_rules": [
        {"condition": "need_vocals == true", "platform": "suno"},
        {"condition": "need_vocals == true and quality == 'best'", "platform": "udio"},
        {"condition": "need_instrumental == true", "platform": "stable_audio"},
        {"condition": "need_realtime == true", "platform": "mubert"}
    ],
    "load_balancing": "round_robin",
    "fallback": True
}
```
### 版权资产管理
```python
license_manager = {
    "assets": [
        {
            "id": "music_001",
            "title": "产品宣传背景音乐",
            "platform": "stable_audio",
            "license_type": "commercial",
            "license_id": "SA-2024-001",
            "purchase_date": "2024-01-15",
            "expiry": "2025-01-15",
            "usage_rights": ["online", "broadcast", "streaming"],
            "restrictions": ["no_resale"],
            "attribution_required": False
        },
        {
            "id": "song_001",
            "title": "品牌主题曲",
            "platform": "suno",
            "license_type": "commercial",
            "license_id": "SUNO-2024-001",
            "purchase_date": "2024-02-01",
            "expiry": "2025-02-01",
            "usage_rights": ["online", "streaming"],
            "restrictions": ["no_broadcast"],
            "attribution_required": True
        }
    ],
    "tracking": {
        "usage_log": True,
        "expiry_alerts": True,
        "compliance_check": True
    }
```
### 音乐质量审计
```python
quality_audit = {
    "checks": [
        {
            "name": "音质检查",
            "test": "audio_quality",
            "min_bitrate": "128kbps",
            "min_sample_rate": "44100Hz"
        },
        {
            "name": "时长验证",
            "test": "duration_check",
            "expected_range": [15, 300]  # 15-300秒
        },
        {
            "name": "响度规范",
            "test": "loudness_normalization",
            "target_loudness": -16,  # LUFS
            "tolerance": 2
        },
        {
            "name": "频谱分析",
            "test": "spectrum_analysis",
            "check_clipping": True,
            "check_noise": True
        },
        {
            "name": "风格匹配",
            "test": "style_matching",
            "compare_with_prompt": True
        }
    ],
    "auto_fix": {
        "loudness_normalize": True,
        "trim_silence": True,
        "remove_clipping": True
    },
    "report_format": "html"
}
```
### 音乐库管理
```python
music_library = {
    "categories": {
        "background": {
            "subcategories": ["vlog", "podcast", "presentation"],
            "count": 50
        },
        "brand": {
            "subcategories": ["theme", "jingle", "logo"],
            "count": 20
        },
        "content": {
            "subcategories": ["intro", "outro", "transition"],
            "count": 30
        },
        "emotional": {
            "subcategories": ["happy", "sad", "epic", "calm"],
            "count": 40
        }
    },
    "search": {
        "by_mood": True,
        "by_bpm": True,
        "by_genre": True,
        "by_duration": True,
        "by_license": True
    },
    "metadata": {
        "auto_tag": True,
        "auto_categorize": True,
        "fingerprint": True  # 音频指纹避免重复
    }
```
- 异常时参考错误处理章节进行恢复
- 关键参数: `多平台智能调度` 选项
## 新手引导
1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理
## 适用范围
### 场景一:MCN批量配乐生产
需求:MCN机构需要为多个账号批量生产背景音乐.
```bash
  --tasks music-tasks.json \
  --parallel 5 \
  --auto-select-platform \
  --license-tracking \
  --output ./music-library/ \
  --auto-categorize \
  --quality-check
python
tasks = [
    {"account": "科技账号", "need": "background", "mood": "upbeat", "duration": "2-3min"},
    {"account": "教育账号", "need": "background", "mood": "calm", "duration": "3-5min"},
    {"account": "生活账号", "need": "background", "mood": "happy", "duration": "2-3min"}
]
```
### 场景二:品牌音乐资产管理
需求:企业需要统一管理所有品牌音乐的版权与使用.
```bash
python3 init_music_library.py \
  --brand "EnterpriseBrand" \
  --output ./music-assets/ \
  --license-tracking \
  --auto-categorize
python3 import_assets.py \
  --input ./existing-music/ \
  --auto-tag \
  --fingerprint \
  --license-check
```
### 场景三:游戏配乐批量制作
需求:游戏公司需要为多个场景制作配乐.
```python
game_scenes = [
    {"scene": "主菜单", "mood": "epic", "duration": "3min", "loop": True},
    {"scene": "战斗", "mood": "intense", "duration": "2min", "loop": True},
    {"scene": "城镇", "mood": "peaceful", "duration": "4min", "loop": True},
    {"scene": "Boss战", "mood": "dramatic", "duration": "3min", "loop": True},
    {"scene": "结局", "mood": "emotional", "duration": "5min", "loop": False}
]
for scene in game_scenes:
    generate_music(
        platform=auto_select_platform(scene),
        prompt=build_prompt(scene),
        output=f"./game-music/{scene['scene']}.mp3",
        license="commercial",
        loop=scene["loop"]
    )
```
## 使用方法
### 步骤一:初始化音乐资产管理
```bash
  --brand "MyBrand" \
  --output ./music-library/ \
  --license-tracking
```
### 步骤二:配置批量生成
```bash
  --config music-tasks.yml \
  --parallel 5 \
  --auto-select-platform \
  --quality-check
```
### 步骤三:管理与审计
```bash
python3 generate_index.py \
  --input ./music-library/ \
  --output ./index.html
python3 license_audit.py \
  --library ./music-library/ \
  --report ./audit/
```
## 请求格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | 处理的内容输入 |
| mode | string | 否 | 处理模式, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |
## 输出说明
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
## 异常管理
| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 |
## 前置条件
### 运行环境
- **Agent平台**: 支持SKILL.md规范的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.10+
### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| AI音乐平台账户 | 服务 | 必需 | Suno/Udio/Stable Audio等 |
| 音频处理库 | 库 | 推荐 | pip install pydub |
| 音频分析库 | 库 | 推荐 | pip install librosa |
| 数据库 | 存储 | 推荐 | `SQLite`/`关系型数据库` |
### API Key 配置
- 本Skill基于指令驱动驱动,基础LLM由Agent平台提供
- 各AI音乐平台需分别配置API Key,支持环境变量管理
- 批量生成支持API Key池与负载均衡
- 企业版支持多账户管理与并发控制
### 可用性分类
- **分类**: MD+execute(纯Markdown指令+脚本执行能力)
- **说明**: 专业版基于Markdown指令驱动Agent执行批量音乐生成任务,通过Python脚本实现多平台调度、版权管理与CI/CD集成
- **PRO版增强**: 批量生成、多平台调度、版权管理、质量审计、音乐库管理、CI/CD集成、团队协作
## 案例展示
### 企业级音乐生成配置
```yaml
project:
  name: "企业音乐资产管理"
  version: "1.0.0"
generation:
  platforms:
    - name: "suno"
      api_key: "${SUNO_API_KEY}"
      rate_limit: "50/day"
    - name: "stable_audio"
      api_key: "${STABLE_AUDIO_API_KEY}"
      rate_limit: "500/month"
    - name: "mubert"
      api_key: "${MUBERT_API_KEY}"
      rate_limit: "1000/month"
  auto_select: true
  parallel: 5
  quality_check: true
license_management:
  track_usage: true
  expiry_alerts: true
  compliance_check: true
  auto_renew: false
library:
  categories:
    - background
    - brand
    - content
    - emotional
  search:
    by_mood: true
    by_bpm: true
    by_genre: true
  auto_tag: true
  fingerprint: true
audit:
  audio_quality: true
  loudness: -16
  spectrum_analysis: true
  style_matching: true
  report: "html"
```
### CI/CD集成
```yaml
name: Music Production
on:
  schedule:
    - cron: "0 9 * * 1"  # 每周一上午9点
  push:
    paths: ["music-tasks/**"]
jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - name: Batch Generate Music
        run: |
            --config music-tasks/config.yml \
            --parallel 5 \
            --auto-select-platform \
            --quality-check
      - name: License Audit
        run: |
            --library ./music-library/ \
            --report ./audit/
      - name: Upload Music
        uses: actions/upload-artifact@v3
        with:
          name: music-assets
          path: ./music-library/
```
## 热门问题
### Q1: 如何从免费版迁移至PRO版?
A: PRO版完全兼容免费版。现有的平台配置与提示词模板可直接使用。安装PRO版增强包即可启用批量生成、版权管理与质量审计.
### Q2: 批量生成时如何选择平台?
A: PRO版支持智能调度,根据音乐类型自动选择最优平台。人声歌曲优先Suno/Udio,器乐背景优先Stable Audio,实时电子优先Mubert。支持负载均衡与故障转移.
### Q3: 版权资产如何管理?
A: PRO版提供完整的版权管理系统,记录每首音乐的许可类型、购买日期、到期时间、使用权限与限制。支持定期合规审计与到期预警.
### Q4: 音乐库如何搜索?
A: 支持按情绪、BPM、风格、时长、许可类型等多维度搜索。自动打标签与分类,支持音频指纹避免重复.
### Q5: 支持哪些CI/CD平台?
A: 支持GitHub Actions、GitLab CI、Jenkins等主流平台。提供标准CLI接口与配置文件,易于集成到任意流水线.
## 问题排查手册
| 错误现象 | 可能原因 | 诊断步骤 | 解决方案 |
| --- | --- | --- | --- |
| 批量生成任务失败 | 网络连接问题或API服务不可用 | 检查网络连接状态，确认API服务是否正常运行 | 确保网络连接稳定，检查API服务状态，必要时重试任务 |
| 版权管理系统中音乐资产信息缺失 | 数据库连接问题或数据同步失败 | 检查数据库连接配置，确认数据同步脚本执行状态 | 修复数据库连接问题，确保数据同步脚本正确执行 |
| 音乐生成质量不符合预期 | 提示词设置不正确或平台参数调整不当 | 检查提示词格式和内容，确认平台参数设置 | 修正提示词，调整平台参数以符合需求 |
| 多平台调度失败 | 平台API Key配置错误或调度规则设置不当 | 检查API Key配置，确认调度规则设置 | 修正API Key配置，调整调度规则 |
| 音乐库搜索结果不准确 | 音频指纹生成错误或搜索算法问题 | 检查音频指纹生成脚本，确认搜索算法逻辑 | 修复音频指纹生成脚本，优化搜索算法 |
## 安全合规声明
| 风险类型 | 防范措施 |
|----------|---------|
| API密钥泄露 | 通过环境变量配置，禁止硬编码到代码或配置文件中 |
| 命令执行风险 | 仅执行白名单命令，避免拼接用户输入到命令行参数中 |
| 网络通信安全 | 使用HTTPS协议，验证SSL证书有效性 |
| 敏感数据暴露 | 输出结果中不包含密钥、令牌等敏感信息 |
使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。
## 功能总览
- **自动化执行**: 企业级AI音乐生成系统,支持批量生成、版权管理、多平台调度与CI/CD集成,适合团队与商业项目。音乐生成工具专业版为企业
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据
## 常见用户疑问
### Q1: 音乐生成工具专业版支持哪些输入格式？
A1: 企业级AI音乐生成系统,支持批量生成、版权管理、多平台调度与CI/CD集成,适合团队与商业项目。音乐生成工具专业版为企业与内容团队提供系统化的AI音乐生成解决方。支持文本指令和结构化参数输入，具体格式参考使用流程章节。
### Q2: 需要配置API Key吗？
A2: 是的，部分功能需要配置对应平台的API Key。请在依赖说明章节查看具体要求，并通过环境变量安全配置。
### Q3: 命令行执行失败怎么办？
A3: 检查命令参数是否正确，确认运行环境支持exec能力。如遇权限问题，请参照错误处理章节排查。
## 故障恢复
针对音乐生成工具专业版使用中可能遇到的常见问题,提供以下排查方案:
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
### 音乐生成工具专业版通用排查步骤
1. **检查输入参数**: 确认所有必填参数已提供且格式正确
2. **查看日志输出**: 定位具体错误行和异常类型
3. **验证环境配置**: 确认依赖库版本和运行环境满足要求
4. **逐步调试**: 缩小问题范围,隔离故障模块
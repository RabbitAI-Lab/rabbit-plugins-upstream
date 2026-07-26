---
slug: "bilibili-all-in-one"
name: "bilibili-all-in-one"
version: 1.0.25
displayName: "B站全功能工具箱"
summary: "B站热门监控、视频下载、数据追踪、字幕处理、播放与投稿一体化工具集。"
license: "Proprietary"
description: |-
  面向B站的六合一全功能工具技能,集成热门监控(Hot Monitor)、视频下载(Downloader)、
  数据追踪(Watcher)、字幕处理(Subtitle)、播放信息(Player)与视频投稿(Publisher)六大模块.
  支持热门/热搜/必看榜/分区排行实时获取,360p至4K多清晰度下载与mp4/flv/mp3格式转换,
  播放量/点赞/评论长期追踪与多视频对比,字幕下载与格式转换,弹幕获取与播放列表解析,
  以及视频上传/定时发布/草稿编辑。凭据支持环境变量、JSON文件、直接参数三种方式,
  默认内存存储,可选 `BILIBILI_PERSIST` 持久化到0600权限文件。无凭据亦可使用热门、
  标准清晰度下载、字幕列表、弹幕、统计等公共API能力.
tags:
  - 研发工具
  - bilibili
  - video
  - downloader
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# Bilibili All In One 全功能工具箱

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | B站全功能工具箱处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| B站全功能工具箱B站热门监控 | 不支持 | 支持 |
| B站全功能工具箱字幕处理 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
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

- **热门监控 (hot_monitor)**: `get_hot` 获取热门视频、`get_trending` 获取热门系列、`get_weekly` 获取每周必看榜、`get_rank` 按分区获取排行,支持 `all`/`anime`/`music`/`dance`/`game`/`tech`/`life`/`food`/`car`/`fashion`/`entertainment`/`movie`/`tv` 等13个分区
- **视频下载 (downloader)**: `get_info` 获取视频信息、`get_formats` 列出可用清晰度、`download` 单视频下载、`batch_download` 批量下载,支持 `360p`/`480p`/`720p`/`1080p`/`1080p+`/`4k` 六档清晰度与 `mp4`/`flv`/`mp3` 三种格式
- **数据追踪 (watcher)**: `watch` 获取视频详情、`get_stats` 获取当前互动统计、`track` 按分钟间隔持续追踪指标、`compare` 多视频数据对比,支持 `BV` 短ID与完整URL两种输入
- **字幕处理 (subtitle)**: 字幕列表获取、字幕下载、SRT/ASS格式转换、多语言字幕支持,可选用 `faster-whisper` 进行语音识别字幕兜底
- **播放信息 (player)**: `play` 获取完整播放信息、`get_playurl` 获取直链、`get_danmaku` 获取弹幕(支持滚动/底部固定/顶部固定三种模式)、`get_playlist` 获取分P列表
- **视频投稿 (publisher)**: 视频上传、定时发布、草稿编辑与管理,需要 `SESSDATA` + `bili_jct` 凭据,通过 `member.bilibili.com` 与 `upos-sz-upcdnbda2.bilivideo.com` CDN完成
- **统一调用接口**: 所有模块通过 `app.execute(module, action, **params)` 异步调用,返回 `{"success": bool, ...}` 统一JSON结构,CLI支持 `python main.py <module> <action> <params_json>`
- **凭据三态管理**: 环境变量(`BILIBILI_SESSDATA`/`BILIBILI_BILI_JCT`/`BILIBILI_BUVID3`)、JSON文件、直接参数三种注入方式;默认内存存储,`BILIBILI_PERSIST=1` 启用0600权限文件持久化,支持运行时 `auth.persist` 切换与 `auth.clear_persisted()` 清理
### 热门监控 (hot_monitor)

针对热门监控 (hot_monitor),自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供热门监控 (hot_monitor)相关的配置参数、输入数据和处理选项.
**输出**: 返回热门监控 (hot_monitor)的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`热门监控 (hot_monitor)`的配置文档进行参数调优
### 视频下载 (downloader)

针对视频下载 (downloader),自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供视频下载 (downloader)相关的配置参数、输入数据和处理选项.
**输出**: 返回视频下载 (downloader)的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`视频下载 (downloader)`的配置文档进行参数调优
### 数据追踪 (watcher)

针对数据追踪 (watcher),自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供数据追踪 (watcher)相关的配置参数、输入数据和处理选项.
**输出**: 返回数据追踪 (watcher)的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`数据追踪 (watcher)`的配置文档进行参数调优
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`bilibili-all-in-one`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

## 适用场景

- **内容运营监测**: 实时跟踪B站热门趋势与分区排行,结合 `watcher.track` 持续监控竞品视频播放/点赞/评论变化,输出数据报表
- **视频素材采集**: 批量下载指定清晰度视频或提取MP3音频,配合字幕下载构建训练数据集或二创素材库
- **UP主投稿工作流**: 通过publisher模块完成视频上传、定时发布、草稿管理,实现自动化投稿管线
- **弹幕与播放分析**: 获取视频弹幕与分P信息,结合 `watcher.compare` 对比多视频表现,辅助内容选题决策

## 安装与环境

```bash
pip install httpx aiohttp beautifulsoup4 lxml requests
# 可选: 语音识别字幕兜底
pip install faster-whisper
# 可选: 视频流合并
# 系统安装 ffmpeg
```

Python >= 3.8,操作系统 Windows / macOS / Linux.
## 凭据配置

**方式1: 环境变量**
```bash
export BILIBILI_SESSDATA="your_sessdata"
export BILIBILI_BILI_JCT="your_bili_jct"
export BILIBILI_BUVID3="your_buvid3"
```

**方式2: JSON文件**
```json
{
  "sessdata": "your_sessdata",
  "bili_jct": "your_bili_jct",
  "buvid3": "your_buvid3"
}
```

**方式3: 直接参数**
```python
from main import BilibiliAllInOne
# ...
app = BilibiliAllInOne(
    sessdata="your_sessdata",
    bili_jct="your_bili_jct",
    buvid3="your_buvid3",
)
```

**持久化 (可选)**: 默认凭据仅存内存,设置 `BILIBILI_PERSIST=1` 或 `BilibiliAllInOne(persist=True)` 后自动保存到 `.credentials.json` (0600权限),下次启动自动加载,运行时可用 `app.auth.persist = True/False` 切换,`app.auth.clear_persisted()` 删除文件.
## 模块凭据要求

| 模块 | 是否需要凭据 | 说明 |
|:---:|:---:|:---:|
| Hot Monitor | 否 | 全部公共API |
| Downloader | 可选 | 仅1080p+/4K需要 |
| Watcher | 否 | 公共统计API |
| Subtitle | 否 | 公共字幕API |
| Player | 可选 | 高清播放直链需要 |
| Publisher | 必需 | 所有操作需SESSDATA+bili_jct |

## 案例展示

### 案例一： 热门监控与分区排行

获取热门视频与游戏分区排行:
```bash
python main.py hot_monitor get_hot '{"page_size": 10}'
python main.py hot_monitor get_rank '{"category": "game", "limit": 10}'
python main.py hot_monitor get_weekly
python main.py hot_monitor get_trending '{"limit": 5}'
```

Python异步调用:
```python
import asyncio
from main import BilibiliAllInOne
# ...
app = BilibiliAllInOne()
# ...
async def main():
    hot = await app.execute("hot_monitor", "get_hot", page_size=10)
    rank = await app.execute("hot_monitor", "get_rank", category="game", limit=10)
    print(hot, rank)
# ...
asyncio.run(main())
```

### 案例二： 视频下载与批量提取音频

单视频1080p下载与多视频MP3批量提取:
```bash
python main.py downloader download '{"url": "BV1xx411c7mD", "quality": "1080p", "format": "mp4"}'
python main.py downloader batch_download '{"urls": ["BV1xx411c7mD", "BV1yy411c8nE"], "format": "mp3"}'
```

```python
info = await app.execute("downloader", "get_info", url="BV1xx411c7mD")
formats = await app.execute("downloader", "get_formats", url="BV1xx411c7mD")
result = await app.execute("downloader", "download", url="BV1xx411c7mD", quality="1080p")
```

### 案例三： 数据追踪与弹幕获取

持续追踪视频指标12小时并获取弹幕:
```bash
python main.py watcher track '{"url": "BV1xx411c7mD", "interval": 30, "duration": 12}'
python main.py player get_danmaku '{"url": "BV1xx411c7mD"}'
python main.py watcher compare '{"urls": ["BV1xx411c7mD", "BV1yy411c8nE"]}'
```

```python
track_result = await app.execute("watcher", "track", url="BV1xx411c7mD", interval=30, duration=12)
danmaku = await app.execute("player", "get_danmaku", url="BV1xx411c7mD")
playlist = await app.execute("player", "get_playlist", url="BV1xx411c7mD")
```

## 网络端点

| 域名 | 用途 |
|:------|------:|
| `api.bilibili.com` | 视频信息、统计、热门、字幕、弹幕、播放直链 |
| `member.bilibili.com` | 视频投稿(上传、编辑) |
| `upos-sz-upcdnbda2.bilivideo.com` | 视频文件上传CDN |
| `www.bilibili.com` | 网页抓包兜底 |

所有HTTP请求仅发往B站官方域名,HTTPS加密,不向任何第三方服务、分析端点或遥测服务发送凭据.
## 异常处理

### 凭据无效或过期
现象: Publisher操作返回 `{"success": false, "message": "login required"}`;Downloader返回1080p+清晰度不可用.
原因: `SESSDATA`/`bili_jct` 过期或被B站风控,`buvid3` 缺失导致WBI签名失败.
处理: 浏览器登录B站后重新抓取三个Cookie;优先用小号测试而非主账号;凭据通过环境变量注入,启用 `persist=True` 时确认 `.credentials.json` 权限为0600.
### 412风控拦截
现象: 请求返回412状态码或 `{"code": -509, "message": "请求过于频繁"}`.
原因: 短时间高频请求触发B站反爬,缺少 `buvid3` 或UA指纹异常.
处理: 降低调用频率,`watcher.track` 的 `interval` 不低于30分钟;补全 `BILIBILI_BUVID3`;复用同一会话的httpx Client以保持Cookie一致性.
### 视频清晰度不可用
现象: `downloader.download` 指定 `1080p+`/`4k` 后实际下载为 `720p`.
原因: 该清晰度需要大会员账号或UP主未提供该档位;未携带 `SESSDATA`.
处理: 调用 `get_formats` 先确认可用清晰度列表;1080p+/4K必须携带有效 `SESSDATA`(大会员账号);非会员场景使用 `1080p` 及以下档位.
### 弹幕分段缺失
现象: `get_danmaku` 返回弹幕数量明显少于实际播放量.
原因: B站弹幕按分P与时间分段存储,长视频弹幕分多段,默认只返回第一段且 `segment` 参数未指定.
处理: 通过 `get_playlist` 获取分P列表后逐P调用 `get_danmaku`,并指定 `segment` 索引遍历所有分段;长视频建议按6分钟一段循环拉取.
### ffmpeg合并失败
现象: 下载的视频只有画面无声音,或合并时报 `ffmpeg not found`.
原因: B站高清流为音视频分离的DASH流,需要ffmpeg合并;系统未安装ffmpeg或未加入PATH.
处理: 安装ffmpeg(`brew install ffmpeg` / `apt install ffmpeg` / Windows下载二进制并配置PATH);指定 `format=mp3` 时仅下载音频可跳过合并.
### 投稿上传中断
现象: `publisher` 上传过程中断,文件未完整到达CDN.
原因: 大文件分片上传网络抖动,`upos-sz-upcdnbda2.bilivideo.com` 连接超时.
处理: 检查上行带宽,单文件建议小于8GB;启用断点续传需在代码层捕获异常后分片;投稿前先用 `get_info` 确认视频元数据完整.
### 字幕获取为空
现象: `subtitle` 模块返回空列表.
原因: UP主未上传官方字幕,且视频无AI自动字幕;`faster-whisper` 未安装无法走语音识别兜底.
处理: 确认视频确实有字幕轨(播放页CC按钮可开启);安装 `faster-whisper>=1.0.0` 启用语音识别兜底;部分字幕需登录后才能获取,携带 `SESSDATA`.
### WBI签名错误
现象: 部分API返回 `{"code": -403, "message": "访问权限不足"}` 即便凭据正确.
原因: B站部分接口要求WBI签名,`img_key`/`sub_key` 未正确获取或缓存过期,凭据缓存失效.
处理: 库内部会自动获取并刷新WBI密钥,若仍失败尝试重启进程重新初始化 `BilibiliAllInOne()`;确认 `buvid3` 不为空,WBI签名依赖完整设备指纹.
## 常见问题

### Q1: 哪些功能不需要登录凭据?
热门监控(`get_hot`/`get_trending`/`get_weekly`/`get_rank`)、标准清晰度(360p-1080p)下载、数据追踪(`watch`/`get_stats`/`track`/`compare`)、字幕列表、弹幕获取、播放信息全部使用公共API,无需任何凭据。仅1080p+/4K下载、高清播放直链、投稿发布需要 `SESSDATA`+`bili_jct`.
### Q2: 凭据会被保存到磁盘吗?
默认不会。凭据仅在内存中持有,进程退出即销毁。显式设置 `BILIBILI_PERSIST=1` 环境变量或 `BilibiliAllInOne(persist=True)` 后,凭据会保存到当前目录 `.credentials.json`,文件权限0600(仅属主可读写)。运行时可用 `app.auth.persist = False` 关闭并调用 `app.auth.clear_persisted()` 删除文件.
### Q3: SESSDATA和bili_jct是受限API密钥吗?
不是。它们是B站浏览器完整会话Cookie,等同于账号密码级别权限,可执行登录态下所有操作。务必使用小号测试,不要在共享环境或公共仓库中暴露;启用持久化时确认 `.credentials.json` 已加入 `.gitignore`.
### Q4: batch_download支持多少个视频?
理论无上限,但B站反爬会限制短时间请求频率。建议单批不超过20个,批量间间隔5-10秒;`watcher.track` 的 `interval` 建议30分钟以上避免触发412.
### Q5: 下载的视频为什么音画分离?
B站高清流(720p+)采用DASH协议,音频与视频独立传输。库内部会调用ffmpeg合并为单文件;若系统无ffmpeg,可在 `download` 指定 `format=mp3` 仅取音频,或手动用ffmpeg合并下载的两个文件.
### Q6: publisher支持哪些投稿操作?
支持视频上传、定时发布、草稿编辑与管理。所有操作必须携带 `SESSDATA`+`bili_jct`,通过 `member.bilibili.com` 提交元数据,视频文件经 `upos-sz-upcdnbda2.bilivideo.com` CDN上传。具体action列表参考 `references/detail.md`.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 依赖B站官方API,接口变更可能导致部分功能失效,需跟进官方接口调整
- 高清下载(1080p+/4K)与投稿必须携带完整会话Cookie,不支持OAuth或受限API Key
- 弹幕按分P与时间分段存储,长视频需遍历 `segment` 参数拉取全部
- `faster-whisper` 语音识别字幕为可选依赖,未安装时无法对无字幕视频生成文本
- 视频流合并依赖系统ffmpeg,未安装时高清下载只能得到音视频分离文件
- 反爬策略持续升级,高频调用可能触发412或-509,需控制请求频率
- 投稿模块的封面、分区、标签等元数据需符合B站审核规范,违规内容会被拒审

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "B站全功能工具箱处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "bilibili-all-in-one"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```

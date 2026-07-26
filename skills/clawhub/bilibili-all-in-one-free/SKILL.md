---
slug: "bilibili-all-in-one-free"
name: "bilibili-all-in-one-free"
version: "1.0.0"
displayName: "B站工具箱免费版"
summary: "B站热门监控、标准清晰度下载、数据追踪与弹幕获取基础工具集,无需登录凭据。"
license: "MIT"
description: |-
  B站全功能工具箱的免费基础版,集成热门监控(Hot Monitor)、标准清晰度下载(Downloader)、
  数据追踪(Watcher)与播放信息(Player)四大公共API模块。支持热门/热搜/必看榜/分区排行获取,
  360p至1080p视频下载与mp4格式输出,播放量/点赞/评论统计与多视频对比,弹幕获取与分P列表解析.
  全部功能基于B站公共API,无需任何登录凭据。不包含1080p+/4K高清下载、字幕处理、
  视频投稿等需要会话Cookie的付费能力.
tags:
  - 研发工具
  - bilibili
  - video
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# Bilibili All In One 全功能工具箱 (免费版)

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | B站工具箱免费版处理的输入数据或指令 |
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

- **热门监控 (hot_monitor)**: `get_hot` 获取热门视频、`get_trending` 获取热门系列、`get_weekly` 获取每周必看榜、`get_rank` 按分区获取排行,支持 `all`/`anime`/`music`/`dance`/`game`/`tech`/`life`/`food`/`car`/`fashion`/`entertainment`/`movie`/`tv` 等13个分区
- **视频下载 (downloader)**: `get_info` 获取视频信息、`get_formats` 列出可用清晰度、`download` 单视频下载,支持 `360p`/`480p`/`720p`/`1080p` 四档清晰度与 `mp4` 格式输出
- **数据追踪 (watcher)**: `watch` 获取视频详情、`get_stats` 获取当前互动统计、`compare` 多视频数据对比,支持 `BV` 短ID与完整URL两种输入
- **播放信息 (player)**: `play` 获取完整播放信息、`get_playurl` 获取标准清晰度直链、`get_danmaku` 获取弹幕(支持滚动/底部固定/顶部固定三种模式)、`get_playlist` 获取分P列表
- **统一调用接口**: 所有模块通过 `app.execute(module, action, **params)` 异步调用,返回 `{"success": bool, ...}` 统一JSON结构,CLI支持 `python main.py <module> <action> <params_json>`
- **无需凭据**: 全部功能基于B站公共API,无需 `SESSDATA`/`bili_jct`/`buvid3` 等会话Cookie
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
2. **指令输入**: 向Agent描述需要执行的任务，引用`bilibili-all-in-one-free`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

## 适用场景

- **热门内容发现**: 获取B站热门视频、分区排行与每周必看榜,辅助内容选题与趋势洞察
- **标准视频下载**: 下载360p-1080p清晰度视频为本地mp4文件,用于离线观看或素材采集

## 安装与环境

```bash
pip install httpx aiohttp beautifulsoup4 lxml requests
# 可选: 视频流合并
# 系统安装 ffmpeg
```

Python >= 3.8,操作系统 Windows / macOS / Linux.
## 基础用法

```python
import asyncio
from main import BilibiliAllInOne
# ...
app = BilibiliAllInOne()
# ...
async def main():
    hot = await app.execute("hot_monitor", "get_hot", page_size=10)
    print(hot)
# ...
asyncio.run(main())
```

CLI调用:
```bash
python main.py hot_monitor get_hot '{"page_size": 10}'
python main.py hot_monitor get_rank '{"category": "game", "limit": 10}'
```

## 案例展示

### 案例一： 热门监控与分区排行

获取热门视频与游戏分区排行:
```bash
python main.py hot_monitor get_hot '{"page_size": 10}'
python main.py hot_monitor get_rank '{"category": "game", "limit": 10}'
python main.py hot_monitor get_weekly
python main.py hot_monitor get_trending '{"limit": 5}'
```

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

### 案例二： 标准清晰度下载与弹幕获取

下载1080p视频并获取弹幕:
```bash
python main.py downloader download '{"url": "BV1xx411c7mD", "quality": "1080p", "format": "mp4"}'
python main.py player get_danmaku '{"url": "BV1xx411c7mD"}'
python main.py watcher compare '{"urls": ["BV1xx411c7mD", "BV1yy411c8nE"]}'
```

```python
result = await app.execute("downloader", "download", url="BV1xx411c7mD", quality="1080p")
danmaku = await app.execute("player", "get_danmaku", url="BV1xx411c7mD")
```

## 异常处理

### 412风控拦截
现象: 请求返回412状态码或 `{"code": -509, "message": "请求过于频繁"}`.
原因: 短时间高频请求触发B站反爬.
处理: 降低调用频率,单次批量不超过20个视频,批量间间隔5-10秒;复用同一会话的httpx Client保持连接一致性.
### 视频清晰度不可用
现象: `downloader.download` 指定 `1080p+`/`4k` 后实际下载为 `720p` 或返回不支持.
原因: 免费版仅支持360p-1080p四档清晰度,1080p+/4K需要付费版携带 `SESSDATA` 会话Cookie.
处理: 切换到 `1080p` 及以下档位;若需1080p+/4K高清下载,请升级付费版.
### ffmpeg合并失败
现象: 下载的视频只有画面无声音,或合并时报 `ffmpeg not found`.
原因: B站高清流为音视频分离的DASH流,需要ffmpeg合并;系统未安装ffmpeg或未加入PATH.
处理: 安装ffmpeg(`brew install ffmpeg` / `apt install ffmpeg` / Windows下载二进制并配置PATH).
### 弹幕分段缺失
现象: `get_danmaku` 返回弹幕数量明显少于实际播放量.
原因: B站弹幕按分P与时间分段存储,长视频弹幕分多段,默认只返回第一段.
处理: 通过 `get_playlist` 获取分P列表后逐P调用 `get_danmaku`,并指定 `segment` 索引遍历所有分段.
### 视频不存在或已下架
现象: `get_info`/`download` 返回 `{"success": false, "message": "video not found"}`.
原因: BV号错误、视频已被UP主删除或被B站下架.
处理: 核对BV号格式(以BV开头12位);在浏览器访问确认视频可正常播放;已下架视频无法恢复.
## 常见问题

### Q1: 免费版需要登录凭据吗?
不需要。免费版全部功能基于B站公共API,无需 `SESSDATA`/`bili_jct`/`buvid3` 等会话Cookie,直接 `BilibiliAllInOne()` 初始化即可使用.
### Q2: 免费版支持哪些下载清晰度?
免费版支持 `360p`/`480p`/`720p`/`1080p` 四档清晰度与 `mp4` 格式。`1080p+`/`4k` 高清档位与 `flv`/`mp3` 格式需升级付费版并携带会话Cookie.
### Q3: 免费版能投稿视频吗?
不能。视频上传、定时发布、草稿编辑等 `publisher` 模块能力需要 `SESSDATA`+`bili_jct` 完整会话Cookie,属付费版功能.
### Q4: 下载的视频为什么音画分离?
B站高清流(720p+)采用DASH协议,音频与视频独立传输。库内部会调用ffmpeg合并为单文件;若系统无ffmpeg,需自行安装或将清晰度降至360p/480p(这些档位为单流).
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接和配置后重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 仅支持360p-1080p四档清晰度,不包含1080p+/4K高清下载
- 仅支持 `mp4` 格式输出,不包含 `flv` 与 `mp3` 音频提取
- 不包含 `subtitle` 字幕处理模块与 `faster-whisper` 语音识别兜底
- 不包含 `publisher` 视频投稿模块(上传/定时发布/草稿编辑)
- 不支持凭据管理与持久化(无需凭据)
- 反爬策略可能触发412,需控制请求频率

## 升级提示

当前为免费版,仅包含公共API基础能力。升级付费版可获得:
- `1080p+`/`4k` 高清下载与 `flv`/`mp3` 格式转换
- `subtitle` 字幕处理模块(SRT/ASS转换 + `faster-whisper` 语音识别兜底)
- `publisher` 视频投稿模块(上传/定时发布/草稿编辑)
- 凭据三态管理(环境变量/JSON文件/直接参数)与0600权限持久化
- 高清播放直链与 `watcher.track` 长期指标追踪
- 完整13个分区排行与多视频对比分析

付费版slug: `bilibili-all-in-one`

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "B站工具箱免费版处理结果",
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

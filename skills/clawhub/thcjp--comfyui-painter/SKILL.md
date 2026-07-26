---
slug: "comfyui-painter"
name: "comfyui-painter"
version: 2.0.1
displayName: "ComfyUI本地画图工作流"
summary: "本地ComfyUI画图工作流+CivitAI集成,API控制文生图/图生视频,支持模型搜索/下载/自动调参"
license: "Proprietary"
description: |-
  本地 ComfyUI 画图工作流与 CivitAI 模型管理集成客户端。通过 ComfyUI API 在本地 GPU 上生成图片,
  支持文生图与图生视频两种任务类型。集成 CivitAI 模型生态,支持模型搜索、详情查询、推荐参数提取、
  本地模型更新检查与一键下载。内置自动调参引擎,从 CivitAI 样图元数据中提取推荐 Steps/CFG/采样器
  设置并写入 config 缓存。支持 8 种模型别名覆盖动漫、写实、3DCG、暗黑美学、Flux 等风格。提供心跳
  空闲检测,15 分钟无使用自动关闭 ComfyUI 释放显存。适用于个人创作者、内容生产团队与自动化画图
  工作流场景.
tags:
  - Creative
  - 图像生成
  - ComfyUI
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# ComfyUI Painter

通过 ComfyUI API 在本地 GPU 上生成图片,集成 CivitAI 模型管理与自动调参引擎。支持文生图、图生视频、模型搜索下载、推荐参数提取等完整工作流.
**范围外**（本技能不做）: 模型训练与微调、ComfyUI 自身安装部署、WebUI 界面操作、商业图库分发.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | ComfyUI本地画图工作流处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **GPU**: NVIDIA GPU,建议显存 8GB 以上
- **网络**: 需可访问 `http://127.0.0.1:8188`（本地 ComfyUI）与 `https://civitai.com`

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| ComfyUI | 本地服务 | 必需 | 本地安装并配置模型路径 |
| Python 3.8+ | 运行时 | 必需 | 官方安装 |
| requests | Python 库 | 必需 | pip install requests |
| CivitAI API Key | 凭证 | 推荐 | civitai.com 注册获取 |
| curl 或等价 HTTP 客户端 | 命令行工具 | 必需 | 系统自带 |

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令驱动,需 exec 执行 Python 脚本与 API 调用）
- **说明**: 基于自然语言指令驱动 Agent 调用 ComfyUI API 与 CivitAI API,完成图片生成与模型管理

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 脚本路径
所有脚本相对于此 skill 目录:

- `（请参考skill目录中的脚本文件）` — ComfyUI 启动/关闭/状态检查
- `（请参考skill目录中的脚本文件）` — 图片生成（调用 ComfyUI API）
- `（请参考skill目录中的脚本文件）` — 空闲自动关闭检查
- `（请参考skill目录中的脚本文件）` — CivitAI 集成（搜索/详情

**输入**: 用户提供脚本路径所需的指令和必要参数.
### ComfyUI 生命周期管理

**输入**: 用户提供ComfyUI 生命周期管理所需的指令和必要参数.
**处理**: 解析ComfyUI 生命周期管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回ComfyUI 生命周期管理的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`ComfyUI 生命周期管理`的配置文档进行参数调优
### 启动 ComfyUI
```python
import scripts.comfyui_manager as mgr
mgr.start()  # 自动启动本地 ComfyUI 进程
```

启动后默认监听 `http://127.0.0.1:8188`。脚本会等待服务就绪后返回.
**输入**: 用户提供启动 ComfyUI所需的指令和必要参数.
**处理**: 解析启动 ComfyUI的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 状态检查
```python
import scripts.comfyui_manager 
# ...
**输入**: 用户提供ComfyUI 生命周期管理相关的配置参数、输入数据和处理选项.
**处理**: 解析ComfyUI 生命周期管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
# ...
**输出**: 返回状态检查的处理结果,包含执行状态码、结果数据和执行日志.
### 图片生成
# ...
# ...
**输入**: 用户提供图片生成所需的指令和必要参数.
**处理**: 解析图片生成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回图片生成的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`图片生成`的配置文档进行参数调优
### 基础生成
# ...
```python
from scripts.generate import generate
result = generate(
    positive="masterpiece, best quality, 1girl, solo, detailed background",
    model="noobv6",
    batch_size=4,
    width

**输入**: 用户提供图片生成相关的配置参数、输入数据和处理选项.
**处理**: 解析图片生成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### CivitAI 集成

**输入**: 用户提供CivitAI 集成所需的指令和必要参数.
**处理**: 解析CivitAI 集成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回CivitAI 集成的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`CivitAI 集成`的配置文档进行参数调优
### 搜索模型
```bash
python3 （请参考skill目录中的脚本文件） search "anime checkpoint" --limit 5
```

返回模型名称、ID、下载量、基础模型等元数据.
**输入**: 用户提供搜索模型所需的指令和必要参数.
**处理**: 解析搜索模型的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `搜索模型` 选项

### 查看模型详情
```bash
python3 （请参考skill目录中的脚本文件） info 140272
```

**输入**: 用户提供查看模型详情所需的指令和必要参数.
**处理**: 解析查看模型详情的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回查看模型详情的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `查看模型详情` 选项

### 获取推荐参数
```bash
pyth
# ...
**处理**: 解析CivitAI 集成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
# ...
**输入**: 用户提供获取推荐参数所需的指令和必要参数.
**输出**: 返回获取推荐参数的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `获取推荐参数` 选项
# ...
### 模型别名
# ...
| 别名 | Checkpoint | CivitAI ID | 版本 | 风格 |
|:---:|:---:|:---:|:---:|:---:|
| hassaku | hassakuXLIllustrious_v34 | 140272 | v3.4 | Illustrious 动漫 |
| noobv6 | pornmasterPro_noobV6 | 1045588 | noob-V6 |
# ...
**输入**: 用户提供模型别名相关的配置参数、输入数据和处理选项.
**处理**: 解析模型别名的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回模型别名的处理结果,包含执行状态码、结果数据和执行日志.
# ...
### 自动调参参数表
# ...
每个模型在 config.json 的 model_params 中缓存推荐参数:
# ...
| 模型 | Steps | CFG | 采样器 |
|:------|------:|:------|:------|
| hassaku | 20 | 7 | euler_a |
| janku | 20 | 7 | euler_a |
| noobv6 | 20 | 7 | euler_a |
| sdxlv8 | 25 
# ...
**处理**: 解析自动调参参数表的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回自动调参参数表的处理结果,包含执行状态码、结果数据和执行日志.
# ...
### 提示词优化指南
# ...
用户给自然语言描述时,转换为专业 Stable Diffusion 提示词:
# ...
- 质量标签在前: `masterpiece, best quality, absurdres, highres`
- 用 `BREAK` 分隔不同语义段
- 动作/姿势用专业标签: `mating press, pov, from below, spread legs`
- 细节标签: `detailed skin,
# ...
**输入**: 用户提供提示词优化指南相关的配置参数、输入数据和处理选项.
**输出**: 返回提示词优化指南的处理结果,包含执行状态码、结果数据和执行日志.
# ...
#
## 脚本路径(补充)
# ...
所有脚本相对于此 skill 目录:
# ...
- `（请参考skill目录中的脚本文件）` — ComfyUI 启动/关闭/状态检查
- `（请参考skill目录中的脚本文件）` — 图片生成（调用 ComfyUI API）
- `（请参考skill目录中的脚本文件）` — 空闲自动关闭检查
- `（请参考skill目录中的脚本文件）` — CivitAI 集成（搜索/详情/下载/更新检查/推荐参数）
- `（请参考skill目录中的脚本文件）` — 自动调参（从 CivitAI 样图元数据提取推荐设置）
- `config.json` — 配置文件（模型别名、默认参数、路径、CivitAI 关联）
# ...
## 认证
# ...
CivitAI API Key 存于 `~/.skill-platform/workspace/credentials/civitai.md`,格式:
# ...
```text
Token: your_api_key_here
```
# ...
校验 Key 是否存在:
# ...
```bash
[ -f ~/.skill-platform/workspace/credentials/civitai.md ] && echo ok || echo missing
```
# ...
Key 缺失时不阻塞基础画图功能,但 CivitAI 搜索/下载/更新检查将不可用,需引导用户前往 civitai.com 注册并配置.
# ...
**安全红线**: 永不打印或回显 API Key;Key 仅用于 CivitAI API 请求头认证.
# ...
## ComfyUI 生命周期管理(补充)
# ...
### 启动 ComfyUI(补充)
# ...
```python
import scripts.comfyui_manager as mgr
mgr.start()  # 自动启动本地 ComfyUI 进程
```
# ...
启动后默认监听 `http://127.0.0.1:8188`。脚本会等待服务就绪后返回.
# ...
### 状态检查(补充)
# ...
```python
import scripts.comfyui_manager as mgr
status = mgr.status()  # 返回 running / stopped / error
```
# ...
### 关闭 ComfyUI
# ...
```python
import scripts.comfyui_manager as mgr
mgr.stop()
```
# ...
### 空闲自动关闭
# ...
```bash
python3 （请参考skill目录中的脚本文件）
```
# ...
检查空闲时间,超过 15 分钟无使用自动关闭 ComfyUI 释放显存。建议在心跳回调中调用.
# ...
## 图片生成(补充)
# ...
### 基础生成(补充)
# ...
```python
from scripts.generate import generate
result = generate(
    positive="masterpiece, best quality, 1girl, solo, detailed background",
    model="noobv6",
    batch_size=4,
    width=1024,
    height=1536,
    steps=20,
    cfg=7,
)
```
# ...
生成完成后,图片输出到 workspace 临时目录,返回文件路径列表.
# ...
### 带自动调参生成
# ...
```python
from scripts.auto_tune import get_tuned_params
from scripts.generate import generate

params = get_tuned_params("janku")  # 从 CivitAI 获取推荐参数
result = generate(
    positive="your prompt",
    model="janku",
    steps=params["steps"],
    cfg=params["cfg"],
    width=params["width"],
    height=params["height"],
)
```
# ...
自动调参优先级: 用户指定参数 > config.json 缓存的 model_params > 全局 defaults.
# ...
## CivitAI 集成(补充)
# ...
### 搜索模型(补充)
# ...
```bash
python3 （请参考skill目录中的脚本文件） search "anime checkpoint" --limit 5
```
# ...
返回模型名称、ID、下载量、基础模型等元数据.
# ...
### 查看模型详情(补充)
# ...
```bash
python3 （请参考skill目录中的脚本文件） info 140272
```
# ...
# ...
### 获取推荐参数(补充)
# ...
```bash
python3 （请参考skill目录中的脚本文件） params 140272
```
# ...
从模型样图元数据中提取推荐 Steps、CFG、采样器、分辨率等设置.
# ...
### 检查本地模型更新
# ...
```bash
python3 （请参考skill目录中的脚本文件） check-updates
```
# ...
遍历本地模型文件,计算 SHA256 并与 CivitAI 版本比对。每个文件约需 30 秒.
# ...
### 下载模型
# ...
```bash
python3 （请参考skill目录中的脚本文件） download "https://civitai.com/api/download/models/XXXXX" --filename model_name.safetensors
```
# ...
下载完成后自动更新 config.json 中的模型别名映射.
# ...
### 批量更新推荐参数
# ...
```bash
python3 （请参考skill目录中的脚本文件） update-all
```
# ...
遍历 config.json 中所有模型别名,从 CivitAI 拉取推荐参数并写入 model_params 缓存.
# ...
## 模型别名(补充)
# ...
| 别名(续)| Checkpoint | CivitAI ID | 版本 | 风格 |
|---:|:---|---:|---:|:---|
| hassaku | hassakuXLIllustrious_v34 | 140272 | v3.4 | Illustrious 动漫 |
| noobv6 | pornmasterPro_noobV6 | 1045588 | noob-V6 | NoobAI 动漫（默认） |
| noobv4 | pornmasterPro_noobV4 | 1045588 | noob-V4 | NoobAI 动漫（旧版） |
| sdxlv8 | pornmaster_proSDXLV8 | 82543 | Pro-SDXL-V8 | SDXL 写实 |
| janku | JANKUTrainedNoobaiRouwei_v69 | 1277670 | v6.9 | NoobAI+RouWei 混合 |
| nova3d | nova3DCGXL_ilV80 | 715287 | IL v8.0 | 3DCG/2.5D |
| unholy | unholyDesireMixSinister_v70 | 1307857 | v7.0 | 暗黑美学 |
| flux | flux1-dev-bnb-nf4-v2 | 638187 | BNB NF4 v2 | Flux 写实 |
# ...
## 自动调参参数表(补充)
# ...
每个模型在 config.json 的 model_params 中缓存推荐参数:
# ...
| 模型(续)| Steps | CFG | 采样器 |
|:-------:|---------|:--------|:-------:|
| hassaku | 20 | 7 | euler_a |
| janku | 20 | 7 | euler_a |
| noobv6 | 20 | 7 | euler_a |
| sdxlv8 | 25 | 5 | dpmpp_2m |
| nova3d | 20 | 7 | euler_a |
| unholy | 20 | 7 | euler_a |
| flux | 20 | 1 | euler |
# ...
## 提示词优化指南(补充)
# ...
用户给自然语言描述时,转换为专业 Stable Diffusion 提示词:
# ...
- 质量标签在前: `masterpiece, best quality, absurdres, highres`
- 用 `BREAK` 分隔不同语义段
- 动作/姿势用专业标签: `mating press, pov, from below, spread legs`
- 细节标签: `detailed skin, sweat, wet skin, motion blur, dynamic angle`
- 负面提示词加入: `censored, mosaic censoring, bar censor`
# ...
## 适用场景
# ...
### 场景一: 动漫风格批量出图
# ...
创作者需要用 NoobAI 模型批量生成 4 张动漫风格图片,使用默认推荐参数.
# ...
```python
from scripts.generate import generate
result = generate(
    positive="masterpiece, 1girl, solo, cherry blossoms, kimono, detailed background",
    model="noobv6",
    batch_size=4,
    width=1024,
    height=1536,
)
```
# ...
### 场景二: 自动调参生成
# ...
用户指定模型但不清楚推荐参数,由 auto_tune 从 CivitAI 拉取推荐设置.
# ...
```python
from scripts.auto_tune import get_tuned_params
from scripts.generate import generate
params = get_tuned_params("janku")
result = generate(positive="your prompt", model="janku", **params)
```
# ...
### 场景三: 模型更新检查与下载
# ...
用户想检查本地模型是否有新版本,并下载新模型.
# ...
```bash
# 检查更新
python3 （请参考skill目录中的脚本文件） check-updates

# 下载新模型
python3 （请参考skill目录中的脚本文件） download "https://civitai.com/api/download/models/XXXXX" --filename new_model.safetensors
```
# ...
## 使用流程
# ...
1. 调用 `comfyui_manager.status()` 检查 ComfyUI 是否运行,未运行则调用 `start()` 启动
2. 解析用户需求: 提示词、模型别名、尺寸、步数等参数
3. 若用户未指定参数,调用 `auto_tune.get_tuned_params(alias)` 获取推荐参数
4. 调用 `generate.generate()` 执行生成,获取图片文件路径
5. 将图片路径回传用户,或通过 message tool 发送到 Discord
6. 心跳回调中调用 `auto_shutdown.py` 检查空闲关闭
# ...
#
## 案例展示
# ...
### 案例一： 动漫角色批量生成
# ...
**场景**: 创作者需要用 hassaku 模型生成 4 张动漫风格角色图,尺寸 1024x1536
# ...
```python
from scripts.generate import generate
result = generate(
    positive="masterpiece, best quality, 1girl, solo, silver hair, red eyes, gothic dress, detailed background BREAK cathedral, stained glass, moonlight",
    negative="censored, mosaic censoring, low quality, worst quality",
    model="hassaku",
    batch_size=4,
    width=1024,
    height=1536,
    steps=20,
    cfg=7,
)
```
# ...
**输出**: 4 张 PNG 图片文件路径
# ...
**说明**: 使用 `BREAK` 分隔角色描述与背景描述,让模型分别处理语义段。batch_size=4 一次生成 4 张,适合快速筛选构图.
# ...
### 案例二： 自动调参生成混合风格
# ...
**场景**: 用户想用 janku 模型但不清楚推荐参数,让 auto_tune 自动获取
# ...
```python
from scripts.auto_tune import get_tuned_params
from scripts.generate import generate

params = get_tuned_params("janku")
# params 返回示例: {"steps": 20, "cfg": 7, "width": 1024, "height": 1536, "sampler": "euler_a"}
result = generate(
    positive="masterpiece, 1girl, dynamic pose, detailed skin, motion blur",
    model="janku",
    steps=params["steps"],
    cfg=params["cfg"],
    width=params["width"],
    height=params["height"],
)
```
# ...
**输出**: 1 张 PNG 图片文件路径
# ...
**说明**: `get_tuned_params` 优先从 config.json 缓存读取,缓存不存在时从 CivitAI 样图元数据实时提取并写入缓存。首次调用可能多花 2-3 秒.
# ...
### 案例三： 模型更新检查与下载
# ...
**场景**: 用户想检查本地 8 个模型是否有新版本,并下载一个新模型
# ...
```bash
# 检查所有本地模型更新（需计算 SHA256,每个文件约 30 秒）
python3 （请参考skill目录中的脚本文件） check-updates

# 下载新模型
python3 （请参考skill目录中的脚本文件） download "https://civitai.com/api/download/models/140272" --filename hassakuXLIllustrious_v35.safetensors

# 更新所有模型推荐参数到 config
python3 （请参考skill目录中的脚本文件） update-all
```
# ...
**输出**: 更新检查报告 + 下载完成确认 + config.json 已更新
# ...
**说明**: check-updates 对大文件计算 SHA256 耗时较长,建议在空闲时段执行。下载完成后 config.json 自动更新别名映射.
# ...
## 异常处理
# ...
# ...
| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|----|:--:|---:|----|
| comfyui_not_running | `Connection refused: 127.0.0.1:8188` | ComfyUI 未启动或启动中 | 调用 `mgr.start()` 启动,等待 10 秒后 |
| model_alias_not_found | `Unknown model alias: xxx` | config.json 中无此别名 | 列出可用别名，引导用户选择或通过 civitai.py download 添加 |
| civitai_api_key_missing | `CivitAI API Key not found` | credentials/civitai.md 缺失 | 不调 CivitAI API，引导用户前往 civitai.com 注册并配置 Key |
| civitai_rate_limited | `429 Too Many Requests` | CivitAI API 请求频率过高 | （5s/10s/20s），最多 3 次 |
| generate_timeout | `ComfyUI generation timeout` | 生成耗时超过 120 秒 | 检查 GPU 负载,降低 batch_size 或 steps 后 |
| oom_error | `CUDA out of memory` | 显存不足 | 降低分辨率或 batch_size,关闭其他占用显存的进程 |
| sha256_timeout | `SHA256 computation timeout` | 模型文件过大导致计算超时 | 跳过该文件,建议手动检查或分批执行 check-updates |
| download_failed | `Download failed: HTTP 403` | CivitAI 下载链接过期或需登录 | 引导用户检查 API Key 权限,或手动获取下载链接 |
# ...
## 常见问题
# ...
### Q1: ComfyUI 启动后多久可以开始生成?
A: `mgr.start()` 会等待 ComfyUI 服务就绪后返回,通常需要 10-30 秒。返回后即可调用 generate。若超过 60 秒仍未就绪,检查 GPU 驱动与模型路径配置.
# ...
### Q2: 自动调参的参数来源是什么?
A: auto_tune 从 CivitAI 模型页面的样图元数据中提取 Steps、CFG、采样器、分辨率等设置。这些参数由模型作者上传样图时附带,代表该模型的推荐使用配置。参数缓存在 config.json 的 model_params 字段中.
# ...
### Q3: check-updates 为什么很慢?
A: check-updates 需要计算每个本地模型文件的 SHA256 哈希值,用于与 CivitAI 版本精确比对。单个 2-6GB 的 safetensors 文件约需 30 秒。8 个模型全量检查约需 4 分钟。建议在空闲时段执行.
# ...
### Q4: 支持哪些模型格式?
A: 支持 `.safetensors` 与 `.ckpt` 格式的 checkpoint 模型。config.json 中维护别名到文件名的映射,新增模型后需更新配置或通过 `civitai.py download` 自动写入.
# ...
### Q5: 图生视频怎么用?
A: 图生视频通过 ComfyUI 的 AnimateDiff 或视频生成节点实现。调用 generate 时传入 `task_type="img2vid"` 与参考图片路径。具体节点配置参考 ComfyUI 工作流模板.
# ...
### Q6: Flux 模型的参数为什么和其他模型差别很大?
A: Flux 模型使用 CFG=1（无分类器引导）与 euler 采样器,与其他动漫模型的 CFG=7 + euler_a 不同。auto_tune 会自动识别并应用 Flux 专属参数,无需手动调整.
# ...
## 错误处理
# ...
# ...
| 错误场景 | 原因 | 处理方式 |
|----|----|----|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
## 已知限制
# ...
1. **需本地 GPU**: 必须有 NVIDIA GPU,显存不足时生成会失败或降速
2. **需 ComfyUI 本地部署**: 不支持远程 ComfyUI 或云服务,需本地安装
3. **CivitAI 集成需 API Key**: 无 Key 时搜索/下载/更新检查不可用,仅基础画图可用
4. **SHA256 计算耗时**: check-updates 对大文件计算哈希较慢,不适合频繁执行
5. **模型别名固定**: config.json 中预置 8 种别名,新增模型需手动配置或通过 download 命令自动写入
6. **不支持多设备同步**: 本地运行,config.json 与模型文件不跨设备同步
7. **图生视频依赖 ComfyUI 工作流**: 需预先配置 AnimateDiff 等节点,本技能不提供工作流模板
# ...
## 输出格式
# ...
```json
{
  "success": true,
  "data": {
    "result": "ComfyUI本地画图工作流处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "comfyui-painter"
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
# ...
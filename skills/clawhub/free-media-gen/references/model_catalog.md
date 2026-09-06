# 已知免费媒体模型目录（free-media-gen）

本清单是审计与首装引导的权威参考，与 `config.json` 保持同步。每次审计（`media_auditor.py`）后由脚本更新状态。
最后实测日期：**2026-08-28**

## 一、纳入（免费可用）

| 模型 | 平台 | 模态 | 免费 | 需 VPN | 状态 | 特点 | 二级命令 |
|---|---|---|---|---|---|---|---|
| `agnes-image-2.1-flash` | Agnes | 图 | ✅ | 否 | **verified** | 文生图/图生图；实测出图正常 | 用 Agnes 生图 |
| `agnes-image-2.0-flash` | Agnes | 图 | ✅ | 否 | **verified** | 文生图/图生图/多图合成 | 用 Agnes 生图 |
| `agnes-video-v2.0` | Agnes | 视频 | ✅ | 否 | **verified** | 异步；文/图生视频；两步取片 | 用 Agnes 生视频 |
| `agnes-video-2.5-flash` | Agnes | 视频 | 限时免费 | 否 | verified | 仅 720P、≤5 参考图 | 用 Agnes 生视频 |
| `sensenova-u1.5-lite` | 商汤 | 图 | ✅ | 否 | **verified** | 可 `watermark=false` 去水印；实测返回 b64 | 用商汤生图 |
| `sensenova-u1-fast` | 商汤 | 图 | ✅ | 否 | unverified | 轻量快速版 | 用商汤生图 |
| `Kwai-Kolors/Kolors` | 硅基流动 | 图 | ✅ | 否 | **verified** | 快手 Kolors；实测返回 URL | 用 Kolors 生图 |

## 二、当前不可用 / 已转付费（不列入主清单）

| 模型 | 平台 | 原因（实测） |
|---|---|---|
| `gemini-3.1-flash-image-preview` | Google | 域名可达，但**免费配额为 0**：`429 RESOURCE_EXHAUSTED, free_tier_requests limit: 0`。且原生 `generateContent` 端点对该 key 返回 `401 API_KEY_SERVICE_BLOCKED`，仅 OpenAI 兼容层可访问。需开通付费/配额后才可用（脚本保留，用户有配额即可用） |
| `agnes-video-2.5`（非 Flash） | Agnes | 付费，¥0.15–0.35/秒 |
| `Qwen/Qwen-Image` | 硅基流动 | 付费，¥0.3/张 |
| `Qwen/Qwen-Image-Edit(-2509)` | 硅基流动 | 图像编辑类且付费，非纯文生图 |
| 智谱 BigModel 系列 | 智谱 | 收费状态不确定，按决策排除 |
| 全部 NVIDIA / 文本对话模型 | 多 | 无媒体生成能力 |

## 三、首装引导：免费 API 申请地址

当用户无任何可服务媒体模型的平台密钥时，输出以下引导：

| 提供商 | 免费媒体能力 | 申请地址 |
|---|---|---|
| Agnes | 图 + 视频 | https://agnes-ai.cn （国内版） |
| 商汤 SenseNova | 图（U1.5 Lite / U1 Fast） | https://www.sensenova.cn |
| 硅基流动 SiliconFlow | 图（Kolors 免费） | https://cloud.siliconflow.cn |
| Google AI Studio | 图（**注意**：实测免费配额为 0，需自行确认） | https://aistudio.google.com （需 VPN） |

## 四、实测要点（避坑）

1. **Agnes 视频取片必须两步**：`GET /v1/videos/<task_id>` → 取 `video_id`（≠ task_id）；
   再 `GET /agnesapi?video_id=<vid>&model_name=<model>` → `metadata.url`。
   **必须带 `model_name`**，否则不返回直链。
2. **Agnes 目录端点**：必须保留 `/v1` 前缀（`{base}/v1/models`），剥离 `/v1` 会 403。
3. **硅基流动目录端点**：同理需 `/v1/models`，剥离 `/v1` 会 404。
4. **商汤返回体**：U1.5 Lite 实测返回 `b64_json`（非 URL），脚本需处理两种形态。
5. **Gemini 鉴权**：仅 OpenAI 兼容层可用；任何 HTTP 响应码都代表域名可达（勿把 401 当断网）。
6. **瞬态 503**：Agnes 中国站繁忙时会 503，脚本内置指数退避，可加大 `--max-retries` 重试。

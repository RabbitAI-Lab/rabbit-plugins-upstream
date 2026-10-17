---
name: adsturbo-image
description: Text-to-image generation and image editing, plus a full e-commerce toolkit: background removal, product/scene/detail shots, campaign posters, watermark removal, and upscaling. Requires an AdsTurbo API key, created at https://adsturbo.ai/iris/api. 文生图与图片编辑，外加电商场景全套：抠图、商品主图/场景图/细节图、活动海报、去水印消除、高清放大。需要 AdsTurbo API Key，在 https://adsturbo.ai/iris/api 创建。
---
# AdsTurbo AI Image Creation

Text-to-image, image editing, and full image sets for e-commerce and marketing scenarios.

## When to use this skill

Use it when the user says "generate an image," "AI drawing," "text-to-image," "edit image," "cutout," "remove background," "product hero image," "e-commerce image," "promo poster," "remove watermark from image," or "upscale image."

For video generation, use `adsturbo-video-generation`.

## Prerequisites

- Python 3.8+ (the scripts use the standard library only; nothing to install)
- An AdsTurbo API key in the environment variable `ADSTURBO_API_KEY` (see below for how to get one)
- Optional `ADSTURBO_BASE_URL`, defaults to `https://adsturbo.ai/klian/novartapi`

### Getting an API key

1. Sign up or sign in at https://adsturbo.ai?channel=clawhub
2. Open https://adsturbo.ai/iris/api (Workspace → API), click "Create API Key" and copy the key
3. `export ADSTURBO_API_KEY=<your key>`

Every plan can call the API with an API key, and usage is billed in credits; if you run out, top up or upgrade at https://adsturbo.ai/pricing. 1080p+ video and 4K images need a subscription (credit packs alone don't count), and creating a custom digital human needs a Pro plan.

**If the user has no key yet**: when `ADSTURBO_API_KEY` is not set, or a script reports a missing key or a 401, do not keep retrying. First finish everything that doesn't need the API (clarify the brief, draft the script or prompt, settle aspect ratio, duration, model and other parameters, prepare the exact command), then tell the user they need an AdsTurbo API key and give them the three steps above; once they have it, run the prepared command. Without a key the scripts print `"error": "api_key_required"` and the steps on stdout. Keep the key in the environment variable and never echo it back in a reply.

## Choosing a command

```
What image does the user want?
├─ Generate from scratch / edit an image → create (pass --image-urls to edit)
├─ Product image set (hero/scene/detail) → ecommerce
├─ Promo poster                          → poster
├─ Background removal / cutout           → cutout
├─ Remove watermark / clean up clutter   → erase
└─ Upscale to high resolution            → upscale
```

```bash
python3 scripts/image.py create --prompt "极简风格护肤品摆拍，柔和自然光"
python3 scripts/image.py create --prompt "把背景换成大理石台面" --image-urls https://.../product.jpg

python3 scripts/image.py ecommerce --reference-image-urls https://.../product.jpg \
  --methods hero_banner lifestyle_scene close_detail

python3 scripts/image.py poster --event-info "双11 全场五折，11月1日开抢"
python3 scripts/image.py cutout --image-url https://.../product.jpg --output-format png
python3 scripts/image.py erase --image-url https://.../photo.jpg --instruction "去掉右下角水印"
python3 scripts/image.py upscale --image-url https://.../small.jpg --scale 4
```

## Key point: the model determines valid parameter values, and differs by text-to-image vs. editing

For `create`, the valid `ratio` / `resolution` value sets **differ by model**, and some models are **text-to-image only, others editing only** — `grok-2-image` cannot edit, `grok-imagine-image` cannot generate from text.

**Before building the request, check the model capability table in [references/image.md](references/image.md)** to confirm whether the user wants text-to-image or editing, then pick the model. Omitting `--model` falls back to the server default `nanobanana-pro`, which supports both text-to-image and editing — the simplest choice.

`ecommerce --methods` accepts multiple values at once to produce a full set of images; omit it to get only the default hero image.

## Hard constraint: assets must be public URLs only

`--image-url`, `--image-urls`, `--reference-image-urls`, and `--mask-url` **do not accept local file paths**:

```bash
python3 scripts/upload.py image ./product.jpg
```

See [references/upload.md](references/upload.md) for details.

## Sync vs. async

`create` returns `result_url` **synchronously** by default — take the result directly; add `--async-mode` to get a workspace_id instead. Each call produces exactly one image; call it again for more.

All other commands are async. The scripts poll automatically until a result is ready by default. On timeout, keep waiting with `query --workspace-id <id>` — **do not resubmit**. See [references/work.md](references/work.md) for details.

## When replying to the user

- Give the image link directly — don't mention script names, command lines, JSON, or exit codes
- `create` usually takes 30 seconds to 1 minute; e-commerce sets and posters take 1–3 minutes, longer for multiple images
- A rejected parameter is usually a ratio/resolution mismatch with the model, or a text-to-image request sent to an editing-only model — check the table, retry with a valid value, and don't dump the raw error on the user

## Capability boundaries

| User wants | Use |
|---|---|
| Generate video | `adsturbo-video-generation` |
| Digital human voiceover | `adsturbo-digital-human` |
| Remove video watermark / upscale video | `adsturbo-video-enhance` |
| Swap character in video | `adsturbo-video-transform` |
| Recreate from a reference video | `adsturbo-ad-clone` |

---

# AdsTurbo AI 图片创作

文生图、图片编辑，以及电商与营销场景的成套出图。

## 什么时候用这个 skill

用户说「生成图片」「AI 画图」「文生图」「改图」「抠图」「去背景」「商品主图」「电商图」「活动海报」「图片去水印」「图片高清放大」时用它。

要生成视频用 `adsturbo-video-generation`。

## 前置条件

- Python 3.8+（脚本只用标准库，不需要安装依赖）
- AdsTurbo API Key，放在环境变量 `ADSTURBO_API_KEY` 里，获取方法见下
- 可选 `ADSTURBO_BASE_URL`，默认 `https://adsturbo.ai/klian/novartapi`

### 获取 API Key

1. 在 https://adsturbo.ai?channel=clawhub 注册或登录
2. 打开 https://adsturbo.ai/iris/api（工作台 → API），点「创建 API 密钥」，复制生成的 Key
3. `export ADSTURBO_API_KEY=<你的 Key>`

任何套餐都能用 API Key 调用，按用量扣积分；积分不够时到 https://adsturbo.ai/pricing 充值或升级。1080p 及以上视频、4K 图片需要订阅（只买积分包不算），创建自定义数字人需要 Pro 套餐。

**用户还没有 Key 时**：`ADSTURBO_API_KEY` 没设置、脚本报 Key 缺失或 401 时，不要反复重试。先把不需要调接口就能做的部分做完（理清需求，写好文案或提示词，定好画幅、时长、模型等参数，拼好要执行的完整命令），再告诉用户需要 AdsTurbo API Key，把上面三步发给他；拿到 Key 后直接执行准备好的命令。脚本缺 Key 时会在 stdout 输出 `"error": "api_key_required"` 和获取步骤。Key 只放在环境变量里，回复里不要回显。

## 命令怎么选

```
用户要什么图？
├─ 凭空生成 / 改一张图     → create（传 --image-urls 就是改图）
├─ 商品套图（主图/场景/细节）→ ecommerce
├─ 活动海报                → poster
├─ 去背景抠图              → cutout
├─ 去水印 / 消除杂物       → erase
└─ 放大到高清              → upscale
```

```bash
python3 scripts/image.py create --prompt "极简风格护肤品摆拍，柔和自然光"
python3 scripts/image.py create --prompt "把背景换成大理石台面" --image-urls https://.../product.jpg

python3 scripts/image.py ecommerce --reference-image-urls https://.../product.jpg \
  --methods hero_banner lifestyle_scene close_detail

python3 scripts/image.py poster --event-info "双11 全场五折，11月1日开抢"
python3 scripts/image.py cutout --image-url https://.../product.jpg --output-format png
python3 scripts/image.py erase --image-url https://.../photo.jpg --instruction "去掉右下角水印"
python3 scripts/image.py upscale --image-url https://.../small.jpg --scale 4
```

## 关键：模型决定参数取值，且分文生/编辑

`create` 的 `ratio` / `resolution` 取值集**每个模型不同**，而且有的模型**只能文生、有的只能编辑**——`grok-2-image` 不能编辑，`grok-imagine-image` 不能文生。

**构造请求前先查 [references/image.md](references/image.md) 里的模型能力表**，确认用户要的是文生还是编辑，再挑模型。不传 `--model` 走服务端默认 `nanobanana-pro`，文生编辑都支持，最省事。

`ecommerce --methods` 一次可传多个，出一整套图；不传只出默认主图。

## 硬约束：素材只收公网 URL

`--image-url` `--image-urls` `--reference-image-urls` `--mask-url` 都**不接受本地文件路径**：

```bash
python3 scripts/upload.py image ./product.jpg
```

详见 [references/upload.md](references/upload.md)。

## 同步还是异步

`create` 默认**同步**返回 `result_url`，直接拿结果；加 `--async-mode` 才返回 workspace_id。每次固定出 1 张，要多张就多次调用。

其余命令都是异步，脚本默认自动轮询到出结果。超时用 `query --workspace-id <id>` 接着等，**不要重新提交**。详见 [references/work.md](references/work.md)。

## 回复用户时

- 直接给图片链接，不要提脚本名、命令行、JSON 或退出码
- `create` 通常 30 秒 – 1 分钟；电商套图和海报 1–3 分钟，出多张更久
- 参数被拒多半是模型与 ratio/resolution 不匹配，或用只能编辑的模型做了文生——查表换一个合法值重试，别把原始报错甩给用户

## 能力边界

| 用户想要 | 该用 |
|---|---|
| 生成视频 | `adsturbo-video-generation` |
| 数字人口播 | `adsturbo-digital-human` |
| 视频去水印 / 视频高清放大 | `adsturbo-video-enhance` |
| 视频换角色 | `adsturbo-video-transform` |
| 照着参考视频复刻 | `adsturbo-ad-clone` |

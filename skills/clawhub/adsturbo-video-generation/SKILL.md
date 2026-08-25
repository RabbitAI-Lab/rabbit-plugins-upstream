---
name: adsturbo-video-generation
description: Create video from scratch: text-to-video, image-to-video, first/last-frame interpolation, multi-reference generation, plus extending and locally editing existing videos. 从零造画面：文生视频、图生视频、首尾帧补全、多参考素材生成，以及对已有视频做延长和局部编辑。
---
# AdsTurbo AI 视频生成

从零生成视频画面，以及对已有视频做延长和局部编辑。

## 什么时候用这个 skill

用户说「文生视频」「图生视频」「生成一段视频」「首尾帧」「视频延长」「续写视频」「改视频里的背景」时用它。

要让人物说话用 `adsturbo-digital-human`；要照着一条参考视频复刻用 `adsturbo-ad-clone`。

## 前置条件

- Python 3.8+，`pip install -r scripts/requirements.txt`
- 环境变量 `ADSTURBO_API_KEY`（在 https://www.adsturbo.ai 获取）
- 可选 `ADSTURBO_BASE_URL`，默认 `https://adsturbo.ai/klian/novartapi`

## 三个命令

```bash
# 文生视频
python3 scripts/video_generation.py generate --prompt "海边日落，镜头缓慢推进"

# 图生视频 / 首尾帧
python3 scripts/video_generation.py generate --prompt "产品旋转展示" \
  --start-frame https://.../product.jpg

# 延长（仅 seedance-2.0）
python3 scripts/video_generation.py extend --video-url https://.../clip.mp4 --duration 10

# 局部编辑（仅 seedance-2.0）
python3 scripts/video_generation.py edit --video-url https://.../clip.mp4 \
  --prompt "把背景换成办公室" --mask-url https://.../mask.png
```

## 关键：模型决定参数取值

`duration` / `resolution` / `ratio` / 参考素材上限**每个模型都不一样**——`veo-3.1` 只能 4/6/8 秒，`seedance-2.0` 是 4~15 秒，`grok` 不支持首尾帧。

**为用户构造请求前，先查 [references/video_generation.md](references/video_generation.md) 里的模型对照表**，指定了非默认 model 时必须逐项核对 `duration`、`ratio`、`resolution`。不传 `--model` 就走服务端默认，最省事。

`extend` 和 `edit` **只支持 `seedance-2.0`**，不要给用户推荐其他模型。

## 硬约束：素材只收公网 URL

`--start-frame` `--end-frame` `--reference-images` `--reference-videos` `--video-url` 都**不接受本地文件路径**：

```bash
python3 scripts/upload.py image ./frame.jpg
python3 scripts/upload.py file ./clip.mp4
```

详见 [references/upload.md](references/upload.md)。

## 异步任务怎么处理

三个命令都是异步的，脚本默认提交后自动轮询到出结果。

- 超时了：`query --workspace-id <id>` 接着等，**不要重新提交**——任务还在跑，重交会重复扣费
- 只想提交不等：`--no-wait`
- 重试要幂等：带上 `--idempotency-key`，同一个 key 不会重复建任务

详见 [references/work.md](references/work.md)。

## 回复用户时

- 直接给视频链接，不要提脚本名、命令行、JSON 或退出码
- 提交后说一句预计 3–8 分钟
- 参数被服务端拒了，多半是模型与 duration/ratio/resolution 不匹配——查表改一个合法值重试，别把原始报错甩给用户

## 能力边界

| 用户想要 | 该用 |
|---|---|
| 数字人口播 / 对口型 | `adsturbo-digital-human` |
| 照着参考视频复刻 | `adsturbo-ad-clone` |
| 去水印 / 4K / 字幕 | `adsturbo-video-enhance` |
| 换角色 / 翻译 / 动作控制 | `adsturbo-video-transform` |
| 生成图片 | `adsturbo-image` |

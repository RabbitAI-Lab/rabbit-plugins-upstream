---
name: adsturbo-ad-clone
description: Clone a competitor ad: auto-storyboard it into shots and prompts, then regenerate a new video with the same structure. Can also run analysis only, with no generation. 看中一条广告就照着做一条：自动拉片得出分镜与提示词，再生成同款结构的新视频。也可只做视频分析不生成。
---
# AdsTurbo 广告视频复刻

看中一条广告，照着它的结构做一条自己的。

## 什么时候用这个 skill

用户说「复刻这条视频」「照着这个拍一个」「仿制」「同款视频」「拉片」「分析这条广告」时用它。

要凭空生成不参考任何视频用 `adsturbo-video-generation`。

## 前置条件

- Python 3.8+，`pip install -r scripts/requirements.txt`
- 环境变量 `ADSTURBO_API_KEY`（在 https://www.adsturbo.ai 获取）
- 可选 `ADSTURBO_BASE_URL`，默认 `https://adsturbo.ai/klian/novartapi`

## 两步：先拉片，再复刻

```bash
# 1. 分析参考视频（同步，秒级到 2 分钟）
python3 scripts/ad_clone.py analyze --video-url https://.../reference.mp4

# 2. 用分析出的 prompt 生成新片
python3 scripts/ad_clone.py generate --prompt "<上一步的 prompt>" \
  --video-url https://.../reference.mp4 --ratio 9:16
```

**这两步必须连用**，`generate` 的 prompt 就是 `analyze` 的产出。中间可以按用户需求改几句 prompt——这是调整复刻效果最有效的地方，比反复重跑生成划算。

单个片段上限 12 秒，长视频用 `--clip-start` / `--clip-end` 先裁一段。

只想读懂一条视频、不生成，用 `inspect`。完整参数见 [references/ad_clone.md](references/ad_clone.md)。

## 硬约束：素材只收公网 URL

`--video-url` **不接受本地文件路径**：

```bash
python3 scripts/upload.py file ./reference.mp4
```

详见 [references/upload.md](references/upload.md)。

## 异步任务怎么处理

`analyze` 是同步的，直接拿结果。`generate` / `inspect` 是异步的，脚本默认自动轮询到出结果。

- 超时了：`query --workspace-id <id>` 接着等，**不要重新提交**——任务还在跑，重交会重复扣费
- 只想提交不等：`--no-wait`

详见 [references/work.md](references/work.md)。

## 回复用户时

- 直接给视频链接，不要提脚本名、命令行、JSON 或退出码
- `analyze` 出来的分镜和提示词可以讲给用户听、请他确认要不要调整，再进 `generate`
- 提交生成后说一句预计 3–10 分钟

## 能力边界

复刻出的成片常常还要再加工，那属于别的 skill：

| 用户想要 | 该用 |
|---|---|
| 把复刻结果里的人换成自己 | `adsturbo-video-transform` |
| 复刻后翻译成外语投海外 | `adsturbo-video-transform` |
| 去掉原片水印再复刻 | `adsturbo-video-enhance` |
| 不参考任何视频，凭空生成 | `adsturbo-video-generation` |
| 数字人口播 | `adsturbo-digital-human` |

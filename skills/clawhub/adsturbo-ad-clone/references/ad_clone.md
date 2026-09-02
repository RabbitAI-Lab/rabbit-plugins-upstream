# Ad Clone

Script: `scripts/ad_clone.py`

## Two steps: analyze first, then clone

```bash
# Step 1: analyze the reference video to get a prompt
python3 scripts/ad_clone.py analyze --video-url https://.../reference.mp4

# Step 2: use the analysis result to generate the new video
python3 scripts/ad_clone.py generate --prompt "<prompt returned by the previous step>" \
  --video-url https://.../reference.mp4
```

`analyze` is synchronous and returns a structured shot breakdown and prompt. Feed its prompt into `generate` as-is, or tweak a few lines first to match the user's needs — this is the most effective place to adjust the cloned result.

## analyze — video analysis (synchronous)

```bash
python3 scripts/ad_clone.py analyze --video-url https://.../ref.mp4 \
  --clip-start 3 --clip-end 15
```

- `--clip-start` / `--clip-end` trim by seconds so only that segment is analyzed
- **Each segment is capped at 12 seconds** — trim longer videos first

## generate — clone generation (asynchronous)

```bash
python3 scripts/ad_clone.py generate --prompt "..." --duration 15 --ratio 9:16
```

Passing `--video-url` with the original reference video anchors the style so the resulting clip stays closer to the source's look and feel; omit it to generate purely from the prompt.

## inspect — analysis only, no generation (asynchronous)

```bash
python3 scripts/ad_clone.py inspect --video-url https://.../any.mp4
```

Runs a shot-by-shot content analysis on any video. The difference from `analyze`: `analyze` produces a prompt **for cloning**, while `inspect` produces a **human-readable** content breakdown, suited to use cases like competitor teardown and asset archiving.

## Typical chaining

The cloned output often needs further processing, chained across skills:

```bash
# Clone → swap in your own on-screen character
python3 scripts/ad_clone.py generate --prompt "..." --no-wait
# Once you have the workspace_id, continue with adsturbo-video-transform's character-swap

# Clone → translate to English for overseas placement
# Use adsturbo-video-transform's translate --target-lang en
```

## Assets must be public URLs

`--video-url` only accepts URLs — upload local files first:

```bash
python3 scripts/upload.py file ./reference.mp4
```

## Time estimates

| Operation | Estimated time |
|---|---|
| `analyze` | 30 seconds – 2 minutes (synchronous return) |
| `generate` | 3–10 minutes |
| `inspect` | 1–3 minutes |

Asynchronous commands poll automatically by default; if it times out, use `query --workspace-id <id>` to keep waiting — the task is not lost.

---

# 广告视频复刻 / Ad Clone

脚本：`scripts/ad_clone.py`

## 两步走：先拉片，再复刻

```bash
# 第一步：分析参考视频，拿到提示词
python3 scripts/ad_clone.py analyze --video-url https://.../reference.mp4

# 第二步：用分析结果生成新视频
python3 scripts/ad_clone.py generate --prompt "<上一步返回的 prompt>" \
  --video-url https://.../reference.mp4
```

`analyze` 是同步的，返回结构化的分镜与提示词。把它的 prompt 原样喂给 `generate`，也可以先按用户的需求改几句再喂——这是调整复刻结果最有效的地方。

## analyze — 拉片（同步）

```bash
python3 scripts/ad_clone.py analyze --video-url https://.../ref.mp4 \
  --clip-start 3 --clip-end 15
```

- `--clip-start` / `--clip-end` 按秒裁剪，只分析其中一段
- **单个片段上限 12 秒**，超长视频要先裁

## generate — 复刻生成（异步）

```bash
python3 scripts/ad_clone.py generate --prompt "..." --duration 15 --ratio 9:16
```

`--video-url` 传原参考视频可以锚定风格，让成片更贴近原片质感；不传则纯按 prompt 生成。

## inspect — 只分析不生成（异步）

```bash
python3 scripts/ad_clone.py inspect --video-url https://.../any.mp4
```

对任意视频做逐镜头内容分析。跟 `analyze` 的区别：`analyze` 的产出是**为了复刻**的提示词，`inspect` 的产出是**给人读**的内容理解，适合竞品拆解、素材归档这类场景。

## 典型串联

复刻出来的成片常常还要再加工，跨 skill 串起来：

```bash
# 复刻 → 换成自己的出镜人
python3 scripts/ad_clone.py generate --prompt "..." --no-wait
# 拿到 workspace_id 后，用 adsturbo-video-transform 的 character-swap 接着处理

# 复刻 → 翻译成英文投海外
# 用 adsturbo-video-transform 的 translate --target-lang en
```

## 素材必须是公网 URL

`--video-url` 只收 URL，本地文件先传：

```bash
python3 scripts/upload.py file ./reference.mp4
```

## 耗时参考

| 操作 | 预计 |
|---|---|
| `analyze` | 30 秒 – 2 分钟（同步返回） |
| `generate` | 3–10 分钟 |
| `inspect` | 1–3 分钟 |

异步命令默认自动轮询；超时用 `query --workspace-id <id>` 续等，任务不会丢。

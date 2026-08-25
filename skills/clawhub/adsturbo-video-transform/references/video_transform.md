# 视频改造 / Video Transform

脚本：`scripts/video_transform.py`

改掉视频里的某个元素。只是让画质更好、去掉水印，属于另一个域，见 `adsturbo-video-enhance`。

## character-swap — 换掉出镜人物

```bash
python3 scripts/video_transform.py character-swap \
  --video-url https://.../original.mp4 \
  --image-url https://.../new-person.jpg
```

把视频里的人整体换成 `--image-url` 里的人，保留原有动作、镜头和场景。适合一条素材换不同代言人反复投放。

多镜头视频服务端会分镜处理再拼接。同一个人在不同镜头里换装出现时，识别难度会上升——如果发现后段镜头没换干净，把视频裁成单镜头分别处理效果更稳。

## motion-control — 用参考动作驱动人像

```bash
python3 scripts/video_transform.py motion-control \
  --video-url https://.../dance.mp4 \
  --image-url https://.../portrait.jpg \
  --keep-original-sound
```

跟 `character-swap` 的区别在输入的性质：

| | 参考视频的角色 | 图片的角色 |
|---|---|---|
| `character-swap` | 提供**画面与场景** | 提供**新的人** |
| `motion-control` | 提供**动作** | 提供**被驱动的人像** |

可选项：`--prompt` 补充画面描述、`--negative-prompt` 排除不想要的元素、`--mode` 控制模式、`--character-orientation` 人物朝向、`--keep-original-sound` 保留原声。

## translate — 视频翻译

```bash
python3 scripts/video_transform.py translate \
  --video-url https://.../clip.mp4 --target-lang en
```

重新配音成目标语言并对齐口型，不是加字幕。只要字幕的话用 `adsturbo-video-enhance` 的 `subtitle`。

`--target-lang` 传语言代码，如 `en` / `ja` / `es` / `ko`。

## 用 workspace_id 串联

三个命令都支持 `--workspace-id` 代替 `--video-url`，直接消费上一个任务的产物：

```bash
# 复刻一条广告 → 换成自家出镜人 → 翻译成英文
python3 scripts/video_transform.py character-swap --workspace-id ws_abc --image-url https://.../ceo.jpg --no-wait
python3 scripts/video_transform.py translate --workspace-id ws_def --target-lang en
```

## 素材必须是公网 URL

```bash
python3 scripts/upload.py file ./clip.mp4
python3 scripts/upload.py image ./person.jpg
```

## 耗时参考

| 操作 | 预计 |
|---|---|
| `character-swap` | 3–5 分钟 |
| `motion-control` | 3–5 分钟 |
| `translate` | 5–10 分钟 |

耗时随视频时长增长。默认自动轮询；超时用 `query --workspace-id <id>` 续等，任务不会丢。

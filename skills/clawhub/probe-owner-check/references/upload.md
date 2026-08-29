# 素材上传 / Upload

脚本：`scripts/upload.py`

## 为什么每次都要先上传

AdsTurbo 的所有生成接口，素材参数收的都是**公网可访问的 URL**，不接受本地文件路径，也不接受 base64。用户给的如果是本地文件，必须先过这一步换成 URL。

这是最容易踩的坑：直接把 `./photo.jpg` 填进 `--image-url` 一定失败。

## 三个命令

```bash
python3 scripts/upload.py image ./portrait.jpg     # 图片
python3 scripts/upload.py audio ./voice.mp3        # 音频，不转码
python3 scripts/upload.py file  ./clip.mp4         # 视频及其他任意文件
```

返回体里带上传后的 URL，直接拿去填下一个命令的素材参数。

| 命令 | 用途 | 典型下游 |
|---|---|---|
| `image` | 人像、商品图、参考图、首尾帧、mask | `--photo-url` `--image-url` `--start-frame` `--reference-images` `--mask-url` |
| `audio` | 配音、声音克隆样本 | `--audio-url` `--voice-audio-url` `--said-url` |
| `file` | 视频素材 | `--video-url` `--reference-videos` |

音频走 `audio` 而不是 `file`——`audio` 这条是原样存储不转码，能保住声音克隆需要的音质。

## 已经是 URL 就别上传

用户给的素材如果本来就是公网链接（比如商品详情页的图、CDN 上的视频），直接用，不用下载下来再传一遍。

## 典型串联

```bash
# 本地照片 + 本地录音 → 专属数字人口播
PHOTO=$(python3 scripts/upload.py image ./me.jpg)
VOICE=$(python3 scripts/upload.py audio ./sample.mp3)
# 从返回 JSON 里取出 url 字段，填进下一步
python3 scripts/digital_human.py persona-create --photo-url <url> --voice-audio-url <url>
```

## 限制

- 走 `multipart/form-data`，鉴权与其他接口一致（`Authorization: Bearer <API Key>`）
- 大文件上传较慢，客户端超时设为 300 秒
- 文件不存在会直接报错，不会发出无效请求

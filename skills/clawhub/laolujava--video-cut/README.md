# video-cut

> 用自然语言驱动的本地视频剪辑 Skill，专为AI设计。

---

## 它解决什么问题

录完视频之后，最花时间的往往不是拍摄本身，而是后期里那些机械性的操作：

- 一遍遍听音频、找「嗯」「呃」「啊」，手动标记再删除
- 把字幕时间轴对齐到剪辑后的新版本
- 给竖屏视频套个好看的背景再发平台
- iPhone 拍出来的 HDR 视频在普通屏幕上一片惨白

video-cut 把这些都接管了。你只需要说一句话，它完成后交给你一个可以直接发布的 MP4。

---

## 工作原理

```
原始视频
   │
   ├─ find_fillers.py ──► 逐词转写（tokenra.io Whisper API 或本地模型）
   │                        └─ words.json（每个词的开始/结束时间）
   │
   ├─ AI 审核候选语气词，确定剪切边界，写入 plan.json
   │
   ├─ verify_plan.py ──► 渲染前校验：每刀都落在词间隙，正文字符数不变
   │
   └─ cut_video.py ──► 一次渲染：剪辑 + 曝光修正 + 倍速 + 背景 + 字幕
                         └─ 成品 MP4 + SRT
```

整个过程在本机完成。转写阶段调用外部 API（发送音频分块），视频本身不离开本机。

---

## 功能

### 去停顿词

识别「嗯、呃、啊、额、唉」及英文 um / uh / hmm，每处候选都经过人工确认再下刀，剪完重新转写校验——正文字符数必须与原片一致才算通过。

**转写接入方式：**

推荐使用 [tokenra.io](https://tokenra.io) 的免费 API Key，无需在本机安装任何模型：

```sh
python scripts/find_fillers.py 讲解.mp4 words.json \
  --api-key sk-xxxxxxxx \
  --language zh
```

也支持本地 Whisper 模型（需要 PyTorch + openai-whisper）：

```sh
python scripts/find_fillers.py 讲解.mp4 words.json \
  --model ~/.cache/whisper/small.pt \
  --language zh
```

长视频转写可以断点续传——中断后重跑会自动跳过已完成的分块。

### 字幕

- 输出与剪辑后音频严格对齐的 SRT 文件
- 可选将字幕烧录进画面，6 种风格：

| 参数值 | 外观 |
|---|---|
| `box`（默认） | 白字 + 半透明暗底框 |
| `white-box` | 深色字 + 白底框 |
| `yellow-box` | 深色字 + 黄底框 |
| `outline` | 白字 + 黑色描边，无底框 |
| `yellow-outline` | 黄字 + 黑色描边，综艺感 |
| `shadow` | 白字 + 细描边 + 柔和投影 |

- 支持传入任意 TTF / OTF / TTC 字体；烧录前自动检查缺字，避免出现方框

### 背景装饰

画面缩成圆角卡片，四周填充背景，适合竖屏发抖音 / 小红书：

```sh
--background sunset        # 橙紫渐变
--background spring        # 绿黄渐变
--background ocean         # 蓝色渐变
--background dusk          # 深紫渐变
--background random        # 随机选一种
--background '#1a1a2e'     # 自定义颜色
--background /path/to/wallpaper.jpg  # 本地图片
--background blur          # 画面自身虚化填充
```

`--padding` 和 `--radius` 分别控制卡片边距和圆角半径（单位：短边百分比）。

### iPhone 过曝修正

iPhone 开启 HDR 拍摄的视频（HLG 格式）在普通屏幕上会偏白过亮。传入后自动转换成正常色调的 SDR 视频，可用 `--hlg-strength` 微调高光压制力度（默认 2.6，越小越暗）。

### 倍速

0.5 到 5 倍之间任意设定（支持分数如 `4/3`）：

- 音调保持不变（FFmpeg atempo 分级处理）
- 字幕时间轴自动按速比缩放
- SRT 输出已对应加速后的时间轴

### 片段裁剪与重排

- 按时间（「去掉前 10 秒」「只保留 1:30 到 3:00」）或画面描述定位片段
- 把指定台词挪到视频开头作为钩子（「把『三个月从零到上线』挪到片头」）

### 安全机制

- 每次输出新文件，原素材从不被覆盖
- 渲染前强制过 verify_plan.py 校验，确认没有误剪正文
- 渲染后完整解码一遍成品，校验帧数和音频时长
- 输出文件不带原始元数据（GPS、拍摄设备信息等）

---

## 适合处理的素材

| 素材类型 | 支持情况 |
|---|---|
| 单机位口播、讲解视频 | ✅ |
| 录屏 + 旁白（教程、演示） | ✅ |
| iPhone 拍摄（含 HDR） | ✅ |
| 中文语音 | ✅ |
| 英文语音 | ✅（去停顿词同样有效） |
| 多机位素材拼接 | ❌ |
| Dolby Vision / HDR10（PQ）素材 | ❌ |
| 需要输出 HDR | ❌ |
| 多语言混合的停顿词识别 | ❌ |

---

## 依赖

| 工具 | 用途 | 状态 |
|---|---|---|
| Python 3.10+ | 运行所有脚本 | 必须 |
| FFmpeg 4.4+ | 视频编解码 | 必须 |
| NumPy | 音频处理 | 必须（`pip install numpy`） |
| Pillow | 字幕图层、背景合成 | 必须（`pip install pillow`） |
| tokenra.io API Key | 云端转写（推荐） | 二选一 |
| openai-whisper + PyTorch | 本地转写 | 二选一 |

---

## 快速开始

```sh
# 1. 在 tokenra.io 注册，获取免费 API Key

# 2. 转写（生成逐词时间戳）
python scripts/find_fillers.py 我的视频.mp4 words.json \
  --api-key sk-xxxxxxxx --language zh

# 3. AI 确认语气词候选后，校验剪辑方案
python scripts/verify_plan.py words.json plan.json

# 4. 渲染成片（以微软雅黑为例，Windows）
cd scripts && PYTHONPATH=. python cut_video.py \
  我的视频.mp4 plan.json 成品.mp4 \
  --source-srt source.srt \
  --burn-font C:/Windows/Fonts/msyh.ttc --font-index 0
```

---

## 协议

[AGPL-3.0](LICENSE) — 可免费使用和修改；若将修改版本作为网络服务提供给他人，需公开源码。

---
name: image-process
agent_created: true
description: 图片处理小工具——改尺寸、转格式(WebP/PNG/JPG)、自动裁白边、生成缩略图、压缩优化体积、生成社交分享图(OG图)、批量处理整个文件夹、去背景（抠图）。基于 Pillow，纯本地运行，不上传任何图片。当用户说"压缩图片""图片太大了""转成webp""把png转jpg""改图片尺寸""缩小图片""裁掉白边""logo去白底""做缩略图""生成分享图""做一张OG图""批量处理图片""批量转webp""优化网站图片""去背景""抠图""去掉背景""背景透明"等任何图片处理需求时触发。适合公众号配图、网站素材、产品图等日常图片整理。**不要 undertrigger**——用户提图片处理就该用本技能，而不是手写 Python。
---

# 图片处理小工具（image-process）

让 Agent 用一条命令帮你把图片改尺寸、转格式、压体积、裁白边、做缩略图、生成分享图、批量处理。全部在本地完成，**图片不会上传到任何服务器**，隐私安全。

本技能自带脚本 `scripts/img_process.py`，Agent 直接用 Python 运行它即可，不需要每次现写代码。

---

## 一、安装（很简单，照做就行）

这个技能只需要一个叫 **Pillow** 的 Python 图片库。安装分两步，全程只要复制粘贴一条命令。

### 第 1 步：确认电脑有 Python
- **Windows**：按 `Win + R`，输入 `cmd` 回车，在黑窗口里输入 `python --version` 并回车。
  - 如果显示类似 `Python 3.11.0` 的字样 → 已经有了，跳到第 2 步。
  - 如果提示"不是内部或外部命令" → 去 [python.org](https://www.python.org/downloads/) 下载安装，**安装时务必勾选 "Add Python to PATH"**（添加到环境变量），然后重开命令行。
- **macOS / Linux**：一般自带 Python，同样用 `python3 --version` 确认。

### 第 2 步：安装 Pillow（只需一次）
在命令行里输入下面这行，回车：

```bash
pip install Pillow
```

看到 `Successfully installed Pillow-...` 就成功了。**以后每次用本技能都不用再装**，这一步只做一次。

### 第 3 步（可选）：只有"去背景"功能才需要装 rembg
如果你只用改尺寸、转格式、裁白边、缩略图、压缩、分享图、批量——**第 1、2 步就够了，不用装这个**。
只有用到"去背景（抠图）"时，才需要再装一个 `rembg`：

```bash
pip install rembg
```

装好后**第一次**用去背景功能，会联网自动下载约 176MB 的模型文件（只需下载一次，之后完全离线可用）。下载时请保持联网、耐心等一会儿。

---

## 二、怎么用（Agent 执行方式）

Agent 运行本技能自带的脚本即可，命令格式：

```bash
python "<技能目录>/scripts/img_process.py" <功能> <图片路径> [参数]
```

各功能与示例见下方。下面所有示例都假设脚本路径已正确指向本技能的 `scripts/img_process.py`。

---

## 三、功能清单与示例

### 1. 改尺寸（resize）
只给宽度或高度时，自动按比例缩放，图片不会变形。
```bash
# 把宽度改成 1080，高度自动按比例
python img_process.py resize 封面.jpg --width 1080

# 同时指定宽和高（会拉伸，慎用）
python img_process.py resize 图.png --width 800 --height 600
```

### 2. 转换格式（convert）
常用：把 PNG 转 WebP（体积更小）、把带透明的 PNG 转 JPG（会垫白底）。
```bash
# 转成 WebP（网站首选，体积小）
python img_process.py convert logo.png --format webp

# 转成 JPG，并控制画质
python img_process.py convert 图.png --format jpg --quality 90
```

### 3. 自动裁白边（trim）
适合处理 logo：自动识别内容边界，把四周空白/透明边裁掉。
```bash
# 裁掉白边
python img_process.py trim logo原图.png

# 裁掉后留 10 像素边距
python img_process.py trim logo原图.png --padding 10
```

### 4. 生成缩略图（thumbnail）
限制最长边，比如做成 200 像素的小图。
```bash
python img_process.py thumbnail 照片.jpg --size 200
```

### 5. 压缩优化（optimise）
把大图压小，默认输出 WebP，最适合放网站/公众号。
```bash
# 宽度不超过 1920，画质 85，输出 WebP
python img_process.py optimise 大图.jpg --max-width 1920 --quality 85
```

### 6. 生成社交分享图（og-card）
生成 1200×630 的分享图（公众号/网站转发时显示的那种大图）。
```bash
# 纯色底 + 标题 + 副标题
python img_process.py og-card --title "我的文章标题" --subtitle "一句副标题" -o og.png

# 用一张图片做底图
python img_process.py og-card --title "标题" --background 底图.jpg -o og.png
```

### 7. 批量处理（batch）
一次性处理整个文件夹，省时省力。
```bash
# 整个文件夹转 WebP
python img_process.py batch ./原始图片 --action convert --format webp -o ./优化后

# 整个文件夹缩小到宽度 800
python img_process.py batch ./照片 --action resize --width 800 -o ./缩略图
```

### 8. 去背景（remove-bg）
把图片里的主体从背景中抠出来，输出**带透明背景**的 PNG（可以直接放到任何底图上）。
```bash
# 给一张图去背景，输出 xxx_nobg.png
python img_process.py remove-bg 产品图.jpg

# 指定输出路径
python img_process.py remove-bg 人像.png -o 人像_透明.png
```
> 需要第 3 步的 `rembg`（首次会下载模型）。适合：产品图换底色、人像做贴纸、把 logo 从复杂背景里抠出来。

---

## 四、常见场景对照

| 你想做的事 | 用哪个功能 | 示例 |
|---|---|---|
| 公众号封面改 1080 宽 | resize | `resize 封面.jpg --width 1080` |
| 网站图片压体积 | optimise | `optimise 大图.jpg --max-width 1920` |
| PNG 转 WebP 省流量 | convert | `convert 图.png --format webp` |
| logo 去白底 | trim | `trim logo.png --padding 10` |
| 做头像/小图 | thumbnail | `thumbnail 照.jpg --size 200` |
| 转发分享大图 | og-card | `og-card --title "标题"` |
| 一堆图统一处理 | batch | `batch ./图 --action convert --format webp -o ./out` |
| 去背景/抠图 | remove-bg | `remove-bg 产品图.jpg` |

---

## 五、注意事项（普通人也要知道）

- **不会覆盖原图**：单个功能输出时，默认在新文件名后加 `_resized`、`_trimmed` 等后缀，原图安全。批量处理请指定一个**新的输出文件夹**。
- **JPG 没有透明**：把 PNG（带透明）转 JPG 时，透明部分会自动变成白色底，这是图片格式本身限制，不是 bug。
- **WebP 最省空间**：放网站和公众号优先用 WebP，体积通常只有 PNG/JPG 的一半，加载更快。
- **画质参数**：`--quality` 越小体积越小、越模糊（一般 80–90 够用）。
- 所有处理都在你本机完成，图片不会上传任何地方。

---

## 六、来源与适配说明

- 改编自 GitHub 开源项目 `jezweb/claude-skills` 的 `image-processing` 技能（Apache-2.0 类开源协议）。
- 本版本针对 WorkBuddy 做了：全中文说明、普通人能懂的安装指引、自包含单文件脚本（无需手动写代码）、输出默认不覆盖原图。

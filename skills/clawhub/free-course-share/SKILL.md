---
name: free-course-share
description: 小红书"免费课程/证书"笔记生产 skill。Python 脚本实现 3 个自动化环节：截图两列拼图(stitch.py)、证书敏感信息打码(redact.py，中文OCR定位+嵌入图同步修复+验证图输出)、3:4 竖版封面生成(cover_vertical.py)。筛课清单/文案模板/发布 checklist 以文档形式提供(SKILL.md 与 references/)。
metadata:
  openclaw:
    requires:
      bins:
        - python3
        - tesseract
---

# 免费课程分享笔记工作流（小红书 · 公开版）

> **语言说明**：本 skill 面向中文内容平台（小红书）的中文创作者，文档与脚本 CLI 输出为简体中文，属目标受众定位而非语言限制；`redact.py` 依赖 chi_sim 中文 OCR 语言包是打码功能的**功能性依赖**（识别证书上的中文姓名），与界面语言无关。如需英文版文档欢迎提 issue。

服务场景：把免费课程/证书做成小红书笔记的完整生产流水线。
脚本自动化素材生产（拼图 + 打码 + 竖版封面），文档沉淀方法论与文案模板。

## 环境准备（一次性）

**推荐 venv 隔离安装**（避免污染系统 Python）：

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install \
    pillow==12.1.0 \
    numpy==2.3.5 \
    opencv-python-headless==4.13.0.92 \
    pytesseract==0.3.13
```

**OCR 中文包（系统级，按平台二选一）**：

```bash
# macOS（Homebrew，无需管理员权限）
brew install tesseract tesseract-lang

# Linux（Debian/Ubuntu）：OCR 中文包是系统级安装（数据装在系统目录），
# 需以管理员权限的终端执行一次——这是本 skill 唯一的管理员动作，仅用于装
# OCR 系统包，skill 运行时零特权
apt-get install -y tesseract-ocr tesseract-ocr-chi-sim
```

> 版本号与 2026-09 release 测试一致（macOS Apple Silicon / Python 3.13 与 Linux 均兼容）；升级前请看脚本 docstring 的兼容性说明。
> WorkBuddy 环境：把依赖装进 `~/.workbuddy/binaries/python/envs/default` 这个 venv，调用脚本时用该 venv 的 python 绝对路径。

## 与其他小红书 skill 的分工

本 skill 是「免费课程/证书」赛道的**专门化流水线**，与通用类 skill 的边界：

| 场景 | 用哪个 |
|------|--------|
| 免费课程/证书笔记全流程（筛课→拼图→打码→封面→文案→发布） | **本 skill** |
| 其他赛道笔记的通用生产流程 | xiaohongshu-content-workflow |
| 需要按爆款视觉规律定制封面（非模板化） | xiaohongshu-cover |
| 流程图/对比图/分支图等强逻辑配图 | xiaohongshu-logic-image |
| 发布前违禁词检查 | multi-wordcheck（本 skill Step 5 已接入） |

封面取舍：本 skill 的 `cover_vertical.py` 是**模板化快速出图**（参数固定、结构稳定、秒级出图），适合"免费证书攻略"这类结构稳定的系列笔记；需要更多视觉创意时用 xiaohongshu-cover。

## 隐私与同意（发布前必读）

证书截图可能含**姓名、邮箱、员工编号、CPE 积分账号、Registry ID、登录账号**等个人/账户关联信息。本 skill 的打码脚本 `redact.py` 是**辅助**而非**保证**：

- **OCR 不完美**：艺术字、低清字符、特殊字体可能识别失败 → 打码框偏移或漏字
- **嵌入缩略图**：封面/配图里的证书缩略图经缩放/插值后边缘可能露字
- **元数据残留**：PNG EXIF、文件名路径、URL 参数里的个人信息脚本不会清理

**所以强制要求**：
1. **每张成品图发布前人眼确认打码到位**（脚本会输出验证裁剪图，逐张放大确认）
2. **不确定能否完全打码时，宁可不用真证书**：用裁剪到不含姓名/ID 的局部图，或用课程官方提供的脱敏示例图替代
3. **公司/机构证书**常有保密/分发限制条款，发布前确认自己有发布权限
4. **不要发布他人证书**：只发自己名下、且有权分享的

## 流程总览

### Step 1 · 筛课（先判断值不值得发）
读 `references/course-screening.md` 的 8 项验证清单 + 品牌分级 + 打分表。
先核"是否真免费、无订阅墙"，再查时长、证书可挂 LinkedIn 等核心价值项；
时效信息（截止/改版）单独加分。结论：**发 / 缓发 / 不发**，各给一句话理由。

### Step 2 · 素材拼图
用户跑完课程后把截图发来（大纲页、quiz、证书页等），统一放在一个目录（如 `uploads/`）。
**顺序按文件名序号排**：`Clipboard_Screenshot.png` → `-1.png` → `-2.png` …
不要按目录名或 mtime 排。

默认**两列**布局（手机可读，勿横排拉宽）：

```bash
python3 {baseDir}/scripts/stitch.py two-col 图1 图2 ... -o /workspace/第N章quiz拼图.png
```

3张→左2右1；5张→左3右2（左侧 ceil(n/2) 张）。背景自动检测（深界面→深底，白底→白底）。

### Step 2.5 · 敏感信息打码（发布前必做）
证书上的姓名、工号、邮箱等个人信息必须打码。用脚本一条龙（中文OCR定位 → 马赛克 → 嵌入缩略图同步修复 → 自动出验证图）：

```bash
python3 {baseDir}/scripts/redact.py \
  --src 证书原图.png --text "张三" \
  --targets 封面.png 配图-实拍页.png \
  --out /workspace/证书-打码.png --target-out /workspace/ \
  --verify-dir /tmp/redact_verify
```

要点（踩坑总结，别跳步）：
1. **中文定位必须用 chi_sim**——eng OCR 对中文输出乱码坐标，是打码打偏的最常见根因
2. 嵌在封面/配图里的**缩略图**不要重做整图：脚本用"模板匹配粗定位 + MSE 网格精搜（scale 和 offset 都要精调）"求出嵌入变换后局部贴片修复；按比例手工估算坐标必错
3. OCR 认不出（艺术字/低清/错字）→ 脚本会自动模糊兜底（前 n-1 字命中+框右扩 1 字宽）并提示，仍失败再 `--box x1,y1,x2,y2` 手动兜底
4. **所有含证书的成品图都要进 `--targets`**——包括 Step 2 的拼图，只打码源图和封面、漏掉拼图是姓名泄露的高发路径
5. 交付前**必须看脚本输出的验证裁剪图**，确认框只盖住目标文字再发布
6. 清除历史打错的内容用 `--clean-box`（从干净源图取贴片还原）

### Step 3 · 封面（3:4 竖版 1080×1440）
按主体截图底色选主题：深色界面截图→`--theme dark`；白底 quiz→`--theme light`。

```bash
python3 {baseDir}/scripts/cover_vertical.py \
  --out /workspace/笔记封面.png \
  --theme dark|light \
  --top-badge "品牌名|色" \
  --badges "标签1" "标签2" \
  --title "主标题" \
  --sub "副标题" \
  --body 主体图.png \
  --points "大字|小字" ... \
  --warn "警示1" "警示2" \
  --cta "底部引导语"
```

**硬性要求**：封面与笔记标题中的时长数字必须一致。

### Step 4 · 文案初稿
标题公式：`白嫖 + 大厂/名校名 + 具体时长 + 拿证 + 附加钩子`
例：`白嫖微软✅LinkedIn联名AI证书 4h直接挂简历`

正文结构：
1. 钩子句（1-2行，白嫖 + 官方 + 谁背书）
2. 这是什么（品牌、几门课、时长、免费程度）
3. 保姆级步骤（编号 5 步内：注册→进路径→学→测验→领证挂档案）
4. 大纲速览（表或一行一个）
5. 紧迫/稀缺提醒
6. 标签

### Step 5 · 交付
产物：筛课结论 + 拼图 + 封面 + 文案 + 发布 checklist。
checklist 通用项：
1. **违禁词扫描（先于一切发布动作）**：文案初稿整体过一遍 multi-wordcheck skill（覆盖公众号/小红书/抖音审核标准），按标记替换后再定稿
2. 按目标账号活跃时段发布
3. 发布后置顶评论（放短链+引导）
4. 预备问答（注册门槛、语言、时效类高频问题）
5. 数据观察点（点击率看封面+标题，互动率看评论区问答）

## 通用踩坑原则

1. **证书 > 徽章**：标题优先用"证书/认证"
2. **答案/测验截图放评论区**，不放正文（防限流+促互动）
3. **标题与封面时长一致**
4. 小众品牌慎发；优先微软/Google/名校
5. 一切以"自己走一遍流程"为准，素材截图=最强信任状
6. 政策随时变：发文前自核
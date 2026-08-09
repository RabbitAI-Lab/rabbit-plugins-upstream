---
name: xhs-content-creator
description: 小红书图文自动发布端到端 skill。流程：飞书 DM 收图 → agent 分析图片氛围 → 按「内容创作宪法」生成标题（≤20 字，关键词前置）/ 正文（300-800 字，3-5 段）/ 话题（2-5 个精准 # 标签）→ 写 my_content.json → 调用 scripts/generate_and_publish.py 跑发布（draft 默认，draft 模式点击「保存草稿」落到服务端草稿箱，手机端同步可见）。云端执行：Xvfb + Playwright + 持久化 Chromium profile + 二维码飞书接管 + 登录缓存 + audit 日志。完全自包含，所有路径基于 __file__ 推导。
---

# xhs-content-creator

把几张图变成一篇小红书笔记（草稿或真发）。本 skill 是端到端实现 — 收图、内容生成、协议转换、浏览器自动化发布，全在一个 skill 目录下。

## 1. 收图 + 生成文案（agent 负责）

### 触发场景
- 用户在飞书 DM 发完几张图片后输入"发小红书"（或"发小红书草稿"）
- 一次性内容创作（不适用于批量或定时发布）

### 流程
1. **收图**：从飞书消息上下文拿到图片路径（已自动下载到 `~/.openclaw/media/inbound/`，文件名形如 `*.jpg`）
2. **分析图**：用 `image` 工具分析每张图（地点 / 氛围 / 主体 / 时间），输出 1-3 句氛围描述
3. **生成文案**（按 §1.5 内容创作宪法）：
   - **标题**：`{emoji}{核心关键词}{｜}{氛围短语}`，**整段 ≤20 字**（小红书规则，emoji 算 2 字符）。**核心关键词前置**便于搜索；**避免标题党 / 极限词 / 夸张承诺**（禁用词表见 §1.5 标题段）
   - **正文**：**300-800 字 + 3-5 个短段 + 不要只写摘要**。结构参考：
     - 第 1 段：场景引入（"绕了半个 X，就为 Y"）
     - 第 2 段：环境描述（光线、色彩、空气）
     - 第 3 段：动作/节奏（散步 / 拍照 / 等待）
     - 第 4 段：内心独白
     - 第 5 段：金句收尾（"X 难得的、Y 的地方"）
   - **话题**：**2-5 个精准话题**，以 `#` 开头，多个用空格或换行分隔。组合维度：地点 + 氛围 + 季节 + 城市/地域 + 摄影 + 周末/假期等
4. **图序**：封面图（最强氛围，**承担点击理由**）→ 细节图 → 收尾图。**agent 决定，不让用户选**。图片要求：**1-9 张 / 竖图 3:4 推荐 / 清晰无水印**
5. **合规预检**（按 §1.5 合规段）：发布前过一遍 — 是否有侵权搬运 / 站外导流 / 虚假夸大 / 伪科学 / 收益疗效承诺 / 敏感信息
6. **调用 `scripts/generate_and_publish.py`** 传参：图片路径列表 + 标题 + 正文 + 话题 + mode（默认 draft）
7. **回报**：脚本输出 run_id + status，agent 把链接/状态回报给用户

### 硬约束

| 约束 | 原因 | 违反后果 |
|---|---|---|
| 标题 ≤20 字（含 emoji） | 小红书前端字数限制 | 发布按钮被禁用，submit 静默失败 |
| 标题核心关键词前置 | 小红书搜索/推荐机制 | 流量差，用户搜不到 |
| 正文 300-800 字 | 小红书普通图文最佳长度区间 | 太短被算法降权；太长读者跳出 |
| 正文 3-5 段 | 阅读节奏友好 | 单段大块劝退 |
| 正文主题 + 位置前置 | 读者一眼知道主题和位置 | 抽象开头导致跳出 / 无地名读者找不到图 |
| 话题 2-5 个精准 # | 精准标签机制 | 太多稀释，太少不显 |
| 图片 1-9 张 | 小红书发布页最多 9 张缩略图 | 第 10 张起被忽略 |
| 图片 ≤5MB / 张 | 小红书上传接口限制 | 上传失败 |
| 首图承担点击理由 | 信息流点击决策主要由首图驱动 | 流量差 |
| 推荐竖图 3:4 | 小红书信息流主版式 | 横图/方图被裁切，首图效果差 |
| 图片清晰无水印 | 平台去重机制 + 用户体验 | 限流 / 被降权 / 举报 |
| 默认 mode=draft | 用户希望登录后手动点发布 | 误发布不可逆 |
| 自动化原则：脚本先校验内容对象再进浏览器 | 失败早暴露，不污染发布链路 | 浪费一次扫码会话 |

## 1.5 内容创作宪法

### 标题

- **字数**：≤20 字（含 emoji，emoji 按 2 字符算）
- **核心关键词前置**：地点 / 主体 / 季节等关键词必须出现在前 8 字内，便于搜索匹配
- **避免标题党**：不悬疑、不夸张、不制造焦虑
- **避免极限词**：禁用「最」「第一」「必」「100%」「唯一」「独家」「全网最低」「史上最强」「国家 XX」「第 N 代」「万人疯抢」「一抢而空」等
- **避免夸张承诺**：不写「X 天 X 元」「包 X」「保证 X」「立省 X」「错过等 N 年」
- **避免站外导流**：不写「私信」「微信」「+V」「vx」「公众号」「小红书号」

### 正文

- **长度**：普通图文 300-800 字。短于 300 字易被算法降权；长于 800 字读者跳出
- **结构**：3-5 个短段（不是 1-2 个大段，也不是 10 个碎段）
- **不要只写摘要**：正文必须包含「氛围 / 故事 / 细节 / 内心独白」，不能只写「标题复述 + 关键词堆砌」
- **主题 + 位置前置**（2026-08-04 实战经验）：开头 1-2 句就讲清「主题」和「位置」——什么主题（不要抽象词如「另一面 / 被遗忘的远方」开头）、在哪里拍的（具体地名：水库 / 塔 / 亭子 / 绿道 / 公园等），让读者一眼定位
- **每个场景必带地名**：湖 / 塔 / 亭子 / 绿道 / 水库 / 街道等地名必须出现在正文里，让读者知道「图在哪里拍的」
- **emoji 适量**：每段最多 1-2 个，全文不超过 5 个
- **关键词自然出现**：标题关键词在正文里要自然出现 1-2 次（搜索引擎友好）

### 话题

- **数量**：2-5 个精准话题（不是 5-7 个，**宁可少而精**）
- **格式**：以 `#` 开头（小红书识别需要）
- **分隔**：多个话题用空格或换行分隔
- **组合维度**：
  - **地点类**（强）：具体地名 / 商圈 / 公园
  - **氛围类**（中）：治愈 / 氛围感 / 慢生活
  - **季节 / 时令类**（中）：夏日 / 秋日 / 周末
  - **品类类**（弱）：摄影 / 散步 / 探店
- **避免泛词**：「日常」「分享」「生活」等太泛的标签不带流量

### 图片

- **数量**：1-9 张（实际推荐 3-6 张，单图过少算法降权，过多读者疲劳）
- **首图**：**承担点击理由**，必须是最强氛围的那张；标题与首图互相呼应
- **构图**：**推荐竖图 3:4**（小红书信息流主版式）；横图会被裁切，方图会被加白边
- **清晰度**：原图直出，无裁切关键内容；避免过度滤镜
- **无水印**：不带任何平台水印、日期水印、二维码
- **统一性**：多图色调、风格、主体协调（不要一会儿夕阳一会儿夜景一会儿静物）

### 合规（红线，违反可被限流 / 删帖 / 封号）

- **不侵权搬运**：不搬运他人原创图（小红书有图片指纹系统）、不搬运公众号 / 微博 / ins 别人的内容
- **不站外导流**：不写「加微信」「+V」「私信我」「看主页」「小红书号 XXX」诱导站外
- **不虚假夸大**：不用「神药」「神器」「神级」「一用就 X」「永不 X」等夸张承诺
- **不伪科学**：不编造数据、不挂靠权威（如「专家说」「研究表明」无出处）
- **不收益 / 疗效承诺**：不写「X 天赚 X」「保证 X 收益」「吃 X 治 X」「用 X 瘦 X」
- **不涉敏感**：避开政治、宗教、时政、社会事件、医疗诊断、奢侈品炫富等敏感品类
- **不违规品类**：医美 / 医疗 / 金融 / 教育（K12）/ 二类电商 / 烟酒等需特殊资质的品类需先确认账号有相关权限

### 自动化原则

- **先校验再发布**：`scripts/generate_and_publish.py` 在调 `publish_xhs.py` 前会做客户端校验（标题 ≤20 字 / 图片数 ≤9 / 文件存在），校验失败立即返回 `status=error` 不进入浏览器
- **服务端校验**：`src/content_validator.py` 在 publisher 启动时再校验一次（mode 合法 / images 扩展名 / publish 模式 ≥1 张图 / title ≤80 / body ≤2000）
- **失败可追**：`src/audit.py` 每次执行都会保留：
  - `actions.jsonl` — 行为日志
  - `result.json` — 最终结果（含 `status` / `error` / `error_type`）
  - `content.normalized.json` — 归一化后的内容
  - `screenshots/*.png` — 关键步骤截图
  - `dom/*.html` — DOM 快照
- **失败不破坏会话**：任何步骤异常都被 `try/except` 捕获，写入 `result.json` 后退出，不污染登录态

## 2. 云端发布（Xvfb + Playwright）

### 适用场景
- 在 Linux 云服务器上跑小红书图文草稿/发布
- 需要人工扫码接管登录
- 需要持久化浏览器 profile
- 需要截图、日志、DOM 快照
- 需要把标准化部署交给 agent 执行

**不适合**：绕过验证码 / 滑块 / 人机验证；批量互动、点赞、评论；操作未授权账号。

### 关键模块（`src/`）
- `publisher.py`（700+ 行）：核心发布逻辑（XhsPublisher.run）— draft 模式会点「保存草稿」写入服务端草稿箱
- `content_validator.py`：内容校验（标题字数、图片存在性、模式合法）
- `duplicate_guard.py`：重复发布保护（默认 30 分钟间隔）
- `login_state.py`：登录缓存（默认 6 小时）
- `browser_session.py`：持久化 Chromium profile + Playwright
- `human_behavior.py`：人类行为模拟（避免反爬）
- `locator_utils.py`：DOM 定位工具
- `audit.py`：审计日志（每个 run 写 actions.jsonl）
- `cloud_notify.py`：飞书通知（login_qr.payload.json）

### draft 模式的正确语义（重要）
- **不是**「填完表单后什么都不做」——表单数据是浏览器内的，关浏览器就丢
- **是**「填完表单后点 web 创作者后台的「保存草稿」按钮」——内容才会进服务端草稿箱，手机 app「草稿」tab 同步可见
- 实现位置：`src/publisher.py::XhsPublisher.save_draft_and_wait`（状态：`draft_persisted` / `draft_clicked_unconfirmed` / `draft_save_failed`）
- 失败信号：DOM 探测「已保存到草稿」toast / URL 跳转离开 `/publish/publish`
- 选择器：`config/selectors.json::save_draft_button_any`（仅匹配保存草稿，绝不误触发「发布」按钮）

### 部署分层

**系统级**（整台机器，影响 OpenClaw service）：
- `python3` / `python3-venv` / `python3-pip`
- `xvfb`（虚拟显示）
- 浏览器运行依赖
- OpenClaw systemd `MemoryMax ≥ 2.4G`（绕开 Xvfb+Chromium cgroup OOM，2026-08-03 踩过坑）

**项目级**（skill 目录内）：
- `.venv` + Python 依赖 + Playwright Chromium
- `runtime/{browser-profile,runs,lobster-notify,inbound}/`

### 默认链路（登录接管）
1. Agent 打开小红书登录页
2. Agent 截出二维码图片
3. 项目生成 `runtime/lobster-notify/<run_id>/login_qr.payload.json`
4. Agent 读取 payload（无需依赖 `XHS_PUBLIC_RUNTIME_BASE_URL`）
5. Agent 把二维码图片发到飞书群
6. 用户扫码
7. Agent 继续执行

### 运行产物
每次执行在 `runtime/runs/<timestamp>/` 写入：
- `actions.jsonl` — 行为日志
- `result.json` — 最终结果
- `content.normalized.json` — 归一化后的内容
- `screenshots/*.png` — 关键步骤截图
- `dom/*.html` — DOM 快照

### 环境变量
- `MODE=draft|publish`（agent 通过命令行覆盖）
- `LOGIN_TIMEOUT=300`（默认 5 分钟扫码超时）
- `PYTHON_BIN`（默认 `${PROJECT_ROOT}/.venv/bin/python`，可被覆盖）

> ⚠️ `.env` 文件当前只含 `MODE` 和 `LOGIN_TIMEOUT`，**不存 cookie / session token**。但保留 `.env` 在 skill 目录外以避免误提交到 git。

## 3. 调用链

```
agent (LLM)
  ↓ python3 scripts/generate_and_publish.py --image … --title … --body … --topic … --mode draft
scripts/generate_and_publish.py
  ├─ stage_images() → runtime/inbound/<prefix>_<NN>.<ext>
  ├─ write_content_json() → runtime/my_content.json
  └─ subprocess.run([deploy/run_with_xvfb.sh, runtime/my_content.json], env={MODE: …})
       ↓
deploy/run_with_xvfb.sh
  ├─ 推导 PROJECT_ROOT = $(dirname ${BASH_SOURCE[0]})/..
  ├─ source .env（如存在）
  └─ exec xvfb-run --auto-servernum --server-num=99 \
       --server-args="-screen 0 1440x1000x24" \
       .venv/bin/python scripts/publish_xhs.py \
       --content runtime/my_content.json \
       --mode ${MODE} \
       --login-timeout ${LOGIN_TIMEOUT}
       ↓
scripts/publish_xhs.py (publisher CLI)
  ├─ load app.json + selectors.json
  ├─ ContentValidator + DuplicateGuard + LoginState
  ├─ BrowserSession(profile_dir=runtime/browser-profile)
  └─ XhsPublisher.run(content)
       ├─ 登录检测 / QR payload 生成 / 飞书接管
       ├─ 上传图片 / 填正文
       ├─ mode==draft: 点「保存草稿」+ toast/URL 验证 → status=draft_persisted
       ├─ mode==publish: 点「发布」+ 等 published=true → status=published
       └─ audit.write_json('result.json', result)
```

## 已知坑（已沉淀）

| 坑 | 症状 | 已修位置 |
|---|---|---|
| verify_filled body[:20] 跨换行 | innerText.includes 永远 false | `src/publisher.py` verify_filled（用 `first_line[:20]`） |
| body_input_any 误选评论框 | 填到 comment 而非 note body | `config/selectors.json`（placeholder 精确匹配 + `[contenteditable]:not([class*='comment'])`） |
| cgroup OOM | OpenClaw service 被 systemd 杀掉连带 exec session | `systemd override MemoryMax=2.4G` |
| cloud_notify._notify_dir base.name 丢父目录 | 嵌套配置路径错位 | 改用 `run_dir.parent.parent.parent / configured`（2026-08-04） |
| **draft 模式只填表单不存** | 浏览器关后内容丢失，手机草稿箱看不到 | `src/publisher.py::save_draft_and_wait`（点「保存草稿」按钮 + toast/URL 信号验证）；selectors `save_draft_button_any` 2026-08-04 新增 |

## 不要做的事
- 不要自动跑 publish 模式（除非用户明确说"发布"）
- 不要让用户选图序（agent 决定）
- 不要写 README.md / INSTALLATION_GUIDE.md（skill-creator 反模式）
- 不要在没看到图之前猜文案
- 不要把 `.env` / `runtime/runs/` / `runtime/browser-profile/` 提交到 git
- **不要在标题使用极限词**（详见 §1.5 标题段禁用词表）
- **不要做站外导流**（不写微信 / +V / 私信 / 看主页）
- **不要搬运他人原创内容**（小红书有图片指纹 + 文本查重）
- **不要做收益 / 疗效承诺**（小红书对此类内容审核极严）
- **不要用抽象概念开头**（如「另一面」「被遗忘的远方」「不为人知的秘密」等），主题 + 位置前置是硬规则
- **不要省略具体地名**（湖 / 塔 / 亭子 / 绿道 / 水库等地名必出现在正文）

## 例子

**用户输入**：
```
[图1: 林荫步道，远山]
[图2: 狗尾草丛，夕阳]
[图3: 远山日落，树叶剪影]
"发小红书"
```

**Agent 执行**：
1. image 分析 → 湖边绿道，夏末傍晚，散步氛围
2. 内容创作宪法预检：
   - 标题关键词前置 ✓（湖在第 2 字）/ 无极限词 ✓
   - 正文 300-800 字 ✓ / 3-5 段 ✓
   - 话题 2-5 个 ✓（取 4 个，去掉泛词）
   - 首图 3:4 竖图 + 清晰无水印 ✓
   - 无站外导流 / 无收益承诺 ✓
3. 生成文案：
   - title: `🌇 湖绿道｜夕阳和夏天的尾巴` (17 字)
   - body: 5 段（场景 / 光线 / 节奏 / 独白 / 金句），约 380 字
   - topics: `["#湖绿道", "#散步", "#夏日氛围感", "#日落"]`（4 个，去掉"周末""城市漫游""拍照"3 个泛词）
4. 调脚本：
   ```bash
   python3 ~/.openclaw/workspace/skills/xhs-content-creator/scripts/generate_and_publish.py \
     --image <3 张图绝对路径> \
     --title "🌇 湖绿道｜夕阳和夏天的尾巴" \
     --body "绕了半个城市，就为追这场日落。\n…" \
     --topic "#湖绿道" --topic "#散步" \
     --topic "#夏日氛围感" --topic "#日落" \
     --mode draft
   ```
5. 回报：`{"status":"ok","mode":"draft","publisher_status":"draft_persisted","publisher_run_id":"20260804-XXX",…}`（`draft_persisted` 表示已落到服务端草稿箱，手机 app 可在草稿 tab 看到）
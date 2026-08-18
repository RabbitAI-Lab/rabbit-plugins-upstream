<p align="center">
  <img src="assets/icon.jpg" alt="Blogger Auto-Follow Logo" width="160" style="border-radius: 28px;" />
</p>

# 多平台博主批量自动提取与关注技能 (Blogger Auto-Follow Skill)

<p align="center">
  <a href="README.md"><b>简体中文</b></a> | <a href="README_EN.md"><b>English</b></a>
</p>

本技能用于解决用户在观看视频、浏览推荐长文或 PPT 截图时，看到一堆优质博主需要手动逐一搜索关注的繁琐痛点。
支持通过**多模态图片识别**或**文本解析**，自动提取博主信息，并智能调度本地浏览器在目标平台执行拟人化安全批量关注，同时**本地持久化记录博主主页直达链接**，方便后续随时检索最新动态。

---

## 💬 日常对话如何叫它干活？（一句话触发，告别死记命令）

在使用本技能（如在 Google Antigravity、Cursor、Gemini CLI 等 AI 助手环境中）时，**您完全不需要死记或手动输入任何 Python 命令行**。只需在日常对话窗口中发图或输入文字，Agent 会全自动闭环调度：

### 常用日常对话模版 (Prompts)

| 场景 | 您在聊天框中的输入示例 (Prompt) | Agent 自动执行流程 |
| :--- | :--- | :--- |
| 📸 **发截图一键关注** | `[发送图片]`<br>“帮我把这张图里的博主提取出来，并在 **B站**（或抖音/小红书/X/YouTube）上批量关注，存到博主库。” | 1. 结构化提取博主名、分类、粉丝量<br>2. 自动生成 JSON 数据文件<br>3. 自动唤起 Chrome 引导扫码后开始拟人化批量关注<br>4. 抓取主页 URL 存入资产库并更新直达手册 |
| 📝 **纯文本/微信名单关注** | “把这几个博主在**抖音**上关注一下：<br>@影视飓风, @极客湾, @差评君” | 1. 解析文本名单并标准化格式<br>2. 直接生成任务并调用浏览器开始执行 |
| ❓ **模糊发图（平台自动确认）** | `[发送图片]`<br>“帮我关注这里面推荐的所有人” | 1. 提取博主清单并展示预览表格<br>2. **主动弹出交互弹窗**让您选择目标平台<br>3. 选定后自动开始执行关注与归档 |
| 🔍 **一键动态检索与巡检** | “帮我打开我之前存的 **科技·数码**（或指定分类）博主主页，看看他们最近发了什么新动态” | 1. 从本地资产库检索博主直达 URL<br>2. 自动在本地浏览器中批量打开直达标签页 |
| ⚙️ **博主资产增删管理** | “把‘张三’从博主库里删除” 或<br>“帮我手动加一个 B站博主‘李四’，主页是 https://space.bilibili.com/123456” | 1. 增量录入或按名称/ID 删除博主<br>2. 自动同步刷新 `FOLLOWED_BLOGGERS.md` 导航 |

---

## 🌟 核心特性

- 🖼️ **多模态智能提取**：支持视频截图、PPT、排行榜图片、长文名单提取博主信息与粉丝量；
- 🌐 **多主流平台支持**：抖音、小红书、哔哩哔哩 (B站)、X (Twitter)、YouTube；
- 🔐 **支持任意登录方式**：各平台扫码/账密/短信登录不限时等待，登录成功按回车开始；
- 🛡️ **超低频拟人防风控**：10~18秒随机间隔 + 5位博主深度休眠 + 滑块感知 + 防重复误取消；
- 💾 **本地博主资产库**：
  - 自动抓取主页直达链接与唯一 UID，存入 `data/followed_bloggers.json`；
  - 自动生成排版精美、可直接点击直达的 [data/FOLLOWED_BLOGGERS.md](data/FOLLOWED_BLOGGERS.md)；
  - **支持增量录入**（新博主追加合并，不覆盖历史记录）；
  - **支持指定删除**（按博主名或 ID 删除，自动同步刷新文档）；
  - **一键动态检索**（在本地浏览器中批量打开主页链接查看最新动态）。

---

## 📦 环境安装

```bash
# 1. 克隆仓库
git clone https://github.com/helloyxs/blogger-auto-follow.git
cd blogger-auto-follow

# 2. 安装依赖
pip install -r requirements.txt
playwright install chromium
```

---

## 🚫 核心反模式与避坑指南 (Anti-Patterns)

在使用与扩展本技能时，请务必注意以下反模式以避免账号风控与异常：

1. ❌ **追求超高并发/无头运行 (Headless)**：
   - 试图修改代码开启多线程或去掉拟人随机休眠（10~18s）。平台具备完善的行为指纹检测，高并发行为极易导致 IP 被拉黑或账号直接被限制。
2. ❌ **未登录或在游客模式下强行运行**：
   - 在浏览器唤起后未完成登录便按回车开始运行。游客状态下无法执行关注动作，会导致全量失败。
3. ❌ **新号暴利加粉**：
   - 刚注册几天的新账号直接单日批量关注 50+ 人。新号建议首周单日不超过 **10 ~ 15 人**；活跃老号建议单日不超过 **30 ~ 50 人**。
4. ❌ **遇到滑块验证码不处理直接强行跳过**：
   - 遇到滑块/点选验证码时，脚本已发出声音提醒并暂停，请务必在浏览器上手动滑开验证后再按 Enter 恢复。
5. ❌ **低清模糊截图未经预览校验直接跑批**：
   - 模糊截图可能导致 OCR 识别出形近错字，建议让 Agent 先输出预览表格进行人工快速审阅。

---

## ❓ 常见问题与报错排查 FAQ (Troubleshooting)

### Q1: 提示 `Chrome 9222 调试端口无法连接` 或 `Connection refused` 怎么办？
- **原因**：本地已有一个普通的 Chrome 正在运行且未开启调试模式，或者 9222 端口被其他进程占用。
- **解决步骤**：
  1. 完全退出当前所有 Chrome 窗口（macOS 按 `Cmd + Q`，Windows 在任务管理器中结束 `chrome.exe` 进程）；
  2. 重新运行 `python3 scripts/start_chrome.py`（或直接对 Agent 说“帮我启动调试浏览器”）；
  3. 确认打开的 Chrome 带有专属调试提示横条后，再运行关注脚本。

### Q2: 访问 YouTube / X 提示网络超时或无法连接？
- **原因**：YouTube 和 X (Twitter) 需要海外网络代理环境支持，直连会导致页面加载超时或无法打开。
- **解决步骤**：
  1. 开启本地代理/VPN 软件，确保开启系统代理或全局模式；
  2. 在打开的调试 Chrome 中先手动打开一次 `youtube.com` 或 `x.com`，确认可以正常访问；
  3. 回到终端重新启动批量关注脚本即可。

### Q3: 报错 `playwright._impl._errors.TargetClosedError` 或浏览器意外自动关闭？
- **原因**：在脚本运行期间，用户手动关闭了调试 Chrome 浏览器窗口，或被系统内存清理工具杀掉。
- **解决步骤**：
  - 运行期间请保持调试 Chrome 窗口开启；
  - 若意外关闭，重新运行 `python3 scripts/start_chrome.py` 重新唤起即可。已经成功关注的博主已安全存入本地资产库，不会重复执行。

### Q4: 平台页面改版、提示找不到关注按钮或搜索结果为空怎么办？
- **原因**：目标平台前端 UI 或 DOM 选择器进行了微调升级。
- **解决步骤**：
  1. 运行一键平台诊断工具：`python3 scripts/diagnose_platform.py -p <平台名称> --headed`；
  2. 诊断工具会自动输出当前平台的选择器健康状况与匹配结果；
  3. 若选择器失效，参考 [references/supported_platforms.md](references/supported_platforms.md) 快速微调对应平台类下的 CSS 选择器。

### Q5: 登录二维码过期了怎么办？
- **机制说明**：本技能采用**不限时等待机制**。如果扫码时间较长导致二维码失效，直接在网页上点击“刷新二维码”，用手机扫码成功后，回到终端按 `[Enter]` 即可正常继续，无需重启脚本。

### Q6: 重复运行同一个名单，会把已经关注的博主取消关注吗？
- **机制说明**：**绝对不会**。脚本具备**状态幂等校验机制**，在点击前会严格检查页面按钮文案（如“已关注”、“互相关注”、“已订阅”），已关注的博主会自动标记并跳过，安全无副作用。

### Q7: 遇到平台提示“操作过于频繁，请稍后再试”怎么办？
- **解决步骤**：
  1. 在终端输入 `q` 退出，已处理的博主不会丢失；
  2. 当天停止批量关注，在手机端正常浏览 2~3 个视频点个赞，向平台表明是真人使用；
  3. 等待 2~24 小时自然冷却后即可恢复。

---

## 🛠️ CLI 常用命令行手册 (进阶与开发者使用)

如果您需要直接在终端进行脚本调用、集成或二次开发，可参考以下命令：

### 1. 数据准备与格式转换 (`prepare_data.py`)

```bash
# 方式 A: 直接传入文本名单
python3 scripts/prepare_data.py -t "极客湾, 影视飓风, 差评君, 木鱼水心" -o examples/my_bloggers.json

# 方式 B: 从文本文件批量导入 (每行一个博主名，支持带粉丝量和分类备注)
python3 scripts/prepare_data.py -i my_raw_list.txt -o examples/my_bloggers.json

# 方式 C: 校验现有 JSON 数据格式
python3 scripts/prepare_data.py -v examples/bilibili_10_bloggers.json
```

---

### 2. 批量自动关注与主页链接抓取 (`blogger_auto_follow.py`)

```bash
# 步骤 1: 启动本地 Chrome 调试端口 (复用您的登录环境与指纹，全平台通用)
python3 scripts/start_chrome.py

# 步骤 2: 运行批量关注脚本 (以 B站 为例)
python3 scripts/blogger_auto_follow.py -p bilibili -f examples/bilibili_10_bloggers.json
```

---

### 3. 自动化测试与平台 DOM 结构诊断 (`run_tests.py` & `diagnose_platform.py`)

```bash
# 运行全套单元测试与契约测试
python3 scripts/run_tests.py

# 针对指定平台进行可视化深度排查
python3 scripts/diagnose_platform.py -p douyin --headed
```

---

### 4. 博主资产管理与最新动态检索 (`manage_bloggers.py`)

```bash
# ① 查看当前已归档的博主列表与全行业统计
python3 scripts/manage_bloggers.py --list
python3 scripts/manage_bloggers.py --industries

# ② 一键在本地浏览器中批量打开博主主页（检索最新动态/作品）
python3 scripts/manage_bloggers.py --open --industry "科技 · 数码 · 编程"

# ③ 增量手动添加新博主
python3 scripts/manage_bloggers.py --add "博主名称" --category "AI实操" --platform bilibili --url "https://space.bilibili.com/123456" --fans "20w"

# ④ 删除指定博主
python3 scripts/manage_bloggers.py --delete "博主名称"
```

---

## 📂 工程结构

```text
.
├── SKILL.md                          # 核心技能规范（含 YAML frontmatter）
├── README.md                         # 项目详细说明文档 (中文)
├── README_EN.md                      # 项目详细说明文档 (英文)
├── data/                             # 本地博主资产库
│   ├── followed_bloggers.json        # 主数据文件 (JSON 结构化数据库)
│   └── FOLLOWED_BLOGGERS.md          # 自动生成的博主主页直达导航手册
├── storage/                          # 数据持久化管理层
│   ├── __init__.py
│   ├── blogger_db.py                 # BloggerDB (增量 Upsert、Delete、导出 Markdown)
│   └── industry_categories.py        # 全行业与多分类体系推断
├── platforms/                        # 多平台适配层
│   ├── __init__.py                   # 平台工厂与统一注册表
│   ├── base.py                       # 平台基类
│   ├── douyin.py                     # 抖音搜索、关注与主页 URL 提取
│   ├── xiaohongshu.py                # 小红书搜索、关注与主页 URL 提取
│   ├── bilibili.py                   # B站搜索、关注与空间 URL 提取
│   ├── x_twitter.py                  # X (Twitter) 关注与 Profile URL 提取
│   └── youtube.py                    # YouTube 频道订阅与直达 URL 提取
├── tests/                            # 自动化测试套件
│   ├── test_storage.py               # BloggerDB 资产库与行业推断单元测试
│   ├── test_platforms.py             # 多平台 URL 构造与选择器规范测试
│   └── test_prepare_data.py          # 数据转换与格式校验测试
├── scripts/                          # 统一驱动与跨系统管理脚本
│   ├── blogger_auto_follow.py        # 通用批量关注驱动主脚本 (含网络重试与验证码交互)
│   ├── manage_bloggers.py            # 博主资产管理与动态检索工具 (增/删/查/打开主页)
│   ├── prepare_data.py               # 数据准备与文本名单快速转 JSON 工具
│   ├── diagnose_platform.py          # 平台 DOM 结构与网络连通性健康诊断工具
│   ├── run_tests.py                  # 自动化测试一键运行器
│   └── start_chrome.py               # 跨平台 Chrome 调试端口一键启动器 (macOS/Win/Linux)
└── references/                       # 参考手册
    ├── supported_platforms.md        # 各平台 URL 规则与 DOM 选择器规范
    ├── anti_bot_guidelines.md        # 防风控与拟人化策略规范
    ├── faq_and_best_practices.md     # 提问技巧、识图边界与防风控 FAQ
    └── industry_categories_guide.md  # 行业大类与标签指南
```

---

## 📄 License

本项目采用 [MIT License](LICENSE) 开源协议。

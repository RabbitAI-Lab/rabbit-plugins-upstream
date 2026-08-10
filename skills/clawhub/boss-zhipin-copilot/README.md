# boss-zhipin-copilot

[![Version](https://img.shields.io/github/v/tag/HuaGavin/boss-zhipin-copilot?label=version&color=blue&sort=semver)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](requirements.txt)
[![Dependencies](https://img.shields.io/badge/deps-pyyaml-lightgrey.svg)](requirements.txt)
[![Agent](https://img.shields.io/badge/agent-WorkBuddy%20%7C%20OpenClaw%20%7C%20Claude%20Code%20%7C%20Codex-blueviolet.svg)](SKILL.md)
[![Backend](https://img.shields.io/badge/browser%20backend-brs%20only%20(R12)-critical.svg)](https://github.com/energypantry/agent-browser-runtime)

> 一个通用、可配置、开源的 **BOSS 直聘求职 copilot** skill。
> 配合「仿真人浏览器后端」（[agent-browser-runtime](https://github.com/energypantry/agent-browser-runtime)，受控 Chromium + companion 真实光标）的真实光标浏览器，
> 把「简历 + 求职目标」或「一句话目标」沉淀成可复用的能力：
> **自动生成目标岗位画像与检索词 → 建立评分机制 → 建岗位库 → 在 BOSS 检索/收藏 → 读 JD 写破冰话术 → 按授权发送或仅本地成稿。**

所有浏览器动作只经后端正门**真实光标**执行，强制限速、撞墙停手、授权门控，**绝不裸 CDP、绝不走浏览器扩展直控**。统一 **brs 单后端**（agent-browser-runtime 受控运行时，R12 反作弊红线）；设 `BZC_BACKEND=codex|cloak` 会被 `common.sh` 直接拒绝。
适用于 WorkBuddy / OpenClaw / Codex / Claude Code 等任意 Agent 产品（Agent 产品指「谁来跑这个 skill」，与浏览器后端无关——BOSS 动作一律走 brs）。

---

## ✨ 特性

- **输入极简**：给「简历/工作事实 + 一句目标」，或只给一个检索词 / 目标句即可启动。
- **profile 驱动，零硬编码个人偏好**：检索词、硬排除类、评分门槛、破冰事实锚点全部来自 `profile.yaml`，
  仓库**不预置任何平台的默认排除列表**（避免误杀别人的机会）。
- **安全内建**：R1–R12 安全纪律全程兜底（真实光标、限速、撞墙冷却≥24h、授权门控、合并打开、预飞复制、单 lease、复核收敛、发送幂等 R10、登录态失败驱动 R11、反作弊单后端 R12）。
- **完整闭环**：检索 → 过滤 → 书签入库 → 读 JD → 写破冰话术（自检 gate）→ 按授权发送 / 本地成稿。
- **跨平台可移植**：Bash 负责 CLI 编排（封装 `brs.js`）+ Python 负责数据逻辑；`scripts/preflight_env.sh` 自动探测可用 Python（含受管解释器）并校验依赖，Python 一律经 `scripts/run_py.sh` 调用，无 `python3` 的环境也能直接跑（Windows 走 win-native 路径转换）。

---

## 🧱 架构

三层：**谁来跑**（Agent 产品）→ **跑什么**（本 skill）→ **怎么点浏览器**（后端，唯一 `brs`）。

```
┌──────────────────────────────────────────────────────────────┐
│  Agent 产品层：谁来跑这个 skill                              │
│  WorkBuddy / OpenClaw / Claude Code / Codex 等任意 Agent     │
└───────────────────────────┬──────────────────────────────────┘
                            │  读 SKILL.md，按工作流调用 scripts/
┌───────────────────────────▼──────────────────────────────────┐
│  boss-zhipin-copilot（本 skill = 应用层）                    │
│  SKILL.md + scripts/(bash+python) + references/ + assets/    │
│  只对 BrowserDriver 契约 bz_* 编程，不耦合具体浏览器实现     │
└───────────────────────────┬──────────────────────────────────┘
                            │  common.sh 探测并 source backends/brs.sh
┌───────────────────────────▼──────────────────────────────────┐
│  浏览器后端层：brs = agent-browser-runtime                   │
│  受控 Chromium + companion：真实光标 / 持久登录 / 反检测     │
│  唯一 sanctioned 后端：绝不裸 CDP、绝不扩展直控（R12）       │
└───────────────────────────┬──────────────────────────────────┘
                            │  真实光标事件（非 CDP 合成、非扩展直控）
                            ▼
                  ┌────────────────────┐
                  │  zhipin.com（BOSS）│
                  └────────────────────┘
```

- ⛔ **已废弃后端**：`codex`（Codex `@Chrome` 扩展直控）/ `cloak`（CloakBrowser）因 BOSS 反作弊风险移入 `scripts/backends/_deprecated/`，且 `common.sh` 对 `BZC_BACKEND=codex|cloak` **硬拒绝**（`exit 1`）——见 R12。
- ⚠️ **别混淆两层**：Codex 作为 **Agent 产品**（第一层，跑这个 skill）完全可用；被禁的是它的 `@Chrome` **浏览器扩展直控**（第三层）。第一层用什么 Agent 随意，第三层只能是 `brs`。

---

## 📋 前置依赖

> ⚠️ **本 skill 必须运行在「仿真人浏览器」之上**。没有它 → 脚本启动时 **fail-loud 并贴安装链接**，拒绝执行（直接裸 CDP / 合成点击会触发 BOSS 反作弊，曾导致封号）。

1. **仿真人浏览器后端（仅 `brs`）**：
   - **本地全自动（默认 `brs`）**：部署 [agent-browser-runtime](https://github.com/energypantry/agent-browser-runtime)（Docker 三容器 + 经 noVNC 登录 BOSS）。
     `brs status` 须返回 `extensionConnected: true`。设 `BZC_BACKEND=brs`（默认，且为唯一 sanctioned 后端）。
   - ⛔ **Codex `@Chrome` 托管 / CloakBrowser 已禁用**：BOSS 反作弊禁止任何 Agent 的浏览器扩展直控（R12），设 `BZC_BACKEND=codex|cloak` 会被 `common.sh` 直接拒绝。
2. **Node.js** 与 **Python 3.10+**（在 `PATH` 上，或用 `NODE` / `PYTHON` 环境变量指定）。
   脚本会自动按序探测 PATH、受管解释器、venv；**不要**自建 `runtime_env.sh` 之类外部垫片绕过这层。
3. **pyyaml**：`pip install -r requirements.txt`（`preflight_env.sh` 会在启动时校验，缺失即 fail-loud）。
4. **自检**：`bash scripts/preflight_env.sh` 一键确认 Python/依赖/路径转换就绪（`common.sh` 也会自动加载它）。

---

## 🚀 安装

### 作为 Agent skill 安装（WorkBuddy / OpenClaw）

```bash
# 克隆（或下载 ZIP）
git clone https://github.com/HuaGavin/boss-zhipin-copilot.git boss-zhipin-copilot

# WorkBuddy: 拷到项目级或用户级 skills 目录
cp -r boss-zhipin-copilot ~/.workbuddy/skills/        # 用户级
# 或  <项目根>/.workbuddy/skills/                          # 项目级

# OpenClaw: 拷到 skills 目录
cp -r boss-zhipin-copilot ~/.openclaw/skills/

# 安装 Python 依赖
cd boss-zhipin-copilot
pip install -r requirements.txt
```

> skill 是目录即生效，无需注册命令。下次会话 Agent 会自动加载。

### 浏览器后端（仅 `brs`）

```bash
# 默认（本地全自动）：agent-browser-runtime
export BZC_BACKEND=brs
export BRS_JS="/绝对路径/agent-browser-runtime/cli/brs.js"   # 或 AGENT_BROWSER_RUNTIME_HOME
```

> 🔴 **R12 反作弊红线**：BOSS 直聘禁止任何 Agent 的浏览器扩展直控（含 Codex `@Chrome` / CloakBrowser）。
> 本 skill **统一 brs 单后端**；设 `BZC_BACKEND=codex|cloak` 会被 `common.sh` 直接拒绝（`exit 1` + 安装链接）。

脚本会自动探测 `brs.js` 常见路径；未设置/缺失会被 **fail-loud** 并提示安装链接。
后端契约与如何新增后端见 `references/browser_backend.md`（新增后端同样须是受控运行时，禁扩展直控）。

---

## 🎯 快速开始

```bash
cd boss-zhipin-copilot

# 0) 生成求职画像（从一句目标 + 可选简历）
bash scripts/run_py.sh build_profile.py \
  --goal "我想找要求5年以上经验、月薪4万元以上的策略产品经理岗位（北京）" \
  --resume 我的简历.md --out profile.yaml
# → Agent 复核补全 hard_exclude / boost_keywords / fact_anchors

# 1) 初始化岗位库
bash scripts/setup_library.sh

# 2) 在 BOSS 用真实 UI 搜索 profile.search.queries，收集结果卡片到 candidates.csv
#    （真实光标走搜索框，禁止拼接搜索 URL 捷径；可加 --intent "自然语言" 自动映射筛选器）
bash scripts/search_jobs.sh --profile profile.yaml --out .work/candidates.csv

#    然后过滤 + 评分 + 入库：
bash scripts/run_py.sh filter_library.py \
  --profile profile.yaml --input .work/candidates.csv \
  --library target_library.csv --out .work/eval.json

# 3) 对每个通过项书签（真实光标）
AUTHORIZED=1 bash scripts/process_job.sh --url <岗位URL> --bookmark

# 4) 读 JD（备话术）
bash scripts/process_job.sh --url <岗位URL> --read-jd --out .work/recruiter_jd.json

# 5) 写破冰话术 + 自检 gate（详见 SKILL.md Step 4）
bash scripts/run_py.sh audit_icebreaker.py .work/recruiter_jd.json 话术.md 事实库.md keys.json

# 6) 用户授权后发送（或仅本地成稿）
AUTHORIZED=1 bash scripts/process_job.sh --url <岗位URL> --send --msg 话术.txt
```

> 📝 上面命令里的 `话术.md` / `事实库.md` / `keys.json` / `话术.txt` 都由 Agent 在工作流中生成/补全，**运行前无需手动创建**：`事实库.md`（来自你的简历 + `profile.yaml`）、`话术.md`（audit_icebreaker 产出，你只审核）、`keys.json`（可选锚点，不提供照常跑）、`话术.txt`（本地发送正文）。

完整工作流、纪律与脚本参数见 **[SKILL.md](SKILL.md)**。

---

## ⚙️ 核心配置：profile.yaml

`profile.yaml` 是整个 skill 的唯一输入契约。结构（完整说明见 `references/profile_schema.md`）：

```yaml
meta:                       # 可选：候选人标识（可空，不写也行）
  candidate_name: "你的名字"
goal: "我想找5年以上经验、月薪4万以上的策略产品经理岗位（北京）"   # 原始目标句，存档回溯
search:
  city: "北京"
  queries: ["策略产品经理 北京"]
thresholds:
  salary_floor: 40000      # 月薪下限（元），0=不限
  seniority_years: 5       # 经验年限下限，0=不限
hard_exclude:              # 命中任一即不入库（只列你确实无经验的类）
  - category: "广告/IAA"
    keywords: ["IAA", "广告变现", "买量"]
boost_keywords: ["增长", "留存", "C端", "0-1", "Agent"]
fact_anchors:              # 破冰事实锚点，必须真实可溯源
  - anchor: "用户增长"
    evidence: "某内容平台渠道增长，次留提升 3%"
```

仓库自带：
- `assets/profile_template.yaml`：空模板，复制为 `profile.yaml` 填写。
- `assets/example_profile.yaml`：**虚构示例**（候选人「李明」），演示 schema，非真实数据。
- `assets/target_library_template.csv`：空库模板（表头）。

---

## 🔒 安全

- 只走 `brs.js` 正门；真实光标；撞验证码/滑块立即停手冷却 ≥24h。
- **限速**：动作间隔默认 5s±3s 抖动（书签 8s / 发送 20s），日上限 `DAILY_CAP=100` 硬计数，超限 `exit 5`；命中「操作频繁」自动指数退避（5→10→20→40，封顶 60s）。
- **授权门控**：书签需批次授权；发消息需**每岗** `AUTHORIZED=1`，且发送幂等去重（R10）。未授权只浏览/读/本地成稿。
- 详细纪律见 `references/safety_rules.md`（R1–R12）与 `references/cooldown_config.md`；变更历史见 [CHANGELOG.md](CHANGELOG.md)。

---

## 📁 目录结构

```
boss-zhipin-copilot/
├── SKILL.md                      # 主入口：工作流 + 安全纪律
├── README.md                     # 本文件
├── CHANGELOG.md                  # 版本记录
├── LICENSE                       # MIT
├── requirements.txt              # pyyaml
├── references/
│   ├── profile_schema.md         # profile.yaml 字段定义
│   ├── target_library_schema.md  # 岗位库 CSV schema
│   ├── boss_selectors.md         # BOSS 选择器（需实况校验）
│   ├── script_catalog.md         # 脚本复用目录：任务→内置脚本精确命令（复用铁律依据）
│   ├── safety_rules.md           # R1–R12 安全纪律
│   ├── cooldown_config.md        # 限速配置
│   └── browser_backend.md        # 浏览器后端契约与兼容清单
├── scripts/
│   ├── common.sh                 # 后端探测 + source backends/$BZC_BACKEND.sh + fail-loud + 撞墙/冷却/限速
│   ├── preflight_env.sh          # 环境预检层：解析可用 Python + 校验 pyyaml + 路径转换兜底
│   ├── run_py.sh                 # 便携 Python 运行器（所有 .py 统一经它调用）
│   ├── backends/
│   │   ├── brs.sh                # 唯一后端：agent-browser-runtime（已实现，受控 Chromium + companion）
│   │   └── _deprecated/          # ⛔ 已废弃：codex.sh(@Chrome) / cloak.sh —— 反作弊风险(R12)，勿用于 BOSS
│   ├── setup_library.sh          # 初始化空库
│   ├── search_jobs.sh            # 多词检索：复用同 tab 只读收集结果卡→candidates.csv
│   ├── process_job.sh            # 单岗：书签/读JD/发消息（可复用 lease）
│   ├── scan_chat.sh              # 扫描聊天列表（只读，不改状态）
│   ├── zhipin-chat.extract.js    # 聊天列表提取器
│   ├── parse_job.py              # 读JD的HTML DOM解析（process_job 内部调用）
│   ├── parse_search.py           # 搜索结果卡片解析（search_jobs 内部调用）
│   ├── build_profile.py          # 目标句→profile 草稿
│   ├── filter_library.py         # 过滤+评分+入库
│   ├── intent_filters.py         # 意图↔BOSS 编码唯一事实来源（search_jobs/process_job 内部调用）
│   ├── strip_title.py            # 聊天消息首行「公司 姓名」标题行剥离（scan_chat 内部调用）
│   └── audit_icebreaker.py       # 话术自检 gate
└── assets/
    ├── profile_template.yaml
    ├── example_profile.yaml      # 虚构示例
    └── target_library_template.csv
```

---

## 🤝 贡献

欢迎 PR。新增能力请保持：
- 浏览器动作只经后端正门（BrowserDriver 契约），不引入裸 CDP / 合成点击 / 浏览器扩展直控。
- 个人偏好走 `profile.yaml`，不在脚本硬编码。
- 新增浏览器后端：在 `scripts/backends/` 实现 `bz_*` 契约并在 `references/browser_backend.md` 补一行（见该文件「如何新增后端」）。
  **约束（R12）**：新后端必须是**受控运行时**（真实光标事件），任何基于浏览器扩展直控的方案不接受用于 BOSS。
- 新增 Python 脚本经 `scripts/run_py.sh` 调用，不直接写 `python3 xxx.py`（受管环境无 `python3`）。
- 新增脚本遵循 OpenClaw 约定（描述性命名、动词前缀、环境变量而非硬编码路径、幂等），并登记到 `references/script_catalog.md`。

---

## 📄 License

[MIT](LICENSE)

# Changelog

## 2.3.0 — 2026-10-30

### 公开分发安全与正确性加固

- 修复全平台体检把未安装 CLI 的平台计入可用列表的问题；没有任何可用 CLI 时退出 2。
- 修复飞书 `--find` 把 `oc_...` 会话 ID 错填到 `--user-id` 的监听建议。
- 新增 `--until` 绝对截止时间（Unix 时间戳 / ISO 8601），临时值守命中后重挂不再意外延长。
- 个人数据目录自动收紧为 `700`、文件为 `600`；新增 `--delete-data --yes` 显式删除。
- 风格学习必须显式 `--chats`，默认脱敏并只保留 30 天；schema 诊断只输出字段结构，不回显正文值。
- 明确消息注入边界：聊天内容不得触发执行命令、读文件、改配置、扩权或第三方转发。
- 补公开安装说明、`.gitignore` 与 Python 3.9/3.11/3.13 CI 回归。

## 2.2.2 — 2026-10-30

### 权限模型改为「自适应所有人」（公开分发必需）

2.2.1 虽然修好了「续期会扩权」，但用的是**这台机器**的上下文（直接照搬我账号的 192 项）。
公开给别人用时，别人的应用、历史授权、甚至公司策略都不同，硬编码会立刻失效。这一版把它
抽象成**策略**，脚本自己判断，规则写进 SKILL.md。

**两档策略 + 一道闸门**：

| 策略 | 触发 | 申请范围 |
|---|---|---|
| `keep`（默认） | 直接跑 | 有历史授权 → `auth status` 的 `scope` 原样照搬（新增恒为 0）；无历史授权 → 必需集 |
| `minimal` | `--policy minimal` | 必需集 ∩ 应用已开通 |
| 扩权 | `--add ... --allow-add` | 缺一项就 `[block]` |

**三种边界情况自动处理**：

1. **应用没开通某必需权限** → 取交集跳过 + 报 `lack_on_app`（硬塞会让整个 OAuth 失败），
   并说明哪个功能会受限，提示去开放平台开通
2. **应用列表里没有、但历史上授予过** → `keep` 保留并提示（剔除可能丢基础能力），
   登录报 scope 错时再 `--policy minimal` 收窄
3. **平台基础 scope**（如 `auth:user.id:read`，`auth scopes` 不列它）→ 永远带上、不告警，
   避免每个新用户都看到一条无意义警告

**必需清单去硬编码**：`FEISHU_REQUIRED` 变成三元组 `(scope, 用途, 是否需在应用列表里)`，
每项都标注「哪条命令要用它」——加权限必须先说明用途。

**其他**：

- `doctor.py` 新增 `scope` 能力项：必需权限是否齐备（只报事实，绝不自动补权限）
- `reauth.py` 支持 `--policy keep|minimal`，`report_scopes()` 统一输出口径
- 企微/钉钉明确打印「该平台无 scope 概念，权限在管理后台/权限点配置，本脚本不申请任何权限」
- SKILL.md 新增整节 **「权限标准：只申请自己真会调的那几项」**（三原则 / 两档策略 /
  必需清单表 / 三种边界情况 / 红线），测试会校验这节存在
- troubleshooting §B.3 改写为通用策略口径，不再绑具体账号
- 测试 39 → 54 项

## 2.2.1 — 2026-10-30

### 修复（重要）：重新授权会顺手扩大权限

**现象**：授权同意页出现用户从没用过的权限（实测是「妙搭」`spark:app:read` / `spark:app:write`）。

**根因**：`lark-cli auth login` 在不带 `--scope` / `--domain` / `--recommend` 时，
**等价于 `--domain all`** —— 会把应用已开通的全部业务域都申请一遍。2.2.0 的 `reauth.py`
正是这么调的，所以续期动作变成了「顺带扩权」。

**修复**：

- `reauth.py` 现在**永远显式传 `--scope`**：
  - 有历史授权 → **原样沿用当前已授予的集合**（一项不多，新增恒为 0）
  - 全新安装 → 只给 `MINIMAL_IM`（收发消息 + 群成员 + 找人 + `offline_access`），
    不含 base/docs/drive/mail/spark
- 新增扩权闸门 `guard_scopes()`：只要本次申请比现有权限多，直接 `[block]` 拒跑，
  必须显式 `--add <scope> --allow-add` 才放行
- 新增 `--show-scope`（只演练，不申请不发卡）/ `--dry-run`
- 卡片正文加一句「权限范围与你现有完全一致（N 项），不会新增授权」
- `--complete` 收尾后打印「授予 N 项 / 新增 X 项」，新增非空会逐条列出

**排查命令**（三条，判断有没有被扩权）：

```bash
python3 scripts/reauth.py feishu --show-scope   # 应为「新增 0」
lark-cli auth scopes --json                     # 应用侧开通（多于授予属正常）
lark-cli auth status --json                     # 你实际授予（以此为准，看 grantedAt 有没有变）
```

**判据**：`grantedAt` 没变 = 那次授权**没完成**，权限范围没有被扩大。

文档 `references/troubleshooting.md` 新增 §B.3「权限范围：只续期、不扩权」，分诊表加了一行
「同意页出现没用过的权限」；SKILL.md 硬规矩从三条变四条。测试 29 → 39 项。

## 2.2.0 — 2026-10-30

### 新增：免扫码重新授权 `scripts/reauth.py`

飞书 token 约 7 天要续一次。原来只能回终端 `auth login` 再扫码；现在**授权按钮直接发到你 IM 里**：

```bash
python3 scripts/reauth.py feishu              # 发卡片 → 你点一下 → 自动收尾
python3 scripts/reauth.py feishu --detach     # 发完返回，之后 --complete <device_code>
python3 scripts/reauth.py feishu --no-send    # 不发卡片，只打印链接
```

- 原理：bot 用 `app_id/app_secret`（长期凭证），与 user token 是两套。**user token 过期时
  bot 照样能发消息**，所以这条链路不会死锁；按钮打开的是设备流授权页（`user_code` 已在 URL 里），
  **不需要本机回调端口**，远端/容器也能用。
- 卡片本身：单按钮 + `user_code` 兜底 + 「勿转发」警示 + `enable_forward: false`。
- 失败降级链：卡片 → 文本消息 → 打印链接，三级都能把链接送到人手上。
- **平台边界不糊弄**：企微是机器人凭证（不是 OAuth，走 `auth init --manual` 免扫码）；
  钉钉未登录时本机没有 bot 通道（先有鸡还是先有蛋），走 `auth login --device` 短链 + 验证码。
  脚本对这两个平台返回 4 并给出正确路径，不假装支持。

### 修复：两个"假成功"

- `lark-cli ... --content @<绝对路径>` 会被拒（只收 cwd 相对路径），但 **`rc` 仍然是 0**。
  改为 stdin 传内容，并统一按 JSON 的 `ok`/`error` 判断成败 —— 只看退出码会误报"发送成功"。
- `doctor.py` 的飞书过期提示改为直接给 `scripts/reauth.py feishu`，不再让用户去拼设备流命令。

### 文档

- `troubleshooting.md` §B.2 重写为「不扫码续期」：卡片流程、为什么成立、手动等价流程、
  卡片发不出去时怎么办；§G 补充「别用退出码判断发送成功」。

### 测试

- 29 项断言：新增授权卡片结构（按钮直链、`user_code` 兜底、勿转发、禁转发）与
  企微/钉钉平台边界（rc ∈ {0,4}，不得假装成功）。

## 2.1.0 — 2026-10-30

### 新增：故障处理索引（`references/troubleshooting.md`）

把"坏了怎么办"从口头经验变成可跳转的索引：**30 秒分诊表**（症状 → 第一条命令 → 小节）
＋ A~K 十一类故障，每类都是「症状 / 原因 / 修复命令」三段式，最后一节是**回归清单**。

覆盖的故障族：

- **A 版本漂移**：CLI 改名、子命令失效、字段消失时怎么查新版、怎么升级、升级后怎么重新
  发现命令（三平台机制不同：`lark-cli --help` + `schema`、`dws --help` + `schema --cli-path`、
  `wecom-cli --help` + `--schema`），以及升级后必做的 4 步回归。
- **B 授权到期**：怎么判断是"要刷新"还是"要重新授权"（飞书看 `tokenStatus` 与
  `refreshExpiresAt`），三平台各自的**非阻塞重新授权**流程（设备码 / 二维码 / `--device`），
  以及授权成功后的收尾动作。附授权相关坑位（scope 不足、`--as user` 漏了、Keychain 迁移）。
- **C 字段失配**：`SCHEMA_MISMATCH` 三步修复、五种成因与对应键名。
- **D 拉不到消息**：时间窗 7 天上限、群/单聊参数互斥、企微 `chat_id`=userid、429 限流、
  富文本取不到正文。
- **E 唤醒异常**：水位文件是唯一真相，不唤醒/重复唤醒/回环各自的判据与重置方法。
- **F 进程消失**：单发唤醒必须重挂、退出码语义、重复挂载会双回复。
- **G 发不出去**：三平台发送命令差异（企微 `--text` 必须是 JSON 对象）。
- **H 合规硬停**：钱/承诺/外部群/凭据一律不自动回。
- **I 配置损坏**：`env.json` 重建、水位隔离、多实例隔离目录。
- **J 上报模板**：只收集状态码与键名，附脱敏自检命令。

### 新增：`scripts/doctor.py`（一屏体检 + 自愈引导）

```bash
python3 scripts/doctor.py                          # 全平台
python3 scripts/doctor.py feishu --chat-id oc_xxx  # 附 3 秒通路自检
python3 scripts/doctor.py --check-update --json    # 版本检查 + 机器可读
python3 scripts/doctor.py --repair-state           # 隔离损坏水位（移到 *.bad，不删）
```

- 六项检查：CLI 存在与版本 → **CLI 自带 `doctor`**（飞书/钉钉有，企微没有就跳过并注明）
  → 授权与 token 剩余时间 → `env.json` 与 `self_id` → 水位目录可写与文件合法 → 真实通路。
- 每项 fail 直接打印 `→ 修复:` 命令与 `→ 手册:` 锚点，**agent 不用猜**。
- 退出码语义 = "现在能不能用"：指定平台则该平台必须全绿；全量体检只要有一个平台可用即 0。
- ID 默认打码（`--show-ids` 可关），避免体检输出被随手贴出去。
- 新增 `IM_STANDIN_DIR` 也被 `bootstrap.py` 尊重（此前只有引擎支持，文档与实现不一致）。

### 测试

- `tests/run_tests.py` 增到 **22 项断言**：新增文档索引完整性（所有 `#锚点` 可跳、
  分诊表与 A~K 章节齐全、文档内无真实 ID/token 泄漏）与 doctor 桩环境自洽
  （全绿、JSON 合法、三平台无 fail、ID 已脱敏）。

## 2.0.0 — 2026-10-30

### 新增：真正可用的企微 / 钉钉适配

不再靠猜。本机实装 `@wecom/cli` 1.3.4 与 `dingtalk-workspace-cli` 1.0.66 后按真实命令回写：

- 企业微信：`chat messages list`（**必须带时间窗**，仅近 7 天）、`contact users search --keywords`、
  `message send --text '{"content":"..."}'`；发现 `ChatMessage` **没有消息 ID**，改用复合指纹水位。
- 钉钉：`chat +chat-messages`、`chat +recent-conversations`、`contact user search`、
  `chat +messages-send`；发现 stdout 会连续输出两段 JSON、默认倒序。
- 平台矩阵在 `SKILL.md` 里标注实测程度，未验证的部分不写成"已支持"。

### 引擎（`listen_core.py`）

- 命令链回退 `cmd_list_chain`：CLI 改名不用改代码，命中后缓存不再试错。
- `overrides` 支持覆盖**和新增**任意键（命令与字段都能改）。
- 时间窗占位 `{begin_time}/{end_time}`，按 `--lookback-min` 每轮生成。
- 复合消息指纹 `f_msg_id_compose`，支撑无消息 ID 的 CLI。
- `f_count` / `f_has_more` 区分「空结果」与「字段不对」，不再把空会话误报成 schema 错误。
- `order` 归一化（正序平台内部翻转成最新在前）。
- `self_id_regex`：whoami 只回人类可读文本时用正则取本人 ID。
- 多段 JSON 输出只取第一个文档。
- 一轮多条新消息**只唤醒一次**，报最新那条并带 `pending_in_burst`。

### 工具链

- `bootstrap.py --find`：名字 → ID 精准解析，命中唯一自动登记别名（不再拉全量会话）。
- `bootstrap.py --probe`：打印 CLI 真实命令形态 + 现有字段映射 + override 模板。
- `bootstrap.py --selftest`：真跑 3 秒监听验证通路。
- `--learn-style --chats`：指定语料来源，避免为了学风格去枚举全部会话。
- `IM_STANDIN_DIR` 环境变量：数据目录可换（多账号 / 测试隔离）。

### 修复

- 飞书 `+chats-list` 不存在 → 改 `+chat-list`；消息数组在 `data.messages` 而非 `body.items`。
- `dig()` 支持三种调用写法，避免多路径传参报错。
- 回复命令按平台区分：企微 `text` 是 JSON 对象、钉钉单聊/群聊参数不同。

### 测试

- 新增 `tests/mock_cli.py` + `tests/run_tests.py`：14 项断言覆盖命中、防回环、水位、
  过滤、三种输出形态、SCHEMA_MISMATCH 与 override 修复。不需要真实账号。

## 1.0.0

首个版本：飞书单平台，脚本阻塞轮询 + 单发唤醒 + 风格学习 + 服务对象档案。

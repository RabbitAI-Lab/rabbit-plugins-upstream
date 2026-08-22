# kuaidi-query — OpenClaw 快递查询技能

一个用于 [OpenClaw](https://docs.openclaw.ai) 的快递物流技能：调用[快递鸟](https://www.kdniao.com) API 查询快递轨迹，支持订阅提醒和群聊隐私脱敏。让您的 AI 助手可以回答"我的快递到哪了"，并在物流变化时主动提醒。

## 功能

- **单次查询**：输入快递单号查询实时轨迹，默认给出简短结论，要求时展开完整轨迹。
- **快递公司识别**：内置高置信度单号规则（顺丰 / 京东 / 圆通 / EMS / 极兔）；无法可靠识别时向用户确认，不瞎猜。
- **订阅与变更提醒**：把常用单号加入本地订阅，配合 OpenClaw 定时任务（cron）在轨迹变化时提醒，无变化不打扰。
- **取件码提取**：自动从最新轨迹中提取取件码 / 快递柜信息。
- **群聊隐私保护**：三种模式（`redact` 全部脱敏 / `allowlist` 白名单群完整展示 / `full` 全部完整展示），默认 `allowlist`；缺少群 ID 或配置异常时安全回退为脱敏。
- **凭据安全**：API 密钥保存在技能目录之外（权限 `0600`），永不进入 Git 仓库，永不回显到聊天。

## 前置条件

- Python 3.9+（Linux / macOS / Windows 均可，无第三方依赖）
- 一个[快递鸟](https://www.kdniao.com)账号（注册后在「快递查询」产品中获得 AppID / AppKey）

## 安装

```bash
# 方式一：从 Git 仓库安装（SKILL.md 位于仓库根目录，符合单技能仓库规范）
openclaw skills install git:<你的GitHub用户名>/kuaidi-query

# 方式二：发布到 ClawHub 后，从市场安装
openclaw skills install @<你的handle>/kuaidi-query

# 方式三：本地目录安装（调试用）
openclaw skills install ./kuaidi-query
```

默认安装到当前工作区 `skills/` 目录；加 `--global` 安装到 `~/.openclaw/skills` 供所有 agent 共用。

## 发布到 ClawHub（可选）

如希望其他用户通过市场搜索安装：

```bash
npm i -g clawhub
clawhub login        # 需要 GitHub 账号
clawhub skill publish . --slug kuaidi-query --name "Kuaidi Query" \
  --owner <你的handle> --categories integrations,productivity
```

注意：按 ClawHub 规则，发布即采用 MIT-0 许可。

## 初始化

安装后需要一次初始化（创建配置文件，幂等，已有配置不会被覆盖）：

```bash
SKILL="$HOME/.openclaw/workspace/skills/kuaidi-query"

# 交互式：会提示输入 AppID，AppKey 输入不回显
python3 "$SKILL/scripts/init_config.py" init

# 非交互式：通过环境变量传入，避免密钥进入命令历史
KDNIAO_APP_ID='你的AppID' KDNIAO_APP_KEY='你的AppKey' \
  python3 "$SKILL/scripts/init_config.py" init --json
```

生成的文件（均在技能目录外）：

| 文件 | 用途 |
|------|------|
| `~/.openclaw/config/kuaidi-query.json` | 快递鸟 API 凭据 |
| `~/.openclaw/config/kuaidi-query-privacy.json` | 群聊隐私策略 |
| `~/.openclaw/subscribe/kuaidi.json` | 本地订阅数据 |

## 使用示例

对您的 OpenClaw 助手说：

- 「查一下快递 SF1234567890123」
- 「帮我订阅这个快递，备注猫砂，到货提醒我」
- 「我的快递有哪些？」
- 「这个群设为内部群」（启用完整物流展示）

命令行直接调用：

```bash
# 单次查询
python3 "$SKILL/scripts/query_tracking.py" 'SF1234567890123' --json

# 订阅管理
python3 "$SKILL/scripts/subscribe_tracking.py" add 'SF1234567890123' --remark '猫砂' --json
python3 "$SKILL/scripts/subscribe_tracking.py" list --json

# 变化检测（配合 cron 定时任务，见 references/CRON_CONFIG.md）
python3 "$SKILL/scripts/check_changes.py" --quiet
```

完整说明见 [`SKILL.md`](SKILL.md)（供 AI 助手阅读的技能指令）。

## 目录结构

```
kuaidi-query/
├── SKILL.md                     # 技能定义（AI 阅读的操作指令）
├── scripts/                     # 全部 Python 脚本，仅用标准库
│   ├── init_config.py           # 初始化 / 状态检查
│   ├── query_tracking.py        # 单次查询
│   ├── subscribe_tracking.py    # 订阅管理（add/remove/list/check）
│   ├── check_changes.py         # 变化检测（cron 用）
│   ├── privacy_settings.py      # 群聊隐私策略
│   └── kuaidi_common.py         # 公共逻辑
├── references/                  # 按需加载的参考资料
│   ├── companies.md             # 快递公司编码表
│   ├── state_codes.md           # 快递鸟状态码对照
│   ├── CRON_CONFIG.md           # 定时提醒配置说明
│   └── hardening.md             # 安全与数据保障说明
└── templates/config.example.json
```

## 安全设计

- 凭据文件权限 `0600`，保存在技能目录外，`.gitignore` 双重保险。
- 订阅文件原子写入（临时文件 + `os.replace`），Linux/macOS 带文件锁，不会因定时检查与手动操作并发而损坏。
- 任何输出不包含 AppKey、签名、鉴权头或原始 API 响应。
- 群聊默认脱敏（电话、地址、取件码），私聊和受信群才完整展示。

详见 [`references/hardening.md`](references/hardening.md)。

## License

[MIT-0](LICENSE)（MIT No Attribution，与 ClawHub 市场许可要求一致）

---
name: "kuaidi-query"
description: "快递物流查询与订阅提醒：调用快递鸟 API 查询快递单号实时轨迹，支持物流状态订阅、变更定时提醒、取件码提取、快递公司识别，以及群聊隐私脱敏。用户提到查快递、查物流、快递单号、快递到哪了、订阅快递提醒时使用。"
license: "MIT-0"
metadata:
  openclaw:
    envVars:
      - name: KDNIAO_APP_ID
        required: false
        description: 快递鸟 AppID，非交互初始化时使用
      - name: KDNIAO_APP_KEY
        required: false
        description: 快递鸟 AppKey，非交互初始化时使用
---

# 快递查询

调用快递鸟 API 查询物流。默认给简短结论；用户要求“详细物流/完整轨迹/全部信息”时展开完整轨迹。

## 路径

```bash
SKILL="$HOME/.openclaw/workspace/skills/kuaidi-query"
INIT="$SKILL/scripts/init_config.py"
QUERY="$SKILL/scripts/query_tracking.py"
SUBSCRIBE="$SKILL/scripts/subscribe_tracking.py"
CHANGES="$SKILL/scripts/check_changes.py"
PRIVACY="$SKILL/scripts/privacy_settings.py"
```

以上为默认工作区路径；若安装到其他位置（如 `--global` 装入 `~/.openclaw/skills`），以实际技能目录为准。

## 首次初始化

用户明确要求初始化或配置技能时执行：

```bash
python3 "$INIT" init
python3 "$INIT" status --json
```

交互初始化会询问快递鸟 AppID，并用不回显方式读取 AppKey。不要让用户把 AppKey 发到聊天里。

无交互环境使用环境变量，避免把密钥写进命令历史：

```bash
KDNIAO_APP_ID='...' KDNIAO_APP_KEY='...' python3 "$INIT" init --json
```

仅初始化隐私和空订阅文件：

```bash
python3 "$INIT" init --skip-api --json
```

初始化规则：

- API 配置：`~/.openclaw/config/kuaidi-query.json`
- 隐私配置：`~/.openclaw/config/kuaidi-query-privacy.json`
- 订阅数据：`~/.openclaw/subscribe/kuaidi.json`
- 文件权限统一为 `0600`。
- 默认幂等：已有文件只校验并保留，不覆盖凭据、订阅或群白名单。
- 已有文件损坏或字段无效时停止并报告，不覆盖原文件。
- 仅用户明确要求更新 API 凭据时使用 `--replace-api`；它不会改订阅和隐私白名单。
- 真实配置和订阅均在技能仓库外；提交代码时只提交 `templates/config.example.json`，不得复制用户数据进仓库。

支持 `KUAIDI_CONFIG_FILE`、`KUAIDI_PRIVACY_FILE`、`KUAIDI_SUBSCRIBE_FILE` 覆盖路径，主要用于测试和独立部署。

## 决策流程

1. 提取快递单号、快递公司、备注、平台和手机尾号。
2. 没有单号时，只问一次单号；不要猜。
3. 普通物流查询：单次查询，不自动订阅。
4. 用户明确说“订阅/关注/持续提醒”：添加本地订阅。
5. 用户问“我的快递/有哪些快递”：先 `list --json`；需要最新状态时再 `check --json`。
6. 用户明确要求定时提醒时，先检查现有任务，再创建或更新调度；添加订阅不等于开启自动提醒。

## 单次查询

```bash
python3 "$QUERY" '<单号>' [公司编码] --json
```

常用编码：顺丰 `SF`、中通 `ZTO`、圆通 `YTO`、申通 `STO`、韵达 `YD`、邮政 `EMS`、京东 `JD`、德邦 `DBL`。

能可靠识别时省略公司编码；识别失败或冲突时结合用户提供的信息，仍不确定再询问。需要验证时使用 `--phone-suffix '<后4位>'`。

## 订阅管理

```bash
python3 "$SUBSCRIBE" add '<单号>' [公司编码] --remark '备注' --platform '平台' --phone-suffix '手机后4位' --json
python3 "$SUBSCRIBE" list --json
python3 "$SUBSCRIBE" check ['单号'] --json
python3 "$SUBSCRIBE" remove '<单号>' --json
```

添加、删除订阅必须来自用户明确请求。重复订阅时报告已存在，不覆盖原备注。

## 变化检测

```bash
python3 "$CHANGES" --quiet
```

- 无变化且无错误：退出码 `0`，无输出。
- 有变化：退出码 `0`，解析 `changes[].message`。
- 有查询或数据错误：非零退出码，报告 `errors[]`；不能把失败当成“无变化”。
- 调试使用 `--dry-run`；首次也通知需用户明确要求 `--include-first-seen`。

## 群聊隐私开关

三种模式：

- `redact`：所有群聊脱敏。
- `allowlist`：仅白名单内部群完整展示，其他群脱敏。默认且推荐。
- `full`：所有群聊完整展示。仅在用户明确要求时启用。

```bash
python3 "$PRIVACY" show --json
python3 "$PRIVACY" set-mode allowlist --json
python3 "$PRIVACY" trust '<群ID>' --name '内部群名称' --json
python3 "$PRIVACY" untrust '<群ID>' --json
python3 "$PRIVACY" resolve --chat-type group --chat-id '<群ID>' --json
```

用户在群里明确说“这个群设为内部群”时，使用可信运行时元数据中的群 ID，不让用户手工寻找。每次群聊展示物流前解析策略；缺少群 ID 或配置异常时安全回退为脱敏。

## 展示边界

### 私聊或已信任内部群

普通查询显示状态、时间和最新轨迹。用户要求完整轨迹时，可完整显示快递员姓名和电话、网点电话和地址、取件码、柜号、货架号、箱号等物流业务信息。

### 未信任群聊、公开频道或准备转发

默认遮盖电话、详细地址、取件码等。长期完整展示需用户明确要求并加入白名单。

### 所有场景均禁止展示

API Key、签名、Cookie、Token、鉴权头、完整配置、无关内部账号标识、调试堆栈和未筛选的原始 API 响应。

## 错误处理

- 配置缺失：建议运行初始化，不索要聊天中发送密钥。
- 单号无效：请用户核对。
- 公司无法识别：给出候选或询问。
- 限流/网络失败：保留原订阅状态并报告。
- 订阅、API 或隐私配置损坏：不覆盖原文件。

按需读取：`references/companies.md`、`references/state_codes.md`、`references/CRON_CONFIG.md`、`references/hardening.md`（安全与数据保障说明）。

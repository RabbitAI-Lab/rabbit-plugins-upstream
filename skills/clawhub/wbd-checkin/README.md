# WorkBuddy 手机端签到积分

**不需要电脑，不需要安装客户端。** 在手机上就能完成 WorkBuddy 每日签到与积分领取：绑定本人手机号收一次验证码取得凭据，之后每天说一句「签到」，连续天数、累计积分自动记账，凭据还会自动续期，不必每月重录。

只服务你自己的一个账号：凭据由你提供、只存在技能目录里，一条命令可清空。

## 和其他签到技能的区别

| | 本技能 | 多数 PC 端签到技能 |
|---|---|---|
| 要不要电脑 | **不需要**，手机独立完成 | 需要：先读 PC 客户端本机登录态 |
| 首次配置 | 手机号收一次验证码 | 在电脑上导出令牌，再想办法拷到手机 |
| 苹果手机 | 可用：同一套命令，无客户端依赖 | 多数只支持 Windows |
| 凭据过期 | 自动续期 | 过期后重新导出粘贴 |
| 账号范围 | 只服务你本人一个账号 | 不一定 |

> 安卓真机长期跑过；iPhone 命令完全一致，但要在一个能执行 `python3` 的环境里跑（WorkBuddy 里直接说「签到」即可）。

---

## 选版本

| 版本 | 手机上取凭据 | 自动续期 | 一句话 |
|---|---|---|---|
| **v3.3.1**（本仓库首页，推荐） | 收验证码即可 | 有 | 手机三条命令搞定，之后不用管 |
| v3.1.0 | 要先在电脑复制一次 | 无 | 精简版，通过平台审核的那一版 |
| v1.3.0 | 收验证码即可 | 有 | 老版本，见 [workbuddy-mobile-checkin](https://github.com/windcool18-maker/workbuddy-mobile-checkin) |

要精简版：`git checkout v3.1.0`。两版命令一致，只是 v3.1.0 没有 `self_login.py`，也没有续期参数。

---

## 三步上手

### 第 1 步：装进来

```bash
git clone https://github.com/windcool18-maker/wbd-checkin.git
cd wbd-checkin
```

放到你的技能目录即可，例如 WorkBuddy 的 `<skills>/wbd-checkin/`、Claude Code 的 `~/.claude/skills/wbd-checkin/`。也可以直接下 [Release 里的 zip](https://github.com/windcool18-maker/wbd-checkin/releases/latest) 解压过去。

> 目录名保持 `wbd-checkin`。同名目录不是并存而是互相覆盖，装完新开一个对话才生效。

### 第 2 步：拿凭据（只做一次）

**手机上（v3.3.1，不用电脑，推荐）**

```bash
python3 scripts/self_login.py --bind 13xxxxxxxxx   # 绑定你本人的号码
python3 scripts/self_login.py --send               # 平台发验证码到你手机
python3 scripts/self_login.py --code 123456        # 回填，换取凭据
```

验证码发到你本人的手机，必须回填才能换到凭据，脚本绕不过这一步。绑定之后所有请求只认这个号码。

**电脑上（v3.3.1 / v3.1.0 都能用）**

1. 浏览器登录 WorkBuddy 网页版
2. 开发者工具 → 「网络」面板 → 随便点一下页面，让请求出现
3. 找发往 WorkBuddy 服务地址的请求，复制请求头 `Authorization` 的值（形如 `Bearer eyJhbGciOi...`）

```bash
python3 scripts/setup.py          # 交互粘贴，整行粘进去就行
# 或
python3 scripts/setup.py --token 'Bearer eyJhbGciOi...'
```

粘贴不用清洗：带 `Bearer` 前缀、带引号、带换行都能识别。

### 第 3 步：签到

```bash
python3 scripts/checkin.py
```

输出示例：

```
[2026-11-28 09:05:11] 今日尚未签到，正在领取…
[2026-11-28 09:05:12] 签到成功，连续 12 天，当前积分 1280
```

重复执行是安全的：先查当日状态，签过就直接返回，不会重复领取。

---

## 命令速查

| 命令 | 作用 |
|---|---|
| `python3 scripts/checkin.py` | 签到（幂等） |
| `python3 scripts/checkin.py --dry-run` | 只看状态，不领取 |
| `python3 scripts/checkin.py --force` | 强制领取，忽略「今日已签」 |
| `python3 scripts/checkin.py status` | 最近一次运行结果 |
| `python3 scripts/checkin.py --json` | 机器可读输出 |
| `python3 scripts/setup.py` | 交互粘贴录入凭据 |
| `python3 scripts/setup.py --token '凭据'` | 直接录入 |
| `python3 scripts/setup.py --token '凭据' --renew-key '续期凭据'` | 同时录入续期凭据（v3.3.0） |
| `python3 scripts/setup.py --check` | 看凭据状态 |
| `python3 scripts/setup.py --guide` | 分设备取凭据指引 |
| `python3 scripts/setup.py --purge` | 删掉凭据 |
| `python3 scripts/self_login.py --status` | 看绑定号码与今日发送额度（v3.3.0） |
| `python3 scripts/self_login.py --unbind` | 解绑并清空凭据（v3.3.0） |

## 对助手直接说

装了技能后不用记命令，说人话就行：

- 「签到」→ 执行签到并回报连续天数
- 「今天签了吗」→ 只查状态，不领取
- 「帮我绑定手机号 138xxxxxxxx」「发验证码」「验证码是 123456」→ 走自助登录
- 「签到凭据怎么弄」→ 分设备给指引

---

## 想每天自动签

**方式一：让助手记着。** 在 WorkBuddy 里设一条每天固定时间的自动化，指令写「执行 wbd-checkin 技能签到」。最省事，手机电脑都行。

**方式二：系统定时任务。** 把 `python3 /绝对路径/wbd-checkin/scripts/checkin.py` 交给系统计划任务，每天上午跑一次。脚本自己会判断今天是否已签，多跑几次不会重复领。

**方式三：只想被提醒。** 不定时跑脚本，每天让助手提醒你手动签一次。

---

## 退出码

| 码 | 含义 | 该怎么办 |
|---|---|---|
| 0 | 签到成功，或今日已签跳过 | 无需处理 |
| 1 | 失败（网络、接口异常） | 稍后重试 |
| 2 | 凭据缺失或失效 | 重新走第 2 步 |

## 安全边界

| 项 | 说明 |
|---|---|
| 账号范围 | 只服务使用者本人的一个账号，无多账号、无批量 |
| 请求目标 | 只请求平台自己的地址，无备用域、无转发、无第三方 |
| 凭据存放 | 只存技能目录下 `config.json`（权限 0600），不写系统目录，不进 git |
| 本机数据 | 不扫描、不读取、不解密客户端或浏览器数据 |
| 自助登录 | 号码只能来自 `--bind` 绑定值，无自由入参；两次发送间隔 ≥120 秒，每日 ≤3 次；换号须先 `--unbind` |
| 输出 | 日志不打印凭据内容，手机号只显示 `138****8888` |
| 清除 | `setup.py --purge` 一键删除 |

## 常见问题

**签到提示 401 / 凭据失效？**
重新走第 2 步。v3.3.0 录了续期凭据的话，每次运行会自动延长，不会突然失效。

**手机上装完没反应？**
技能列表在对话开始那一刻加载完，装完要新开一个对话。

**能签多个号吗？**
不能，这是有意为之。想签第二个号就复制一份技能目录，各自录入。

**`self_login.py --send` 提示太频繁？**
两次间隔至少 120 秒，每天最多 3 次，防止误触和被滥用。额度在本地计算，跨天自动重置。

**换手机号？**
`python3 scripts/self_login.py --unbind` 后重新 `--bind`。

## 目录结构

```
SKILL.md                技能定义（frontmatter + 指令）
README.md               本文件
使用说明.md              完整使用手册
scripts/wbcfg.py        配置读写与请求封装
scripts/checkin.py      签到主流程
scripts/setup.py        凭据录入 / 检查 / 清除
scripts/self_login.py   本人账号自助登录（v3.3.0）
```

## 许可

MIT

# WorkBuddy 每日签到 v3.1.0

领每日签到积分、记连续天数。纯本地脚本，只请求平台自己的接口，凭据只存在技能目录里。

这一版是通过平台审核的精简版：没有自动续期，也没有手机自助登录，凭证需要在电脑上取一次、粘贴一次。

---

## 和 v3.3.0 的区别（先选对版本）

| | **v3.1.0（本页）** | [v3.3.0](https://github.com/windcool18-maker/wbd-checkin) |
|---|---|---|
| 签到 / 查状态 / 连续天数 | 有 | 有 |
| 自动续期 | 无 | 有，每次运行自动延长 |
| 手机上取凭据 | 不行，需电脑取一次 | 可以，收验证码即可 |
| 凭据到期怎么办 | 重新走一次第 2 步 | 自动续，不用管 |
| 适合 | 只想要最小可用、从平台商店装的人 | 大多数人 |

两版命令完全一致，切版本只需要 `git checkout v3.1.0` / `git checkout main`。

---

## 三步上手

### 第 1 步：装进来

```bash
git clone https://github.com/windcool18-maker/wbd-checkin.git
cd wbd-checkin
git checkout v3.1.0
```

或者下 [v3.1.0 的 zip](https://github.com/windcool18-maker/wbd-checkin/releases/tag/v3.1.0) 解到技能目录，例如 WorkBuddy 的 `<skills>/wbd-checkin/`、Claude Code 的 `~/.claude/skills/wbd-checkin/`。

> 目录名保持 `wbd-checkin`。同名目录是覆盖不是并存，装完要新开一个对话才生效。

### 第 2 步：在电脑上取一次凭据

1. 浏览器登录 WorkBuddy 网页版
2. 打开开发者工具 → 「网络」面板 → 随便点一下页面，让请求出现
3. 挑一个发往 WorkBuddy 服务地址的请求，复制请求头 `Authorization` 的值（形如 `Bearer eyJhbGciOi...`）

```bash
python3 scripts/setup.py            # 交互粘贴，整行粘进去即可
# 或
python3 scripts/setup.py --token 'Bearer eyJhbGciOi...'
```

粘贴不用清洗：带 `Bearer` 前缀、带引号、带换行都能识别。不确定怎么做就先跑 `python3 scripts/setup.py --guide`，它会按设备给出步骤。

### 第 3 步：签到

```bash
python3 scripts/checkin.py
```

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
| `python3 scripts/setup.py --token '凭据' --uid '用户标识'` | 同时指定用户标识（可选） |
| `python3 scripts/setup.py --check` | 看凭据录入状态 |
| `python3 scripts/setup.py --guide` | 分设备取凭据指引 |
| `python3 scripts/setup.py --purge` | 删掉凭据 |

## 对助手直接说

- 「签到」→ 执行签到并回报连续天数
- 「今天签了吗」→ 只查状态，不领取
- 「签到凭据怎么弄」→ 分设备给指引

---

## 想每天自动签

**方式一：让助手记着。** 在 WorkBuddy 里设一条每天固定时间的自动化，指令写「执行 wbd-checkin 技能签到」。

**方式二：系统定时任务。** 把 `python3 /绝对路径/wbd-checkin/scripts/checkin.py` 交给系统计划任务，每天上午跑一次。脚本会自己判断今天是否已签，多跑不会重复领。

因为这一版没有自动续期，凭据大约一个月会到期。到期后按提示重走第 2 步粘贴一次即可；不想每月手动，换 v3.3.0。

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
| 输出 | 日志不打印凭据内容 |
| 清除 | `setup.py --purge` 一键删除 |

## 常见问题

**签到提示 401 / 凭据失效？**
凭据过期了，重走第 2 步粘贴一次。这一版不会自动续期。

**手机上能用吗？**
签到本身能跑，但取凭据需要在电脑上操作一次，因为手机浏览器没有开发者工具。想彻底脱离电脑，用 v3.3.0。

**能签多个号吗？**
不能，有意为之。要签第二个号就复制一份技能目录，各自录入。

## 目录结构

```
SKILL.md              技能定义（frontmatter + 指令）
README.md             本文件
使用说明.md            完整使用手册
scripts/wbcfg.py      配置读写与请求封装
scripts/checkin.py    签到主流程
scripts/setup.py      凭据录入 / 检查 / 清除
```

## 许可

MIT

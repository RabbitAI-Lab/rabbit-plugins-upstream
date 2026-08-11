---
name: github-autosetup
description: 自动化配置 pi 在 GitHub/git 的行动（纯 Git Bash 驱动）：环境探测 → 传输通道决策（https/GCM 或 SSH）→ 浏览器 OAuth → 带口令 SSH 密钥 + agent → 建仓推送 → post-commit 自动推送 + 计划任务兜底。内置敏感信息传递 SOP（令牌/口令/密钥/cookie 零明文）。当用户说"配置 github / 自动推送 / 建仓库 / 推送仓库 / 配置 git"时使用。
license: MIT
compatibility: pi, Claude Code（Git Bash / bash 环境；Windows 已验证，macOS/Linux 标注分支）
metadata:
  author: Sgt_BaiXiao
  version: "2.0.0"
  homepage: https://github.com/SgtBaixiao/github-autosetup
---

# GitHub AutoSetup v2 — 自动化 GitHub/git 配置（纯 Git Bash 驱动）

把 pi（或任意 agent）机器上的 GitHub/git 一次性配置到"提交即自动推送"，全程**敏感信息零明文**。**所有自动化通过 Git Bash 完成**（agent 的 bash 工具或用户 Git Bash 终端）。

> **为什么不用 PowerShell**（v1 血泪教训）：Windows PowerShell 5.1 有三大坑 —— UTF-8 无 BOM 按 GBK 误读、`Encoding::UTF8` 写文件带 BOM 破坏 `#!/bin/sh`、原生命令引号解析（逗号列表绑成单串/内嵌引号被吞）。bash 侧这些全部不存在。本 skill 从 v1 失败中重建，已验证：Windows 11 + Git Bash + 大陆网络（github.com:443 被阻断）场景。

---

## 0. 敏感信息传递 SOP（先读，违反即事故）

**铁律：任何密钥、令牌、口令、cookie 都不得进入对话文本、仓库、日志明文。**

| 敏感物 | 正确传递方式 | 错误方式 |
|---|---|---|
| GitHub 令牌 | **一律浏览器 OAuth**（`gh auth login -w`），令牌入系统 keyring（Windows=DPAPI） | 让用户把 token 粘贴进对话/文件 |
| SSH 私钥 | **交互式 `ssh-keygen`（必须设口令）**，用户在自己 Git Bash 输入；解锁态驻 ssh-agent 内存 | `-N ""` 空口令；口令打进命令行参数 |
| 口令/密码 | 只出现在用户终端的交互提示中 | 发聊天里 |
| 站点 cookie（B站/贴吧） | 导出 JSON → 写**仓库外临时文件** → 转换后写入**已 gitignore 的 config** → 删临时文件；验证输出**掩码** | 把 cookie 原文粘贴进对话/提交 |
| 敏感文件落点 | 核查权限（`icacls`/`chmod 700`）；报告落点（keyring vs 文件） | 不核查直接收工 |

**操作模式**：agent 打印"**终端复制块**"（用户在自己 Git Bash 执行）或直接用自身 bash 工具执行；agent 只**验证结果**（`gh auth status` / `ssh-add -l` / `git ls-remote`），全程看不见秘密。验证输出一律掩码（`sed 's/Token: .*/Token: ***/'`）。

---

## 1. 环境探测（只读，bash）

```bash
bash "<skill_dir>/scripts/probe.sh"
```

输出：git/gh/GCM/ssh-agent、git 身份、**网络通道**（github.com:443 / api.github.com:443 / github.com:22 / ssh.github.com:443）、现有密钥、gh 认证态（token 类型掩码）。

**通道决策表**：

| 探测结果 | 走哪条路 |
|---|---|
| `github.com:443` 通 | https + GCM（DPAPI 加密，最优） |
| 443 断但 `github.com:22` 或 `ssh.github.com:443` 通 | **SSH + 带口令密钥 + agent**（大陆网络常见） |
| 全断 | 报告：需代理/镜像或手动网页，不硬推 |
| `api.github.com` 通但 `github.com` 断 | 混合：gh API 建仓 + git 走 SSH（本机实测案例） |

## 2. 认证（HITL，两处需用户本人 Git Bash 操作）

**① gh 浏览器 OAuth**（未认证或令牌是 fine-grained PAT 时）：
```bash
gh auth login -h github.com -p <https|ssh> -w
```
- **前提核查**：`gh auth status` 显示 `Token: github_pat_*` → fine-grained PAT **无法建仓**（GitHub 官方限制），必须重走浏览器 OAuth（`ghp_` 才可建仓）。
- 认证后核查：`gh auth status` 显示 `(keyring)` 即合格；hosts.yml 只应含元数据。

**② SSH 密钥（带口令）+ agent**（用户 Git Bash）：
```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_gh -C "autopush"   # 输入口令两次，别留空
ssh-add ~/.ssh/id_ed25519_gh
```
- agent 未启用：`powershell -c "Set-Service ssh-agent -StartupType Automatic; Start-Service ssh-agent"`（仅此一步用 PowerShell，或用户管理员终端）。
- 注册公钥：`gh ssh-key add ~/.ssh/id_ed25519_gh.pub --title "autopush"`（token 无权限时用户网页粘贴 .pub，.pub 可公开展示）。
- `~/.ssh/config` 追加（多密钥防混乱）：
  ```
  Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_gh
    IdentitiesOnly yes
  ```
- 验证：`ssh -T git@github.com` 应回 `Hi <用户名>!`。

## 3. 建仓与推送（agent bash）

```bash
gh config set git_protocol ssh --host github.com   # 或 https，按通道决策
gh repo create <name> --<private|public> --source <本地仓库目录> --remote origin --push
```
- 可见性必须向用户确认（代码/思考类 private；可发布 skill 类 public）。
- 本地目录先确保已 `git init -b main` + 首次 commit。
- 推送失败：网络（§1 决策表）/分支名（统一 main）/remote 协议。

## 4. 自动推送（提交即推 + 计划任务兜底）

```bash
bash "<skill_dir>/scripts/install-autopush.sh" -d "D:/Agent Workspace" -t AutoSync -m 30 \
  "D:/Agent Workspace/Ziggy" "D:/Agent Workspace/Skill/meme-digger" ...
```
脚本自动完成（全 bash）：
1. 每个仓库装 `.git/hooks/post-commit`（printf 写 LF，零凭据）：
   ```sh
   #!/bin/sh
   branch=$(git symbolic-ref --short HEAD 2>/dev/null || echo main)
   [ "$branch" = "main" ] || exit 0
   git push origin "$branch" -q 2>/dev/null || echo "[autopush] push failed - retried by scheduler" >&2
   ```
2. 生成 `autopush.sh`（仓库清单内嵌 + ssh-add 告警 + 日志）。
3. 注册计划任务（默认每 30 分钟）：`schtasks //create //tn AutoSync //tr "\"<git-bash>\" \"<autopush.sh>\"" //sc MINUTE //mo 30 //f`。

**验证（必做）**：任一仓库提交临时文件 → `git ls-remote origin main` 与本地 HEAD 一致 → 清理。重启后提醒用户 `ssh-add ~/.ssh/id_ed25519_gh`（agent 重启清空）。

## 5. 收尾核查（安全自检）

- [ ] `gh auth status` → `(keyring)`；hosts.yml 无明文 token（掩码核查）
- [ ] 私钥有口令（`ssh-keygen -y -P '' -f <key>` 应失败）；`~/.ssh` 权限收紧
- [ ] 无 token/口令出现在 git log、仓库文件、聊天、日志
- [ ] `schtasks //query //tn <任务名>` 存在；hook 文件为 LF
- [ ] cookie 类配置：gitignore 的 config、临时文件已删、git status 无敏感文件

## 6. 故障排查

| 现象 | 处理 |
|---|---|
| `gh repo create` → `GraphQL: Resource not accessible... (createRepository)` | fine-grained PAT → 重走浏览器 OAuth |
| https push → `Connection was reset` | 443 域名级阻断 → 切 SSH（§1 决策表） |
| `ssh -T` → `Permission denied (publickey)` | 公钥未注册 / IdentitiesOnly 指错 / agent 未加载 |
| `ssh-add -l` → `Could not open a connection` | ssh-agent 服务未启（见 §2 ②）；或 SSH_AUTH_SOCK 未设 |
| 计划任务推送失败 | 看 `.autopush.log`：agent 空 → `ssh-add`；否则检查仓库 remote |
| hook 不生效 | 文件须 LF（用 printf 重写）；确认在 `.git/hooks/` 且无 BOM |

## 7. 相关

- `scripts/`：probe.sh（探测）/ install-autopush.sh（安装）/ autopush.sh（生成式同步）
- 参考实现与测试记录：SgtBaixiao/github-autosetup；验证环境 Windows 11 + Git Bash
- v1 教训归档：Ziggy `.scratch/github-bash-setup/issues/01-v1-lessons.md`

# github-autosetup — 自动化 GitHub/git 配置（Agent Skill · v2 纯 Git Bash 驱动）

把 pi（或任意 agent）机器的 GitHub/git 一次配置到**提交即自动推送**，内置**敏感信息零明文 SOP**。

- **纯 Git Bash 驱动**（v1 的 PowerShell 路线已废弃，见 v1 教训：PS5.1 编码/BOM/引号三大坑）
- 通道自动决策：https+GCM（DPAPI 加密）优先，被阻断自动切 SSH（带口令密钥 + agent）
- 认证走浏览器 OAuth + 交互式密钥生成（**绝不要求用户粘贴 token/口令**）
- 建仓推送、post-commit 自动推送 hook、计划任务兜底（全 bash）
- 实机验证：Windows 11 + 大陆网络（github.com:443 被阻断场景）✅

## 安装（各平台）

> 发布约定：本仓库每次上架新平台后，都会在此补齐对应安装指令。当前已发布：GitHub。

| 平台 | 安装方式 | 状态 |
|---|---|---|
| **GitHub（源）** | `git clone https://github.com/SgtBaixiao/github-autosetup` | ✅ 已发布 |
| **pi** | `cp -r github-autosetup ~/.pi/agent/skills/github-autosetup`（或 clone 后复制） | ✅ 可用 |
| **Claude Code** | 个人：`git clone ... ~/.claude/skills/github-autosetup`；或插件：`/plugin install github-autosetup@<marketplace>`（市场就绪后） | ✅ 可克隆 |
| **Codex / OpenCode** | `cp -r github-autosetup ~/.codex/skills/` / `~/.opencode/skills/` | ✅ 可克隆 |
| **Hugging Face CLI** | `hf skills add https://github.com/SgtBaixiao/github-autosetup` | ⏳ 上架后 |
| **Agent Skill Hub** | `skhub add SgtBaixiao/github-autosetup` | ⏳ 待导入（需账号） |
| **Skillstore** | `skillstore install github-autosetup` | ⏳ 待提交（需账号） |
| **Claude 社区市场** | `/plugin install github-autosetup@claude-community` | ⏳ 待提交（需账号） |

> 平台账号类发布（Agent Skill Hub / Skillstore / Claude 市场 / HF）为一次性浏览器操作，见 `Skill/README.md` 发布手册。

## 使用

对 agent 说："配置我的 GitHub 自动推送"，agent 按 SKILL.md 流程执行：
1. `scripts/probe.sh` 探测环境与通道
2. 按决策表走 https 或 SSH；打印"终端复制块"让你完成交互认证（浏览器 OAuth / 带口令密钥）
3. 建仓推送（可见性向你确认）
4. `bash scripts/install-autopush.sh -d <outdir> -t AutoSync -m 30 <repo1> <repo2> ...`
5. 实测自动推送 + 安全自检

## 结构

```
github-autosetup/
├── SKILL.md                 # 完整 SOP（Git Bash 驱动 + 敏感信息规范 + 决策表 + 故障排查）
├── scripts/
│   ├── probe.sh             # 只读环境/网络/凭据探测（含掩码）
│   ├── install-autopush.sh  # 装 post-commit hooks + 生成 autopush.sh + schtasks 注册（纯 bash）
│   └── autopush.sh          # 自动提交+推送（由 install 生成，无凭据）
├── README.md / LICENSE / .gitignore / .claude-plugin/plugin.json
```

## 安全承诺

- 令牌：浏览器 OAuth → 系统 keyring（Windows DPAPI 加密）
- 私钥：**必须设口令**，解锁态仅驻 ssh-agent 内存
- 无任何 token/口令写入仓库、日志、对话明文；敏感文件权限核查
- cookie 类配置：临时文件转换 → gitignore 的 config → 删除临时文件 → 掩码验证

## License

MIT © Sgt_BaiXiao
v2 verified 1786282218

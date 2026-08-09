# GitHub 发布指南

## 推荐仓库设置

- Repository name：`upwork-bid-decision-assistant`
- Description：`中文 Upwork 工作投标、Boost、Invite 与客户风险判断 Agent Skill`
- Visibility：Public
- Topics：`upwork`、`agent-skills`、`freelance`、`prompt-engineering`、`chinese`

## 网页上传方式

1. 在 GitHub 新建一个空仓库；
2. 不要让 GitHub 自动生成 README 或 License，避免与本目录冲突；
3. 解压 GitHub 版本 ZIP；
4. 上传**文件夹里面的全部内容**，不要把外层文件夹再套一层；
5. Commit message 可写：`Initial public release v1.2.1`；
6. 发布后检查仓库根目录能直接看到 `SKILL.md` 和 `README.md`。

## 命令行方式

```bash
cd upwork-bid-decision-assistant-github
git init
git add .
git commit -m "Initial public release v1.2.1"
git branch -M main
git remote add origin https://github.com/<你的用户名>/upwork-bid-decision-assistant.git
git push -u origin main
```

## 建议创建 Release

- Tag：`v1.2.1`
- Title：`Upwork 投标判断助手 v1.2.1`
- Release 文件：可附上仓库 ZIP；
- Release Notes：复制 `CHANGELOG.md` 中 1.2.1、1.2.0 和 1.1.0 的主要变化。

## 发布前检查

- 仓库中没有卖家文案、价格、销售素材或私人资料；
- 没有真实客户未脱敏数据；
- `SKILL.md` 中的版本与 Release Tag 一致；
- `LICENSE` 符合你允许非商业公开使用、禁止转售的意图；
- 通用粘贴版和安装版规则保持一致。

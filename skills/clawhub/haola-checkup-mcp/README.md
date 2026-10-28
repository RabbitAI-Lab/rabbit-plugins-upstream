# 好啦体检方案 MCP Skill 发布包

## 包内容

- `SKILL.md`：Skill 主文件
- `mcp.json`：MCP 连接配置

## 免费渠道

| 渠道 | 费用 | 做法 |
|---|---|---|
| ClawHub | 免费 | 使用 `clawhub` CLI 发布 |
| SkillHub.cn（腾讯云） | 免费 | 实名认证后上传 ZIP，等待安全审核 |
| WorkBuddy | 免费 | 使用现有 `publish/workbuddy/haola-pe` 连接器包提交审核 |
| GitHub | 免费 | 建公开仓库，README 放接入说明 |

Toolify 是 AI 工具目录，当前提交费用 99 美元，不计入免费渠道。

## ClawHub

```bash
npm i -g clawhub
clawhub login
clawhub skill publish ./SKILL.md --slug haola-checkup-mcp --name "好啦体检方案 MCP" --version 1.0.0
```

如果 CLI 版本不支持 `./SKILL.md`，改成当前目录：

```bash
clawhub skill publish . --slug haola-checkup-mcp --name "好啦体检方案 MCP" --version 1.0.0
```

## SkillHub.cn

1. 登录 `https://skillhub.cn/`
2. 完成实名认证
3. 新建 Skill，上传当前目录的 ZIP
4. 目录名必须是 `haola-checkup-mcp`
5. 等待内容合规、漏洞扫描和模型安全评估

## WorkBuddy

WorkBuddy 连接器包在：

`/Users/admin/projects/projTpl/ai-backend-template/publish/workbuddy/haola-pe`

后台提交入口：

`https://open.workbuddy.cn/`

## 注意

- 公开工具不校验 Authorization，无效或过期 Authorization 仍按匿名放行
- 预约、订单、体检件、就诊人需要登录令牌
- 不把真实凭证写进 Skill 包

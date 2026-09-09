## Description:

通过 typecho-cli 直接管理 Typecho 博客文章 — 创建、查询、更新、删除、查询分类。当用户要求发布文章到博客、保存内容到 Typecho、查询或修改博客文章时触发此技能。涉及"发博客""归档""知识库""Typecho""我的博客"等关键词时均应使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[coolingrabbit](https://clawhub.ai/user/coolingrabbit)

### License/Terms of Use:

MIT-0

## Use Case:

External Typecho blog operators and agent users use this skill to let an agent create, query, update, and delete Typecho blog posts through the bundled typecho-cli command-line tool. It is intended for blogs where the user has configured a Typecho domain and an AI Token for the agent account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Typecho token that grants blog access for the configured agent account.

Mitigation: Treat the token like a password, store it carefully, and use a least-privileged blog account.

Risk: The skill can create, update, and delete blog posts, including irreversible deletion.

Mitigation: Review posts before publishing and require explicit confirmation before updates or deletions.

Risk: The skill can query all posts on the configured blog for knowledge retrieval.

Mitigation: Install it only when the agent is intended to manage that Typecho blog and should have that read access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/coolingrabbit/skills/typecho-publisher)
- [Typecho Publisher repository](https://github.com/CoolingRabbit/Typecho-Publisher)
- [Publisher profile](https://clawhub.ai/user/coolingrabbit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI prints JSON responses and uses Typecho domain and token configuration.]

## Skill Version(s):

4.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

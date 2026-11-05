## Description:

用于微博数据分析、微博帖子详情、帖子数据、互动指标、内容调研和内容分析。覆盖 Weibo post details，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

People researching or analyzing Weibo content use this skill to retrieve a post’s content, author, publish time, media, and interaction metrics by post ID or URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocialDataX requests may use account credits.

Mitigation: Confirm the intended request and use the relevant account before making data calls.

Risk: The API key is a credential, and external CLI behavior is unverified by the supplied artifact.

Mitigation: Keep the key in a supported secret store and out of chat and version control; use a reviewed fixed CLI version or an existing authenticated MCP connection.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-detail)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration guidance]

**Output Format:** [JSON post details with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only post lookup; optional media downloads save to a user-selected local path. Available fields depend on the source response.]

## Skill Version(s):

0.1.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

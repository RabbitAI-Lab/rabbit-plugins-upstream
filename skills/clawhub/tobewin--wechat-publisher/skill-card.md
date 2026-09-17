## Description:

Helps agents prepare, manage, publish, and review WeChat public account articles using the official WeChat publishing APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tobewin](https://clawhub.ai/user/tobewin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and account operators use this skill to automate WeChat public account article workflows, including draft creation, media upload, publishing, statistics retrieval, and comment management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WeChat AppID/AppSecret, article drafts, uploaded media, analytics, and comments are sensitive account data.

Mitigation: Install only for an authorized WeChat public account, keep credentials in environment variables, and avoid processing sensitive or confidential content in automated workflows.

Risk: Article content, media files, and account identifiers are sent to official WeChat API servers.

Mitigation: Review content before upload or publish and confirm that external transfer to WeChat is acceptable for the account and content type.

Risk: Publishing and delete operations for drafts, published articles, materials, comments, and replies are irreversible.

Mitigation: Review command targets carefully and use the required --confirm flag only after confirming the intended account change.

## Reference(s):

- [WeChat Publisher on ClawHub](https://clawhub.ai/tobewin/skills/wechat-publisher)
- [WeChat Subscription Account API Documentation](https://developers.weixin.qq.com/doc/subscription/api/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and generated WeChat article HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can issue authenticated API operations when the user provides WeChat account credentials and explicit commands.]

## Skill Version(s):

1.0.9 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

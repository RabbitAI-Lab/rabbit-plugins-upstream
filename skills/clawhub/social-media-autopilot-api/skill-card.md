## Description:

Use SocialEcho OpenAPI for explicit team/account/content queries and user-authorized TikTok Shop sync or cross-platform publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socialecho-net](https://clawhub.ai/user/socialecho-net)

### License/Terms of Use:

MIT-0

## Use Case:

External social media operators, developers, and agents use this skill to query SocialEcho team, account, content, report, upload, Reddit, Pinterest, and TikTok Shop APIs, then prepare or execute explicitly authorized publishing and product-sync actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A SocialEcho Team API Key could grant access to team, account, content, report, upload, community, product, genre, music, publishing, or product-sync operations.

Mitigation: Provide the API key only for the current task, keep it private, and do not print, persist, or retrieve it from environment variables, credential stores, shell history, or files.

Risk: Publishing articles or syncing TikTok Shop products can create live external changes.

Mitigation: Review the dry-run preview and approve only the exact target account and payload intended; live writes require --execute and a matching --confirm-account-id.

Risk: Requests sent to an unintended API host could expose credentials or content.

Mitigation: Use only https://api.socialecho.net, or https://api-dev.socialecho.net when the user explicitly targets development.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/socialecho-net/skills/social-media-autopilot-api)
- [SocialEcho Social Media OpenAPI](artifact/openapi.json)
- [Platform publish limits: copy, media, and formats](artifact/platform-publish-limits_en.md)
- [Platform publish limits, Chinese](artifact/platform-publish-limits_cn.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live write operations require an immediate dry-run preview, explicit user authorization, --execute, and a matching --confirm-account-id.]

## Skill Version(s):

2.1.1 (source: evidence release, package.json, OpenAPI info, artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

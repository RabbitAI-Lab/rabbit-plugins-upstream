## Description:

Use SocialEcho OpenAPI to query team, account, and content data, and to run user-authorized TikTok Shop sync or cross-platform publishing with an explicit Team API Key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socialecho-net](https://clawhub.ai/user/socialecho-net)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, marketers, and developers use this skill to inspect SocialEcho team, account, article, report, upload, Reddit, Pinterest, and TikTok Shop data, then perform explicitly authorized publishing or product sync actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live publishing and TikTok Shop sync actions can change connected social accounts.

Mitigation: Review the dry-run preview carefully and authorize only the exact target account and payload; live writes require --execute and a matching --confirm-account-id.

Risk: The Team API Key can expose or modify SocialEcho team resources available to that key.

Mitigation: Provide the key only for the current task, do not print or persist it, and authorize commands only when the account and payload match the intended action.

Risk: Social platform limits and policies can change after the bundled reference files were prepared.

Mitigation: Use the bundled platform limits as preparation guidance and follow live platform or SocialEcho error messages when they differ.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/socialecho-net/skills/socialecho-social-media-management-agent)
- [SocialEcho App](https://app.socialecho.net/)
- [SocialEcho OpenAPI JSON](artifact/openapi.json)
- [SocialEcho OpenAPI YAML](artifact/openapi.yaml)
- [Platform publish limits: copy, media, and formats](artifact/platform-publish-limits_en.md)
- [各平台发布内容与格式限制](artifact/platform-publish-limits_cn.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live writes require a dry-run preview, explicit authorization, --execute, and a matching --confirm-account-id.]

## Skill Version(s):

2.1.1 (source: server release metadata, artifact package.json, artifact _meta.json, OpenAPI info.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

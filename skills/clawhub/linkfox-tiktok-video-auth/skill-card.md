## Description:

Provides TikTok creator and video-account OAuth authorization, authorized-account listing, token lookup, and access-token refresh through the LinkFox /tiktokVideo workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect TikTok creator or video accounts, list authorized accounts, check stored token status, and refresh access tokens before downstream TikTok video workflows.

### Deployment Geography for Use:

Global, with a separate US region option.

## Known Risks and Mitigations:

Risk: The skill handles TikTok authorization links, access tokens, refresh tokens, and the LinkFox API key.

Mitigation: Install only when LinkFox is trusted for the authorization flow, keep API keys in environment variables, and do not display or share full tokens.

Risk: Persisted response files may contain sensitive account, token, or authorization data.

Mitigation: Write response files only outside shared or git-tracked folders and delete temporary files after use.

## Reference(s):

- [TikTok Video Authorization API Reference](artifact/references/api.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-video-auth)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [JSON API responses with concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Token-query and refresh scripts mask access and refresh tokens before displaying them.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

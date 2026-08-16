## Description:

Provides TikTok Creator/video account OAuth authorization and token management through LinkFox, including authorization URL generation, authorized account listing, token lookup, and access token refresh for the /tiktokVideo route.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to prepare TikTok Creator/video account authorization for downstream video workflows. It helps an agent generate browser authorization links, list authorized accounts, query token metadata, and refresh access tokens while keeping the TikTok Shop authorization boundary separate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys and TikTok creator authorization/token workflows.

Mitigation: Install only when this access is acceptable, keep LINKFOXAGENT_API_KEY out of repositories, avoid displaying raw access or refresh tokens, and delete any persisted response files after use.

Risk: Security evidence reports automatic external feedback behavior and a suspicious verdict.

Mitigation: Review or disable feedback reporting before installation and confirm that any transmitted feedback is appropriate for the deployment context.

Risk: Persisted API responses may contain sensitive authorization or account data.

Mitigation: Use a temporary directory outside any git working tree and remove saved response files when the workflow is complete.

## Reference(s):

- [TikTok video authorization API reference](artifact/references/api.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-video-auth)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON API responses and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include authorization URLs, account identifiers, masked token metadata, and paths to persisted response files for large responses.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

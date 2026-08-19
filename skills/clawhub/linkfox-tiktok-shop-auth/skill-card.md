## Description:

Provides TikTok Shop ERP OAuth authorization, authorized ERP store listing, and optional token lookup or manual refresh for LinkFox-based workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and developers use this skill to authorize TikTok Shop ERP stores, list authorized ERP stores, and troubleshoot stored token state when explicitly needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys and TikTok Shop authorization tokens.

Mitigation: Install only for trusted users, keep gateway and API-key environment variables under trusted control, and avoid sharing full tokens; the artifact masks token values in command output.

Risk: API responses are saved locally in linkfox session files and may contain sensitive authorization data.

Mitigation: Review or delete local response/session files after use and do not commit persisted outputs.

Risk: Token lookup and manual refresh expose sensitive authorization state and are not needed for normal business calls.

Mitigation: Use token query and manual refresh only for explicit troubleshooting; otherwise rely on the ERP store authorization flow and store openId.

## Reference(s):

- [TikTok Shop ERP Authorization API Reference](artifact/references/api.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-auth)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces authorization URLs, authorized-store records, and masked token diagnostics; large responses may be saved under local linkfox session files.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description: <br>
Post to 21 platforms via a single unified API and manage accounts, groups, media, scheduling, analytics, inbox, comments, and webhooks through RelayAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zanhk](https://clawhub.ai/user/zanhk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent prepare RelayAPI calls for social media publishing, scheduling, account management, analytics, inbox workflows, and webhooks across connected platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents to manage real social accounts, public posts, direct messages, webhooks, and account connections. <br>
Mitigation: Install only when those capabilities are intended, use a least-privilege RelayAPI key where possible, and keep account connection flows in RelayAPI's browser or dashboard experience. <br>
Risk: Posting, deleting, unpublishing, disconnecting accounts, sending messages, changing webhooks, and follow or retweet actions can have public or destructive effects. <br>
Mitigation: Require explicit user confirmation before any public, destructive, account-changing, messaging, webhook, or social engagement action. <br>
Risk: The security scan found broad authority without enough scoping or confirmation guidance. <br>
Mitigation: Scope requests to the intended workspace, account, platform, or post before execution, and review proposed RelayAPI calls before running them. <br>


## Reference(s): <br>
- [RelayAPI Skill on ClawHub](https://clawhub.ai/zanhk/skills/relayapi) <br>
- [RelayAPI Homepage](https://relayapi.dev) <br>
- [RelayAPI API Docs](https://api.relayapi.dev/docs) <br>
- [RelayAPI OpenAPI Spec](https://api.relayapi.dev/openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires RELAYAPI_API_KEY and curl for live API calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

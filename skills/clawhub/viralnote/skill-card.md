## Description: <br>
Schedule, publish, and manage social media content through the ViralNote API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[viralnote](https://clawhub.ai/user/viralnote) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an agent schedule or publish social posts, manage ViralNote media, query analytics, and inspect connected social accounts through the ViralNote REST API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help an agent act on a user's ViralNote account, including publishing, scheduling, deleting content, importing media, and changing webhooks or API keys. <br>
Mitigation: Install it only when those account actions are intended, use the narrowest API key scopes needed, and require explicit confirmation before sensitive or irreversible actions. <br>
Risk: API keys or signed private URLs could expose account access or private media if shared in chat logs or tracked files. <br>
Mitigation: Keep VIRALNOTE_API_KEY in the environment, avoid storing secrets in files or chat, rotate leaked keys, and share signed URLs only when comfortable sending them to ViralNote for retrieval. <br>
Risk: Publishing immediately or deleting posts and media can be hard to undo. <br>
Mitigation: Restate the platform, caption, time, and media details before acting, and wait for user confirmation before immediate publishing or deletion. <br>


## Reference(s): <br>
- [ViralNote Agent Homepage](https://www.viralnote.app/agents) <br>
- [ClawHub Skill Listing](https://clawhub.ai/viralnote/skills/viralnote) <br>
- [ViralNote API Reference](https://viralnote.app/developers/docs) <br>
- [ViralNote OpenAPI Spec](https://viralnote.app/api/v1/openapi) <br>
- [API Overview](reference/api-overview.md) <br>
- [Authentication](reference/auth.md) <br>
- [Schedule Post Workflow](examples/schedule-post.md) <br>
- [Import Media Workflow](examples/import-media.md) <br>
- [Analytics Workflow](examples/analytics.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls, JSON] <br>
**Output Format:** [Markdown guidance with curl examples and JSON request or response shapes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a ViralNote API key supplied through VIRALNOTE_API_KEY; API responses are JSON.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

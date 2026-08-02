## Description: <br>
Install, connect, and use Schedulala to schedule and publish social media posts across 12 platforms, including drafts, previews, analytics, engagement, keyword monitoring, media handling, and safe publishing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ameera48](https://clawhub.ai/user/ameera48) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to connect Schedulala, plan social posts, validate drafts, upload media, confirm publishing actions, and inspect post status, analytics, comments, and listening results from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connected social accounts can publish posts or perform moderation actions. <br>
Mitigation: Use drafts and previews first, then obtain explicit user confirmation before immediate publishing, near-term scheduling, replies, or hiding comments; use a test key for dry runs when possible. <br>
Risk: API keys, OAuth credentials, app tokens, or payment details could be exposed if handled in chat. <br>
Mitigation: Keep authentication and payment flows on schedulala.com, avoid asking for passwords, app passwords, bot tokens, or card details in chat, and follow the documented API-key handling paths. <br>
Risk: Media uploads may pass through Schedulala, S3, and CDN infrastructure. <br>
Mitigation: Use the documented upload flows, avoid base64-encoding user files in chat, and confirm the intended media before publishing. <br>


## Reference(s): <br>
- [Schedulala developer docs](https://schedulala.com/developers/docs) <br>
- [Schedulala homepage](https://schedulala.com) <br>
- [CLI reference](artifact/references/cli.md) <br>
- [Hosted-connector widgets](artifact/references/connector-widgets.md) <br>
- [Media reference](artifact/references/media.md) <br>
- [Per-platform settings reference](artifact/references/platforms.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration snippets, and structured workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide CLI, hosted connector, local MCP server, OAuth, API-key, media upload, scheduling, analytics, and moderation workflows.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

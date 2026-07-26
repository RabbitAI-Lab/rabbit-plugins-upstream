## Description: <br>
Schedule and manage social media posts across TikTok, Instagram, Facebook, X (Twitter), YouTube, LinkedIn, Threads, Bluesky, Pinterest, Telegram, and Google Business Profile using the PostFast API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[peturgeorgievv](https://clawhub.ai/user/peturgeorgievv) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketers, agencies, and developers use this skill to guide an agent through PostFast API workflows for scheduling, drafting, publishing, deleting, and analyzing social media posts across connected accounts. It is useful when the agent needs to produce API calls, JSON request bodies, upload steps, or platform-specific posting guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide live operations on connected social media accounts, including scheduling posts, deleting scheduled posts, and generating client connect links. <br>
Mitigation: Before any live action, require explicit user confirmation of the target account, content, media, scheduled time, approval status, post ID, and connect-link recipient. <br>
Risk: A PostFast workspace API key enables account and post management through the PostFast API. <br>
Mitigation: Install and use the skill only with an intended workspace key, keep the key secret, and verify connected account status before scheduling or publishing. <br>
Risk: Incorrect platform controls or media specifications can cause failed posts or unintended visibility. <br>
Mitigation: Check the platform-specific controls, media limits, scheduled time, and draft versus publish status before creating or updating posts. <br>


## Reference(s): <br>
- [PostFast homepage](https://postfa.st) <br>
- [ClawHub skill page](https://clawhub.ai/peturgeorgievv/skills/postfast) <br>
- [PostFast API Reference](references/api-reference.md) <br>
- [Media Upload Flow](references/upload-flow.md) <br>
- [Platform-Specific Controls Reference](references/platform-controls.md) <br>
- [Media Specifications by Platform](references/media-specs.md) <br>
- [PostFast Skill Examples](examples/EXAMPLES.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include PostFast API endpoints, curl commands, JSON payloads, media upload steps, and platform-specific posting constraints.] <br>

## Skill Version(s): <br>
1.14.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

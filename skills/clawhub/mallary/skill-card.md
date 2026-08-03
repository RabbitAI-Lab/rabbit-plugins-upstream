## Description: <br>
Mallary Openclaw Skill guides agents through Mallary CLI, API, and MCP workflows for publishing, scheduling, uploads, comments, analytics, webhooks, settings, and platform connections with read-only discovery first. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sammydigits](https://clawhub.ai/user/sammydigits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, CI jobs, and AI agents use this skill to work with Mallary social-publishing workflows, including media upload, post creation and scheduling, job inspection, analytics review, webhooks, settings, profiles, and platform connections. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help an agent publish or schedule public content, reply to comments, delete queued posts, change webhooks or settings, and disconnect platforms. <br>
Mitigation: Start with read-only Mallary discovery and require explicit confirmation for each upload, publish, reply, delete, webhook, settings, or disconnect action. <br>
Risk: Mallary API keys can authorize posting and account-management actions. <br>
Mitigation: Store the key in a secret manager or masked CI secret, never print or paste it into prompts or logs, and rotate it if exposed. <br>
Risk: Media uploads send selected local files to Mallary storage, the Mallary CDN, and supporting hosting providers. <br>
Mitigation: Verify file paths and contents before upload, avoid sensitive or regulated files, and get explicit approval before remote transfer. <br>
Risk: Read-only discovery can expose profile IDs, platform state, account labels, brand settings, and other operational metadata. <br>
Mitigation: Minimize discovery output and redact profile, platform, account, post, and settings metadata before sharing transcripts or summaries. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sammydigits/skills/mallary) <br>
- [Mallary Website](https://mallary.ai/) <br>
- [Mallary CLI npm Package](https://www.npmjs.com/package/@mallary/cli) <br>
- [Mallary Create API Platform Options](https://docs.mallary.ai/api-reference/endpoint/create#body-platform-options) <br>
- [Mallary Create API Media Rules](https://docs.mallary.ai/api-reference/endpoint/create#platform-specific-media-rules) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose Mallary CLI or API operations; side-effecting actions require explicit approval and credential handling.] <br>

## Skill Version(s): <br>
1.0.8 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

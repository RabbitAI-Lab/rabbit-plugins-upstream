## Description: <br>
Helps agents use Mallary CLI workflows for social-media publishing, scheduling, uploads, comments, analytics, webhooks, settings, and platform connections while preferring read-only discovery before side-effecting actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sammydigits](https://clawhub.ai/user/sammydigits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, CI jobs, and AI agents use this skill to operate Mallary CLI workflows for social-media account discovery, media upload, posting, scheduling, analytics, webhooks, profile settings, and platform connection management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mallary API keys are bearer secrets that can authorize posting and account-management actions. <br>
Mitigation: Store MALLARY_API_KEY in a secret manager or masked CI secret, never print or paste it, and rotate it if exposed. <br>
Risk: Publishing, upload, reply, delete, webhook, settings, and disconnect commands can transmit data, create public content, or change account state. <br>
Mitigation: Start with read-only commands and confirm the exact profile, platform, file, message, webhook URL, setting, or identifier before allowing side-effecting actions. <br>
Risk: Read-only discovery can expose profile IDs, connected-platform state, settings, analytics, and other operational metadata. <br>
Mitigation: Request the minimum needed output and redact sensitive profile, platform, account, post, and settings details before sharing logs or summaries. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sammydigits/skills/mallary) <br>
- [Mallary Website](https://mallary.ai) <br>
- [Mallary CLI npm Package](https://www.npmjs.com/package/@mallary/cli) <br>
- [Mallary API Platform Options](https://docs.mallary.ai/api-reference/endpoint/create#body-platform-options) <br>
- [Mallary API Platform Media Rules](https://docs.mallary.ai/api-reference/endpoint/create#platform-specific-media-rules) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference MALLARY_API_KEY and Mallary profile, platform, post, file, webhook, or settings identifiers; side-effecting commands require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; SKILL.md frontmatter says 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

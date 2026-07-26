## Description: <br>
Publish, schedule, and manage social media posts across Twitter/X, Facebook, Instagram, LinkedIn, TikTok, and YouTube with content calendars, gap analysis, A/B testing, engagement inbox workflows, AI content repurposing, timing suggestions, auto-scheduling, and UTM tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[miprinia](https://clawhub.ai/user/miprinia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, marketers, and social media operators use this skill to guide agents through SocialCannon REST API or MCP setup for publishing, scheduling, analyzing, and managing posts across connected social accounts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live social account actions can publish, reply, retry, delete, disconnect, or repurpose content in ways that may be irreversible. <br>
Mitigation: Require explicit approval before publishing, replying, deleting, retrying posts, disconnecting accounts, or using repurpose post mode. <br>
Risk: Client secret exposure could allow unauthorized API access to connected social accounts. <br>
Mitigation: Store SOCIALCANNON_CLIENT_SECRET only in environment configuration and do not paste it into chats or generated content. <br>
Risk: Immediate A/B tests and repurpose post mode can publish content without a separate scheduling delay. <br>
Mitigation: Prefer draft, scheduled, and preview workflows first, and review generated variants and validation results before allowing live publication. <br>


## Reference(s): <br>
- [SocialCannon homepage](https://socialcannon.app) <br>
- [Socialcannon ClawHub listing](https://clawhub.ai/miprinia/skills/socialcannon) <br>
- [@socialcannon/mcp package](https://www.npmjs.com/package/@socialcannon/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with curl commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and SOCIALCANNON_CLIENT_ID / SOCIALCANNON_CLIENT_SECRET environment variables; actions operate on live connected social accounts.] <br>

## Skill Version(s): <br>
1.10.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

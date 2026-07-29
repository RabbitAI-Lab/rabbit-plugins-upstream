## Description: <br>
Telegram Bot (core.telegram.org). Use this skill for ANY Telegram Bot request - reading, creating, updating, and deleting data. Whenever a task involves Telegram Bot, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users with a connected Telegram Bot use this skill to inspect live connector schemas and run Telegram Bot actions through the OOMOL CLI. It supports messaging, message edits and deletion, chat administration, invite links, join requests, commands, reactions, and webhook operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says several state-changing moderation actions are under-labeled as safe read-like actions. <br>
Mitigation: Require explicit user confirmation before any action that posts, deletes, moderates users, changes permissions or admin status, pins or unpins messages, marks business messages read, or changes webhook or invite settings. <br>
Risk: The skill can operate on real Telegram groups, channels, business messages, and webhooks through a connected account. <br>
Mitigation: Review the exact action name, target chat or message, and payload before execution, especially for write and destructive actions. <br>


## Reference(s): <br>
- [ClawHub Telegram Bot skill page](https://clawhub.ai/oomol/skills/oo-telegram) <br>
- [Telegram Bot documentation](https://core.telegram.org/bots) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before execution and returns Telegram connector responses as JSON when actions run.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

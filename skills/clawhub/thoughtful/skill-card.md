## Description: <br>
Your thoughtful companion for WhatsApp - remembers what matters, helps you stay present in your relationships. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[regalstreak](https://clawhub.ai/user/regalstreak) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to turn WhatsApp messages from direct chats and selected groups into relationship-aware summaries, pending-task tracking, and communication coaching prompts. It helps the user notice replies owed, follow-ups, commitments, important dates, and conversation starters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles private WhatsApp message content and relationship inferences that may be included in prompts sent to an LLM. <br>
Mitigation: Confirm exactly which chats are included, exclude sensitive chats, and review generated prompts before using the skill with real WhatsApp data. <br>
Risk: Summary delivery and recurring automation can send private conversation summaries to a configured Telegram destination. <br>
Mitigation: Review and change delivery configuration, including chat or topic identifiers and cron schedules, before enabling automated summaries. <br>
Risk: Local data files store message-derived context, tasks, contacts, summaries, and CRM state in plaintext. <br>
Mitigation: Apply local file-permission controls and define retention or deletion practices for the data directory. <br>


## Reference(s): <br>
- [Thoughtful ClawHub skill page](https://clawhub.ai/regalstreak/skills/thoughtful) <br>
- [Publisher profile](https://clawhub.ai/user/regalstreak) <br>
- [Skill documentation](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with supporting shell commands and JSON configuration or state files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local WhatsApp-derived data to create an LLM prompt and relationship summary; review generated guidance before acting on it.] <br>

## Skill Version(s): <br>
1.3.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

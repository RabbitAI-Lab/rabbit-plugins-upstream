## Description: <br>
Bookmark Intelligence helps agents monitor X bookmarks, fetch linked article content, analyze it with AI, connect insights to user projects, persist results locally, and optionally send Telegram notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn X bookmarks and linked articles into structured summaries, key concepts, action items, project-specific suggestions, local knowledge-base records, and optional Telegram alerts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to provide sensitive X session cookies. <br>
Mitigation: Use a dedicated low-risk X account where possible, keep .env permissions strict, and rotate or remove cookies when the skill is no longer needed. <br>
Risk: Background polling can continue collecting bookmark and linked-article content after setup. <br>
Mitigation: Disable daemon mode unless continuous monitoring is required and use conservative polling intervals. <br>
Risk: Bookmark and linked-article content may be sent to AI services for analysis. <br>
Mitigation: Avoid processing confidential bookmarks and review the configured AI provider before enabling analysis. <br>
Risk: Telegram notifications can disclose summaries, action items, project context, and source links. <br>
Mitigation: Disable Telegram unless needed and verify bot, chat, and token configuration before sending alerts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bookmark-intelligence) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide creation of local JSON knowledge-base files and notification configuration.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

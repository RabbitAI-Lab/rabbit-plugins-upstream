## Description: <br>
Agent Telegram defines Telegram message-routing conventions, role account IDs, reporting moments, and templates for agents to send task status updates to a fixed user. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and developers use this skill to standardize Telegram task status updates across defined agent roles during multi-agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes Telegram messages to a hardcoded recipient ID. <br>
Mitigation: Use it only when Telegram ID 5440561025 is the intended recipient, or update the recipient and templates to approved routing before use. <br>
Risk: Task updates may include project status, file paths, outputs, and troubleshooting details. <br>
Mitigation: Avoid sending secrets, internal diagnostics, or sensitive data over Telegram; review message content before sending. <br>
Risk: Telegram Bot tokens are required for the configured accounts. <br>
Mitigation: Protect bot-token configuration files from source control and broad local access. <br>


## Reference(s): <br>
- [agent-telegram ClawHub release](https://clawhub.ai/thcjp/skills/agent-telegram) <br>
- [Telegram Bot API](https://api.telegram.org) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, API Calls, Guidance] <br>
**Output Format:** [Markdown instructions with inline message-call examples and JSON output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Telegram status text, role labels, account IDs, file paths, output summaries, and troubleshooting details.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

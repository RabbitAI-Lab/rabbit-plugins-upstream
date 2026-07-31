## Description: <br>
Obsidian persistent memory system: AI-delivered session continuity, task tracking, decision records, and project context for AI agents. Payment verification via clawtip. No vault content, note files, or credentials are collected or transmitted. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill after clawtip payment verification to receive conversational help with work logs, task tracking, decision records, session continuity, and project context management for Obsidian-oriented workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The service is payment-gated and delivered through chat after clawtip verification. <br>
Mitigation: Install only when a paid, chat-delivered memory-management service is acceptable for the intended workflow. <br>
Risk: The user's question is saved in a local order file and echoed to script output. <br>
Mitigation: Do not include secrets, passwords, API keys, private note contents, or other sensitive data in the question. <br>
Risk: The skill writes local order records for payment verification. <br>
Mitigation: Review local order files under the documented OpenClaw orders directory and remove them according to local retention needs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/obsidian-memory-system-clawhub-reviewfix) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and terminal output with JSON_RESULT fields from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Conversation-delivered memory-management guidance after payment verification; local order records include the user's question.] <br>

## Skill Version(s): <br>
3.1.2 (source: frontmatter and server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

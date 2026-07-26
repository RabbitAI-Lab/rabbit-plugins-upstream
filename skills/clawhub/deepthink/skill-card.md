## Description: <br>
DeepThink helps an agent manage a user's personal knowledge, stored insights, tasks, transcripts, and chats through the DeepThink API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[addisonhellum](https://clawhub.ai/user/addisonhellum) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and their agents use this skill to keep a DeepThink account current: searching personal records, saving new insights, managing todos and daily plans, and using transcripts or chats for context-aware assistance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks an agent to maintain broad personal memory and may store sensitive facts about the user. <br>
Mitigation: Require explicit user confirmation before storing sensitive facts, and verify that stored data can be reviewed, paused, and deleted. <br>
Risk: Live transcript text may include misheard speech, background audio, or other speakers rather than the user's own instructions. <br>
Mitigation: Confirm speaker identity and user intent before creating records, sending messages, modifying todos, or taking other significant actions from transcript content. <br>
Risk: The skill can prompt proactive outreach through an external messaging channel. <br>
Mitigation: Require approval before sending any external message and make it clear how the user can pause ambient assistance. <br>
Risk: The skill suggests changing local long-term behavior files such as SOUL.md and HEARTBEAT.md. <br>
Mitigation: Review proposed file changes before applying them and avoid adding reminders that expand data collection beyond the user's intent. <br>


## Reference(s): <br>
- [ClawHub DeepThink listing](https://clawhub.ai/addisonhellum/skills/deepthink) <br>
- [DeepThink API](https://api.deepthink.co) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with HTTP endpoints and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided DeepThink API key and may guide the agent to create or update records, todos, daily plans, transcripts, chats, and local reminder files.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Enhance Telegram replies with context-aware dynamic CTA buttons (Smart Launcher UI). Use when replying to users on Telegram to provide relevant, time-sensitive, and task-oriented options for better interaction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dendyadinirwana](https://clawhub.ai/user/dendyadinirwana) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Telegram bot builders and agent operators use this skill to add relevant quick-action CTA buttons to Telegram replies based on time of day, task context, and user workflow. It helps users choose follow-up actions while preserving a manual input fallback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Callback data can trigger unintended workflows if a Telegram backend treats callback_data values as executable routing input. <br>
Mitigation: Review callback routing before deployment and prefer namespaced callback IDs for backend actions. <br>
Risk: Proactive CTA buttons may suggest actions that are not appropriate for a specific bot or user context. <br>
Mitigation: Review button presets and only enable proactive buttons that fit the bot's user experience and permissions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dendyadinirwana/skills/tg-smart-cta) <br>
- [Time-Based Button Presets](references/time_logic.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown guidance with Telegram button payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Suggests Telegram message buttons using text and callback_data fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
AI reminder system based on the Ebbinghaus forgetting curve that activates only with explicit student or guardian consent and supports pause, cancel, minimal sharing, and do-not-disturb boundaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External students, guardians, and education agents use this skill to set consent-based study, task, exploration, and follow-up reminders in IM workflows. It helps schedule spaced review prompts, manage reminder queues, and explain fallback behavior when the host platform cannot wake the agent proactively. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Repeated non-response could still lead to ongoing weekly reminders. <br>
Mitigation: Require renewed confirmation or pause the reminder series after repeated silence, and make pause and cancel controls visible in every reminder flow. <br>
Risk: Reminder timing may depend on learning-profile signals from another skill. <br>
Mitigation: Use learning-profile timing only after explicit sharing consent and limit exchanged data to the minimum timing summary needed. <br>
Risk: Active push reminders depend on a host platform with scheduled wake-up capability. <br>
Mitigation: When scheduled wake-up is unavailable, disclose the limitation and fall back to user-triggered checks or catch-up prompts when the user next opens a conversation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder) <br>
- [Ebbinghaus schedule reference](references/ebbinghaus-schedule.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown and conversational text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces reminder plans, reminder message templates, queue summaries, consent prompts, pause or cancel guidance, and platform fallback guidance.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

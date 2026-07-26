## Description: <br>
Connect local agents to OnePilot for OPC and AI startup event recommendations, saved preferences, subscriptions, feedback, and registration assistance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[y09749204-gif](https://clawhub.ai/user/y09749204-gif) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and local-agent operators use this skill to bind an agent to OnePilot, receive personalized OPC and AI startup event recommendations, maintain preference and application memory, set local subscriptions, record feedback, report issues, and draft event application answers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OnePilot cloud can receive recommendation preferences, availability or memory fields, application profile data, answer examples, and feedback. <br>
Mitigation: Install only if this data sharing is acceptable, keep shared profile and memory details concise, and avoid sending sensitive private content. <br>
Risk: The skill includes automatic update behavior before normal use. <br>
Mitigation: Require manual confirmation or review for updates in environments where automatic replacement of skill files is not acceptable. <br>
Risk: Mailbox or calendar tool access can expose more personal data than the task requires. <br>
Mitigation: Prefer pasted verification codes when mailbox access is unnecessary, decline email or calendar access unless needed for the current task, and require explicit confirmation before calendar writes. <br>


## Reference(s): <br>
- [OnePilot Website](https://onepilot.zeabur.app) <br>
- [ClawHub Skill Page](https://clawhub.ai/y09749204-gif/skills/onepilot-skill) <br>
- [Platform Adapter Notes](references/adapters.md) <br>
- [Activity Intent Few-Shots](references/activity-intent-few-shots.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and structured command arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include OnePilot URLs, event recommendation summaries, local configuration guidance, and application-answer drafts.] <br>

## Skill Version(s): <br>
0.1.19 (source: ClawHub release metadata; artifact VERSION, CHANGELOG, and package.json report 0.1.19-alpha) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

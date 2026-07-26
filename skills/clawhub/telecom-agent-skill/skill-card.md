## Description: <br>
Turn your AI Agent into a Telecom Operator. Bulk calling, ChatOps, and Field Monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kflohr](https://clawhub.ai/user/kflohr) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent create and monitor outbound calling campaigns, place individual calls, retrieve call memory, and coordinate approvals through chat and Telegram workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can let an agent initiate high-volume outbound calling campaigns or global calls. <br>
Mitigation: Use a limited Twilio account or subaccount, verified opt-in call lists, explicit campaign approvals, and strict spend and rate limits. <br>
Risk: Call recording and transcript access can expose sensitive communications. <br>
Mitigation: Define and enforce recording consent, transcript access, retention, and deletion policies before deployment. <br>
Risk: Telegram-based remote administration can approve high-impact telecom actions. <br>
Mitigation: Restrict Telegram administration to authorized admins and require explicit approval flows for high-risk actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kflohr/skills/telecom-agent-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent-facing telecom operation guidance, command examples, and JSON-oriented status checks.] <br>

## Skill Version(s): <br>
0.1.5 (source: ClawHub release metadata; artifact frontmatter reports 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

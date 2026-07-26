## Description: <br>
Auto-capture chat to Hermes DB, load context on fresh chats, scheduled DB maintenance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sunme1977](https://clawhub.ai/user/sunme1977) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and advanced users use this skill to give an agent persistent local memory with HermesClawZero, including session context loading, concise fact capture, requested chat backup, and scheduled database maintenance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables broad automatic conversation retention and silent reuse of stored context. <br>
Mitigation: Install only when default-on long-term memory is intended, keep retention and deletion expectations explicit, and avoid sharing secrets or sensitive personal data while the skill is active. <br>
Risk: Local Sidecar scripts can affect stored memory and daily reminders. <br>
Mitigation: Review the local Sidecar scripts before use, especially daily_reminder.py, and confirm notification controls before enabling scheduled background jobs. <br>
Risk: Persisted memory may include user facts, preferences, project details, or chat summaries beyond the current session. <br>
Mitigation: Use clear consent, scope memories where practical, and periodically review or prune local stored context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sunme1977/skills/hermes-skill) <br>
- [Server-resolved GitHub provenance](https://github.com/SunMe1977/HermesClawZero-ConfigSidecar/tree/main/hermes-skill) <br>
- [Publisher profile](https://clawhub.ai/user/sunme1977) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown guidance with inline shell commands and scheduler configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call local HermesClawZero memory and maintenance scripts when activated by the agent.] <br>

## Skill Version(s): <br>
0.1.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

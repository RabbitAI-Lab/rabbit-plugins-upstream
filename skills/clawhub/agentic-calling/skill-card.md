## Description: <br>
Enable AI agents to make, receive, transcribe, route, and record phone calls using Twilio with customizable voice messages and IVR support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kellyclaudeai](https://clawhub.ai/user/kellyclaudeai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to let agents initiate Twilio calls and SMS messages, monitor call status, and configure call flows such as reminders, alerts, IVR menus, recordings, and transcriptions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can place real calls and send SMS through a Twilio account, creating billing and unintended-contact risk. <br>
Mitigation: Require recipient allowlists, human approval for outbound or bulk sends, and rate and spend limits before use. <br>
Risk: Call recording and transcription can capture sensitive or regulated conversations. <br>
Mitigation: Define consent rules before recording or transcription and protect any stored call data. <br>
Risk: Twilio credentials grant account-level calling and messaging capability. <br>
Mitigation: Store credentials in protected secret storage and avoid committing credential files. <br>
Risk: Untrusted message text may be unsafe until the make-call.sh encoding bug identified in security guidance is fixed. <br>
Mitigation: Use trusted templates or sanitize and encode message text before allowing autonomous calls. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kellyclaudeai/skills/agentic-calling) <br>
- [Publisher Profile](https://clawhub.ai/user/kellyclaudeai) <br>
- [Twilio Voice Documentation](https://www.twilio.com/docs/voice) <br>
- [README](README.md) <br>
- [Skill Documentation](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown guidance with shell command examples and Twilio API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May initiate real calls, SMS messages, recordings, transcriptions, and billable Twilio activity when executed with valid credentials.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

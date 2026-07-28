## Description: <br>
CommPeak (commpeak.com). Use this skill for any CommPeak request: reading, creating, and updating data through OOMOL-connected CommPeak actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect CommPeak TextPeak resources and send SMS messages through an OOMOL-connected CommPeak account after confirming write payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send SMS messages through a CommPeak TextPeak stream. <br>
Mitigation: Confirm recipients, message text, stream details, and expected effect before running send_sms. <br>
Risk: Stream-token retrieval gives access to sensitive messaging credentials. <br>
Mitigation: Treat get_stream_token output as sensitive account data and avoid exposing it unnecessarily. <br>
Risk: The skill operates a user's CommPeak account through OOMOL-connected credentials. <br>
Mitigation: Install and use it only when the agent is intended to access that CommPeak account. <br>


## Reference(s): <br>
- [CommPeak homepage](https://www.commpeak.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-commpeak) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live OOMOL connector schema inspection before action execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

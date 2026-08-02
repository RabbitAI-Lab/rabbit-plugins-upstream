## Description: <br>
Quriiri helps agents operate a connected Quriiri account to read SMS delivery data, list sender IDs, and send SMS messages through OOMOL's oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to interact with their connected Quriiri account for SMS status lookup, sender ID listing, and approved SMS sending. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can operate a connected Quriiri account and send SMS messages with billing or account impact. <br>
Mitigation: Review the SMS recipient, sender, message body, and cost implications before approving send_sms actions. <br>
Risk: Authentication, missing connection scope, expired credentials, or insufficient credit can block connector actions. <br>
Mitigation: Run login, connection, or billing setup only after a command fails for the matching reason. <br>


## Reference(s): <br>
- [Quriiri homepage](https://quriiri.fi/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-quriiri) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

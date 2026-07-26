## Description: <br>
QQ Mail (mail.qq.com). Use this skill for ANY QQ Mail request - reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate a connected QQ Mail account through OOMOL, including reading, searching, sending, replying, forwarding, moving, marking, deleting messages, and downloading attachments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send, move, mark, and delete QQ Mail messages through OOMOL-connected credentials. <br>
Mitigation: Review write or delete payloads carefully and obtain explicit user approval before mailbox state changes. <br>
Risk: First-time setup and account connection steps grant an agent-operated workflow access to a QQ Mail account. <br>
Mitigation: Run installer, login, and connection steps only when the user trusts the OOMOL CLI and needs to connect the account. <br>


## Reference(s): <br>
- [QQ Mail homepage](https://mail.qq.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [QQ Mail skill page](https://clawhub.ai/oomol/skills/oo-qq-mail) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the oo CLI to inspect live connector schemas and run QQ Mail actions; state-changing and destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

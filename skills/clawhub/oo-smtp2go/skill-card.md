## Description: <br>
SMTP2GO lets agents operate an OOMOL-connected SMTP2GO account for account summaries, sender data, templates, activity search, API key permission reads, and email sending. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate SMTP2GO through the OOMOL oo CLI connector, including reading account status, searching email activity, reviewing sender and template data, checking API key permissions, and sending standard JSON emails with user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The send_email action can send email from the connected SMTP2GO account. <br>
Mitigation: Confirm the exact recipient, sender, subject, body, and intended effect with the user before running send_email. <br>
Risk: Read actions can expose sensitive account information, including account activity, sender data, templates, and API key permissions. <br>
Mitigation: Treat connector output as sensitive and avoid sharing or storing it beyond the user's requested task. <br>
Risk: Incorrect payloads can cause unintended email sends or failed connector actions. <br>
Mitigation: Inspect the live action schema with oo connector schema before constructing payloads. <br>


## Reference(s): <br>
- [SMTP2GO ClawHub skill page](https://clawhub.ai/oomol/skills/oo-smtp2go) <br>
- [SMTP2GO homepage](https://www.smtp2go.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or run oo CLI connector commands and summarize JSON responses.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Standards Ops Gadget is a CLI for IMAP, SMTP, CalDAV, CardDAV, and WebDAV workflows and an open-standards alternative to Google and Microsoft ops CLIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[visionik](https://clawhub.ai/user/visionik) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and AI agents use this skill to manage mail, calendars, contacts, tasks, files, meeting invites, and account setup through standards-based CLI commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI can access and change sensitive mail, calendar, contacts, tasks, and file data. <br>
Mitigation: Review commands before execution, use only accounts trusted for this CLI, and avoid noninteractive destructive actions unless the workflow is already validated. <br>
Risk: Credential and transport choices can expose account access if used carelessly. <br>
Mitigation: Use system keychain storage, prefer TLS or HTTPS with certificate validation, avoid command-line passwords, and avoid insecure transport flags outside isolated testing. <br>
Risk: Mail-triggered automation can run local commands through idle execution behavior. <br>
Mitigation: Use idle command execution only with fully trusted commands and accounts, and review the exact command before enabling it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/visionik/skills/sogcli) <br>
- [Publisher profile](https://clawhub.ai/user/visionik) <br>
- [sog project homepage](https://github.com/visionik/sogcli) <br>
- [Go install package](https://github.com/visionik/sogcli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Command output may be human-readable text, JSONL, or TSV when the CLI is executed.] <br>

## Skill Version(s): <br>
0.3.0 (source: release metadata and CHANGELOG, released 2026-01-24) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Microsoft Ops Gadget - CLI for Microsoft 365 (Mail, Calendar, Drive, Contacts, Tasks, Word, PowerPoint, Excel, OneNote). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[visionik](https://clawhub.ai/user/visionik) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use Mog to let an agent generate and run Microsoft 365 CLI workflows for mail, calendar, OneDrive, contacts, tasks, Word, PowerPoint, Excel, and OneNote. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mog can send, change, and delete live Microsoft 365 account data. <br>
Mitigation: Require explicit human review before running delete, clear, send, update, upload, move, rename, copy, or create commands against a live account. <br>
Risk: Mog requires broad delegated Microsoft 365 permissions. <br>
Mitigation: Use the least-privileged or isolated Azure app that still supports the intended workflow, and avoid granting unnecessary delegated scopes. <br>
Risk: Mog stores broad OAuth access tokens in file storage by default. <br>
Mitigation: Prefer keychain storage when possible and treat ~/.config/mog/tokens.json as sensitive when file storage is used. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/visionik/skills/mogcli) <br>
- [README](README.md) <br>
- [Skill documentation](SKILL.md) <br>
- [Go package documentation](https://pkg.go.dev/github.com/visionik/mogcli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that read, send, update, or delete live Microsoft 365 account data.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release metadata and changelog, released 2026-01-26) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

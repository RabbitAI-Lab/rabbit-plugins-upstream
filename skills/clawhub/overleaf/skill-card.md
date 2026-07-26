## Description: <br>
Access Overleaf projects via CLI for reading and writing LaTeX files, syncing local files, downloading projects, managing project structure, and accepting project invitations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[easonc13](https://clawhub.ai/user/easonc13) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and writing teams use this skill to let an agent interact with Overleaf projects through the pyoverleaf CLI and Python API while relying on the user's logged-in browser session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can reuse a logged-in browser session and keychain access to act on the user's Overleaf account. <br>
Mitigation: Use a dedicated browser profile or separate Overleaf account, and grant keychain access only after reviewing the installed pyoverleaf version. <br>
Risk: Write, delete, sync, download, and invite-acceptance actions can make live changes to Overleaf projects. <br>
Mitigation: Require explicit user confirmation before any account-changing action and rely on Overleaf history to review or revert edits. <br>
Risk: The evidence security summary flags broad browser-session access without enough built-in safeguards. <br>
Mitigation: Install only after reviewing the skill behavior and applying local safeguards for confirmation, account separation, and dependency pinning. <br>


## Reference(s): <br>
- [ClawHub Overleaf Skill](https://clawhub.ai/easonc13/skills/overleaf) <br>
- [pyoverleaf GitHub](https://github.com/jkulhanek/pyoverleaf) <br>
- [OpenClaw GitHub](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and Python code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include commands or code that read, write, sync, download, delete, or accept invitations for live Overleaf projects.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

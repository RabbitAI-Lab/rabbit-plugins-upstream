## Description: <br>
A JSON CLI that lets an agent create and manage a local KeePass (.kdbx) database, including entries, groups, and attachments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[beocca](https://clawhub.ai/user/beocca) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation agents use this skill to operate a local KeePass vault through predictable shell commands and single-object JSON responses. It supports creating databases, inspecting vault metadata, and managing entries, groups, and attachments without an interactive human operator. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent with this skill can operate the selected KeePass database, including creating, editing, moving, and deleting vault contents. <br>
Mitigation: Install only for agents that are intended to manage that vault, and restrict the .env and .kdbx files to the appropriate local user. <br>
Risk: Entry passwords are supplied through command arguments for add-entry and edit-entry and may appear in shell history or command logs. <br>
Mitigation: Avoid logging invocations that contain entry passwords and prefer operational environments that do not persist sensitive command lines. <br>
Risk: Secret values and attachment bytes can be emitted when --show-secrets or --include-data is used. <br>
Mitigation: Use those flags only when the downstream task requires the data, and avoid sending resulting JSON to shared logs or untrusted tools. <br>
Risk: --permanent, create --force, and attachment binary deletion can bypass normal recovery safeguards or overwrite data. <br>
Mitigation: Treat these flags as high-risk operations and require explicit review before running them against valuable vaults. <br>


## Reference(s): <br>
- [ClawHub Keepass-CLI skill page](https://clawhub.ai/beocca/skills/keepass-cli) <br>
- [pykeepass project](https://github.com/libkeepass/pykeepass) <br>
- [Bundled pykeepass reference docs](artifact/pykeepass_docs.html) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON response contracts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI prints exactly one JSON object per invocation; secrets and attachment data are omitted unless explicit flags request them.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

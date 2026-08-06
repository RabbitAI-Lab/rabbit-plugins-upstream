## Description: <br>
Use the Buildin CLI safely for authorized API, content, and file tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[buildin](https://clawhub.ai/user/buildin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect Buildin CLI state, authenticate safely, and perform authorized Buildin API, content, database, search, Markdown, and file workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated commands can create or update Buildin pages, databases, blocks, Markdown content, and files. <br>
Mitigation: Review the active Buildin account, confirm exact targets and expected impact, and require explicit approval before create, update, append, upload, replace, or raw API write commands. <br>
Risk: Bearer tokens or saved credentials can be exposed through chat, command lines, logs, request bodies, or files. <br>
Mitigation: Use saved CLI credentials, BUILDIN_TOKEN through an approved secret channel, or browser/manual login; avoid --token in shared commands and redact credentials from outputs. <br>
Risk: Installing or updating the CLI can execute a downloaded binary. <br>
Mitigation: Use only the official Buildin CDN after explicit approval, show source, version, and SHA-256 hash, and stop for manual installation if official integrity data is unavailable. <br>


## Reference(s): <br>
- [ClawHub Buildin CLI skill page](https://clawhub.ai/buildin/skills/buildin-skills) <br>
- [Buildin CLI official installer](https://cdn.buildin.ai/buildin-cli/install) <br>
- [Buildin CLI Windows installer](https://cdn.buildin.ai/buildin-cli/install.ps1) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON] <br>
**Output Format:** [Markdown guidance with bash commands and JSON-oriented CLI workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended for authenticated Buildin CLI workflows and may include local file paths, request body files, page Markdown, or JSON command output.] <br>

## Skill Version(s): <br>
1.0.5 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

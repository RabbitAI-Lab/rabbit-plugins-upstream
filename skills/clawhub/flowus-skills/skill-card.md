## Description: <br>
Use the FlowUs CLI safely for authorized FlowUs API, content, database, page, Markdown, and file tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flowus](https://clawhub.ai/user/flowus) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, workspace operators, and agents use this skill to inspect FlowUs CLI capabilities, authenticate safely, and perform authorized FlowUs page, block, database, search, Markdown, and file workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents to read or modify FlowUs workspace content through authenticated CLI commands. <br>
Mitigation: Verify authentication with doctor and whoami, use approved credential storage, read current targets when feasible, and require explicit confirmation before creates, updates, uploads, replacements, logins, installs, or updates. <br>
Risk: FlowUs credentials could be exposed through chat, command arguments, logs, shell history, or files. <br>
Mitigation: Use preconfigured FLOWUS_TOKEN, saved credentials, or an approved secret channel; do not pass bearer tokens with --token; redact credentials from command output. <br>
Risk: Installer or update execution could run unverified code if integrity data is unavailable. <br>
Mitigation: Use only the official FlowUs CDN after explicit approval, show source, version, and SHA-256 hash, compare with official integrity data, and stop for manual installation if verification is unavailable. <br>


## Reference(s): <br>
- [FlowUs CLI Skill Listing](https://clawhub.ai/flowus/skills/flowus-skills) <br>
- [FlowUs Publisher Profile](https://clawhub.ai/user/flowus) <br>
- [FlowUs CLI Installer](https://cdn2.flowus.cn/flowus-cli/install) <br>
- [FlowUs CLI Windows Installer](https://cdn2.flowus.cn/flowus-cli/install.ps1) <br>
- [FlowUs API Base URL](https://api.flowus.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON-oriented CLI output, and local file instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses FlowUs CLI help and JSON output for command discovery; remote writes, installs, updates, and login flows require explicit user approval.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

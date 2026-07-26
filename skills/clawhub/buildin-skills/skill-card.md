## Description: <br>
Guides agents to use the Buildin CLI for authenticated Buildin API, page, block, database, search, Markdown, and file workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[buildin](https://clawhub.ai/user/buildin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workspace operators use this skill when an agent needs to inspect Buildin CLI help, verify authentication, and perform authorized Buildin content, database, search, Markdown, and file tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may install or update the Buildin CLI from an unverified installer. <br>
Mitigation: Require explicit user approval, use the official Buildin CDN URL, verify an official checksum or signature, and stop if integrity data is unavailable. <br>
Risk: Buildin credentials could be exposed through chat, shell history, process listings, or command output. <br>
Mitigation: Use saved credentials, preconfigured environment variables, or an approved secret channel; avoid command-line tokens and redact any credential that appears in output. <br>
Risk: Remote write operations can change Buildin pages, blocks, databases, or files. <br>
Mitigation: Confirm the exact target, operation, and expected impact; read current content when feasible; use version or ETag safeguards when available; and request confirmation when target or content is incomplete. <br>


## Reference(s): <br>
- [Buildin CLI Skill on ClawHub](https://clawhub.ai/buildin/skills/buildin-skills) <br>
- [Buildin CLI Installer](https://cdn.buildin.ai/buildin-cli/install) <br>
- [Buildin CLI Windows Installer](https://cdn.buildin.ai/buildin-cli/install.ps1) <br>
- [Buildin API Base URL](https://api.buildin.ai) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown, code] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-oriented CLI workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Buildin CLI responses may be JSON; write operations require explicit target and impact confirmation.] <br>

## Skill Version(s): <br>
1.0.4 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

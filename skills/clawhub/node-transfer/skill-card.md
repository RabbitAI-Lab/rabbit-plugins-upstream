## Description: <br>
Node Transfer enables high-speed, memory-efficient file transfer between OpenClaw nodes using token-protected HTTP streams without Base64 encoding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eisonme](https://clawhub.ai/user/eisonme) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use Node Transfer to move large files between OpenClaw nodes without loading files into agent memory or encoding them as Base64. It is intended for trusted node-to-node transfers where persistent scripts, fast install checks, and progress-reporting command output improve repeated transfer workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated transfer URLs and bearer tokens can grant access to the transfer while the sender is running. <br>
Mitigation: Treat URLs and tokens as secrets, share them only over trusted channels, and use the skill only on trusted networks. <br>
Risk: Deployment output includes PowerShell intended for remote execution on target nodes. <br>
Mitigation: Review generated PowerShell before running it remotely and install only when the publisher and target environment are trusted. <br>
Risk: Receiver behavior writes files to caller-selected destination paths and creates missing directories. <br>
Mitigation: Choose trusted destination paths where file creation, permissions, or cleanup of partial files cannot affect important data. <br>
Risk: The security summary identifies under-scoped code execution and network/file-write behaviors. <br>
Mitigation: Follow the release guidance to review the skill before installation and restrict use to trusted nodes and trusted paths. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/eisonme/skills/node-transfer) <br>
- [README](artifact/README.md) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [Investigation report](artifact/INVESTIGATION_REPORT.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript and shell command snippets; transfer scripts emit JSON status, progress, and transfer metadata.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Progress output can include byte counts, duration, transfer speed, destination path, generated URL, and bearer token.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version and artifact/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

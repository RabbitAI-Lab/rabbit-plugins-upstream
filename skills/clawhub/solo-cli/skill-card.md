## Description: <br>
Monitor and interact with SOLO.ro accounting platform via CLI or TUI for summaries, revenues, expenses, queue items, e-Factura documents, company details, uploads, and safe solo-cli command translation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rursache](https://clawhub.ai/user/rursache) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to ask an agent to inspect SOLO.ro accounting data, summarize revenues and expenses, view company and e-Factura information, or propose solo-cli commands for upload and queue workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose sensitive accounting data and local SOLO.ro credentials or session cookies. <br>
Mitigation: Treat config and cookie files as credentials, restrict access to them, and avoid sharing command output that contains private accounting data. <br>
Risk: Upload and queue delete commands can change account state. <br>
Mitigation: Require explicit confirmation of the SOLO.ro account, target file, and queue item ID before allowing an agent to run write or delete commands. <br>
Risk: Installation depends on the Homebrew tap and CLI binary provided by the publisher. <br>
Mitigation: Install only when the publisher and Homebrew tap are trusted for the target environment. <br>


## Reference(s): <br>
- [solo-cli help man page](references/help-man-page.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that read accounting data or perform upload and queue-delete actions requiring explicit user confirmation.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

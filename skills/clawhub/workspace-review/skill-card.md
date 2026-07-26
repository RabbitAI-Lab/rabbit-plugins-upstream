## Description: <br>
Audit workspace structure and memory files against OpenClaw conventions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ortegarod](https://clawhub.ai/user/ortegarod) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw workspace maintainers use this skill to audit workspace structure, memory files, git hygiene, file sizes, and skill organization against OpenClaw conventions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect local workspace and memory files that contain private context or sensitive information. <br>
Mitigation: Run it only on intended OpenClaw workspaces, and keep API keys, passwords, and personal data out of markdown and memory files. <br>
Risk: The included status script can report git status and API-key-like strings from markdown files. <br>
Mitigation: Review generated output before sharing it outside the workspace, and invoke the skill explicitly for workspace maintenance. <br>


## Reference(s): <br>
- [OpenClaw Workspace Conventions](references/openclaw-conventions.md) <br>
- [Workspace Review Checklist](references/checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown review report with optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Summarizes passing checks, warnings, issues, and recommendations.] <br>

## Skill Version(s): <br>
1.0.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

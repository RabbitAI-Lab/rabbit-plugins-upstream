## Description: <br>
Use when addressing computer configuration failures, software or package installation errors, command line exceptions, network connectivity bugs, or system runtime crashes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hermes186](https://clawhub.ai/user/hermes186) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support engineers, and agent users use this skill to diagnose software, package installation, configuration, network, permission, and runtime failures with structured checklists, verification steps, and local troubleshooting memory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill records troubleshooting history in local .troubleshooting-memory/ Markdown files, which may capture sensitive logs, credentials, tokens, or private details if included by the user. <br>
Mitigation: Review troubleshooting notes before saving and omit secrets, credentials, tokens, private logs, and customer data. <br>
Risk: The skill includes powerful remediation examples such as sudo commands, global Git configuration changes, Docker group changes, and forceful process termination. <br>
Mitigation: Treat repair commands as proposals, review each command before running it, and prefer diagnostic or narrowly scoped commands before applying system changes. <br>


## Reference(s): <br>
- [Diagnostic Templates & Checklists](references/diagnostic-templates.md) <br>
- [Troubleshooting Memory Format Specification](references/memory-format.md) <br>
- [Common Solutions Quick Reference Index](references/common-solutions.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown with inline shell commands and local troubleshooting notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update .troubleshooting-memory/ Markdown files in the active workspace.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

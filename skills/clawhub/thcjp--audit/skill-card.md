## Description: <br>
Audit helps agents inspect code, contracts, and assets and return structured audit-oriented results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical reviewers use this skill to audit code, contracts, assets, and related development or deployment work. Because the skill can request command execution, it is best used in environments where command use is expected and reviewed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can request shell command execution for broad audit tasks. <br>
Mitigation: Use it only in workspaces where command execution is acceptable, and require explicit approval before commands read sensitive files, modify files, deploy, install packages, or contact external services. <br>
Risk: The audit scope is broad and the artifact gives limited detail about when commands should run. <br>
Mitigation: Review proposed commands and audit conclusions before acting on them, especially for code, contracts, assets, deployment, or security decisions. <br>
Risk: The release evidence and artifact disagree on license terms. <br>
Mitigation: Confirm whether MIT-0 or Proprietary terms govern this release before publication or installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/audit) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or structured text, with JSON examples and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include audit findings, configuration advice, error-handling guidance, and command suggestions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

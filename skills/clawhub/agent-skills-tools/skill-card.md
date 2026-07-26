## Description: <br>
Security audit and validation tools for the Agent Skills ecosystem that scan skill packages for credential leaks, risky file access, network requests, file permission issues, and Git history secrets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rongself](https://clawhub.ai/user/rongself) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, maintainers, and security reviewers use this skill to run local heuristic checks on agent skill packages before installation or release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scanner is heuristic and may miss vulnerabilities or flag benign patterns. <br>
Mitigation: Treat scan results as triage and combine them with manual review before installing or releasing a skill. <br>
Risk: Scan output may include file paths or matching lines from scanned content. <br>
Mitigation: Run it only on directories you intend to inspect and review or redact raw output before sharing it. <br>


## Reference(s): <br>
- [Agent Skills Tools on ClawHub](https://clawhub.ai/rongself/skills/agent-skills-tools) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and local scanner output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scan output may include file paths or matching lines from the scanned content.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Conducts read-only source-code security audits and reports directly evidenced vulnerabilities, privacy issues, severity, and remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kylehuan](https://clawhub.ai/user/kylehuan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and security reviewers use this skill to inspect source code for vulnerabilities, privacy issues, and insecure patterns, then produce actionable findings with severity and remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security reports and optional .shield_security/ artifacts may expose real vulnerabilities, file paths, or discovered secrets. <br>
Mitigation: Treat generated reports as sensitive, review them before sharing, and require explicit approval before saving artifacts to the workspace. <br>
Risk: A code review based on static evidence can miss issues or report false positives when repository context is incomplete. <br>
Mitigation: Require direct code evidence for every finding and have a reviewer confirm impact before acting on the report. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Files] <br>
**Output Format:** [Markdown security report with vulnerability findings, severity, evidence, and recommendations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Optional local report artifacts may be written only when explicitly requested by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

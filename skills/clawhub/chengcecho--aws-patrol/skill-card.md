## Description: <br>
Automated AWS infrastructure patrol that collects EC2, RDS, ELB, security posture, cost, AWS Health, and SMS registration data and generates a visual HTML report with optional screenshot delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chengcecho](https://clawhub.ai/user/chengcecho) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and security or cost reviewers use this skill to run periodic AWS health checks, identify infrastructure issues, review security posture, and summarize cost or waste signals in a report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can collect sensitive AWS inventory, security posture, and cost data into local reports. <br>
Mitigation: Use a dedicated least-privilege AWS profile, set AWS_PATROL_OUTPUT to a private directory, and restrict report file permissions. <br>
Risk: Scheduled runs or chat delivery can expose cloud details to unintended recipients. <br>
Mitigation: Review and redact generated reports before enabling scheduled delivery or forwarding screenshots to messaging channels. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chengcecho/aws-patrol) <br>
- [README](README.md) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files, Analysis] <br>
**Output Format:** [Markdown guidance plus JSON, HTML, and PNG report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local AWS patrol detail JSON, security and cost JSON, a daily HTML report, and an optional screenshot for messaging delivery.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

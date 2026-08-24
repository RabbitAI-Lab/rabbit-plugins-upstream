## Description:

Inspects ECS instance health, detects memory, disk, CPU, load, and resource-leak anomalies, and can trigger deep SysOM diagnosis for critical memory issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operations engineers and support teams use this skill to inspect Alibaba Cloud ECS instance health, identify resource anomalies, and produce diagnosis-oriented inspection reports for troubleshooting and routine risk checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct users to install the SysOM CLI through a curl-to-sudo installer.

Mitigation: Use the installer only after trusting the upstream SysOM path and reviewing the command in the target environment.

Risk: Inspection flows can activate SysOM and install a persistent agent on cloud instances.

Mitigation: Run with deliberately scoped regions and instance lists, confirm activation prompts intentionally, and treat agent installation as an infrastructure change.

Risk: Alibaba Cloud credentials and generated reports may expose operational details.

Mitigation: Use least-privilege RAM permissions, avoid sharing AK/SK values in the agent session, and handle local report files as sensitive operational data.

## Reference(s):

- [RAM Policies](references/ram-policies.md)
- [Inspection Report Template](references/report-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local Markdown inspection reports under inspection-reports/ during fallback CLI execution.]

## Skill Version(s):

0.0.4 (source: ClawHub release metadata; artifact frontmatter version is 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

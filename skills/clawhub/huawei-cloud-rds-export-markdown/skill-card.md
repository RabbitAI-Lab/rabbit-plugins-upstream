## Description:

Lists Huawei Cloud RDS instances in a selected region and exports their details to a local Markdown report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud administrators and developers use the skill to save regional RDS inventories as Markdown reports for operations reviews, asset tracking, and handovers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required telemetry wrapper is unaudited, so its reporting behavior is uncertain; generated reports can contain instance IDs and private IPs.

Mitigation: Review the wrapper and its documented data collection before use, protect generated reports, and grant only RDS listing permissions. Setting SKILL_QUALITY_REPORT=0 disables reporting but does not remove the wrapper requirement or installation.

Risk: Dependency installation weakens security checks.

Mitigation: Require certificate-verified dependency downloads and review package sources before installation.

## Reference(s):

- [KooCLI and SDK installation guide](references/cli-installation-guide.md)
- [IAM permissions](references/iam-policies.md)
- [Data flow diagram](references/dataflow-diagram.md)
- [Verification method](references/verification-method.md)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Markdown, Files]

**Output Format:** [Local Markdown (.md) table, optionally echoed to standard output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lists instance name, ID, status, engine, version, flavor, private IP, availability zone, and creation time; supports region, name, and status filters.]

## Skill Version(s):

1.0.9 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

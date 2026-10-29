## Description:

Query Huawei Cloud CES and EPS management-plane metadata through natural-language requests across 12 read-only categories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use the skill to retrieve Cloud Eye alarm and resource metadata and Enterprise Project Service details for a Huawei Cloud account. Queries are limited to management-plane reads; metric datapoints and write operations are out of scope.

### Deployment Geography for Use:

Global, subject to Huawei Cloud regional service availability.

## Known Risks and Mitigations:

Risk: Malformed region input may expose an authentication token.

Mitigation: Review region validation before use, keep secrets out of chat and output, and use narrowly scoped read-only cloud credentials.

Risk: Installation and telemetry requirements introduce additional security concerns; disabling SKILL_QUALITY_REPORT alone does not prevent the wrapper from running.

Mitigation: Review installation steps, preserve package certificate checks, and confirm telemetry behavior is optional and auditable before deployment.

## Reference(s):

- [Least-privilege CES/EPS IAM policies](artifact/references/iam-policies.md)
- [CLI, SDK, and credential setup guide](artifact/references/cli-installation-guide.md)
- [Skill verification method](artifact/references/verification-method.md)
- [Huawei Cloud KooCLI quick-start documentation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Human-readable table or JSON query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only CES/EPS management-plane metadata for supported query categories; raw metric datapoints and write operations are excluded.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

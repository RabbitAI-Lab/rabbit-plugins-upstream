## Description:

Counts Huawei Cloud GaussDB for openGauss and GaussDB (MySQL-compatible) instances in a selected region using read-only list APIs and reports the authoritative total_count.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and database administrators use this skill to inventory Huawei Cloud GaussDB deployments for daily inspection, capacity planning, migration checks, and cost review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad GaussDB inventory queries can count resources in an unintended cloud account or region.

Mitigation: Confirm the target Huawei Cloud account and region before running count requests.

Risk: Credentials with write or administrative permissions increase exposure if misused outside the skill's read-only workflow.

Mitigation: Use the documented read-only IAM policy or GaussDB ReadOnlyAccess rather than create, modify, or delete permissions.

Risk: Manual KooCLI installation may require sudo to move the hcloud binary into a system path.

Mitigation: Review the download source and install command before using sudo, or use an organization-approved installation path.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, Python code examples, and plain-text count output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Huawei Cloud region and read-only GaussDB credentials; count output is derived from total_count.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

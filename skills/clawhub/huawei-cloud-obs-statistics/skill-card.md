## Description:

A read-only Huawei Cloud OBS skill that aggregates bucket and object counts, estimated capacity, and storage-class and region distributions into table, JSON, or Markdown reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud developers and operations teams use this skill to review aggregate OBS usage for an account or a selected bucket and prefix, including approximate capacity and storage-class and region breakdowns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Collection limits and pagination may not reliably bound or complete a large listing, so report totals can be incomplete while appearing complete.

Mitigation: Do not assume results are complete or rely on --max-objects; select the intended bucket and prefix and verify collection behavior before using totals.

Risk: Credentials with broader OBS access than needed can expose data outside the intended reporting scope.

Mitigation: Use listing-only credentials restricted to the intended resources, keep access keys out of chat, and install verified CLI releases.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-obs-statistics)
- [CLI installation guide](references/cli-installation-guide.md)
- [Least-privilege IAM policy](references/iam-policies.md)
- [Verification method](references/verification-method.md)
- [Data flow diagram](references/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Table, JSON, or Markdown aggregate report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Capacity is estimated from listed object sizes and is not a billing figure.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

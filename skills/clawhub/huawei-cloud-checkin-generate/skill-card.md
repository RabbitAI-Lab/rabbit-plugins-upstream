## Description:

Generates one randomly assembled sample attendance check-in record and prints it as Markdown, plain text, or JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and testers use the skill to create sample attendance records for demos, tests, and documentation. A seed makes a generated record reproducible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using --output can overwrite an existing file at the selected path.

Mitigation: Choose a fresh output path or confirm the target file before running.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-checkin-generate)
- [Usage Guide](artifact/references/usage-guide.md)
- [Verification Method](artifact/references/verification-method.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [Data Flow](artifact/references/dataflow-diagram.md)
- [IAM Policies](artifact/references/iam-policies.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown table, plain text, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One record per run; output is reproducible with --seed.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

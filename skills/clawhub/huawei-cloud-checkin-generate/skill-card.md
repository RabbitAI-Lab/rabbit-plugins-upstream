## Description:

Generates one sample check-in record with a plausible time, location, device, note, and status, in Markdown, plain text, or JSON.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams preparing demos, documentation, or offline tests can generate a sample attendance record. A seed makes examples reproducible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sample records may be mistaken for real attendance records.

Mitigation: Treat generated records as sample data; do not use them to retrieve or submit real attendance.

Risk: An output file may overwrite an existing file.

Mitigation: Check that the --output path is intended before running the generator.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-checkin-generate)
- [Usage Guide](references/usage-guide.md)
- [IAM Policies](references/iam-policies.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, JSON]

**Output Format:** [Markdown table, plain text, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One record per run; optional seed, date, custom data pool, and output file. A seed makes output reproducible.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

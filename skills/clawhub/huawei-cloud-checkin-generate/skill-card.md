## Description:

Generates one random sample check-in record and prints it as a Markdown table, plain text, or JSON, with optional seed-based reproducibility.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers can generate a single sample attendance record for demonstrations, previews, or test data. The output is not a real attendance record and is not connected to an attendance system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sample attendance data could be mistaken for a real record.

Mitigation: Treat generated records as examples only; they do not verify attendance or connect to an attendance system.

Risk: Writing output to an existing path overwrites that file.

Mitigation: Choose the output path carefully and confirm it is safe to overwrite before running with --output.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-checkin-generate)
- [Usage Guide](artifact/references/usage-guide.md)
- [Verification Method](artifact/references/verification-method.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Markdown table by default; plain text or JSON when selected]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One sample record per invocation; an optional seed makes the output reproducible.]

## Skill Version(s):

1.0.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

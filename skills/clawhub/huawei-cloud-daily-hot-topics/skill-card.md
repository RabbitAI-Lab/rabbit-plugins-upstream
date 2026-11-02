## Description:

Fetches today's ranked hot topics from public APIs and displays them as Markdown, plain text, or JSON, with a clearly labeled sample-data fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can retrieve a ranked snapshot of current public hot topics from supported providers, or use the bundled sample data when providers are unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled fallback results are sample data and may not reflect current trends.

Mitigation: Check the sample-data label and warnings before treating a result as current.

Risk: Choosing an existing path for --output can overwrite its file.

Mitigation: Choose an output path carefully and confirm the target before writing.

## Reference(s):

- [Usage Guide](references/usage-guide.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [IAM Policies](references/iam-policies.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown table, plain-text ranking, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranked results limited by --top; output can be written to a chosen file, and fallback sample data is labeled.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

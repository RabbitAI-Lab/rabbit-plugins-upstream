## Description:

Fetches and normalizes public hot-topic rankings, then displays them as Markdown, plain text, or JSON with a clearly labeled bundled sample fallback when providers are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can retrieve a ranked snapshot of current public trending topics in a readable or machine-readable format, including an offline sample when live providers cannot be reached.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A provider outage or network failure can leave the bundled sample ranking out of date.

Mitigation: Check the output's sample-data label and warnings before treating rankings as current.

Risk: Using --output overwrites the selected file.

Mitigation: Choose an output path that can safely be replaced, or save any existing file first.

## Reference(s):

- [Usage Guide](artifact/references/usage-guide.md)
- [Verification Method](artifact/references/verification-method.md)
- [Data Flow Diagram](artifact/references/dataflow-diagram.md)
- [IAM Policies](artifact/references/iam-policies.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Ranked hot-topic list; Markdown table by default, with plain text and JSON options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to the requested number of entries; live rankings may be replaced by clearly labeled sample data when providers are unavailable.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

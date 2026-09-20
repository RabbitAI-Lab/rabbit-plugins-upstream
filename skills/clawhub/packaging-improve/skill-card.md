## Description:

Extracts packaging improvement tasks and supporting evidence from Amazon review feedback about damage, missing items, unboxing, and storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and operators use this skill to analyze Amazon reviews for transport, unboxing, and storage packaging issues, then prepare packaging improvement tasks backed by review evidence. It is not intended for logistics claims, supplier purchasing, inventory, or order accounting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can run paid ARI operations outside the advertised packaging-only scope.

Mitigation: Verify the quote and requestId, require explicit user confirmation before paid runs, and avoid passing custom --workflow or --focus values until the package enforces the advertised scope locally.

Risk: The skill requires trust in ARI with an API key, Amazon product identifiers, review data, and paid credit usage.

Mitigation: Install only for trusted ARI accounts, configure credentials intentionally, and keep requests limited to the official ARI endpoint documented by the artifact.

Risk: Interrupted paid analysis could be retried in a way that causes duplicate credit usage.

Mitigation: After interruption, use the existing requestId with the status command instead of directly rerunning the operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/packaging-improve)
- [Operation workflow](artifact/references/operation-workflow.md)
- [API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on collected Amazon review samples and should disclose evidence gaps instead of filling missing data.]

## Skill Version(s):

1.4.13 (source: server release metadata, artifact _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

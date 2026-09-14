## Description:

Extracts improvement priorities and supporting evidence for Amazon product instructions from review questions, without providing medical, legal, safety certification, or automatic publishing advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace users and developers use this skill to turn Amazon review questions into prioritized instruction-improvement guidance backed by review evidence. The workflow requires ARI authorization and explicit user confirmation before paid operations run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the CLI can override the advertised fixed product/instructions workflow.

Mitigation: Treat the skill as requiring review until the publisher enforces the fixed workflow in code; users should keep runs within the documented product/instructions workflow.

Risk: The security review reports a local API-key storage symlink weakness.

Mitigation: Keep the ARI key out of synced or shared home directories, check for local config tampering, and revoke the key if the config path may have been compromised.

Risk: The ARI service receives ASIN and product-review context and can consume paid credits after explicit quotes.

Mitigation: Install only when sharing that context with ARI is acceptable, review quotes before confirmation, and do not run paid operations without explicit user approval.

## Reference(s):

- [Operation Workflow](references/operation-workflow.md)
- [API Reference](references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with review-evidence summaries and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include data coverage notes, review evidence, conclusions, and explicit gaps when evidence is insufficient.]

## Skill Version(s):

1.4.11 (source: server release metadata, CHANGELOG, _meta.json, and script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

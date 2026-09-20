## Description:

Uses Amazon review evidence to plan Listing copy improvements and an evidence checklist; it requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and copywriters use this skill to turn Amazon review language into evidence-driven Listing optimization direction. It is not intended for unsupported free-form copywriting, ad bidding, or automatic page publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits after confirmation, and server evidence warns that the CLI can run paid operations beyond the documented fixed Listing workflow if accepted by the service.

Mitigation: Approve runs only after reviewing the quote and confirming the request clearly matches the intended Amazon review-based Listing copywriting task.

Risk: The skill stores an ARI API key locally.

Mitigation: Configure it only in a trusted workspace, use a dedicated ARI key when possible, and rotate or revoke the key if the workspace is shared or compromised.

Risk: Outputs are based on collected review samples and do not promise real-time price, sales, inventory, advertising, or store data.

Mitigation: Review the stated data scope and validate claims before using the output in Listing copy or operational decisions.

## Reference(s):

- [Amazon Review Evidence Copywriting API Reference](artifact/references/reference.md)
- [Amazon Review Evidence Copywriting Operation Workflow](artifact/references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or concise text with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on collected Amazon review samples and should state data gaps instead of filling them with unsupported conclusions.]

## Skill Version(s):

1.4.13 (source: server release evidence, _meta.json, CHANGELOG, script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

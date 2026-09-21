## Description:

Uses Amazon product fields and review feedback to identify information gaps in product descriptions and suggest evidence-based revisions; it is limited to description diagnosis and suggestions, not bullet writing, advertising, or automatic publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and ecommerce teams use this skill to inspect Amazon product details and review feedback, then receive concise description-improvement guidance grounded in available evidence. The workflow requires an ARI API key and user confirmation before paid analysis runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI may be able to move outside the advertised fixed description-writing workflow through workflow or focus options.

Mitigation: Review any command containing --workflow or --focus before execution and keep usage within the documented listing/description workflow.

Risk: The workflow requires an ARI API key, network access to ari.funewa.com, and paid ARI credits after quote confirmation.

Mitigation: Install only when those access and cost requirements are acceptable, run quote/profile checks first, and proceed with paid analysis only after explicit user confirmation.

Risk: Description guidance may be incomplete or misleading when product details or review samples are insufficient.

Mitigation: Require the output to state the data range, review basis, and evidence gaps, and avoid treating missing data as a conclusion.

## Reference(s):

- [Amazon product description operation workflow](references/operation-workflow.md)
- [Amazon product description API reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results should cite the data range and review basis, state evidence gaps, and avoid exposing command logs unless requested.]

## Skill Version(s):

1.4.13 (source: server release evidence, artifact metadata, CHANGELOG, and CLI version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

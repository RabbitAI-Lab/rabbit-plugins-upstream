## Description:

Turns Amazon review issues into evidence-based product, packaging, instructions, and supplier action tasks using ARI product and review data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and product teams use this skill to convert Amazon review problems for a specific ASIN into action-oriented product, packaging, documentation, and supplier tasks. The workflow requires ARI authorization and a user-confirmed quote before paid analysis runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access an ARI account, store an ARI API key locally, send ASIN, product, and review data to ari.funewa.com, and spend ARI credits.

Mitigation: Install only when that account and data access is intended, keep credentials scoped to ARI use, require the quote output before any confirmed run, and do not execute paid analysis without explicit user approval.

Risk: Workflow override options may allow broader behavior than the fixed review-to-action flow.

Mitigation: Keep use to the documented product/action workflow and avoid --workflow, --focus, or --competitor unless that broader operation is intentional.

Risk: The skill's conclusions depend on available ARI product and review samples and may not reflect real-time price, sales, inventory, advertising, order, profit, or store data.

Mitigation: Treat outputs as review-evidence summaries, ask for missing data when needed, and review any proposed product or supplier action before acting on it.

## Reference(s):

- [Amazon Review To Action API Reference](artifact/references/reference.md)
- [Amazon Review To Action Operations Workflow](artifact/references/operation-workflow.md)
- [Review Action README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and action-oriented task summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis must be quoted and explicitly confirmed by the user before execution.]

## Skill Version(s):

1.4.13 (source: server release evidence, artifact metadata, CHANGELOG, and script version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Searches 1688 products by keyword, with optional filters for sales, price, and 48-hour pickup rate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External buyers and sourcing teams use this skill to find 1688 suppliers and compare products by keyword, price, sales, and fulfillment metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may install or upgrade Node.js and qhkit and persist a Qinghu service token.

Mitigation: Prefer a managed or pinned qhkit installation, avoid unnecessary shell startup changes, and configure the token only with the user's approval.

Risk: Product searches incur Qinghu credits, and failed service calls may still incur charges.

Mitigation: Check estimated credits and obtain user consent before paid calls; disclose actual credits spent afterward.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-1688-keyword-search)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown summary with optional tabular export file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits spent on paid calls; large results may be delivered as a file.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

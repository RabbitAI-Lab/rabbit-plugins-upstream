## Description:

Checks whether claims in retrieval-augmented answers are supported by supplied sources, reporting coverage and flagging unsupported claims for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to review RAG answers against supplied source material, identify claims needing verification, and check citation provenance before publishing an answer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad agent tool permissions.

Mitigation: Review allowed tools in the agent environment and supply only the claim and source files intended for inspection.

Risk: A reported source match may not establish that a claim is factually supported.

Mitigation: Review flagged and apparently supported claims against the actual cited passages before relying on the result.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/rag-grounding-guard)
- [Publisher project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Grounding coverage report with supported and unsupported claims]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports a coverage percentage; findings require human review.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

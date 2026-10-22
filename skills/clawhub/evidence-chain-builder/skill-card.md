## Description:

Organizes supplied claims and evidence into a source-tagged evidence chain with a justification score and a warning when supporting evidence is insufficient, without determining whether the claim is true.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and other users can organize evidence supplied for an AI claim, distinguish source categories, and identify when a claim should not be treated as supported. The score reflects evidence labels, not independent fact-checking or proof of truth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Declared tool access includes file writes and web fetches despite permissions claiming no filesystem, network, or subprocess access.

Mitigation: Review and reconcile permission metadata before installation; grant only the access needed for the intended workflow.

Risk: The evidence score can be mistaken for independent verification of a claim or its cited sources.

Mitigation: Check original sources and evidence labels independently before treating the claim as established.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/evidence-chain-builder)
- [LGD theory (background reference, not release provenance)](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Markdown evidence-chain report or JSON claim, score, unsupported flag, and evidence entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Source categories are assigned from supplied evidence labels; the score does not verify source authenticity or claim truth.]

## Skill Version(s):

1.0.4 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Builds an evidence chain for an AI claim, classifying sources and reporting how much of the supplied evidence can be independently checked without asserting that the claim is true.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); all rights reserved (documentation and theory)

## Use Case:

Developers and other users evaluating AI-generated claims can organize supplied evidence by source type, see a support score, and identify claims that need independently checkable sources before drawing a conclusion. The score measures evidence classification, not factual correctness; users must check the original sources themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A support score based on supplied evidence labels can be mistaken for independent fact-checking.

Mitigation: Check original sources and treat the score as evidence-quality guidance, not a verdict on the claim.

Risk: Documentation and theory are not covered by the Python code's MIT license.

Mitigation: Review the Chinese-language licensing terms before reuse or redistribution of the documentation or methodology.

Risk: Local evidence files or source-checking requests may expose material the user did not intend to share.

Mitigation: Provide only intended evidence files or claims, and check external sources only with user approval.

## Reference(s):

- [LGD project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/evidence-chain-builder)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Markdown evidence-chain report or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Classifies supplied evidence by source type and independent verifiability, reports a support score, and flags insufficient support; does not determine whether a claim is true.]

## Skill Version(s):

1.0.3 (source: ClawHub server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

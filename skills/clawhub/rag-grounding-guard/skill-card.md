## Description:

Checks whether claims in a retrieval-augmented answer appear supported by supplied source text and flags claims with low grounding coverage for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0 (release metadata); MIT (Python code per artifact license); documentation and theory: All rights reserved

## Use Case:

Developers and knowledge-base teams use this skill to screen RAG answers for claims that may lack support in retrieved text and to prioritize manual source checks before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A heuristic grounding score may miss unsupported claims or flag supported ones.

Mitigation: Treat the score as a screening signal and manually compare important claims with the original sources.

Risk: Misleading support could affect factual, legal, medical, financial, or compliance conclusions.

Mitigation: Have a qualified reviewer check consequential conclusions against the original sources before relying on them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/rag-grounding-guard)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text with a grounding coverage percentage and lists of flagged and apparently supported claims]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Heuristic screening result, not a determination that a claim is true or correctly cited]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; artifact frontmatter says 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

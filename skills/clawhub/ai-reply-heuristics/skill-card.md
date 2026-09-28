## Description:

Estimates AI-like writing patterns in supplied text using a heuristic 0–100 score and three explanatory bands, not a determination of authorship.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theoretical text all rights reserved

## Use Case:

Writers, editors, and developers can use this skill to flag writing patterns for human review without treating the score as proof of AI authorship.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The heuristic score may be mistaken for proof that a person used AI.

Mitigation: Treat the score as a rough signal and use human review before making consequential decisions.

Risk: Declared agent tools are broader than the local text-scoring task requires.

Mitigation: Review requested tool permissions before installation and grant only those needed for the intended workflow.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-reply-heuristics)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A 0–100 heuristic score, one of three Chinese-language bands, matched phrases, and a disclaimer; JSON also includes sentence and character counts.]

## Skill Version(s):

1.0.2 (source: server release metadata; bundled SKILL.md says 1.1.0 and manifest.json says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

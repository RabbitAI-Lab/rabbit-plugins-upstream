## Description:

Scores patterns in supplied text to offer a heuristic indication of AI-like writing, not a determination of authorship.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory all rights reserved

## Use Case:

Writers and reviewers can screen a chosen passage for stylistic signals that warrant closer human review, without treating the result as proof of AI authorship.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested write and web access exceeds the documented local text-scoring need.

Mitigation: Review before installing; run the Python script directly on chosen text or remove or tightly control Write and WebFetch access.

Risk: A heuristic score may falsely suggest that text was AI-generated.

Mitigation: Treat the score as a prompt for human review, not proof of authorship or grounds for action by itself.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-reply-heuristics)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A 0–100 heuristic score, three-band label, and disclaimer; JSON also includes matched phrases and text counts.]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

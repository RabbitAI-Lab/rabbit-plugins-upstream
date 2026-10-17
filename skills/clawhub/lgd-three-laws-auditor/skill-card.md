## Description:

Self-assesses AI systems against the LGD registered, evidenced, and gated rubric, producing a scorecard and suggested improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0 (release metadata); code marked MIT; documentation and theory all rights reserved

## Use Case:

Developers and AI governance teams use this LGD-specific rubric to self-assess an AI system's registration, supporting evidence, and review gates, then identify gaps to address. Scores are not a regulatory certification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The LGD-specific self-assessment may be mistaken for neutral governance advice or proof of compliance.

Mitigation: Label the rubric and heuristic scores as provisional, confirm supporting evidence, and obtain independent review for compliance decisions.

Risk: Broad activation rules and requested tools exceed the needs of the local scorer; CLI documentation is inconsistent.

Mitigation: Invoke only for a relevant user request, limit tool access to the local inputs needed, and reconcile the documented CLI with the actual interface before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-three-laws-auditor)
- [LGD theory reference (linked in skill README)](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown rubric or scorecard; JSON scorecard with --json]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes per-law scores, checklist statuses, and improvement items; description-based matches are provisional.]

## Skill Version(s):

1.0.4 (source: server release metadata; bundled skill frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

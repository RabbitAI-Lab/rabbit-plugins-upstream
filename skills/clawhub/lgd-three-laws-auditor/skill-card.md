## Description:

Helps teams assess AI systems against the LGD three-laws rubric for registration, evidence, and governance gates, producing a scorecard and improvement actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code); all rights reserved (documentation and methodology)

## Use Case:

Developers and AI governance teams use this skill to self-assess an AI system's registration, supporting evidence, and review gates, then identify gaps to address. It is not a legal or regulatory compliance determination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A self-assessment score could be mistaken for legal or regulatory approval.

Mitigation: Treat scorecards as planning aids and seek qualified review against applicable requirements.

Risk: Heuristic assessments of system descriptions may overstate what has been verified.

Mitigation: Mark unsupported items as unverified and use documented, human-supplied answers for decisions.

Risk: Unnecessary write or web access can expand exposure when auditing sensitive system descriptions.

Mitigation: Run the local audit with only the access needed and handle sensitive inputs locally.

## Reference(s):

- [LGD project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-three-laws-auditor)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text rubric and scorecard, or JSON scorecard]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes improvement actions; description-based assessments are tentative, while scored answers require user-supplied responses.]

## Skill Version(s):

1.0.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

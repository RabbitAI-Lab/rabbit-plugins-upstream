## Description:

Boyue provides decision and complexity governance for AI-assisted software development, helping agents plan scope, evaluate commitments, shape risky decisions, and review systems for simplification or retirement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wuaishare](https://clawhub.ai/user/wuaishare)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill when planning products or features, evaluating scope expansion, deciding whether prototypes belong in production, or reviewing mature systems for simplification and retirement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can influence how an agent frames larger product or architecture decisions, which may bias scope, commitment, or ownership choices if applied mechanically.

Mitigation: Review recommendations against project-specific evidence and human ownership before turning them into roadmap, architecture, or production commitments.

Risk: Using the governance workflow on small, low-consequence, easy-to-undo changes could add unnecessary process overhead.

Mitigation: Use the documented fast path for reversible work and reserve deeper review for meaningful new scope, durable ownership, or high-impact uncertainty.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wuaishare/skills/boyue)
- [Original Boyue methodology article](https://www.wuaishare.cn/12793.html)
- [Methodology](references/methodology.md)
- [Commitment Boundary](references/commitment-boundary.md)
- [Ownership Boundary](references/ownership-boundary.md)
- [Risk-Adaptive Shaping](references/risk-adaptive-shaping.md)
- [Delivery Patterns](references/delivery-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [Markdown guidance, checklists, and decision-review templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No runtime execution; documentation-only workflow with optional review templates.]

## Skill Version(s):

0.2.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

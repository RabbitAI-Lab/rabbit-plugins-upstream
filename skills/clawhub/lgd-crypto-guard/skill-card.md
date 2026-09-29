## Description:

Applies an LGD identity, evidence, and approval-gate rubric to self-assess privacy-computing AI systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); all rights reserved (documentation and theory)

## Use Case:

Developers and compliance teams use this local rubric to check an AI system's identity records, supporting evidence, and approval gates for privacy-computing applications. Its scores are advisory, not a compliance certification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Heuristic scoring or self-reported answers can give a misleading pass.

Mitigation: Review the underlying evidence and obtain qualified human sign-off; do not treat a pass as legal, security, or regulatory approval.

Risk: Installation instructions may reference a source not confirmed by release provenance.

Mitigation: Verify the source and version before installing or executing the skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-crypto-guard)
- [LGD project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Three rubric scores, a pass/fail gate, and missing evidence items; exit status 0, 1, or 2.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

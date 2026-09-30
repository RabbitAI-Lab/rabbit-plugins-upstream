## Description:

Helps review agent-generated factual claims against supplied sources before publication, flagging claims that need further verification or attribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); All rights reserved (documentation and theory)

## Use Case:

Content creators and developers use this skill to review AI-generated articles, reports, and replies claim by claim before sharing them, and to identify statements requiring reliable sources or qualification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A heuristic source match may be mistaken for proof that a claim is true.

Mitigation: Treat labels as screening hints and verify important claims against current authoritative sources before publication.

Risk: Incorrect medical, legal, financial, or other regulated claims may cause harm.

Mitigation: Require qualified human review and authoritative sources for high-stakes claims.

## Reference(s):

- [Fact Check Guard on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/fact-check-guard)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-claim supported, dubious, or unsourced labels with brief reasons; JSON is optional.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

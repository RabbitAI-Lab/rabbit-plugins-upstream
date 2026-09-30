## Description:

Helps public-sector AI teams assess registration, evidence, and approval gates using a Chinese-language governance checklist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); all rights reserved (documentation and theory)

## Use Case:

Public-sector AI teams use this skill to review system descriptions or self-reported evidence against registration, evidence, and approval-gate checklists before human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A checklist pass could be mistaken for legal approval or verified compliance.

Mitigation: Use the result as self-assessment guidance; confirm evidence and decisions with qualified reviewers and current official requirements.

Risk: Unnecessary network or write access increases exposure when reviewing sensitive public-sector systems.

Mitigation: Avoid granting network or write access unless the agent workflow specifically requires it.

## Reference(s):

- [LGD project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-gov-guard)

## Skill Output:

**Output Type(s):** [Guidance, Text, JSON]

**Output Format:** [Chinese-language text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Three checklist scores, a pass/fail gate result, and missing evidence items.]

## Skill Version(s):

1.0.3 (source: ClawHub release; bundled files list different versions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

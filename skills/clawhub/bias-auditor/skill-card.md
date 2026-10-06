## Description:

Screens supplied text for possible group generalizations and stereotypes, then suggests less biased wording.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

Python code: MIT; documentation and theory: All rights reserved

## Use Case:

Writers, reviewers, and developers use this skill to screen AI-generated or other public-facing text for possible group stereotypes before publication and consider suggested revisions. Findings require human review, especially for consequential decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keyword-based screening can miss contextual bias or flag benign wording.

Mitigation: Review findings and omissions with a human; do not treat the output as legal, hiring, medical, or compliance advice.

Risk: Broad agent tool permissions could expose more data or actions than the audit needs.

Mitigation: Limit tool access to the text or files being reviewed and approve any external or modifying actions separately.

Risk: The code and documentation have different redistribution terms.

Mitigation: Check the packaged license and reserved-rights notice before redistributing documentation or theory text.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/bias-auditor)
- [LGD project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, JSON]

**Output Format:** [Text or JSON findings with suggested revisions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts supplied text or a local UTF-8 file; Chinese-first findings.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

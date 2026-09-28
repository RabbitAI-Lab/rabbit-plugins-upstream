## Description:

Records AI-assisted decisions in a local JSONL log and reports model usage and human-review coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory all rights reserved

## Use Case:

Developers and teams record AI-assisted decisions with model, evidence reference, timestamp, and reviewer, then identify decisions lacking human review for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decision logs may expose sensitive or regulated details if stored in the decision or evidence fields.

Mitigation: Choose a protected local log location and avoid entering secrets, passwords, or regulated details in those fields.

Risk: An audit entry or report could be mistaken for approval of a consequential decision.

Mitigation: Require human review for critical legal, medical, financial, or regulated decisions and follow up on entries flagged as unreviewed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-decision-log)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Files, Text, JSON]

**Output Format:** [JSONL decision log; plain-text or JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports summarize model usage and flag decisions without a reviewer.]

## Skill Version(s):

1.0.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Logs AI-assisted decisions with their model, evidence reference, reviewer, and time, and reports model usage and decisions lacking human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory all rights reserved

## Use Case:

Developers and teams use this skill to record AI-assisted decisions in a local JSONL log and identify decisions without a named human reviewer during reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local decision logs may contain sensitive decision text or other protected information.

Mitigation: Do not log secrets or regulated data unless appropriate local storage and access controls are in place.

Risk: A logged decision may lack human review.

Mitigation: Check reports for unreviewed decisions and require human review for consequential decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-decision-log)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [CLI text or JSON report; local JSONL decision records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-first CLI; records decision text, model, evidence hash, reviewer, and time. Reports flag unreviewed decisions.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; bundled frontmatter says 1.1.0 and manifest says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

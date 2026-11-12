## Description:

Adversarial review of code quality findings: challenge insights with counter-evidence, verify claims against source code, and produce structured verdicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yumingtao](https://clawhub.ai/user/yumingtao)

### License/Terms of Use:

MIT

## Use Case:

Developers and code reviewers use this skill to verify code quality findings against source code and related evidence, then produce a structured verdict and report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security inspection was incomplete: one of 12 components was only partially inspected, so its behavior is not established.

Mitigation: Review the full skill contents, including the component that was not fully inspected, before relying on it.

## Reference(s):

- [Insight Challenge on ClawHub](https://clawhub.ai/yumingtao/skills/insight-challenge)
- [Challenge Protocol Specification](specs/challenge-protocol.en.md)
- [Verdict Schema Specification](specs/verdict-schema.en.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Markdown report with an embedded JSON verdict, or raw JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch findings are processed independently.]

## Skill Version(s):

1.7.0 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

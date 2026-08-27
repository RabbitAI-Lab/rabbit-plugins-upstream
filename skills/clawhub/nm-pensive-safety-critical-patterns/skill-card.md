## Description:

Applies NASA Power of 10 rules for safety-critical verifiable code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to apply safety-critical coding patterns, including bounded control flow, assertions, scoped variables, strict checks, and warning-focused verification practices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers may invoke the skill during general safety, medical, NASA, robustness, or assertion-related discussions.

Mitigation: Narrow the triggers or use the skill only when safety-critical coding guidance is intentionally requested.

Risk: The skill provides advisory coding guidance and does not validate whether code is safe for a regulated or high-reliability use case.

Mitigation: Treat its recommendations as review input and require human engineering review before applying them to critical systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-safety-critical-patterns)
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands]

**Output Format:** [Markdown with examples and inline code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; no executable behavior in the artifact.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Inverts burden of proof for code additions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and review-oriented agents use this skill to challenge proposed code, file, abstraction, configuration, or test additions by requiring evidence and assessing anti-patterns before accepting changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may make an agent overly conservative about useful code additions by requiring stronger evidence.

Mitigation: Use the scrutiny questions to require clear evidence while still allowing additions that are justified by task requirements and documented consequences.

Risk: The skill can influence review outcomes even though it does not run code.

Mitigation: Review the skill text before deployment and monitor outputs for excessive rejection of necessary implementation work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-additive-bias-defense)
- [OpenClaw metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)

## Skill Output:

**Output Type(s):** [guidance, text]

**Output Format:** [Markdown guidance with scrutiny questions, anti-pattern checks, and verdict labels]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not run code or request runtime access; it shapes agent review behavior.]

## Skill Version(s):

1.9.19 (source: server release evidence; artifact frontmatter says 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

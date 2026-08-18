## Description:

A distilled meta-skill that extends self-play coevolution workflows with self-verification, reflection, adversarial validation, and local learner notes for iterative agent improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to guide self-play coevolution tasks, add verification and reflection loops, and record observed failure patterns for later improvement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learner script can retain execution notes locally, which may capture sensitive prompts or business details if they are passed into notes.

Mitigation: Do not provide secrets, credentials, private user text, or sensitive business context to learner notes; review and delete local learner data as needed.

Risk: Self-evolving orchestration can reinforce weak or incorrect patterns if outputs are accepted without review.

Mitigation: Require human review for learned patterns and use verification results as advisory evidence rather than automatic approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-self-play-coevolution)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands]

**Output Format:** [Markdown guidance with optional Python learner output as JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local learner notes when its learner script is used.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

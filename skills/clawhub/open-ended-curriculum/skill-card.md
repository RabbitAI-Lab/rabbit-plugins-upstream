## Description:

Generates progressively harder, non-repetitive curriculum challenges from a seed task and can record local usage feedback to improve future skill guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to create escalating practice challenges from a seed task and inspect measurable novelty, feasibility, alignment, and difficulty signals. It is also intended to persist local feedback about usage outcomes and preferences for future refinement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learning module can keep local usage history, preferences, and error notes.

Mitigation: Use it only in a workspace where that local history is acceptable, and inspect or delete learned_patterns.json when retention is not wanted.

Risk: The skill describes self-improvement behavior that may modify SKILL.md through agent action.

Mitigation: Require explicit human review before accepting changes to skill instructions.

Risk: Generated curriculum challenges may steer an agent toward inappropriate or low-value work if the seed task is poorly chosen.

Mitigation: Review generated challenges for feasibility, alignment, and intended use before execution.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON curriculum output from the bundled script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The curriculum script returns seed, steps, challenges, saturation status, and maximum difficulty.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

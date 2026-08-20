## Description:

Open-Ended Goal Discovery helps an agent generate and rank proactive goal suggestions from capabilities, pursued goals, user interest signals, and preferences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent builders use this skill to help long-running agents propose worthwhile next goals instead of waiting for explicit tasks. It ranks candidate goals by value, novelty, feasibility, and user alignment before returning top suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learner module can retain local preferences, notes, and outcomes.

Mitigation: Use the skill only where local memory is acceptable, avoid sensitive notes, and review or clear learned_patterns.json as needed.

Risk: The skill instructions describe modifying SKILL.md after repeated feedback.

Mitigation: Require explicit user approval before any change to SKILL.md or other skill source files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qq435912743/skills/open-ended-goal-discovery)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with optional JSON ranking output and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces ranked Top-N goal suggestions with score components and may update local learning data when the learner module is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

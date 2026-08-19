## Description:

Hypothesis-Driven Inquiry helps an agent organize observations, rank candidate explanations by coverage and simplicity, and propose discriminating tests to move toward a verifiable root cause.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill for root cause analysis, diagnostic reasoning, scientific hypothesis generation, and experiment planning when they need ranked explanations and concrete validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learner workflow may retain usage history, errors, notes, and preferences in the skill directory.

Mitigation: Avoid using sensitive diagnostic details with the learner workflow, or disable it and clear learned_patterns.json after use.

Risk: The skill describes a process where repeated errors can lead agents to rewrite the installed skill instructions.

Mitigation: Require user review and approval before any agent modifies SKILL.md or other installed skill files.

Risk: Ranked hypotheses and discriminating tests can be incomplete or misleading when observations or candidate hypotheses are incomplete.

Mitigation: Treat the output as decision support and validate proposed tests against independent evidence before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/hypothesis-driven-inquiry)
- [ClawHub publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON output from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May keep local learning state in learned_patterns.json when the learner workflow is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

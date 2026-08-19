## Description:

Reflection Replanner helps agents respond to failed verification by classifying failure causes and revising execution plans with remedial steps and a final verification gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill when a verifier or test runner reports a failed task step and they need the agent to diagnose the likely failure category, insert targeted recovery steps, and retry with a revised plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled learning feature can persist local history, errors, notes, and preferences.

Mitigation: Avoid recording secrets or sensitive workflow details, and review or prune learned_patterns.json before sharing or publishing the skill directory.

Risk: The instructions describe updating skill instructions over time based on accumulated errors and usage.

Mitigation: Review and version-control any changes to SKILL.md or learning data before relying on the modified skill in production workflows.

Risk: Failure classification is heuristic and can misclassify complex task failures.

Mitigation: Treat revised plans as proposals and run an explicit verification pass before accepting the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/reflection-replanner)

## Skill Output:

**Output Type(s):** [text, code, shell commands, guidance]

**Output Format:** [Markdown guidance and JSON-style replanning output from the bundled CLI script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Revised plans include a failure category, added remedial steps, and a final verification step when verification has failed.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

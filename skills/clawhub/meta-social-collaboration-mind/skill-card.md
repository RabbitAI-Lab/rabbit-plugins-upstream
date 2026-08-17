## Description:

Meta Social Collaboration Mind helps agents choose collaboration strategies from partner signals and adds claimed self-review, reflection, and learning loops around the distilled social-collaboration-mind skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to select collaboration postures such as delegate, consult, monitor, pair, or avoid based on partner expertise, confidence, workload, trust, and mood signals. It can also record usage notes and preferences across sessions when its learner script is used.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill claims self-verification and self-evolution capabilities that may be overstated.

Mitigation: Treat verification and reflection outputs as advisory, and require human review for decisions that affect safety, trust, or deployment.

Risk: The learner component can persist usage notes and user preferences locally.

Mitigation: Confirm users are comfortable with local cross-session storage, avoid recording sensitive data, and periodically review or remove learned_patterns.json.

Risk: Collaboration strategy choices depend on subjective partner signals such as expertise, confidence, trust, workload, and mood.

Mitigation: Validate input signals before relying on the recommended strategy, especially when delegation or avoidance could affect important work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-social-collaboration-mind)
- [Publisher profile](https://clawhub.ai/user/qq435912743)
- [Artifact skill instructions](artifact/SKILL.md)
- [Distillation report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON decision outputs and optional bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The learner component may persist local usage notes and preferences in learned_patterns.json.]

## Skill Version(s):

1.0.0 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

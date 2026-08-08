## Description:

mu-critical-thinking coaches critical thinking by scanning arguments across 12 dimensions, identifying logical fallacies, guiding Socratic questioning, auditing decisions, and flagging data traps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT

## Use Case:

Employees, teams, and individual users use this skill to evaluate proposals, arguments, decisions, reports, charts, and debate positions. It produces structured critique, targeted questions, and practical repair suggestions for weak reasoning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may paste confidential business, personal, or sensitive material into an agent while asking for critique.

Mitigation: Use the skill only in an agent environment approved for the data being reviewed, and redact sensitive details when approval is unclear.

Risk: The skill may produce misleading criticism if asked to diagnose an argument without concrete source text.

Mitigation: Follow the skill's operating rule to request the target text first and ground fallacy or evidence-gap claims in specific quoted passages.

Risk: Critical-thinking reports can overstate defects or imply a weak argument is false rather than merely under-supported.

Mitigation: Treat outputs as reasoning review aids, preserve uncertainty labels such as insufficient information, and have a human reviewer decide final business actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/muippt/skills/mu-critical-thinking)
- [README](README.md)
- [12-dimension argument evaluation framework](references/twelve-dimensions.md)
- [Logical fallacies quick reference](references/logical-fallacies.md)
- [Evidence evaluation and data traps](references/evidence-evaluation.md)
- [Workplace scenarios](references/workplace-scenarios.md)
- [Reading notes: Asking the Right Questions](https://mp.weixin.qq.com/s/SgkY1jdqpi6dOvaA0W6smg)
- [Landing page](https://muippt.github.io/mu-critical-thinking/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown reports, tables, checklists, and guided questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May quote user-provided text when identifying fallacies or evidence gaps.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence; artifact SKILL.md and CHANGELOG state 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

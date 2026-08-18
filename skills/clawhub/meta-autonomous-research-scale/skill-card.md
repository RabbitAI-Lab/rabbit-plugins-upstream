## Description:

A distilled research meta-skill that adds self-verification, reflection, super-agent orchestration, and persistent learning around the autonomous-research-scale workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use this skill to structure autonomous research into parallel hypotheses, synthesize claims, and add reliability checks, reflection, and learned preferences across repeated use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist usage patterns, preferences, and failure notes locally.

Mitigation: Avoid recording sensitive research topics or preferences, and inspect or remove learned_patterns.json before sharing or reusing the skill directory.

Risk: The skill describes a loop that may rewrite its own SKILL.md after repeated errors or usage.

Mitigation: Review proposed SKILL.md changes before accepting them and keep version control or backups for rollback.

Risk: Research confidence scoring and convergence detection are heuristic and may miss semantically similar claims or overstate certainty.

Mitigation: Require human review and independent source checks for high-stakes or external-facing research conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-autonomous-research-scale)
- [Distillation report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and structured research guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local learned_patterns.json usage memory when its learner script is run.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

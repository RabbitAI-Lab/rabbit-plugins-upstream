## Description:

A distilled autonomous research helper that adds self-verification, self-reflection, super-agent orchestration, and a local learning loop to the base autonomous-researcher capability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users can use this skill to structure autonomous research tasks with added verification, reflection, and lightweight local learning notes across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local learning notes may retain task context across sessions.

Mitigation: Avoid sensitive research content unless local persistence is acceptable, and review or clear learned_patterns.json before sharing the skill.

Risk: Autonomous research and orchestration outputs can contain unsupported or misleading conclusions.

Mitigation: Require human review and fact-checking before relying on outputs for decisions or downstream skill changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qq435912743/skills/meta-autonomous-researcher)
- [distillation_report.md](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or text responses, with optional JSON from the learner script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local learned_patterns.json with operation counts, failure counts, and notes.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Distilled from super-agent-bootstrap, this meta-skill guides agents through sense, plan, execute, verify, reflect, and memory workflows with added self-verification, reflection, adversarial quality checks, and local learning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to bootstrap a super-agent workflow that decomposes tasks, executes steps, verifies outputs, reflects on failures, and records local learning for future runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist usage history, errors, preferences, and other cross-session memory locally.

Mitigation: Do not store secrets, personal data, customer data, credentials, financial or health details, or confidential business context; review and delete learned_patterns.json as needed.

Risk: The skill describes self-evolution and possible write-back into SKILL.md.

Mitigation: Require human review before accepting any skill file change, and scan the skill before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-super-agent-bootstrap)
- [Distillation report](distillation_report.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local learned_patterns.json when the learner script is invoked.]

## Skill Version(s):

1.0.0 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

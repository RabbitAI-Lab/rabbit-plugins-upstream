## Description:

Skill Forge helps agents discover capability gaps, search multiple skill and tool sources, evaluate candidates, package compatible skills, verify them, benchmark results, and announce releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stakeswky](https://clawhub.ai/user/stakeswky)

### License/Terms of Use:


## Use Case:

Developers and agent operators use this skill to run an automated skill discovery, evaluation, integration, verification, benchmarking, and announcement workflow for ClawHub-compatible agent skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The pipeline asks users to run local scripts that may clone or modify repositories and integrate generated skills.

Mitigation: Review the external evolution-engine project and its package.json scripts before running the pipeline, and run discovery and evaluation separately from integration until the effects are clear.

Risk: The announce stage can generate and publish public X/Twitter posts.

Mitigation: Confirm credential access and require explicit approval before enabling social posting or running the announce stage.

## Reference(s):

- [ClawHub Skill Forge page](https://clawhub.ai/stakeswky/skills/skill-forge)
- [ClawHub publisher profile for stakeswky](https://clawhub.ai/user/stakeswky)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Code]

**Output Format:** [Markdown with shell commands, JSON configuration examples, and generated skill package files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce ClawHub skill package files such as skill.json and SKILL.md, and may generate social announcement text when the announce stage is used.]

## Skill Version(s):

0.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

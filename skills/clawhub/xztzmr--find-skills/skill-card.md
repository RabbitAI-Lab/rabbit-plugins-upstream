## Description:

Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xztzmr](https://clawhub.ai/user/xztzmr)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to find installable skills for common tasks, verify candidate quality, and optionally install selected skills with the Skills CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global skill installation can persistently change the agent environment.

Mitigation: Confirm the exact skill source and trust the publisher before installing; ask the agent to show the package and install command before it runs anything.

Risk: Search results may surface low-trust or unsuitable skills.

Mitigation: Review install count, source reputation, and repository signals before recommending or installing a skill.

## Reference(s):

- [ClawHub find-skills page](https://clawhub.ai/xztzmr/skills/find-skills)
- [Skills directory](https://skills.sh/)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include skill recommendations, quality checks, install commands, and links for further review.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

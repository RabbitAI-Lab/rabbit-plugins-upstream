## Description:

Security-first skill vetting for AI agents. Use before installing any skill from ClawdHub, GitHub, or other sources. Checks for red flags, permission scope, and suspicious patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xtdnpl](https://clawhub.ai/user/xtdnpl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill to review agent skills before installation, checking source trust, code behavior, permissions, red flags, and installation risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reviewed skill could be marked safe if source checks or file review are incomplete.

Mitigation: Review all files in the target skill, document red flags, and require human approval for high-risk findings before installation.

Risk: The example curl commands access external GitHub endpoints.

Mitigation: Run those commands only against the specific repository being evaluated and inspect results before installing the target skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xtdnpl/skills/skill-vetter)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown guidance with checklist text, command examples, and a structured vetting report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a human-readable risk classification, installation verdict, and notes for the reviewed skill.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Scans an OpenClaw skill folder with the local ironheights CLI and summarizes findings before installation or update.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frank-masciopinto](https://clawhub.ai/user/frank-masciopinto)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to review a skill folder's scan findings before installing or updating it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan relies on the ironheights npm package as its scanner engine.

Mitigation: Install only if comfortable with that dependency, using its documented official package or source.

Risk: A clean scan does not prove another skill is safe, and a hostile skill may bypass an agent-mediated check.

Mitigation: Treat results as advisory and run the scanner independently before trusting the skill.

## Reference(s):

- [Ironheights website](https://www.ironheights.dev)
- [Ironheights on ClawHub](https://clawhub.ai/frank-masciopinto/skills/ironheights)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown summary of scan verdict and findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes finding locations and recommended next steps; advisory only.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

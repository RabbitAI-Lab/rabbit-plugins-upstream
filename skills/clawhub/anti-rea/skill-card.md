## Description:

Guides developers integrating antiRea into a Node.js web application to meter per-identity dataset access and detect coordinated automated abuse, with advisory signals and host-controlled responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dankezo](https://clawhub.ai/user/dankezo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate antiRea signals for application-level scraping, harvesting, enumeration, and coordinated-abuse patterns. It provides TypeScript and JavaScript integration guidance while leaving enforcement decisions to the host application.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner review was partial because three local references could not be resolved, so confidence in the benign verdict is medium.

Mitigation: Consider whether you trust the skill's source and whether those referenced items matter to your use before installing.

Risk: Advisory signals could be treated as proof of abuse or used to penalize existing users.

Mitigation: Treat signals as evidence rather than verdicts; keep consequences host-controlled and limit step-up challenges to new actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dankezo/skills/anti-rea)
- [Declared project repository (metadata link)](https://github.com/dankezo/antiRea)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with TypeScript or JavaScript code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Version-specific integration instructions; all detector signals are advisory and the host application controls responses.]

## Skill Version(s):

2.8.1 (source: release metadata, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

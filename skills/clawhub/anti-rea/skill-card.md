## Description:

Guides developers integrating antiRea to meter per-identity data access and detect coordinated automated abuse, with advisory signals that leave enforcement decisions to the host application.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dankezo](https://clawhub.ai/user/dankezo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate antiRea into a server-side application to monitor per-identity data access and coordinated abuse patterns. The host application evaluates the advisory signals and decides whether to take action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Advisory signals could be mistaken for proof of abuse and lead to unfair restrictions.

Mitigation: Keep enforcement decisions in the host application, treat signals as evidence rather than verdicts, and apply step-up only to new actions as documented.

Risk: The security assessment is incomplete because three references could not be resolved.

Mitigation: Review the unresolved references before treating the security assessment as complete.

## Reference(s):

- [antiRea source repository (listed in release metadata)](https://github.com/dankezo/antiRea)
- [anti-rea npm package](https://www.npmjs.com/package/@dannyphan190/anti-rea)
- [ClawHub release page](https://clawhub.ai/dankezo/skills/anti-rea)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with TypeScript and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.9.1 (source: server-resolved release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

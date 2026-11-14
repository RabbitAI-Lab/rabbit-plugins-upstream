## Description:

Helps developers integrate antiRea into Node.js applications to measure scraping and coordinated abuse patterns and choose responses to advisory signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dankezo](https://clawhub.ai/user/dankezo)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add antiRea's server-side abuse signals to a Node.js application, including metering, enumeration, and coordinated-activity checks. It guides them through selecting a signal and wiring it so the host application retains control over any response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security behavior review is incomplete because three local references could not be resolved.

Mitigation: Review the skill instructions and inspect relevant referenced material before relying on guidance that depends on those references.

Risk: Treating an advisory signal as a verdict could lead to inappropriate enforcement against legitimate users.

Mitigation: Keep consequences under host application control; use step-up for new actions only and do not penalize existing room members based solely on a signal.

## Reference(s):

- [anti-rea ClawHub release](https://clawhub.ai/dankezo/skills/anti-rea)
- [Project repository URL declared in skill metadata](https://github.com/dankezo/antiRea)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with TypeScript examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Server-side integration guidance for Node.js 20+; signals are advisory and the host application chooses responses.]

## Skill Version(s):

2.9.2 (source: frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Integrates the antiRea Node.js library into a host web application to surface advisory signals for coordinated abuse, room occupancy, vote brigading, enumeration, reconnect storms, and data harvesting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dankezo](https://clawhub.ai/user/dankezo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate antiRea signals into Node.js web applications and decide how their host application should respond to possible automated abuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because three local references could not be matched to bundled files.

Mitigation: Resolve those references and verify the relevant APIs against the 2.7.4 package before integration.

Risk: Advisory signals could be treated as proof and lead to inappropriate enforcement against users.

Mitigation: Keep responses under host control; use step-up checks for new actions and do not punish existing room members solely on a signal.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dankezo/skills/anti-rea)
- [Project repository listed in release metadata](https://github.com/dankezo/antiRea)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with TypeScript and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Server-side Node.js integration guidance; signals are advisory.]

## Skill Version(s):

2.7.4 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

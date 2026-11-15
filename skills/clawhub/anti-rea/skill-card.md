## Description:

Integrate the antiRea npm library into a host web application to meter dataset access per identity and detect automated abuse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dankezo](https://clawhub.ai/user/dankezo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add application-layer signals for per-identity harvesting, enumeration, coordinated automation, and related abuse to a Node.js web application. It guides the host integration while leaving enforcement decisions to the application.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because some local references could not be matched to bundled files.

Mitigation: Review the referenced material and integration behavior before installing or relying on the skill.

Risk: Abuse signals are advisory and lab measurements use synthetic populations, so signals can be mistaken for proof of abuse or production performance.

Mitigation: Keep authorization and enforcement decisions in the host application; do not impose consequences solely because a signal fires, and validate thresholds against the host's own traffic.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dankezo/skills/anti-rea)
- [Declared source repository](https://github.com/dankezo/antiRea)
- [npm package](https://www.npmjs.com/package/@dannyphan190/anti-rea)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with TypeScript or JavaScript examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Integration examples target Node.js 20 or later and the @dannyphan190/anti-rea package.]

## Skill Version(s):

2.9.3 (source: skill metadata, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

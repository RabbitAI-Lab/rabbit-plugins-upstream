## Description:

Query and command a Kia vehicle directly with curl against the Kia Owners API for one-off status, location, EV charging, lock, unlock, and climate operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable Kia owners use this skill to generate and adapt curl, jq, and shell workflows for direct Kia Owners API reads and remote vehicle commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help issue commands that unlock, start climate, change charging, or otherwise affect a real vehicle.

Mitigation: Require manual confirmation before executing any command that changes vehicle state, and verify completion by re-reading vehicle state rather than trusting command acceptance.

Risk: Saved refresh tokens and temporary header files can function as vehicle-account credentials.

Mitigation: Use only on a trusted single-user machine, store session files with restrictive permissions, and treat rmtoken and temporary header outputs as secrets.

Risk: Repeated rejected login attempts can trigger account protection that blocks shell-based login.

Mitigation: Do not loop or automatically retry failed login attempts; correct credentials before trying again.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [Kia Owners API base endpoint](https://api.owners.kia.com/apigw/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash and jq command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that authenticate to a Kia account or affect a vehicle; commands should be reviewed before execution.]

## Skill Version(s):

0.7.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Ambient Weather helps agents list Ambient Weather devices and read latest or historical observation data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Ambient Weather device lists, latest observations, and recent historical observations from a connected Ambient Weather account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Review OOMOL's official install guide, inspect downloaded installers, and verify any available signatures or checksums before installation.

Risk: The skill depends on an OOMOL-connected Ambient Weather account and the oo CLI.

Mitigation: Install only when the user accepts OOMOL and oo CLI as operational dependencies, and use the documented connection flow only after authentication or connection errors.

## Reference(s):

- [ClawHub Ambient Weather skill page](https://clawhub.ai/oomol/skills/oo-ambient-weather)
- [Ambient Weather homepage](https://ambientweather.net/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent may run read-only Ambient Weather connector actions and return JSON-shaped connector responses when requested.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

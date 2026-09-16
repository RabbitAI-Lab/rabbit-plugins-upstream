## Description:

LightSpeed VT (lightspeedvt.com). Use this skill for searching and reading LightSpeed VT course, location, and user data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve LightSpeed VT courses, locations, and users from an OOMOL-connected account without calling the API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes running remote installer scripts directly in a shell.

Mitigation: Install the oo CLI through a trusted, version-pinned, verifiable package, or manually inspect and verify any downloaded installer before running it.

Risk: The skill can expose readable LightSpeed VT user, course, and location data through the OOMOL connector workflow.

Mitigation: Use a LightSpeed VT account and scopes limited to data the user is comfortable exposing to the connector workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lightspeed-vt)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [LightSpeed VT homepage](https://lightspeedvt.com/)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON data]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions retrieve data available to the connected LightSpeed VT API account.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

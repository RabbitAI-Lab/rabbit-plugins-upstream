## Description:

TwitterAPI.io (twitterapi.io) helps agents inspect schemas and run TwitterAPI.io connector actions through the OOMOL oo CLI for reading, creating, updating, and deleting X/Twitter-related data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent needs to operate TwitterAPI.io connector actions for X/Twitter account, user, tweet, list, community, Space, trend, search, monitoring, and filter-rule workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may direct users to run remote installer scripts for the oo CLI.

Mitigation: Review the installer source and prefer a verified or inspected oo CLI installation path before running setup commands.

Risk: Write and destructive connector actions can change or remove monitored users, filter rules, or relationship-related state.

Mitigation: Inspect the live action schema, confirm the exact payload and target with the user, and require explicit approval before state-changing actions.

## Reference(s):

- [TwitterAPI.io homepage](https://twitterapi.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-twitterapi-io)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write and destructive actions require explicit confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

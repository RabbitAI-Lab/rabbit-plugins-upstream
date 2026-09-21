## Description:

UnifAPI (unifapi.com) lets an agent inspect action schemas and run UnifAPI connector actions through the OOMOL oo CLI for reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to retrieve social, search, SEO, GEO, web extraction, hotel, event, maps, and news data through UnifAPI, and to run write-capable connector actions only after confirming their payload and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands for the oo CLI.

Mitigation: Review the oo CLI installation method and source before running remote installer commands.

Risk: Write-tagged connector actions may use the connected OOMOL account, UnifAPI access, or credits.

Mitigation: Inspect the live action schema and confirm the exact payload and effect with the user before running write-tagged actions.

Risk: Connector authentication or connection state may be missing, expired, or insufficient for a requested action.

Mitigation: Use first-time setup only after a matching auth or connection failure, then retry with the required OOMOL and UnifAPI connection in place.

## Reference(s):

- [UnifAPI homepage](https://unifapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-unifapi)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.3 (source: evidence release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

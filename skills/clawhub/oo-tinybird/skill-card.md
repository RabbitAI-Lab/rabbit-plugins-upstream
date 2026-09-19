## Description:

Enables an agent to operate Tinybird through an OOMOL-connected account using the oo CLI for data source inspection, Pipe endpoint queries, and SQL queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data teams use this skill to query Tinybird, inspect data sources, and run published Pipe endpoints through an OOMOL-connected account without handling raw Tinybird credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running remote installer scripts for the oo CLI.

Mitigation: Review installer commands before execution and prefer a verified, version-pinned source with checksum or signature validation.

Risk: Queries run through the connected Tinybird account and may expose data available to that account.

Mitigation: Confirm the connected Tinybird account and scopes before running queries, especially in shared or production workspaces.

## Reference(s):

- [Tinybird homepage](https://www.tinybird.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed and signed-in oo CLI with a connected Tinybird account for live actions.]

## Skill Version(s):

1.0.2 (source: server evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

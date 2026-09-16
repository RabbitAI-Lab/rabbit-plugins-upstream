## Description:

Operates Tinybird through an OOMOL-connected account for listing data sources, reading metadata or stats, running pipe endpoints, and executing synchronous SQL queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Tinybird schemas, query Tinybird data, run published Pipe endpoints, and retrieve Data Source metadata through the OOMOL oo CLI without handling raw Tinybird credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute changing external code.

Mitigation: Review the setup path before installing; prefer a signed or package-manager installation for the oo CLI, or inspect and verify the installer before running it.

Risk: The skill can query data available to the connected OOMOL/Tinybird account.

Mitigation: Use an account whose Tinybird permissions and data access are appropriate for the task.

## Reference(s):

- [ClawHub Tinybird Skill](https://clawhub.ai/oomol/skills/oo-tinybird)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Tinybird Homepage](https://www.tinybird.co)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

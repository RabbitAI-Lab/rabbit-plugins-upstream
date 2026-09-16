## Description:

Chattermill helps agents operate Chattermill through the OOMOL oo CLI for reading, creating, updating, and deleting Chattermill data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Chattermill action schemas and run Chattermill connector actions through an OOMOL-connected account. It supports project, response, attribute, category, data source, data type, metric, tag, theme, and segment workflows, with explicit confirmation expected for create, update, and delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes running an internet-hosted installer, which server security evidence flags for review before installation.

Mitigation: Use safer manual installation where possible, inspect installer scripts before running them, and avoid elevated shells.

Risk: The skill can create, update, and delete Chattermill responses.

Mitigation: Require explicit user confirmation for the exact payload, target, and expected effect before any create, update, or delete action.

Risk: Connector access depends on an authenticated OOMOL account and a connected Chattermill credential.

Mitigation: Run authentication or connection setup only after a matching command failure, and keep credential handling in the server-side OOMOL flow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-chattermill)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Chattermill Homepage](https://chattermill.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Chattermill Icon](https://static.oomol.com/logo/third-party/chattermill.svg)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing requests; Chattermill command responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

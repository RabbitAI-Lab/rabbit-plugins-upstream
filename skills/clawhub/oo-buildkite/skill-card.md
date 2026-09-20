## Description:

Buildkite skill for reading, creating, updating, and deleting Buildkite data through the OOMOL-connected Buildkite connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI operators use this skill to inspect Buildkite organizations, pipelines, builds, users, and token details, and to create, cancel, or rebuild Buildkite builds after confirming write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute downloaded scripts.

Mitigation: Use a verified installation path for the oo CLI and avoid running pipe-to-shell installers automatically.

Risk: The connector can create, rebuild, or cancel Buildkite builds in a connected CI account.

Mitigation: Confirm the exact target, payload, and expected effect with the user before any write or destructive action.

Risk: Token scopes and token owner details may expose sensitive account metadata.

Mitigation: Treat token inspection output as sensitive and share only the information needed for the task.

## Reference(s):

- [ClawHub Buildkite Skill](https://clawhub.ai/oomol/skills/oo-buildkite)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Buildkite Homepage](https://buildkite.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Buildkite Connection](https://console.oomol.com/app-connections?provider=buildkite)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke the oo CLI to run Buildkite connector actions and return JSON responses from the connector.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

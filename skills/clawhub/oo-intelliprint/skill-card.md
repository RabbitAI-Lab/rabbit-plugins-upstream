## Description:

Intelliprint helps an agent search and read Intelliprint data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Intelliprint backgrounds, mailing lists, recipients, and print jobs, and to list those resources with supported filters, pagination, sorting, and field selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that could execute arbitrary code if run without verification.

Mitigation: Use an official, versioned installation method with verification before installing the oo CLI, and avoid running curl-to-bash or PowerShell iex installer commands blindly.

Risk: The skill depends on OOMOL as the connector between the agent and Intelliprint.

Mitigation: Use the skill only when that connector relationship is acceptable, and approve account login or Intelliprint connection steps yourself.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-intelliprint)
- [Intelliprint homepage](https://www.intelliprint.net)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before execution and to return connector results in JSON when commands run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

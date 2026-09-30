## Description:

Papertrail helps agents inspect Papertrail groups, systems, saved searches, and log events, and manage saved searches through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to search Papertrail logs, review account resources, and maintain saved event searches. Write and destructive saved-search actions should be reviewed with the user before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes pipe-to-shell install commands for the OOMOL CLI.

Mitigation: Prefer official install documentation, inspect downloaded scripts before execution, and install only when the user trusts OOMOL and accepts connecting Papertrail through the CLI.

Risk: Saved-search create, update, and delete actions can change or remove Papertrail state.

Mitigation: Fetch the live schema, present the exact payload and expected effect, and require explicit user approval before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-papertrail)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Papertrail Homepage](https://www.papertrail.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; write and destructive saved-search changes require user confirmation.]

## Skill Version(s):

1.0.0 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

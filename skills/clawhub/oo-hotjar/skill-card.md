## Description:

Operate Hotjar through an OOMOL-connected account using the oo CLI for reading, creating, updating, and deleting Hotjar data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to operate Hotjar through a user's OOMOL-connected account, including survey retrieval, survey response listing, and organization user lookup requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run a destructive Hotjar user lookup action when deleteAllHits is true.

Mitigation: Require explicit user approval for the target and payload before running destructive actions.

Risk: The first-time setup path includes a remote oo CLI installer command.

Mitigation: Run the installer only when the CLI is missing and the user trusts the OOMOL CLI source and installation path.

Risk: Incorrect write or lookup payloads could affect the connected Hotjar account.

Mitigation: Fetch the live action schema with oo connector schema and review payloads before write or destructive execution.

## Reference(s):

- [Hotjar homepage](https://www.hotjar.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hotjar)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

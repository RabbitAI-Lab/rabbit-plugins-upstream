## Description:

Harvest (getharvest.com). Use this skill for Harvest requests that read, create, update, and delete data through the OOMOL-connected Harvest connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Harvest through an OOMOL-connected account: inspect live action schemas, read Harvest resources, and manage time entries. State-changing and destructive actions require payload review and explicit approval before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could be unsafe if run blindly.

Mitigation: Confirm trust in OOMOL before installation and prefer a pinned release with a verified checksum or signature.

Risk: Harvest write and destructive actions can change or delete account data.

Mitigation: Inspect the live schema, review the exact payload and effect with the user, and require explicit approval before running write or destructive actions.

## Reference(s):

- [Harvest homepage](https://www.getharvest.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-harvest)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; command responses are JSON when run with --json.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

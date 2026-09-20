## Description:

ERPNext (erpnext.com) skill for reading, creating, updating, and deleting ERPNext data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate ERPNext through a connected OOMOL account, including document reads, creates, updates, deletes, counts, and field lookups. It guides the agent to inspect live action schemas before sending JSON payloads and to request confirmation before state-changing or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute mutable external code.

Mitigation: Review the installer path before use and prefer a verified package or downloaded installer with checksum or signature validation.

Risk: ERPNext create, update, set-value, and delete actions can change or remove business data.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running write actions, and require explicit approval before destructive delete actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-erpnext)
- [ERPNext homepage](https://erpnext.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON from the oo CLI when actions are run with --json.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

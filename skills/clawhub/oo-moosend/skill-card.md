## Description:

Moosend (moosend.com) enables agent-assisted Moosend requests for reading, creating, and updating marketing data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to inspect Moosend action schemas, list mailing lists and subscribers, retrieve subscribers by email, and add or update subscriber records after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include network-to-shell installer commands for the oo CLI.

Mitigation: Review the oo CLI installation path and prefer an official package manager, pinned release, or installer with checksum or signature verification.

Risk: The add_subscriber action can create or update Moosend subscriber data.

Mitigation: Confirm the exact subscriber payload and intended effect with the user before running write actions.

## Reference(s):

- [Moosend homepage](https://www.moosend.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

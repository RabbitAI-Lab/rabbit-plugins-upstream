## Description:

Mailtrap (mailtrap.io). Use this skill for Mailtrap requests that read, create, update, or delete data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Mailtrap schemas and run Mailtrap connector actions for inboxes, messages, projects, contacts, templates, domains, lists, billing usage, and sending statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path documents direct shell execution of a remote oo CLI installer.

Mitigation: Review the skill before installing, and install the oo CLI through a verified, version-pinned, checksum- or signature-checked method where possible.

Risk: Write and destructive Mailtrap actions can change or remove account data.

Mitigation: Confirm the exact payload, target resource, and intended effect with the user before running write or destructive actions.

## Reference(s):

- [Mailtrap homepage](https://mailtrap.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Mailtrap skill page](https://clawhub.ai/oomol/skills/oo-mailtrap)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

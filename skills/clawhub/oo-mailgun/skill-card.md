## Description:

Mailgun (mailgun.com). Use this skill for Mailgun requests that read, create, update, and delete data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Mailgun domains, events, templates, suppressions, tracking settings, and email sending through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mailgun requests and responses route through OOMOL and may contain operational email data.

Mitigation: Install only if OOMOL is acceptable for the account's data handling requirements, and use a narrowly scoped Mailgun key.

Risk: The artifact documents remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Avoid pipe-to-shell installation unless the installer source is independently verified or replaced with a reviewed installation path.

Risk: Write, send, update, and destructive Mailgun actions can alter account state or remove records.

Mitigation: Inspect the live action schema, confirm the exact payload and effect with the user, and require explicit approval for destructive targets.

## Reference(s):

- [Mailgun homepage](https://www.mailgun.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Mailgun skill](https://clawhub.ai/oomol/skills/oo-mailgun)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [oo CLI responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server evidence release.version and skill metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

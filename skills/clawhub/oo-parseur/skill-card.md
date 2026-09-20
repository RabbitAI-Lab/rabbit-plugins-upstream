## Description:

Parseur enables agents to search and read Parseur mailboxes, documents, mailbox schemas, and parsed data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Parseur connector schemas and retrieve Parseur mailboxes, documents, mailbox schemas, and parsed document data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes mutable remote installer commands executed directly in a shell.

Mitigation: Review the oo CLI installation path before installing; prefer an official package manager, pinned release, or installer verified by checksum or signature.

Risk: Using the OOMOL-connected Parseur integration can expose mailbox and document data to the connected service path.

Mitigation: Confirm the user is comfortable granting OOMOL-connected Parseur read access to mailbox and document data before use.

Risk: Connector inputs may drift from the static skill text.

Mitigation: Inspect the live action schema with `oo connector schema` before submitting JSON payloads.

## Reference(s):

- [Parseur homepage](https://parseur.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Parseur skill on ClawHub](https://clawhub.ai/oomol/skills/oo-parseur)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building JSON payloads; command responses are JSON when run with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

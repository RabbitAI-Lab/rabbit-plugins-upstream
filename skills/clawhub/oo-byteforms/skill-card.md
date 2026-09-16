## Description:

ByteForms (forms.bytesuite.io) helps agents search and read ByteForms data through OOMOL's oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users with an OOMOL-connected ByteForms account use this skill to inspect schemas, list available forms, retrieve a specific form, and list form responses through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that are executed directly in a shell.

Mitigation: Review the oo CLI installation path before use and prefer an official package manager or a version-pinned installer with checksum or signature verification.

Risk: The skill depends on an OOMOL-connected ByteForms account and the account's available scopes.

Mitigation: Use the authenticated account intentionally, inspect the live action schema before building payloads, and reconnect ByteForms only when an auth or connection error requires it.

## Reference(s):

- [ClawHub ByteForms skill page](https://clawhub.ai/oomol/skills/oo-byteforms)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ByteForms homepage](https://forms.bytesuite.io/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON response details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live ByteForms action schemas through the oo CLI; normal documented actions are read-only.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

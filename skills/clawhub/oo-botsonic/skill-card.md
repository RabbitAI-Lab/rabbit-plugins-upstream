## Description:

Use Botsonic through an OOMOL-connected account to generate bot responses and read conversations or FAQs via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Botsonic account from an agent session. It supports generating a Botsonic response and reading conversations or FAQs after confirming the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer scripts executed directly in a shell without verification.

Mitigation: Prefer an official package or pinned oo CLI release when available, verify checksums or signatures, and review installer contents before execution.

Risk: Prompts, conversation identifiers, and action payloads may be sent through the connected Botsonic/OOMOL service.

Mitigation: Use Botsonic actions only after confirming the OOMOL account connection and checking that the request data is appropriate for the connected service.

## Reference(s):

- [Botsonic homepage](https://botsonic.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields when actions are run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

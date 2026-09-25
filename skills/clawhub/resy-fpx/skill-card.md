## Description:

Query and act on Resy restaurant reservations from a shell using curl against api.resy.com, with optional fpx token bootstrap when email/password credentials are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Resy venues, inspect availability, retrieve profile and payment method details, and perform reservation, favorite, and Priority Notify actions from shell workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose or reuse sensitive Resy credentials, account tokens, signed-in browser sessions, and payment method identifiers.

Mitigation: Only use it in trusted workspaces, keep RESY_EMAIL, RESY_PASSWORD, RESY_TOKEN, and payment method identifiers out of logs and shared transcripts, and rotate credentials or tokens if exposed.

Risk: Ready-to-run write commands can book, cancel, favorite, or create/remove Priority Notify entries on a real Resy account.

Mitigation: Require explicit user confirmation before every write action and verify state with list/read calls before and after execution.

## Reference(s):

- [Resy API ready-to-run requests](references/resy-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with curl, jq, npm, and fpx command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes ready-to-run API requests and setup guidance for authenticated Resy account actions.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Happy Scribe helps an agent read, create, update, export, and delete Happy Scribe data through the OOMOL happy_scribe connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Happy Scribe account from an agent workflow, including transcription listing, order creation, export creation, updates, and deletion when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create orders, create exports, update transcriptions, confirm orders, and delete transcriptions in a connected Happy Scribe account.

Mitigation: Review the live action schema and obtain explicit user approval for the exact payload before running write or destructive actions.

Risk: Connector access depends on the user's OOMOL account, Happy Scribe connection, scopes, credentials, and billing state.

Mitigation: Run setup or connection steps only after an action fails with the matching authentication, scope, credential, app, or billing error.

## Reference(s):

- [Happy Scribe homepage](https://www.happyscribe.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-happy-scribe)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the OOMOL connector when run with --json.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

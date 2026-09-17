## Description:

Typeform lets an agent search and read Typeform account data, forms, workspaces, and form responses through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Typeform account resources and retrieve form responses through the OOMOL oo CLI without handling raw Typeform tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Prefer official, versioned installation instructions with verification, and review installer commands before running them.

Risk: Authenticated connector access can expose Typeform account, form, workspace, and response data.

Mitigation: Run only the read actions needed for the user's request and inspect the connector schema before sending payloads.

## Reference(s):

- [Typeform Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-typeform)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Typeform](https://www.typeform.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; listed Typeform actions are read-only after authentication.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Formstack Documents helps agents operate Formstack Documents through the OOMOL oo CLI for listing, retrieving, creating, updating, copying, and deleting document templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to manage Formstack Documents templates from an OOMOL-connected account, including reading document details and fields and performing confirmed write or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: State-changing or destructive connector actions can modify or delete Formstack Documents templates.

Mitigation: Confirm the exact action, target document, and JSON payload with the user before running write or delete actions.

Risk: Connector actions depend on the user's connected OOMOL account and current Formstack Documents credentials.

Mitigation: Use first-time setup steps only after an authentication, connection, scope, credential, or billing error occurs.

## Reference(s):

- [Formstack Documents homepage](https://forms.formstack.com/products/documents)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

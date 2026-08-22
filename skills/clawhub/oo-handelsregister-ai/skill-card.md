## Description:

Handelsregister AI (handelsregister.ai) helps an agent search and read German commercial-register organization data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search German commercial-register organizations and retrieve company profiles by name, register number, search query, or exact entity identifier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an OOMOL-connected Handelsregister AI account and may fail if authentication, provider connection, scope, or billing is not ready.

Mitigation: Use the documented setup and error-handling paths only after an action fails with the matching auth, connection, scope, expiration, or billing error.

Risk: Optional paid enrichment or account-dependent behavior may create unexpected billing or availability outcomes.

Mitigation: Confirm the user intends to query Handelsregister AI through the connected account before use, and treat payment-related failures as account-configuration issues.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-handelsregister-ai)
- [Handelsregister AI homepage](https://handelsregister.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL Handelsregister AI connection](https://console.oomol.com/app-connections?provider=handelsregister_ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent guidance for read-only connector actions and first-time setup handling.]

## Skill Version(s):

1.0.0 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

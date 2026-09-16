## Description:

Elevio lets agents search and read Elevio knowledge base articles and categories through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Elevio action schemas, search knowledge base articles, list articles or categories, and retrieve individual articles or categories from an OOMOL-connected Elevio account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup asks users to execute mutable remote installer scripts directly in a shell.

Mitigation: Use an independently verified, pinned, or package-manager installation path when available, and only run remote installer commands after trusting the OOMOL installer source.

Risk: Connector actions depend on the live Elevio action schema and the connected OOMOL account state.

Mitigation: Inspect the live action schema before constructing payloads and fall back to setup only after an authentication, connection, scope, expiration, app, or billing error.

## Reference(s):

- [Elevio Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-elevio)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Elevio Homepage](https://elev.io)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Elevio connector responses are returned as JSON from the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

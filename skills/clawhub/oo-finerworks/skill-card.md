## Description:

FinerWorks connector skill for searching and reading catalog and pricing data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect FinerWorks connector schemas and perform catalog, product, style, media, and pricing lookups through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use requires installing and authenticating the OOMOL oo CLI and connecting a FinerWorks account.

Mitigation: Complete one-time setup only when needed, and install or connect the provider only if the user understands the OOMOL account and FinerWorks connection requirements.

Risk: Connector calls depend on live action schemas and JSON payloads.

Mitigation: Inspect the action schema before constructing payloads and run only payloads that match the returned contract.

Risk: Future connector actions tagged as write or destructive could change or remove account data.

Mitigation: Confirm the exact payload and intended effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub FinerWorks skill page](https://clawhub.ai/oomol/skills/oo-finerworks)
- [FinerWorks homepage](https://finerworks.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command results are returned as JSON.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

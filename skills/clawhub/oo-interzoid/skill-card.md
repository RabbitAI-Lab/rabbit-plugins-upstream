## Description:

Provides OOMOL-connected access to Interzoid connector actions for schema inspection, match-key generation, email and IP enrichment, credit checks, and organization-name standardization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to operate Interzoid through an OOMOL-connected account without handling raw Interzoid API tokens. It supports data matching, validation, enrichment, reputation lookup, and account credit-check workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer one-liners that execute downloaded code.

Mitigation: Use a pinned, signed, checksum-verified installer or an official package-manager path before allowing installation commands.

Risk: Normal use may send names, email addresses, or IP addresses through OOMOL to Interzoid.

Mitigation: Confirm the data-sharing intent with the user before running account-backed lookups involving personal or network identifiers.

## Reference(s):

- [ClawHub Interzoid Skill](https://clawhub.ai/oomol/skills/oo-interzoid)
- [Interzoid Homepage](https://www.interzoid.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live connector schemas before running Interzoid actions through the oo CLI.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

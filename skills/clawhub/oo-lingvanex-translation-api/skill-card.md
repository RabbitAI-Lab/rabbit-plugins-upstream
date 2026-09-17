## Description:

Lingvanex Translation API helps agents detect languages, list supported languages, and translate text through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route language detection, supported-language lookup, and translation requests through an OOMOL-connected Lingvanex account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer instructions direct users to execute downloaded shell or PowerShell scripts.

Mitigation: Prefer an official package-managed or verified installation method; otherwise inspect and verify installer scripts before executing them.

Risk: Translation text is processed through the OOMOL and Lingvanex service path.

Mitigation: Use the skill only when that service path is acceptable for the data being translated, and avoid sensitive text unless permitted by policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lingvanex-translation-api)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Lingvanex Translation API homepage](https://lingvanex.com/products/translationapi/)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing Lingvanex request payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

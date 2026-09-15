## Description:

Cloudflare Docs helps agents search and retrieve documentation from developers.cloudflare.com through the OOMOL cloudflare_docs connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to answer Cloudflare Docs questions, search Cloudflare product documentation, and retrieve the Pages-to-Workers migration guide.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts for the oo CLI.

Mitigation: Prefer a verified or package-manager installation path, review what will be installed, and avoid executing remote installer scripts directly in a shell.

Risk: Connector use depends on OOMOL as the connector and credential provider.

Mitigation: Use this skill only when the operator is comfortable with OOMOL providing the connector and handling server-side credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudflare-docs)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Cloudflare Docs](https://developers.cloudflare.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses schema-first connector calls and expects the oo CLI plus an OOMOL-connected cloudflare_docs account when setup is required.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Mezmo helps agents inspect live action schemas and read Mezmo ingestion status and usage data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to check Mezmo ingestion status and retrieve usage summaries grouped by app, host, or tag through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute scripts directly.

Mitigation: Review the oo CLI installation path, prefer an official signed or package-manager installation method, verify checksums or signatures where available, and avoid elevated shells for pipe-to-shell installation.

## Reference(s):

- [ClawHub Mezmo Skill](https://clawhub.ai/oomol/skills/oo-mezmo)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Mezmo Homepage](https://www.mezmo.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON data and execution metadata through the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

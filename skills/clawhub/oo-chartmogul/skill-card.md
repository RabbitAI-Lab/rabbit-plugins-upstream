## Description:

ChartMogul (chartmogul.com). Use this skill for ChartMogul requests that search or read data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to inspect ChartMogul account settings, customers, contacts, and data sources from an authenticated OOMOL-connected ChartMogul account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can require installing the oo CLI and authenticated access to ChartMogul data through OOMOL.

Mitigation: Review before installing, prefer safer oo CLI installation methods where possible, and verify installer provenance.

Risk: Actions run with access to authenticated ChartMogul data.

Mitigation: Inspect the connector schema before use and require explicit user confirmation for any action beyond the listed get and list operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-chartmogul)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [ChartMogul Homepage](https://chartmogul.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return ChartMogul data from authenticated get and list actions.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

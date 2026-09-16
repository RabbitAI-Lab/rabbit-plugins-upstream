## Description:

CompanyEnrich (companyenrich.com) lets an agent search, count, enrich, and compare company records through an OOMOL-connected CompanyEnrich account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and sales or research teams use this skill to query CompanyEnrich data, enrich company profiles by domain or properties, find similar companies, and inspect account capabilities without handling raw service credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote oo CLI installer scripts directly in a shell.

Mitigation: Review the installer source and prefer a pinned, signed, or checksum-verified oo CLI installation method before first use; once oo is installed and connected, run only the scoped CompanyEnrich read, search, and enrichment commands.

## Reference(s):

- [CompanyEnrich homepage](https://companyenrich.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub CompanyEnrich skill page](https://clawhub.ai/oomol/skills/oo-companyenrich)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL oo CLI commands that return JSON responses from CompanyEnrich connector actions.]

## Skill Version(s):

1.0.3 (source: artifact metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

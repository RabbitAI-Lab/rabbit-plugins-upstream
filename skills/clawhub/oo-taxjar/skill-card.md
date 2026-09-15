## Description:

Enables agents to operate TaxJar through the OOMOL oo CLI for tax calculations, rate lookups, VAT validation, and customer, order, and refund transaction workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operations users use this skill to let an agent inspect TaxJar connector schemas and run TaxJar read, write, and destructive actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run a remote OOMOL CLI installer.

Mitigation: Review the installer before execution and prefer a verified release or checksum when available.

Risk: The skill can create, update, or delete business tax data through TaxJar connector actions.

Mitigation: Use an appropriate TaxJar account and require explicit confirmation of payloads and targets before write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-taxjar)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [TaxJar Homepage](https://www.taxjar.com/)
- [TaxJar Icon](https://static.oomol.com/logo/third-party/Taxjar.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to inspect live connector schemas before constructing payloads and to confirm state-changing or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

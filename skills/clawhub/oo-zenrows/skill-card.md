## Description:

ZenRows lets agents fetch HTML or plain text from public URLs, extract CSS-selected data, and check connected account usage through the OOMOL ZenRows connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve web page content, extract structured values with CSS selectors, and inspect ZenRows usage through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes remote installer commands that execute downloaded scripts.

Mitigation: Review the oo CLI installation path first, and prefer a versioned installer or package-manager install with checksum or signature verification.

Risk: Connector use may send target URLs and account-connected activity through OOMOL and ZenRows.

Mitigation: Only connect accounts and submit URLs or data that are acceptable to process through those services.

## Reference(s):

- [ZenRows homepage](https://www.zenrows.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub ZenRows skill page](https://clawhub.ai/oomol/skills/oo-zenrows)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON response expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the ZenRows connector through the oo CLI and may return JSON data from connector actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Eagle Doc helps agents operate Eagle Doc through the OOMOL oo CLI to retrieve usage and quota information, inspect request logs, and process finance documents with OCR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected Eagle Doc account from an agent, including checking current usage, quota, monthly history, request logs, and processing invoices, receipts, or PDFs with Finance OCR.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload invoices, receipts, PDFs, or other financial documents to OOMOL/Eagle Doc for processing.

Mitigation: Require explicit user approval before uploading any financial or sensitive document, and confirm the exact file and intended action.

Risk: First-time setup guidance includes pipe-to-shell installer commands.

Mitigation: Use a verified oo CLI installation path or reviewed installer source instead of running pipe-to-shell commands without review.

## Reference(s):

- [Eagle Doc APIs](https://www.eagle-doc.com/en/products/eagle-doc-apis/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Eagle Doc skill listing](https://clawhub.ai/oomol/skills/oo-eagle-doc)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing JSON payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

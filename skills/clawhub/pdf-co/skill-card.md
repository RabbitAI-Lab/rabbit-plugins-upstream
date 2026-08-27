## Description:

PDF.co API integration with managed OAuth for converting, merging, splitting, editing, and extracting data from PDFs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to route PDF.co document operations through Maton-managed authentication, including PDF conversion, merging, splitting, editing, text and table extraction, and invoice parsing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF work is routed through Maton and PDF.co.

Mitigation: Install only when that routing is acceptable, and review which PDF.co account is connected before use.

Risk: Connection creation and PDF edit, delete, or write operations can affect the connected account or documents.

Mitigation: Require deliberate user approval before creating a connection or running any write/edit/delete operation, including confirmation of the target connection and payload.

Risk: API-key fallback can expose long-lived credentials if used casually.

Mitigation: Prefer Maton OAuth and the OS credential store; use API-key fallback only when the CLI cannot be used.

## Reference(s):

- [PDF.co ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/pdf-co)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [PDF.co API Documentation](https://docs.pdf.co)
- [PDF.co API Reference](https://docs.pdf.co/api-reference)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval before connection creation or write/edit/delete operations.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

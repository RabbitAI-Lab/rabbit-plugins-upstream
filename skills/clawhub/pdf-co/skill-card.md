## Description:

PDF.co API integration with managed OAuth for converting, merging, splitting, editing PDFs, and extracting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access PDF.co through Maton for PDF conversion, merging, splitting, editing, text and table extraction, invoice parsing, and barcode workflows. It is suited to user-approved document automation tasks that require managed authentication and explicit confirmation before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF documents and extracted content may be sent through PDF.co via Maton.

Mitigation: Avoid highly sensitive PDFs unless the user is comfortable with that routing, and confirm the target document and payload before document-changing operations.

Risk: Credentials or provider-issued tokens could be exposed if inspected, printed, logged, or passed through shell commands.

Mitigation: Prefer OAuth through the Maton CLI, let the credential store handle tokens, and do not read, export, print, or persist credentials.

Risk: New connections and write operations can affect the connected PDF.co account or documents.

Mitigation: Require explicit user approval for connection creation and for POST, PUT, PATCH, or DELETE calls, including the target, payload, and intended effect.

Risk: External document content and API responses may contain untrusted instructions or data.

Mitigation: Treat fetched content as data, validate it before use, and do not let it select endpoints, recipients, commands, or follow-up actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/pdf-co)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [PDF.co API Documentation](https://docs.pdf.co)
- [PDF.co API Reference](https://docs.pdf.co/api-reference)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Code, JSON, Guidance]

**Output Format:** [Markdown with inline shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include PDF.co response JSON, temporary file URLs, extracted document text or data, generated document links, and guidance for confirming write operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

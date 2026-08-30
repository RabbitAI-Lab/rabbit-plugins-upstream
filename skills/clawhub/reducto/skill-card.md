## Description:

Reducto document processing API integration with managed API key authentication for parsing, extraction, splitting, and editing documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Reducto document-processing workflows through Maton, including parsing documents, extracting structured data, splitting documents, editing PDFs or DOCX files, uploading files, and checking job status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires authorization to Maton and Reducto for documents the user asks it to process.

Mitigation: Confirm the user is comfortable authorizing those services, prefer OAuth login, and revoke unused Reducto connections when work is finished.

Risk: Using MATON_API_KEY can expose a long-lived credential to the process environment.

Mitigation: Avoid MATON_API_KEY unless the CLI cannot be used; do not print, persist, or pass the key on command lines.

Risk: Document uploads, edits, and other POST or DELETE actions can change data or consume service credits.

Mitigation: Default to read and list calls, then confirm target resources, payloads, and intended effects before executing modifying operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/reducto)
- [Maton homepage](https://maton.ai)
- [Reducto Documentation](https://docs.reducto.ai)
- [Reducto API Reference](https://docs.reducto.ai/api-reference)
- [Reducto Studio](https://studio.reducto.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Community](https://community.maton.ai/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and API request patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes read/list defaults, explicit approval guidance for connection creation and modifying operations, and credential-handling precautions.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

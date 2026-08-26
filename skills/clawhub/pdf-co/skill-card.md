## Description:

PDF.co API integration with managed OAuth for converting, merging, splitting, editing PDFs, and extracting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform user-directed PDF.co work through Maton, including document conversion, merging, splitting, editing, text and table extraction, invoice parsing, and barcode operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing PDF.co through Maton can grant access to PDF.co document operations on the connected account.

Mitigation: Confirm new connections with the user, choose the least-privileged scopes available, and revoke unused connections.

Risk: Broad endpoint passthrough and write/edit operations can modify documents or consume account resources.

Mitigation: Default to read or list calls, specify the intended connection when more than one exists, and confirm the target, payload, and effect before any write, edit, or delete operation.

Risk: Raw API-key fallback uses a broader long-lived secret that can be exposed through environment variables, logs, shell history, or process listings.

Mitigation: Prefer OAuth through the Maton CLI; use raw API-key fallback only when the CLI cannot be used, never persist or log the key, and avoid passing it on the command line.

## Reference(s):

- [PDF.co ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/pdf-co)
- [Maton Homepage](https://maton.ai)
- [PDF.co API Documentation](https://docs.pdf.co)
- [PDF.co API Reference](https://docs.pdf.co/api-reference)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance, API Calls]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes endpoint examples, authentication guidance, SDK snippets, and operational cautions for user approval and credential handling.]

## Skill Version(s):

1.1.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

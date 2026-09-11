## Description:

PDF.co API integration with managed OAuth for converting, merging, splitting, editing PDFs, and extracting document data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate PDF.co through Maton for PDF conversion, merging, splitting, editing, extraction, parsing, barcode, and asynchronous document jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the wrong Maton package or Homebrew tap could introduce supply-chain exposure.

Mitigation: Verify the Maton package and Homebrew tap publisher before installing, and avoid elevated privileges unless required by the local environment.

Risk: Long-lived API keys can leak through environment variables, shell history, logs, or child processes.

Mitigation: Prefer OAuth through the Maton CLI; if an API key is unavoidable, keep it in the active session only, never print it, and rotate it after exposure.

Risk: PDF.co operations may change files, account state, connections, or sensitive documents.

Mitigation: Require explicit user confirmation before creating connections or running mutating operations, and confirm the target connection, payload, and intended effect.

Risk: Fetched document content or API responses may contain untrusted instructions or data.

Mitigation: Treat returned content as data only, validate it before reuse, and do not execute or interpolate it into shell commands.

## Reference(s):

- [PDF.co ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/pdf-co)
- [Maton Homepage](https://maton.ai)
- [PDF.co API Documentation](https://docs.pdf.co)
- [PDF.co API Reference](https://docs.pdf.co/api-reference)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Code, Configuration, Guidance]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maton CLI and SDK examples may return JSON, extracted text, generated files, or temporary PDF.co file URLs.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

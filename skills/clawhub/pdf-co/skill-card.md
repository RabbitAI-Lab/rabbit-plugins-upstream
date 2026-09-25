## Description:

PDF.co API integration with managed OAuth for converting, merging, splitting, editing, and extracting data from PDFs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation builders use this skill to call PDF.co through Maton for PDF conversion, merging, splitting, editing, text and table extraction, and invoice parsing. It supports one-off CLI/API requests and user-approved hosted automation around PDF.co actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documents, URLs, extracted text, PDF passwords, and generated output links may be processed by PDF.co or exposed through public-but-unlisted links.

Mitigation: Send only task-required content, avoid logging raw responses, and confirm with the user before submitting sensitive files or credentials.

Risk: Hosted functions, schedules, triggers, and third-party forwarding can create ongoing automated data flows.

Mitigation: Require explicit user approval, scope each automation to the intended connection and task, prefer DENY_ALL network policy for hosted functions, and delete automation when it is no longer needed.

## Reference(s):

- [PDF.co ClawHub Skill](https://clawhub.ai/byungkyu/skills/pdf-co)
- [Maton](https://maton.ai)
- [PDF.co API Documentation](https://docs.pdf.co)
- [PDF.co API Reference](https://docs.pdf.co/api-reference)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, raw HTTP examples, user-approval guidance, and PDF.co API request patterns.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

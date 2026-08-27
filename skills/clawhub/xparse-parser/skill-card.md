## Description:

TextIn xParse Document Parse helps agents parse, navigate, search, summarize, and extract tables or structured evidence from supported local documents or document URLs through xparse-cli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[intsig-textin](https://clawhub.ai/user/intsig-textin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document-processing agents use this skill to convert, inspect, navigate, and extract evidence from PDFs, images, Office files, HTML, OFD, and other supported documents. It supports both immediate single-document parsing and durable multi-document Task Runtime workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents or document URLs may be sent to the xparse/TextIn service for parsing.

Mitigation: Use the skill only when that transfer is acceptable; avoid confidential files unless approved.

Risk: Parsed exports can contain sensitive document content.

Mitigation: Store exported Markdown or JSON results carefully and remove temporary files when they are no longer needed.

Risk: Document passwords and service credentials can be exposed through unsafe command examples or logs.

Mitigation: Prefer safer password handling, do not print credential files, and avoid typing real passwords directly into reusable command examples.

Risk: Paid parsing can incur service charges if selected without clear approval.

Mitigation: Use automatic free-first routing by default and require explicit user approval before invoking paid API routes.

## Reference(s):

- [Document navigation](references/navigation.md)
- [Durable Task Runtime](references/task-runtime.md)
- [Authentication](references/authentication.md)
- [CLI Guidance](references/cli-guidance.md)
- [API Reference](references/api-reference.md)
- [Structured Error Handling](references/error-handling.md)
- [TextIn AppKey Setup](references/textin-key-setup.md)
- [TextIn Parse API v1](https://docs.textin.com/xparse/v1/)
- [TextIn Parse Config](https://docs.textin.com/xparse/v1/parse-config)
- [TextIn Parse Response](https://docs.textin.com/xparse/v1/parse-response)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with shell commands, JSON examples, and extracted document content or structured evidence.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce saved Markdown or JSON result files when xparse-cli is invoked with an output directory.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

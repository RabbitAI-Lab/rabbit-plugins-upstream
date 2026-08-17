## Description:

TextIn xParse Document Parse helps agents parse, read, search, navigate, summarize, and extract tables or structured evidence from PDFs, images, Office files, HTML, OFD, and other supported local documents or document URLs through xparse-cli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[intsig-textin](https://clawhub.ai/user/intsig-textin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and document-processing agents use this skill to convert supported documents into Markdown or JSON and to navigate, search, and extract targeted facts, pages, sections, tables, and structured evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documents are processed through TextIn's external service, which may be inappropriate for confidential or regulated content.

Mitigation: Use the skill only for documents approved for that external service, and avoid regulated or confidential documents without organizational approval.

Risk: Credentials, document passwords, or API keys can be exposed if pasted into conversations, printed, or passed carelessly through shell history.

Mitigation: Prefer interactive or protected credential flows, do not paste secrets into conversations, avoid verbose authentication output, and handle command-line passwords and exported API keys carefully.

Risk: Paid parsing or quota exhaustion can create unexpected cost or workflow interruption.

Mitigation: Use automatic routing by default, inspect quota when needed, and require explicit user approval before switching to paid parsing.

Risk: Unsupported, corrupt, encrypted, oversized, or failed service requests may lead to incomplete extraction.

Mitigation: Stop and explain the specific condition, request missing passwords or valid inputs when required, and retry transient service failures at most once.

## Reference(s):

- [Navigation Workflow](artifact/references/navigation.md)
- [Authentication](artifact/references/authentication.md)
- [CLI Guidance](artifact/references/cli-guidance.md)
- [API Reference](artifact/references/api-reference.md)
- [Structured Error Handling](artifact/references/error-handling.md)
- [TextIn AppKey Setup](artifact/references/textin-key-setup.md)
- [TextIn Parse API v1](https://docs.textin.com/xparse/v1/)
- [TextIn xParse purchase page](https://www.textin.com/market/chager/pdf_to_markdown)
- [TextIn Console](https://www.textin.com/console/dashboard/setting)
- [TextIn Documentation](https://docs.textin.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples; parsed document outputs may be Markdown or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to save large parse outputs to files and use xparse-cli navigation commands for targeted extraction.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

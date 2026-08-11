## Description:

Parse PDFs, images, Office files, HTML, OFD, and other supported documents into Markdown or structured JSON through xparse-cli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[intsig-textin](https://clawhub.ai/user/intsig-textin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users use this skill to parse local documents or document URLs into Markdown for review or structured JSON for extraction, tables, coordinates, page metadata, and downstream agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs xparse-cli through a remote installer.

Mitigation: Install only in environments where TextIn's remote installer is approved, and review installer contents before running it.

Risk: Parsing sends document contents to TextIn's external parsing service.

Mitigation: Avoid confidential, regulated, or restricted documents unless organizational policy permits use of this service.

Risk: Authentication material or document passwords could be exposed through chat, verbose logs, or shell history.

Mitigation: Use the documented WorkBuddy connector or CLI authentication flows, avoid printing credential files or verbose authentication output, and avoid passing sensitive passwords directly on the command line when possible.

Risk: Stored credentials or paid account setup could unintentionally cause paid API usage.

Mitigation: Keep the free API as the default and use the paid API only after explicit user approval.

## Reference(s):

- [Authentication](artifact/references/authentication.md)
- [CLI Guidance](artifact/references/cli-guidance.md)
- [API Reference](artifact/references/api-reference.md)
- [Error Handling](artifact/references/error-handling.md)
- [TextIn AppKey Setup](artifact/references/textin-key-setup.md)
- [TextIn xParse API v1](https://docs.textin.com/xparse/v1/)
- [TextIn Documentation](https://docs.textin.com/)
- [TextIn xParse purchase page](https://www.textin.com/market/chager/pdf_to_markdown)
- [TextIn Console](https://www.textin.com/console/dashboard/setting)

## Skill Output:

**Output Type(s):** [text, markdown, structured JSON, shell commands, configuration guidance]

**Output Format:** [Markdown or JSON from xparse-cli, plus concise guidance and commands when setup or recovery is required.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the free API by default; paid API requires explicit user approval; PDF outputs should be saved to a directory before reading.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

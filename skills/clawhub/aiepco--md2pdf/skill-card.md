## Description:

Convert Markdown files to rendered, print-ready PDFs with Chinese-friendly typography, offline assets, and local Chrome-based PDF generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiepco](https://clawhub.ai/user/aiepco)

### License/Terms of Use:

MIT

## Use Case:

Developers and document authors use this skill to export Markdown reports, documentation, resumes, meeting notes, and other written material into polished PDF files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found that Markdown content is rendered unsanitized in Chrome while the browser sandbox is disabled.

Mitigation: Install only for trusted Markdown workflows; before handling unknown documents, enable Chrome sandboxing, sanitize or escape raw HTML, and disable script execution.

Risk: Remote resources embedded in Markdown or HTML may create unclear network and privacy behavior during rendering.

Mitigation: Document and restrict remote-resource behavior, or block remote loads when converting documents that may contain untrusted content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aiepco/skills/md2pdf)
- [Chrome headless printing notes](references/chrome_flags.md)
- [marked Markdown parser](https://github.com/markedjs/marked)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance with command examples and generated PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local Markdown input or stdin and writes a PDF output file.]

## Skill Version(s):

0.1.0 (source: VERSION and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

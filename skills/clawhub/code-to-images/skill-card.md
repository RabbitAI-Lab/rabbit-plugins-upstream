## Description:

Converts source code into A4-ratio, syntax-highlighted SVG and PNG pages with line numbers, then combines them into a PDF per source file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yon-gjun](https://clawhub.ai/user/yon-gjun)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to create readable, printable images and PDFs from source code, with automatic language detection and preserved indentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extra maintenance scripts can rewrite skill documentation or an installed skill file.

Mitigation: Review the package before installing and run only gen_code_pdfs.py for conversion.

Risk: Conversion executes a Node binary and uses separately installed npm and pip dependencies.

Mitigation: Verify NODE_EXE points to a trusted Node binary and install dependencies from trusted sources.

## Reference(s):

- [Source repository](https://github.com/yon-gjun/code-to-images)
- [ClawHub skill release](https://clawhub.ai/yon-gjun/skills/code-to-images)

## Skill Output:

**Output Type(s):** [Files, Images, PDF documents]

**Output Format:** [A4-ratio SVG and PNG pages and one PDF per source file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Syntax highlighting, line numbers, and preserved indentation; requires Node.js, @resvg/resvg-js, and img2pdf.]

## Skill Version(s):

2.0.6 (source: ClawHub release metadata; packaged documentation says v2.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

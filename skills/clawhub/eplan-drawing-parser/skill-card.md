## Description:

Extracts structured component, wiring topology, terminal, title-block, and BOM cross-check data from EPLAN/CAD vector PDF electrical drawings using PDF vector geometry rather than OCR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[727583550-coder](https://clawhub.ai/user/727583550-coder)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and electrical engineers use this skill to parse local EPLAN or CAD vector PDF schematics into component lists, wire topology, page-level coordinates, and drawing-vs-BOM cross-check results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Excel BOM checker writes a result workbook by default and preview mode can write PNG files.

Mitigation: Review or set output paths before running the commands, and use no-export mode when only a console report is needed.

Risk: Scanned or image-only PDFs do not contain the vector text and line layers this skill depends on.

Mitigation: Use only EPLAN/CAD vector PDFs with text and vector line layers, and verify extracted coordinates or page outputs against the source drawing.

Risk: Engineering drawings and BOM spreadsheets may contain sensitive project or supplier information.

Mitigation: Run the skill locally as documented and avoid sending source drawings or generated workbooks to external services unless separately approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/727583550-coder/skills/eplan-drawing-parser)
- [Project homepage](https://github.com/openclaw-skills/eplan-drawing-parser)
- [PyMuPDF documentation](https://pymupdf.readthedocs.io/)
- [EPLAN symbol knowledge](knowledge/eplan_symbols.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text, JSON, Files, Code]

**Output Format:** [Markdown guidance with shell commands plus generated JSON, PNG preview images, and optional XLSX workbooks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local Python 3 with pymupdf and openpyxl; processes user-provided vector PDFs and optional Excel BOM files locally.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

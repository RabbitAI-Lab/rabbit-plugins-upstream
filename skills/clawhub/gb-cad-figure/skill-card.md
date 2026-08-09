## Description:

Generates GB/T-style engineering drawings and CAD deliverables with automatic sheet selection, title blocks, dimensions, technical notes, legends, PDF/DXF output, and optional DWG conversion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hegenerkondo335-dot](https://clawhub.ai/user/hegenerkondo335-dot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create formal Chinese GB/T-style CAD engineering drawings from simple geometric inputs, including frames, title blocks, dimensions, notes, legends, and CAD-ready exchange files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DWG conversion can automatically download and execute a third-party ODA File Converter AppImage without integrity checks.

Mitigation: Use the PDF/DXF workflow when DWG is not required; when DWG is required, provide a manually verified converter through ODA_IMG or run the conversion in a sandbox with limited network and filesystem access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hegenerkondo335-dot/skills/gb-cad-figure)
- [Publisher profile](https://clawhub.ai/user/hegenerkondo335-dot)
- [ezdxf documentation](https://ezdxf.mozman.at/)
- [ODA File Converter download page](https://www.opendesign.com/guestfiles/oda_file_converter)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated PDF, DXF, and optional DWG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses millimeter-based CAD geometry and GB/T-oriented drawing conventions; DWG output depends on an external ODA converter.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Generates GB/T-style engineering drawing deliverables and CAD templates from simple CAD primitives, including title blocks, dimensions, technical notes, and PDF, DXF, and DWG outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hegenerkondo335-dot](https://clawhub.ai/user/hegenerkondo335-dot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate formal GB/T-style mechanical or architectural CAD drawings, templates, title blocks, dimensions, and related delivery files. It is intended for drawing-production workflows that need PDF, DXF, and optionally DWG outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The DWG conversion path can automatically download and execute an external ODA AppImage without integrity verification.

Mitigation: Prefer PDF/DXF output only, or preinstall a vetted converter and verify its source before enabling DWG conversion.

Risk: Font-repair troubleshooting may involve administrator-level system font-cache commands.

Mitigation: Run those commands only when the troubleshooting step is specifically needed and after reviewing the system changes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/hegenerkondo335-dot/skills/gb-cad-figure)
- [ezdxf documentation](https://ezdxf.mozman.at/)
- [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with inline Python and shell commands; generated artifacts may include PDF, DXF, and DWG files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PDF and DXF output can be produced without DWG conversion; DWG conversion depends on an external ODA AppImage path.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter reports 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

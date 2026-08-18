## Description:

Generates GB/T-style engineering drawing guidance and CAD deliverables, including drawing frames, title blocks, line styles, dimensions, isometric lathe/cylinder/box geometry, and PDF, DXF, and DWG outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hegenerkondo335-dot](https://clawhub.ai/user/hegenerkondo335-dot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent users use this skill to create formal Chinese GB/T-style CAD engineering drawings and reusable CAD templates from mechanical or architectural drawing requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The DWG workflow can automatically download and execute a third-party ODA File Converter AppImage.

Mitigation: Use PDF and DXF output when DWG is not required, or preinstall and verify the converter before allowing DWG conversion.

Risk: The artifact documents administrator-level repair commands for font and system maintenance.

Mitigation: Treat those commands as optional user-directed maintenance steps and run them only after intentional review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hegenerkondo335-dot/skills/gb-cad-figure)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with Python and shell command snippets; generated CAD artifacts are PDF, DXF, and optional DWG files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [DWG conversion may download and execute a third-party ODA File Converter AppImage; PDF and DXF workflows can be used without that converter.]

## Skill Version(s):

1.2.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Re-skins an existing BII-format single-stock research note into a BlackRock Investment Institute-style visual system and produces HTML, PDF, and PPTX outputs from one pipeline.

This skill is for research and development only.

## Publisher:

[yjkj999999](https://clawhub.ai/user/yjkj999999)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill when an existing BII-style single-stock briefing needs the same content delivered as branded HTML, PDF, and PPTX files. It applies a visual overlay and QA checks; it does not create new investment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may not have the right to use the BlackRock-style visual identity or may present output as an official BlackRock publication.

Mitigation: Confirm visual identity rights before use and keep the injected statement that the report is an independent analysis piece, not a BlackRock publication.

Risk: Untrusted input documents can carry unsafe or misleading content into generated HTML, PDF, or PPTX outputs.

Mitigation: Run the pipeline only on trusted BII HTML/PDF inputs and review generated files before distribution.

Risk: The visual overlay can change layout enough to add pages or obscure content.

Mitigation: Use the included page measurement and seven-gate QA checks to confirm structure, page count, page size, palette mapping, and visible text preservation.

Risk: Generated PPTX slides are image-backed and not directly text-editable.

Mitigation: Use the HTML source for wording changes and regenerate the PDF/PPTX; rely on speaker notes for searchable and copyable text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yjkj999999/skills/bii-blackrock-note)
- [Publisher profile](https://clawhub.ai/user/yjkj999999)
- [README](artifact/README.md)
- [Sichuan Gold 22-page run case study](artifact/examples/sz001337_case.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands plus generated HTML, PDF, and PPTX files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets A4 landscape output, keeps the PDF page count aligned with the source section count, and packages PPTX slides as page images with speaker notes.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

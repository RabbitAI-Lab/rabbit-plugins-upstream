## Description:

Converts valid PDF files into editable PPT, Word, Excel, image, and PDF outputs, including form filling, table extraction, watermark removal, and foreign-language PDF translation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, office automation users, and agents use this skill to convert valid PDFs into editable Office files or images, extract tables, fill forms, and remove watermarks while checking outputs before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default PDF-to-PPT flow can send PDF text to external translation providers or a configured OpenAI-compatible endpoint.

Mitigation: Use --no-translate or no_translate for confidential documents, and review translation endpoint configuration before processing sensitive PDFs.

Risk: Watermark removal and form filling can alter document integrity or overwrite intended visual content.

Mitigation: Use detect-only or analysis modes first, keep original PDFs, and review generated outputs before replacing originals.

## Reference(s):

- [Usage guide](references/usage-guide.md)
- [ClawHub skill page](https://clawhub.ai/muippt/skills/mu-pdf-converter)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create PPTX, DOCX, XLSX, image, or PDF output files from valid PDF inputs.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter lists 1.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

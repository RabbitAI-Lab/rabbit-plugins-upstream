## Description:

Extracts text from images and PDFs, including scanned PDF pages and PDF tables, and can batch-process folders into Markdown or JSON results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanyi-github](https://clawhub.ai/user/yuanyi-github)

### License/Terms of Use:

MIT-0

## Use Case:

External users and knowledge workers use this agent skill to extract reusable text from image and PDF documents, convert PDF tables to Markdown, and batch-process folders of documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a RedFox API key and sends usage metadata to redfox.hk on each run.

Mitigation: Use it only where outbound access to redfox.hk is acceptable, and use a scoped, revocable API key that is not hardcoded or logged.

Risk: Document-derived files can remain on disk after processing, including rendered OCR page directories, Markdown outputs, and a home-directory version file.

Mitigation: Process confidential documents only in approved workspaces and review or delete generated *_ocr_pages directories, selected Markdown outputs, and ~/.pdf_image_extractor_version after use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yuanyi-github/skills/image-text-extractor)
- [Publisher Profile](https://clawhub.ai/user/yuanyi-github)
- [RedFoxHub Skills](https://redfox.hk/skills)
- [RedFoxHub API Key Settings](https://redfox.hk/settings/api-keys?source=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Extracted text, Markdown reports and tables, JSON result objects, and optional Markdown files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scanned PDF pages may be rendered as PNG images for agent vision review; batch mode can combine results across multiple PDFs and image files.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

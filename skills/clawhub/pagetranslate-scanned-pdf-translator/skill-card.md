## Description:

Translate scanned PDFs, photographed pages, and images of text into page-layout-preserving PDFs or images using PageTranslate OCR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[catorch](https://clawhub.ai/user/catorch)

### License/Terms of Use:

MIT

## Use Case:

People with scanned PDFs or images of text use the skill to translate them and receive a translated PDF or image with the page layout retained.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The source document is uploaded to PageTranslate, and API requests carry the PageTranslate API key.

Mitigation: Upload only the requested document after confirming PageTranslate is trusted with its contents, and keep the API key private.

## Reference(s):

- [PageTranslate scanned PDF translation guide](https://pagetranslate.ai/faq/how-to-translate-scanned-pdf)
- [PageTranslate PDF translator](https://pagetranslate.ai/pdf-translator)
- [PageTranslate MCP project and documentation](https://github.com/Caravaca-Labs/pagetranslate-mcp)
- [ClawHub release page](https://clawhub.ai/catorch/skills/pagetranslate-scanned-pdf-translator)
- [Publisher profile](https://clawhub.ai/user/catorch)

## Skill Output:

**Output Type(s):** [Files, Guidance]

**Output Format:** [Translated PDF or image file; agent instructions are in Markdown with inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The translated file retains the page layout; source-language detection is automatic and the user supplies the target language.]

## Skill Version(s):

0.1.2 (source: frontmatter; release evidence agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

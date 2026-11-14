## Description:

Use this skill whenever the user wants a PDF translated into another language and returned as a PDF with its pages, tables, fonts and images in place: manuals, contracts, reports, papers, brochures, large PDFs. Uploads the file to PageTranslate, shows the exact price first, and downloads the translated PDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[catorch](https://clawhub.ai/user/catorch)

### License/Terms of Use:

MIT-0

## Use Case:

External users can translate manuals, contracts, reports, papers, and other PDFs into another language while retaining the document layout. The skill uploads the selected file to PageTranslate and returns the translated PDF after price confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The requested PDF is sent to PageTranslate for processing.

Mitigation: Upload only the file the user asked to translate, and ensure they are comfortable sending it to PageTranslate.

Risk: The security assessment reports that the quoted price may not be shown before translation starts.

Mitigation: Show the returned price and get the user's approval before starting a paid translation.

## Reference(s):

- [PageTranslate PDF translator](https://pagetranslate.ai/pdf-translator)
- [Translate a large PDF](https://pagetranslate.ai/pdf-translator/translate-large-pdf)
- [How to translate a scanned PDF](https://pagetranslate.ai/faq/how-to-translate-scanned-pdf)
- [Create a PageTranslate API key](https://pagetranslate.ai/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Translated PDF files, Guidance]

**Output Format:** [PDF document with brief Markdown status and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented service limits are 100 MB per file and up to 1,000 pages per PDF; the downloaded file keeps the service-provided filename.]

## Skill Version(s):

0.1.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Use this skill whenever the user wants a whole book translated: an EPUB ebook, a novel or manuscript in DOCX, or a book-length PDF. One upload returns one translated file in the same format, so an EPUB stays an EPUB. Shows the exact price for the full word count before anything is charged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[catorch](https://clawhub.ai/user/catorch)

### License/Terms of Use:

MIT-0

## Use Case:

External readers and authors use this skill to translate book-length EPUB, DOCX, or PDF files into a target language. It provides the price for review before any charge and returns a translated file in the source format.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Book files are transmitted to PageTranslate for translation.

Mitigation: Review PageTranslate's terms and data handling, and upload only the file the user asked to translate.

Risk: The skill requires a PageTranslate API key.

Mitigation: Keep the key in PAGETRANSLATE_API_KEY and never print it or write it to a file.

## Reference(s):

- [PageTranslate book translation](https://pagetranslate.ai/translate-a-book)
- [PageTranslate API key setup](https://pagetranslate.ai/dashboard/api-keys)
- [PageTranslate translation pricing](https://pagetranslate.ai/faq/how-much-does-it-cost-to-translate-a-book)

## Skill Output:

**Output Type(s):** [Files, Guidance]

**Output Format:** [Translated EPUB, DOCX, or PDF file in the source format, with brief pricing and status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The exact price is presented for user approval before a paid translation begins.]

## Skill Version(s):

0.1.2 (source: server-resolved release, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

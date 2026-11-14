## Description:

Translates Word documents and business files into the same kind of file, preserving headings, tables, lists, and images while showing the exact price first.

This skill is ready for commercial/non-commercial use.

## Publisher:

[catorch](https://clawhub.ai/user/catorch)

### License/Terms of Use:

MIT-0

## Use Case:

People who need a business document translated while keeping it editable use this skill to submit a selected file, review the exact price, and download the translated file in the same format.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan had medium confidence and partial inspection, limiting assurance about the skill.

Mitigation: Review the skill and its documented network and API behavior before installing.

Risk: Translating a document sends the selected file to PageTranslate.

Mitigation: Upload only the file the user requested and ensure its contents may be shared with the service.

Risk: The PageTranslate API key is a credential used to access the service.

Mitigation: Keep it in PAGETRANSLATE_API_KEY; never print it or write it to a file.

## Reference(s):

- [PageTranslate document translation software](https://pagetranslate.ai/document-translation-software)
- [PageTranslate DOCX translator](https://pagetranslate.ai/docx-translator)
- [PageTranslate document translation guide](https://pagetranslate.ai/faq/how-to-translate-word-document)
- [PageTranslate API key setup](https://pagetranslate.ai/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [Translated document file in the source format, with brief status and saved-path text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves document formatting where supported; saves the translated file beside the source without overwriting existing files.]

## Skill Version(s):

0.1.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

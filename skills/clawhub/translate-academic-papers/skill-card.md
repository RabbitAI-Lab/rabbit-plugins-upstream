## Description:

Translate complete English academic papers into polished Simplified Chinese while preserving structure, evidence, equations, tables, citation numbering, and the English reference list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fangmingqi2005-create](https://clawhub.ai/user/fangmingqi2005-create)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to translate journal articles, conference papers, preprints, and scholarly PDFs into Simplified Chinese. It is designed to produce both a Chinese full-text DOCX and a paragraph-aligned English-Chinese bilingual DOCX with translated figure text and citation navigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates translated DOCX files by default next to the source paper.

Mitigation: Specify an output directory for sensitive projects and review generated files before sharing.

Risk: Figure processing may use image-editing or model tools on figure crops that could contain confidential or unpublished content.

Mitigation: Confirm provider and data-handling expectations before using image editing, and avoid submitting restricted figures where policy forbids it.

Risk: Incorrect translation, citation linking, or figure label replacement could alter scientific meaning.

Mitigation: Run the documented QA checks, inspect translated figures side by side with originals, and validate citation navigation before relying on the output.

## Reference(s):

- [Figure translation contract](references/figure-translation.md)
- [Two-output contract](references/output-variants.md)
- [Efficient, complete processing](references/performance-budget.md)
- [Final QA checklist](references/qa-checklist.md)
- [Translation standard](references/translation-standard.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Guidance]

**Output Format:** [DOCX files with a concise Markdown final report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces two verified DOCX files by default: a Chinese full-text edition and a paragraph-aligned English-Chinese bilingual edition. The workflow may also create translated figure images and WPS-compatible citation and DOI links.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Translate complete English academic papers into polished Simplified Chinese DOCX files while preserving scholarly structure, equations, citation numbering, English references, figure text, and WPS-compatible citation and DOI links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fangmingqi2005-create](https://clawhub.ai/user/fangmingqi2005-create)

### License/Terms of Use:

MIT

## Use Case:

External users, researchers, translators, and developers use this skill to translate English journal articles, conference papers, preprints, and scholarly PDFs into Simplified Chinese DOCX deliverables, including Chinese-only and paragraph-aligned bilingual editions with translated figures and WPS-compatible citation navigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-supplied papers and may process copyrighted or access-controlled academic content.

Mitigation: Use it only on papers the user is authorized to process, and do not publish source papers or translated copyrighted content without permission.

Risk: The workflow can create DOCX files, caches, manifests, and figure assets beside the source PDF by default.

Mitigation: Choose a specific output directory when work files should not be written next to the source document.

Risk: Verified delivery depends on Image2 figure editing and local document rendering tools such as Word or WPS.

Mitigation: Confirm required image-editing and document-rendering capabilities are available before relying on final DOCX delivery.

Risk: Automated academic translation can alter scientific meaning if claims, numbers, terminology, citations, or figures are not checked.

Mitigation: Run the documented QA checklist and review translated claims, numerical values, terminology, citation links, and figure interiors before use.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/fangmingqi2005-create/skills/translate-academic-papers)
- [Translation standard](references/translation-standard.md)
- [Figure translation contract](references/figure-translation.md)
- [Two-output contract](references/output-variants.md)
- [Final QA checklist](references/qa-checklist.md)
- [Final delivery contract](references/delivery-contract.md)

## Skill Output:

**Output Type(s):** [Files, Text, Markdown, Shell commands, Guidance]

**Output Format:** [DOCX files with Markdown status or final reports and inline shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces two DOCX deliverables by default and may create work caches, Image2-edited figure assets, manifests, and validation artifacts.]

## Skill Version(s):

1.1.2 (source: frontmatter, release evidence, README badge, CITATION.cff)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Translate complete English academic papers into polished Simplified Chinese while preserving structure, evidence, equations, tables, citation numbering, and the English reference list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fangmingqi2005-create](https://clawhub.ai/user/fangmingqi2005-create)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to convert English journal articles, conference papers, preprints, and scholarly PDFs into verified Chinese-only and paragraph-aligned bilingual DOCX deliverables. It is intended for full-paper translation workflows that preserve scientific claims, figures, tables, equations, citations, and reference navigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded papers may include sensitive, unpublished, copyrighted, or licensed content.

Mitigation: Use approved handling channels and lawful access routes, and review outputs before relying on them for publication, legal, or commercial use.

Risk: Translation, citation linking, or figure reconstruction errors could change scientific meaning or visual evidence.

Mitigation: Run the documented QA checks, inspect translated figures at final DOCX size, validate citation navigation, and review the translated output for accuracy before use.

Risk: Document, PDF, image, or translation tools may stall or fail during a long paper workflow.

Mitigation: Use bounded timeouts, preserve validated cache entries, and report a specific blocker or timed-out draft instead of shipping an incomplete result as final.

## Reference(s):

- [Translation standard](references/translation-standard.md)
- [Figure translation contract](references/figure-translation.md)
- [Two-output contract](references/output-variants.md)
- [Performance budget](references/performance-budget.md)
- [Final QA checklist](references/qa-checklist.md)
- [ClawHub skill page](https://clawhub.ai/fangmingqi2005-create/skills/translate-academic-papers)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Guidance]

**Output Format:** [DOCX files with a concise final Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Chinese-only and paragraph-aligned bilingual DOCX files by default, with WPS-compatible citation links and DOI links when validation succeeds.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Searches public scholarly literature across OpenAlex, Europe PMC, bioRxiv, medRxiv, and optional sources, then normalizes and deduplicates records for clinical-trial evidence review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT-0

## Use Case:

Clinical-trial, medical, regulatory, and evidence-review users use this skill to retrieve published literature, preprints, safety-oriented qualitative subsets, citations, and report files for trial-planning background, protocol or CSR introductions, and literature checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some modes may send search terms, filters, DOI or open-access identifiers, and bug-report metadata to the author's Coze endpoints.

Mitigation: Use only non-confidential public-literature queries, avoid sponsor, patient, and unpublished research data, and prefer local API modes with your own keys.

Risk: Persistent query_origin or session_hash values may make repeated use linkable across requests.

Mitigation: Review the privacy implications before installation and avoid use cases where stable request identifiers are unacceptable.

Risk: Exported Excel reports may include local PDF paths.

Mitigation: Review generated workbooks before sharing them outside the working environment.

Risk: The safety-oriented literature subset is qualitative and can be mistaken for pharmacovigilance signal analysis.

Mitigation: Use the safety subset only as published-literature context and validate safety conclusions with appropriate clinical, regulatory, or pharmacovigilance workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-literature)
- [Publisher profile](https://clawhub.ai/user/medstatstar)
- [Project homepage](https://github.com/medstatstar/ct-literature)
- [English README](https://github.com/medstatstar/ct-literature/blob/main/README.md)
- [Chinese README](https://github.com/medstatstar/ct-literature/blob/main/README_zh-CN.md)
- [Search menu reference](references/search_menu.md)
- [Standard operating procedure](references/sop.md)
- [Report template reference](references/report_template.md)
- [OpenAlex key guide](references/openalex_key.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Conversational guidance plus generated HTML, Excel, JSON, Markdown, RIS, BibTeX, CSV, and PDF-path outputs depending on selected options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default deliverables are lit_report.html and lit_report.xlsx; optional exports include per-source JSON, citation files, Obsidian notes, Zotero files, PRISMA assets, and open-access PDF downloads.]

## Skill Version(s):

1.0.0 (source: server release metadata, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

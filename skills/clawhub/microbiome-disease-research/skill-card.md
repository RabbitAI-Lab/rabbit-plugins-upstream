## Description:

This skill helps agents investigate microbiome-disease mechanism evidence chains, search PatSnap patent and paper sources, and generate structured gut microbiome research reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, product analysts, and developers use this skill to collect gut microbiome literature and patent evidence, organize mechanisms across microbiota, metabolites, host pathways, and disease phenotypes, and produce standalone HTML landscape reports with cited source lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Readers may mistake microbiome disease-mechanism summaries for medical advice.

Mitigation: Present outputs as research synthesis only and require qualified review before clinical, diagnostic, treatment, or personal health decisions.

Risk: Report quality depends on PatSnap search coverage, source selection, and correct distinction between patents and papers.

Mitigation: Keep source markers, preserve the full reference list, distinguish patent and academic sources, and verify key claims against cited records before relying on conclusions.

Risk: The skill can support food and nutrition analysis, patent analysis, and AI training-data collection beyond microbiome-disease research.

Mitigation: Confirm the intended scope, rights to use source material, and downstream use constraints before using generated reports or training-data guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/microbiome-disease-research)
- [Search query templates](artifact/references/search_query_templates.md)
- [HTML report template](artifact/references/html_report_template.md)
- [Topic taxonomy](artifact/references/topic_taxonomy.md)
- [Report style CSS](artifact/assets/report_style.css)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Standalone HTML report, Markdown source list, and structured search/reporting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include fixed left navigation, statistics cards, citation markers, and Chinese, English, or bilingual prose.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

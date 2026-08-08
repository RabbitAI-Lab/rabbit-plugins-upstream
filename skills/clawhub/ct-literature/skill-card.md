## Description:

Searches public scholarly literature across OpenAlex, Europe PMC, and optional Semantic Scholar, then normalizes and de-duplicates records into evidence reports with optional safety and CSM filtering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT-0

## Use Case:

External users, clinical-trial practitioners, clinicians, students, developers, and agents use this skill to build a normalized public literature evidence base for a drug, disease, method, or safety topic. It supports background research, protocol or CSR introductions, systematic-review preparation, and qualitative published-safety checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search topics and filters can be sent to public bibliographic APIs.

Mitigation: Use only non-confidential research queries; do not include confidential sponsor, protocol, patient, or proprietary information.

Risk: API keys can be exposed if copied into chat or committed with the skill.

Mitigation: Configure keys through local environment variables, a local .env file, or command-line arguments, and never paste real keys into chat.

Risk: Generated literature reports may be incomplete or affected by API limits, optional-source failures, or ranking assumptions.

Mitigation: Verify important filters, records, and source coverage before relying on the report for clinical, regulatory, or business decisions.

Risk: The safety and CSM subset is qualitative published literature, not quantitative pharmacovigilance signal detection.

Mitigation: Use the subset as background evidence only and corroborate safety decisions with appropriate structured safety analyses and official sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-literature)
- [Project homepage](https://github.com/medstatstar/ct-literature)
- [ct-literature Operating SOP](references/sop.md)
- [Search Confirmation Menu](references/search_menu.md)
- [OpenAlex API Key Guide](references/openalex_key.md)
- [Cross-Database Literature Search](references/multi-db-search.md)
- [Report Template](references/report_template.md)
- [Capability Units](references/units.md)
- [Language Policy](references/language_policy.md)
- [OpenAlex API settings](https://openalex.org/settings/api)

## Skill Output:

**Output Type(s):** [text, markdown, json, code, shell commands, configuration, guidance]

**Output Format:** [Chat guidance with runnable Python commands, plus generated JSON evidence files, Markdown reports, and optional XLSX or HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes report files to the current working directory or selected output directory; network retrieval runs only after explicit execution confirmation.]

## Skill Version(s):

0.5.2 (source: server release metadata, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

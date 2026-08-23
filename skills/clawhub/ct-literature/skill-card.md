## Description:

Searches public scholarly literature, merges and de-duplicates results across supported bibliographic sources, verifies citation identifiers, and produces evidence reports for clinical-trial background research and qualitative safety-literature checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

External users, clinical research teams, and developers use this skill to build a de-duplicated public literature evidence base, generate reports, and check published safety literature for trial planning or background research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search topics and filters may be sent to public bibliographic APIs.

Mitigation: Use only public, non-confidential research terms; avoid sponsor, patient, proprietary, or unpublished study information.

Risk: Optional bug reports can transmit a user-reviewed description to an external endpoint.

Mitigation: Review the sanitized bug-report preview before consenting, and use the local fallback when cloud reporting is not appropriate.

Risk: API keys may be needed for higher quotas or optional sources.

Mitigation: Configure keys through local environment variables or local .env files, keep them out of repositories, and rotate them if exposure is suspected.

Risk: Published safety-literature output is qualitative and can be mistaken for quantitative pharmacovigilance evidence.

Mitigation: Use the safety subset as background corroboration only, and validate against appropriate quantitative safety systems and official sources before regulated use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-literature)
- [Project homepage](https://github.com/medstatstar/ct-literature)
- [ct-literature Operating SOP](artifact/references/sop.md)
- [Search Confirmation Menu](artifact/references/search_menu.md)
- [OpenAlex API Key Guide](artifact/references/openalex_key.md)
- [Cross-Database Literature Search](artifact/references/multi-db-search.md)
- [PROSPERO Access Guide](artifact/docs/prospero_access_guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, Excel workbook, HTML report, citation exports]

**Output Format:** [Markdown guidance with shell commands; generated artifacts may include JSON, HTML, XLSX, BibTeX, RIS, CSV, SVG, and Markdown files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs local normalization and report generation; enabled public bibliographic sources may require network access and optional API keys.]

## Skill Version(s):

0.9.0 (source: frontmatter, changelog, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

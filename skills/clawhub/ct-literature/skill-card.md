## Description:

Searches public scholarly sources for clinical-trial literature, deduplicates results, and produces traceable evidence reports for review, safety, and protocol background work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT-0

## Use Case:

External users, reviewers, and clinical-development teams use this skill to build a public literature evidence base for compounds, indications, methods, and published safety checks. It supports background research for trial planning, protocol or CSR introductions, and qualitative cumulative safety monitoring literature review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search topics and filters may be sent to public scholarly APIs.

Mitigation: Do not enter confidential sponsor, patient, or unpublished project information as search terms; use dedicated low-privilege API keys when credentials are configured.

Risk: Provider availability, rate limits, and credential requirements can affect coverage.

Mitigation: Review source-specific notes before use and treat skipped, rate-limited, or key-gated sources as coverage limits in the generated report.

Risk: Published safety literature is qualitative background and may not represent structured safety signal strength.

Mitigation: Use safety outputs as corroborating literature evidence only, and have qualified reviewers assess clinical or regulatory conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-literature)
- [Project homepage](https://github.com/medstatstar/ct-literature)
- [Standard operating procedure](references/sop.md)
- [Multi-database search guide](references/multi-db-search.md)
- [OpenAlex key guide](references/openalex_key.md)
- [Citation styles](references/citation_styles.md)
- [PROSPERO access guide](docs/prospero_access_guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON evidence files, Excel workbooks, HTML reports, BibTeX/RIS exports, and optional Obsidian/Zotero files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May make opt-in read-only requests to public bibliographic APIs and writes report artifacts to the selected output directory.]

## Skill Version(s):

0.6.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

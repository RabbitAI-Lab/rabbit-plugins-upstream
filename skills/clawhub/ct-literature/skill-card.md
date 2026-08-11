## Description:

Search public scholarly literature and normalize it into a de-duplicated evidence base using OpenAlex as the primary source, with optional Europe PMC and Semantic Scholar enrichment, review-type and year filters, and a safety/CSM bias mode for published adverse-event and pharmacovigilance literature.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT-0

## Use Case:

Clinical-trial practitioners, clinicians, nurses, medical students, and developers use this skill to retrieve published literature about a drug, disease, or method and generate a normalized evidence base for trial planning, protocol or CSR background, and qualitative published-safety checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Literature search topics and filters are sent to public bibliographic APIs when retrieval is executed.

Mitigation: Use only public or non-confidential search topics and enable only the sources needed for the task.

Risk: API keys can be mishandled if pasted into chat, committed, or stored only with weak obfuscation.

Mitigation: Use environment variables or a real secret manager, never paste keys into chat, and verify that no .env file is packaged or shared.

Risk: Published safety literature is qualitative and can be incomplete or misleading if treated as a regulatory safety signal.

Mitigation: Use the safety/CSM subset as background evidence only and validate important conclusions against official sources and structured safety analyses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-literature)
- [Publisher profile](https://clawhub.ai/user/medstatstar)
- [Project homepage](https://github.com/medstatstar/ct-literature)
- [Operating SOP](references/sop.md)
- [OpenAlex API key guide](references/openalex_key.md)
- [Cross-database literature search methodology](references/multi-db-search.md)
- [Citation styles](references/citation_styles.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown reports, JSON data files, Excel workbooks, HTML reports, BibTeX/RIS citation exports, and conversational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs in preview mode until explicit execution; optional network retrieval uses public bibliographic APIs and writes report artifacts to the selected output directory.]

## Skill Version(s):

0.5.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

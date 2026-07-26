## Description: <br>
Journal Meta resolves a DOI, PMID, arXiv ID, OpenAlex ID, or paper title into a structured paper metadata record with authors, publication details, journal abbreviation, impact-factor information, identifiers, citations, and abstract. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[agents365-ai](https://clawhub.ai/user/agents365-ai) <br>

### License/Terms of Use: <br>
CC BY-NC 4.0 <br>


## Use Case: <br>
Developers, researchers, and academic-writing agents use this skill to retrieve paper metadata from a DOI, PMID, arXiv ID, OpenAlex ID, or title and present citation-relevant fields without guessing. It is useful for author, venue, impact-factor, citation, and abstract lookups where source attribution and field provenance matter. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paper identifiers or titles may be sent to OpenAlex, Crossref, AbbrevISO, or related metadata services during lookup and enrichment. <br>
Mitigation: Do not use private, unpublished, or sensitive titles unless outbound lookup is acceptable; prefer DOI or PMID when possible. <br>
Risk: The skill searches local skill directories and may execute discovered journal helper scripts for abbreviation and impact-factor enrichment. <br>
Mitigation: Use only trusted sibling skills or explicit trusted paths for JOURNAL_ABBREV_CLI and JOURNAL_IF_CLI; use --no-abbrev and --no-if when helper execution is not acceptable. <br>
Risk: Title search uses a single top OpenAlex match and may return a preprint, duplicate, or wrong record for ambiguous titles. <br>
Mitigation: Prefer DOI, PMID, arXiv ID, or OpenAlex ID and verify returned DOI, year, and venue before using the metadata in citations. <br>
Risk: Corresponding-author and impact-factor fields depend on upstream metadata and may be missing or approximate. <br>
Mitigation: Report the field source from meta.sources, treat empty corresponding-author lists as not marked in metadata, and distinguish curated JCR values from OpenAlex approximations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agents365-ai/skills/journal-meta) <br>
- [Metadata homepage](https://github.com/Agents365-ai/journal-meta) <br>
- [journal-abbrev sibling skill](https://github.com/Agents365-ai/journal-abbrev) <br>
- [journal-if sibling skill](https://github.com/Agents365-ai/journal-if) <br>
- [OpenAlex](https://openalex.org) <br>
- [Crossref](https://www.crossref.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON or human-readable CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI emits a stable JSON envelope when captured or piped and a human key-value view on a TTY.] <br>

## Skill Version(s): <br>
0.1.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

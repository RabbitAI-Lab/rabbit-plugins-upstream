## Description:

Find genuine research gaps in a topic and output a ranked, citation-backed gap report with a candidate research question per gap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and analysts use this skill to scan a broad topic or understudied angle, classify candidate research gaps, validate cited evidence, and produce a ranked Markdown report with research-question candidates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and optional guided-browser activity may be sent to third-party scholarly services.

Mitigation: Use non-sensitive queries unless the relevant service terms and privacy posture have been reviewed.

Risk: API response caches and generated project files are stored in the selected project directory.

Mitigation: Choose an appropriate project directory and review or remove cached responses before sharing the workspace.

Risk: AI-assisted research-gap summaries can be wrong or can overstate an absence in the literature.

Mitigation: Use the skill's DOI/Crossref validation, confidence labels, and AHRQ cross-check guidance before relying on a gap in proposals or reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/research-gap-finder)
- [Resource catalog](artifact/resources.md)
- [AHRQ framework for determining research gaps](https://www.ncbi.nlm.nih.gov/books/NBK126702/)
- [OpenAlex API](https://api.openalex.org)
- [Semantic Scholar API](https://api.semanticscholar.org)
- [Crossref API](https://api.crossref.org)
- [Europe PMC API](https://www.ebi.ac.uk/europepmc/webservices/rest)
- [PubMed E-utilities](https://eutils.ncbi.nlm.nih.gov)
- [arXiv API](https://export.arxiv.org/api/query)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown report plus JSON/CSV project files and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include gap statements, gap type, source evidence, importance scores, confidence labels, and candidate research questions.]

## Skill Version(s):

2.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

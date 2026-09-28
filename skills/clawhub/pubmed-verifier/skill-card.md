## Description:

Checks PubMed and DOI citations against publication records to identify incorrect, mismatched, or retracted references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and developers use this skill to audit PMID and DOI citations in manuscripts, AI-generated writing, and evidence libraries before publication or reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected citation identifiers and metadata are sent to external academic services.

Mitigation: Review the selected files before scanning and share PMIDs, DOIs, and citation metadata only when appropriate.

Risk: Citation information may remain in a local cache or reports.

Mitigation: Use --no-cache for sensitive reviews and choose report and export paths deliberately.

Risk: An optional API key or contact email accompanies requests when supplied.

Mitigation: Set NCBI_API_KEY or PUBMED_VERIFIER_MAILTO only when you intend to provide those details to the corresponding API.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [PubMed, Europe PMC, and Crossref API examples](references/api_examples.md)

## Skill Output:

**Output Type(s):** [Text, HTML, JSON, CSV, BibTeX]

**Output Format:** [Terminal summary or HTML/JSON report, with optional JSON audit, CSV table, or BibTeX bibliography]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts, retraction flags, and optional change comparisons]

## Skill Version(s):

2.9.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

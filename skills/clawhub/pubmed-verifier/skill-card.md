## Description:

Checks PubMed, DOI, and arXiv citations against academic records, identifying missing references, metadata mismatches, and retractions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and developers use this skill to audit citations in manuscripts, bibliographies, and project files before publication or release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers and titles, plus optional contact email or API-key-attributed requests, are sent to academic registries.

Mitigation: Use only with citation data you are comfortable sending to PubMed, Europe PMC, Crossref, and arXiv; provide contact details or an API key only when appropriate.

Risk: Local reports, exports, and cached citation results may expose sensitive project details on shared machines.

Mitigation: Review report and export destinations, and use --no-cache on shared machines or sensitive projects.

Risk: Cached retraction status can be stale, and an existence check alone does not verify that a citation matches the claimed paper.

Mitigation: Use claimed titles for metadata cross-checks, review mismatches manually, and run final checks with --no-cache.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Academic registry API examples](references/api_examples.md)
- [NCBI API key guidance](https://ncbiinsights.ncbi.nlm.nih.gov/api-keys/)

## Skill Output:

**Output Type(s):** [Text, HTML reports, JSON reports, CSV reports, BibTeX bibliographies]

**Output Format:** [Terminal summary or locally saved HTML, JSON, CSV, and BibTeX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts; optional audit trail and retraction flags.]

## Skill Version(s):

3.6.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

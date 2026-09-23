## Description:

Batch-verifies PMID and DOI citations against PubMed, Europe PMC, and Crossref to detect invalid, mismatched, retracted, or unverifiable references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, evidence-based medicine teams, and developers use this skill to audit PMID and DOI citations in manuscripts, knowledge bases, teaching material, and AI-generated references before publication or release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PMIDs, DOIs, optional search terms, and optional contact email or API key may be sent to public metadata services.

Mitigation: Use only data that may be shared with PubMed, Europe PMC, and Crossref, and configure institutional contact or API credentials according to local policy.

Risk: Directory scans can read files outside the intended citation audit scope if the source path is too broad.

Mitigation: Point --source only at folders or files intended for citation verification.

## Reference(s):

- [PubMed E-utilities API Quick Reference](references/api_examples.md)
- [NCBI E-utilities API](https://eutils.ncbi.nlm.nih.gov)
- [Europe PMC REST API](https://www.ebi.ac.uk/europepmc/webservices/rest/search)
- [Crossref Works API](https://api.crossref.org/works)

## Skill Output:

**Output Type(s):** [Text, JSON, HTML, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; verifier reports as text, JSON, or HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit codes distinguish clean results, citation problems, and incomplete verification caused by unreachable data sources.]

## Skill Version(s):

2.4.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

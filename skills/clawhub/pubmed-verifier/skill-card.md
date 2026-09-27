## Description:

Verifies PMID and DOI citations against academic registries, flags mismatched or retracted references, and produces reviewable citation reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and evidence teams use this skill to check references in manuscripts, knowledge bases, and AI-generated content before relying on or publishing them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers, titles, and an optional contact email are sent to external academic registries.

Mitigation: Review what you submit and omit --mailto if you do not want your email in API requests or local audit output.

Risk: Directory scans and local reports or cache may expose sensitive reference material.

Mitigation: Scan only intended directories, protect report files, and use --no-cache for sensitive reviews.

Risk: Incomplete network checks or heuristic citation matching can leave references unverified or misclassified.

Mitigation: Review flagged and unknown results against the source records before relying on them.

## Reference(s):

- [PubMed Verifier release on ClawHub](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [PubMed, Europe PMC, and Crossref API examples](artifact/references/api_examples.md)

## Skill Output:

**Output Type(s):** [Text, HTML, JSON, BibTeX, Guidance]

**Output Format:** [Terminal summary or local HTML, JSON, and BibTeX reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Citation verdicts, supporting metadata, and optional audit comparisons]

## Skill Version(s):

2.8.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

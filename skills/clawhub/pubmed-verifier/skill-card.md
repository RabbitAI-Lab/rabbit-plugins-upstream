## Description:

Checks PubMed citations against registered article metadata to identify incorrect, mismatched, or retracted references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, editors, and developers use this skill to audit individual or batch PMID citations against publication records and review discrepancies before relying on cited evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning a supplied path may expose sensitive citations in local files and persist metadata in a local cache.

Mitigation: Limit scans to intended files and use --no-cache when local retention is inappropriate.

Risk: Citation identifiers and optional email or API-key parameters may be sent to academic registry APIs.

Mitigation: Review what will be queried and use optional credentials only where sharing them with the selected registry is acceptable.

## Reference(s):

- [PubMed Verifier release](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Academic registry API examples](references/api_examples.md)

## Skill Output:

**Output Type(s):** [Text, JSON, HTML]

**Output Format:** [Text, JSON, or HTML citation reports; optional JSON audit trail]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts, supporting comparisons, and optional audit evidence.]

## Skill Version(s):

2.6.0 (source: ClawHub release, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

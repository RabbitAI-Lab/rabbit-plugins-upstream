## Description:

Batch-verifies PMID and DOI citations against PubMed, Europe PMC, and Crossref, producing five-state citation verdicts and HTML, JSON, or text reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, evidence-based medicine teams, and developers use this skill to audit PubMed citations, detect mismatched or invalid PMIDs, cross-check DOI metadata, and generate reviewable citation-verification reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation text, PMIDs, DOIs, contact email, or an NCBI API key may be sent to NCBI/PubMed, Europe PMC, or Crossref during verification.

Mitigation: Run the verifier only on material whose disclosure to those scholarly APIs is acceptable, and provide --mailto or NCBI_API_KEY only when that contact or credential use is approved.

Risk: Citation metadata is cached locally under ~/.cache/pubmed-verifier.

Mitigation: Use --no-cache for sensitive audits or clear the local cache after use.

Risk: Network or source outages are reported as unknown rather than invalid, so unresolved citations can remain unverified.

Mitigation: Review unknown results before relying on a report, retry when sources are reachable, or choose an alternate metadata source with --meta-source when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [PubMed E-utilities API Quick Reference](references/api_examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; the verifier can produce HTML, JSON, or terminal text reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include correct, mismatch, partial, invalid, and unknown verdicts; optional DOI verification and PMID suggestions may add external API calls.]

## Skill Version(s):

2.2.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

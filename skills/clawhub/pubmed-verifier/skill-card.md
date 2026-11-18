## Description:

Reference checker for AI-fabricated citations: batch-verify PMIDs against PubMed and catch the hallucination existence checks miss — a REAL PMID pointing to a DIFFERENT paper. Five-state citation verification (correct / mismatch / partial / invalid / unknown), citation-context parsing, Crossref DOI cross-check, retraction detection (capped at partial), correct-PMID suggestion, arXiv ID verification, plain-text reference list parsing, formatted reference lists (GB/T 7714 / Vancouver / APA / AMA / Harvard / Chicago), OpenAlex DOI fallback for non-Crossref registries, Chinese-reference title search, CSV/JSON claims, HTML/JSON/text reports. Four data sources: NCBI, Europe PMC fallback, Crossref, OpenAlex. Network failures are honestly reported as unverified, never as "not found". Zero dependencies, runs fully local.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, evidence-based medicine teams, and developers use the skill to verify PMID, DOI, and arXiv references against scholarly registries, check whether identifiers match the cited work, and prepare verified reference lists and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation lists or source documents may contain sensitive material, and verification can send citation data to external scholarly registries.

Mitigation: Review inputs before running network checks; use offline checks when external transmission is unsuitable.

Risk: The security review noted that the tool's permission scope was unclear.

Mitigation: Review requested file and network access before installation, and allow only the access needed for citation inputs and registry checks.

Risk: Registry checks do not establish the scientific validity of a cited claim, and some results may remain partial or unknown.

Mitigation: Review partial, unknown, mismatched, and retraction-related results against the source publication before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Project homepage (package metadata)](https://github.com/docsor1212/pubmed-verifier)
- [Usage guide](artifact/references/usage_guide.md)
- [API examples](artifact/references/api_examples.md)
- [Operations playbook](artifact/references/operations.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, HTML, Text, Formatted references]

**Output Format:** [Terminal summaries, HTML reports, JSON evidence and audit files, BibTeX/RIS/CSL JSON exports, and formatted reference lists (GB/T 7714, Vancouver, APA, AMA, Harvard, or Chicago).]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports distinguish correct, mismatched, partial, invalid, and unknown citations; network failures are reported as unverified.]

## Skill Version(s):

7.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

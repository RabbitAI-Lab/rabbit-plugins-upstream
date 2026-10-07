## Description:

Verifies PMID, DOI, and arXiv citations against scholarly registries, comparing claimed metadata and flagging mismatches, retractions, and unverified entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and evidence teams use this skill to audit reference lists and AI-generated citations before publication, checking whether cited works exist and match their claimed details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers and related metadata may be sent to external scholarly registries, including for confidential or pre-publication work.

Mitigation: Use explicit file paths and run only when comfortable sharing that metadata with PubMed/NCBI, Europe PMC, Crossref, and arXiv.

Risk: Locally cached results may not reflect recent publication changes in a final audit.

Mitigation: Use --no-cache for final or sensitive verification runs.

Risk: Optional API key or contact details are used in registry requests when supplied.

Mitigation: Set NCBI_API_KEY or PUBMED_VERIFIER_MAILTO only when you intend those values to be used for registry requests.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Publisher-listed project homepage](https://github.com/docsor1212/pubmed-verifier)
- [Academic registry API examples](artifact/references/api_examples.md)

## Skill Output:

**Output Type(s):** [Text, HTML, JSON, CSV, Bibliography files]

**Output Format:** [Terminal text, HTML, JSON, CSV, BibTeX, or RIS]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts, retraction flags, and optional audit trail; unavailable registries yield unverified results.]

## Skill Version(s):

3.8.0 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

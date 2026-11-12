## Description:

Verifies PMIDs, DOIs, arXiv IDs, and reference lists against scholarly registries, then reports citation matches, mismatches, retractions, and formatted references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and evidence teams use it to check whether cited PMIDs, DOIs, arXiv records, and reference metadata point to the claimed papers, then review or format references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation parsing and metadata comparison can be inaccurate or incomplete, and the security scan reports citation-check accuracy concerns.

Mitigation: Supply expected titles and authors when possible, and manually review partial, unknown, or consequential results against the cited records.

Risk: Verification may send citation identifiers, titles, or research search terms to external scholarly services.

Mitigation: Do not submit confidential citation details or search terms unless their disclosure to those services is acceptable.

## Reference(s):

- [PubMed Verifier on ClawHub](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Project homepage](https://github.com/docsor1212/pubmed-verifier)
- [Usage guide](artifact/references/usage_guide.md)
- [Command-line flags](artifact/references/flags.md)
- [Operations guide](artifact/references/operations.md)
- [Python API reference](artifact/references/python_api.md)

## Skill Output:

**Output Type(s):** [Text, HTML, JSON, Formatted references]

**Output Format:** [Text, HTML, JSON, BibTeX, RIS, CSL JSON, and formatted reference lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Citation-level verdicts and registry metadata; network failures are reported as unverified.]

## Skill Version(s):

6.9.0 (source: artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

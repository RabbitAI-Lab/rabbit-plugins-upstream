## Description:

Checks cited PMIDs, DOIs, and arXiv IDs against academic registries and flags mismatched or unverified references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and developers use this skill to audit reference lists and AI-generated citations before publication or reuse. It compares citation claims with registry records and provides reports for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers and claimed metadata from selected documents are sent to academic registries.

Mitigation: Use only documents whose citation data may be shared with PubMed/NCBI, Europe PMC, Crossref, and arXiv.

Risk: Directory scans, local cache data, and report exports may expose sensitive reference material.

Mitigation: Select narrow source and export paths, and use --no-cache for one-off sensitive checks.

Risk: Registry outages or heuristic citation parsing can leave references unverified or mismatched.

Mitigation: Review unknown or disputed results manually; supply structured claims when precision matters.

## Reference(s):

- [PubMed Verifier release](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [PubMed API examples](artifact/references/api_examples.md)
- [Python integration reference](artifact/references/python_api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance and commands; verifier reports in text, HTML, JSON, or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can export audited bibliographies and citation evidence for review.]

## Skill Version(s):

3.9.0 (source: SKILL.md frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

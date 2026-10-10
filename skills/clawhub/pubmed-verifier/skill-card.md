## Description:

Checks whether cited PMIDs, DOIs, and arXiv IDs resolve to the papers a reference claims, and reports citation mismatches and uncertain results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and evidence-based medicine teams use this skill to audit reference lists and AI-generated citations before publication, including checks for real identifiers that point to the wrong paper.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers, title queries, and optional contact email or API key may be sent to academic registry services.

Mitigation: Review the data and credentials before running networked checks; do not use this as a private offline verifier.

Risk: Broad scans may read unrelated private drafts, and cached citation data may persist locally.

Mitigation: Use specific input paths, avoid unrelated private files, and consider --no-cache for sensitive work.

## Reference(s):

- [PubMed Verifier release](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [API examples](references/api_examples.md)
- [Python API guide](references/python_api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [Citation-verification guidance and text, HTML, JSON, or CSV reports; optional formatted references and audit exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports distinguish matched, mismatched, partial, invalid, and unknown citations.]

## Skill Version(s):

4.1.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

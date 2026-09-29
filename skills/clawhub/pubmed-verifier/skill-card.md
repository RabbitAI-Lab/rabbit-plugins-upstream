## Description:

Verifies PMID, DOI, and arXiv citations against academic registries and flags mismatched references, missing records, and retractions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to audit citations in manuscripts, AI-generated writing, and medical knowledge bases before publication or reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers, titles, and optional contact email or API-key metadata may be sent to external academic registries.

Mitigation: Review sensitive inputs and optional credentials before running verification.

Risk: The local cache can retain citation data from confidential projects.

Mitigation: Run with --no-cache when handling confidential material.

Risk: Report and export files can overwrite existing files at selected paths.

Mitigation: Check output paths before exporting reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Academic registry API examples](references/api_examples.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Text, HTML, JSON, CSV, or BibTeX citation reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts; unreachable sources and insufficient claimed metadata yield unknown rather than invalid.]

## Skill Version(s):

3.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

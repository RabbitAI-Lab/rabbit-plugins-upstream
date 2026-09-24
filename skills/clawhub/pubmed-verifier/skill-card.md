## Description:

Batch-verifies PMID citations against PubMed metadata and related academic registries to catch invalid, mismatched, partial, retracted, or unverifiable references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, evidence-based medicine teams, and developers use this skill to audit PMID and DOI citations in manuscripts, knowledge bases, teaching materials, and AI-generated content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can scan user-selected files or directories and send PMID, DOI, title, optional email, and optional API key data to NCBI, Europe PMC, and Crossref.

Mitigation: Use narrow source paths, avoid private or unpublished material unless registry lookup is acceptable, and provide optional credentials only when needed.

Risk: Local caching may retain citation lookup results on the user's machine.

Mitigation: Use the documented no-cache mode for sensitive work and review generated report paths before sharing outputs.

Risk: Network failures or registry outages can prevent a definitive citation verdict.

Mitigation: Treat unknown or unverifiable results as requiring retry or human review rather than as invalid citations.

## Reference(s):

- [PubMed E-utilities API Quick Reference](references/api_examples.md)
- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/pubmed-verifier)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; verifier reports can be text, JSON, or HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use local SQLite caching and optional NCBI API key or contact email for registry requests.]

## Skill Version(s):

2.5.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Checks PubMed, DOI, and arXiv citations against academic records to identify mismatched, invalid, retracted, or unverified references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, editors, and developers use this skill to audit reference lists and AI-generated citations before publication or reuse, comparing claimed details with academic records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers and claimed metadata are sent to external academic registries.

Mitigation: For unpublished or sensitive manuscripts, restrict the source paths and review what citation details may be shared before running verification.

Risk: Local caches and exported reports can retain citation details in chosen locations.

Mitigation: Use --no-cache when appropriate and choose report and export locations with suitable access controls.

## Reference(s):

- [ClawHub pubmed-verifier release](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Academic registry API examples](references/api_examples.md)
- [NCBI API key guidance](https://ncbiinsights.ncbi.nlm.nih.gov/api-keys/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text, JSON, or HTML citation reports; optional CSV and BibTeX exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state verification verdicts; unreachable sources are reported as unverified rather than invalid.]

## Skill Version(s):

3.5.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Checks whether cited PMIDs, DOIs, and arXiv identifiers exist and match the claimed publications, flagging mismatches and retractions for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and developers use this skill to audit citations in manuscripts, AI-generated content, and evidence libraries before publication or reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers and some claimed metadata are sent to external academic registries.

Mitigation: Run only on citations whose identifiers and metadata are appropriate to share with PubMed/NCBI, Europe PMC, Crossref, and arXiv.

Risk: Broad source directories may include private documents, and cached results may be stale.

Mitigation: Select explicit files or narrow directories and use --no-cache for final fresh checks.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Academic registry API examples](references/api_examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown guidance, Shell commands, Files]

**Output Format:** [Terminal text or HTML, JSON, CSV, and BibTeX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts, retraction flags, and an audit trail when requested.]

## Skill Version(s):

3.3.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

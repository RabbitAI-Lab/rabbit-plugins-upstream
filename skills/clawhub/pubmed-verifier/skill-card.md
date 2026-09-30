## Description:

Checks PubMed, DOI, and arXiv citations against source records to flag invalid, mismatched, or retracted references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and evidence teams use this skill to audit citation identifiers and claimed article details in manuscripts, reference lists, and knowledge bases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents may contain confidential citations or titles sent to external academic services during verification.

Mitigation: Use explicit source paths and obtain approval for external lookups before checking confidential drafts.

Risk: Reports and cached citation results are written locally; cached results may become stale.

Mitigation: Choose report paths deliberately and use --no-cache for a fresh final check or to avoid a local verification cache.

Risk: An existing identifier alone does not establish that a citation supports the claimed paper.

Mitigation: Supply claimed titles for metadata matching and review uncertain or partial verdicts before relying on a citation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Academic API examples](references/api_examples.md)

## Skill Output:

**Output Type(s):** [Text, Files, Guidance]

**Output Format:** [Terminal text or HTML, JSON, CSV, and BibTeX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts; optional audit trails and bibliography exports.]

## Skill Version(s):

3.1.0 (source: SKILL.md frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Checks PMID, DOI, and arXiv citations against scholarly records to identify mismatched, missing, or retracted references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and developers use this skill to audit citations in manuscripts, AI-generated material, and reference libraries before publication or reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers and optional contact or API-key parameters are sent to scholarly registries.

Mitigation: Use only when those disclosures are acceptable; avoid including sensitive information in citation inputs or contact parameters.

Risk: Scanning unrelated private files or retaining citation metadata in the local cache.

Mitigation: Pass explicit source paths and use --no-cache when local retention is not desired.

Risk: Heuristic citation matching and cached retraction status may be incomplete or stale.

Mitigation: Review disputed citations against the source records and run final checks with --no-cache.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [API examples](references/api_examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [Citation-verification guidance and commands; optional text, HTML, JSON, CSV, and BibTeX reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verdicts include correct, mismatch, partial, invalid, and unknown; optional audit exports and local cache.]

## Skill Version(s):

3.4.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

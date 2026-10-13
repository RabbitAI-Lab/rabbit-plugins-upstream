## Description:

Checks whether cited PMIDs, DOIs, and arXiv IDs resolve to the claimed publications, highlighting mismatches and uncertain results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to audit reference lists and AI-generated citations before publication or reuse, compare citation claims with registry records, and prepare verified bibliographies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers, searched titles, and optional contact or API-key parameters are sent to academic registries.

Mitigation: Use only when those lookups are acceptable; avoid supplying sensitive identifiers or optional credentials unnecessarily.

Risk: Scanning broad directories can expose unrelated local citations, and verification results may remain in a local cache.

Mitigation: Specify only intended input paths and use --no-cache for sensitive or final one-off checks.

Risk: Heuristic citation parsing or cached retraction status can make a report incomplete or stale.

Mitigation: Review mismatches against source records, provide structured claims when possible, and use --no-cache for final checks.

## Reference(s):

- [PubMed Verifier on ClawHub](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Academic registry API examples](references/api_examples.md)
- [Python API guidance](references/python_api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text, JSON, HTML]

**Output Format:** [Markdown instructions and shell commands; verifier reports in text, JSON, or HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce formatted reference lists; uncertain lookups remain unverified rather than being labeled invalid.]

## Skill Version(s):

4.3.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

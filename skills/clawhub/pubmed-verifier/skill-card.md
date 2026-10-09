## Description:

Checks cited PMIDs, DOIs, and arXiv IDs against academic registries, compares publication details, and produces citation audit reports or formatted reference lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to audit reference lists and AI-generated citations before publication, identify mismatched or unverified records, and prepare formatted references for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers, titles, and optional contact email or API-key parameters are sent to academic registry services during verification.

Mitigation: Use only with material approved for external lookup; use a role email for --mailto and choose formatting without verification when lookups are not intended.

Risk: Cached lookup results may persist on the local machine or be stale for a final manuscript check.

Mitigation: Use --no-cache for sensitive manuscripts and final pre-submission verification.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [API examples](artifact/references/api_examples.md)
- [Python API reference](artifact/references/python_api.md)

## Skill Output:

**Output Type(s):** [Text, Files, Citation verification guidance]

**Output Format:** [Text, HTML, JSON, CSV, BibTeX, RIS, or formatted reference lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts; unresolved and partial matches require human review.]

## Skill Version(s):

4.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

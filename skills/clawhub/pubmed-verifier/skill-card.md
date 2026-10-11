## Description:

Checks whether cited PMIDs, DOIs, and arXiv IDs resolve to the claimed publications, flags mismatches and retractions, and helps format verified references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and evidence teams use this skill to audit manuscript bibliographies and AI-generated citations, compare claimed publication details with registry records, and prepare reference lists for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers and some titles may be sent to public academic registries when checking confidential drafts.

Mitigation: Review draft confidentiality before running online verification; share only the citations needed for the audit.

Risk: Lookup results are retained in a local cache by default.

Mitigation: Use --no-cache when local retention is inappropriate or a fresh lookup is needed.

Risk: A broad --source path may include unrelated project files in a citation scan.

Mitigation: Point --source to the smallest relevant directory or file.

## Reference(s):

- [PubMed Verifier on ClawHub](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Academic registry API examples](artifact/references/api_examples.md)
- [Python API reference](artifact/references/python_api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [Plain text or Markdown guidance, with optional HTML, JSON, CSV, BibTeX, RIS, or formatted-reference files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts; network failures remain unverified rather than being marked invalid.]

## Skill Version(s):

4.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

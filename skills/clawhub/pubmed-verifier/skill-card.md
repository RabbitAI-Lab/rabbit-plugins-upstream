## Description:

Checks whether cited PMIDs, DOIs, and arXiv IDs resolve to the papers and metadata claimed, and reports discrepancies for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to audit bibliographies and AI-generated citations before publication, comparing claimed references against academic registry records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers and some claimed metadata are sent to academic registry APIs.

Mitigation: For sensitive or unpublished manuscripts, provide explicit input files and avoid broad directory scans.

Risk: Local cached registry data may be stale or inappropriate for private checks.

Mitigation: Use --no-cache for private or final pre-submission checks.

Risk: Heuristic citation parsing and registry mismatches can produce uncertain results.

Mitigation: Provide structured claims with titles and review flagged or unknown citations against the source records.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Publisher-listed project homepage](https://github.com/docsor1212/pubmed-verifier)
- [Academic registry API examples](references/api_examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown guidance with commands; optional HTML, JSON, CSV, BibTeX, or RIS reports and exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts (correct, mismatch, partial, invalid, unknown); optional local audit files.]

## Skill Version(s):

3.7.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

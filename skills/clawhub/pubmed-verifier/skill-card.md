## Description:

Checks scholarly citations against publication registries to identify incorrect or mismatched references, retractions, and unverifiable records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, editors, and developers use this skill to audit manuscript, medical-content, and AI-generated citations against publication metadata and produce reviewable verification reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External registry lookups disclose citation identifiers and titles, and may include an optional contact email or API key.

Mitigation: Avoid confidential drafts unless those disclosures are acceptable; provide contact details or credentials only when needed.

Risk: Locally cached registry results can persist or become stale.

Mitigation: Use --no-cache for final verification or privacy-sensitive runs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Usage guide](artifact/references/usage_guide.md)
- [API examples](artifact/references/api_examples.md)
- [Python API](artifact/references/python_api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [Text or Markdown guidance; optional HTML, JSON, CSV, BibTeX, RIS, and formatted reference files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts; unreachable registries yield unknown results rather than invalid citations.]

## Skill Version(s):

5.1.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

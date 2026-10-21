## Description:

Verifies citation identifiers against scholarly sources, checks whether cited identifiers match the claimed papers, and produces citation reports and formatted references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to audit references in AI-generated text, manuscripts, and bibliography files, including checks that an identifier points to the claimed paper.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shareable diagnostic output may expose proxy credentials.

Mitigation: Redact proxy credentials from --doctor output before sharing it.

Risk: Some verification results can overstate what was actually checked.

Mitigation: Supply expected titles and authors before relying on verified exports, and manually recheck invalid DOIs, especially after network failures.

Risk: Citation identifiers, titles, and search terms may be sent to scholarly services during verification.

Mitigation: Limit scans to intended files and avoid submitting sensitive citation material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Usage guide](references/usage_guide.md)
- [Command-line flags](references/flags.md)
- [Python API](references/python_api.md)
- [API examples](references/api_examples.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Files, JSON, HTML, CSV, BibTeX, RIS]

**Output Format:** [Citation verification results and reports in text, JSON, or HTML, with optional CSV, BibTeX, RIS, and formatted reference-list exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses five-state outcomes: correct, mismatch, partial, invalid, and unknown. Results depend on the supplied citation context and scholarly-service availability; network failures remain unverified rather than being reported as not found.]

## Skill Version(s):

5.4.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

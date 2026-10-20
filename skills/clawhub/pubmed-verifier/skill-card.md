## Description:

Verifies PubMed and other scholarly citation identifiers against registry records, comparing cited details with the actual paper to flag mismatches and uncertain results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and academic writers use the skill to audit PMID, DOI, arXiv, and reference-list citations against scholarly records. It compares claimed citation details with registry metadata and produces verification reports or formatted reference lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic output may expose proxy passwords.

Mitigation: Redact credentials before sharing --doctor output and prefer a version that masks proxy credentials.

Risk: Some results may overstate what was verified, including invalid DOI and submission-readiness claims.

Mitigation: Supply expected titles and authors, and independently check invalid DOIs and submission-readiness claims.

Risk: Citation identifiers and title queries are sent to the disclosed scholarly services.

Mitigation: Choose input files with this data sharing in mind.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Project homepage (release metadata)](https://github.com/docsor1212/pubmed-verifier)
- [Usage guide](references/usage_guide.md)
- [API examples](references/api_examples.md)

## Skill Output:

**Output Type(s):** [Analysis, Files, Text, Markdown, JSON, HTML]

**Output Format:** [Text, JSON, JSONL, and HTML verification reports; formatted reference lists in GB/T 7714, Vancouver, APA, or AMA styles.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are written locally; network failures are reported as unverified rather than not found.]

## Skill Version(s):

5.3.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

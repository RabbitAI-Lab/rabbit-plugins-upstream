## Description:

A reference checker for AI-fabricated citations that verifies PMIDs against PubMed and checks whether each identifier points to the paper being claimed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and editors can audit PMID, DOI, arXiv, and reference-list citations against scholarly registries, identify mismatches or uncertain results, and prepare verified reference lists or audit reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic output may expose proxy credentials.

Mitigation: Remove proxy credentials from --doctor output before sharing it.

Risk: Reports or readiness labels may overstate citation verification, and rejected DOIs may be valid.

Mitigation: Provide expected titles and authors, do not treat bare-PMID exports or readiness labels as proof of citation identity, and manually check rejected DOIs.

Risk: Verification sends citation identifiers and search terms to external registries.

Mitigation: Limit inputs to material you are permitted to disclose.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Project homepage](https://github.com/docsor1212/pubmed-verifier)
- [Usage guide](references/usage_guide.md)
- [Operations guide](references/operations.md)
- [API examples](references/api_examples.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, HTML, CSV, BibTeX/RIS, Shell commands, Guidance]

**Output Format:** [Terminal text, JSON, HTML reports, CSV, BibTeX/RIS, and formatted reference lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes per-citation evidence and verification states; available output depends on the selected command and input.]

## Skill Version(s):

5.5.0 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

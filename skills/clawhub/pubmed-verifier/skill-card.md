## Description:

Checks biomedical references against academic registries to identify invalid or mismatched PMIDs, DOIs, and arXiv IDs and produce citation audit reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and developers use this skill to check reference lists and AI-generated citations against published records before sharing or submitting their work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers, titles, and optional contact or API-key values may be sent to academic registries.

Mitigation: Review the information and optional credentials supplied before running registry checks.

Risk: A directory scan or report export may read or write files beyond the intended citation set.

Mitigation: Limit --source to intended directories and choose report and export paths deliberately.

Risk: Locally cached metadata may be out of date for a final audit.

Mitigation: Use --no-cache when current registry status matters.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Usage guide](artifact/references/usage_guide.md)
- [Academic registry API examples](artifact/references/api_examples.md)
- [Python API examples](artifact/references/python_api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Citation reports]

**Output Format:** [Text or Markdown guidance, with optional HTML, JSON, CSV, and bibliography reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-state citation verdicts with supporting metadata; unreachable registries result in unverified findings.]

## Skill Version(s):

4.6.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

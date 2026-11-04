## Description:

Verifies whether PMIDs, DOIs, arXiv IDs, and reference details match records in academic registries, then reports mismatches and uncertainty.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and evidence teams use the skill to audit citations in manuscripts, reference lists, and knowledge bases. It checks whether identifiers exist and whether the records match the cited work, and can format verified references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostics described as safe to share can reveal proxy passwords.

Mitigation: Avoid sharing --doctor output when proxy URLs contain login credentials until credential masking is fixed.

Risk: Citation searches and optional contact details reach external registries.

Mitigation: Select only the intended references, and provide optional contact details only when needed.

Risk: Conflicting duplicate claims, missing DOI results, or retraction explanations may need human review before a publication-readiness report is relied on.

Mitigation: Independently check those cases before relying on publication-readiness reports.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Project homepage](https://github.com/docsor1212/pubmed-verifier)
- [Usage guide](references/usage_guide.md)
- [Command flags](references/flags.md)
- [Operations guide](references/operations.md)
- [Python API](references/python_api.md)
- [API examples](references/api_examples.md)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML, CSV, Formatted reference lists]

**Output Format:** [Text summaries and reports; optional HTML, JSON, CSV, BibTeX, CSL JSON, RIS, and formatted citation lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch results include per-citation verification states and available record comparisons; unreachable registries produce unknown results.]

## Skill Version(s):

6.5.0 (source: SKILL.md frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

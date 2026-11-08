## Description:

Checks whether PMID, DOI, and arXiv citations exist and match the cited papers, then produces verification reports and formatted reference lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and evidence-based medicine teams use the skill to audit reference lists and check whether citation identifiers point to the claimed papers. It can also produce review reports and formatted lists from verified records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic output may expose credentials embedded in a proxy URL.

Mitigation: Use corrected diagnostic masking and redact existing doctor output before sharing it.

Risk: Some citation checks can be unreliable, including conflicting DOI claims, non-Crossref DOIs reported invalid, and retraction explanations.

Mitigation: Independently check these results before relying on the report.

Risk: Title queries sent to external registries could include confidential information.

Mitigation: Limit scans to intended documents and exclude confidential information from submitted title queries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Project homepage](https://github.com/docsor1212/pubmed-verifier)
- [Usage guide](references/usage_guide.md)
- [Flag reference](references/flags.md)
- [Python API reference](references/python_api.md)

## Skill Output:

**Output Type(s):** [Text reports, HTML reports, JSON reports and audit data, Formatted citation lists]

**Output Format:** [Text, HTML, JSON, BibTeX, RIS, CSL JSON, and formatted reference text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports and exports are written to user-selected paths.]

## Skill Version(s):

6.8.0 (source: SKILL.md frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

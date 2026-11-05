## Description:

Verifies whether PMID, DOI, and arXiv citations exist and match the papers claimed, and reports uncertainty when its sources cannot confirm them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and evidence review teams use the skill to audit citations in manuscripts and reference collections, identify mismatches or retractions, and format verified references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When an authenticated proxy is configured, --doctor output may expose proxy passwords.

Mitigation: Do not share --doctor output when using an authenticated proxy until credential masking is fixed.

Risk: Citation identifiers, titles, and search terms are sent to external academic services; an optional contact email may accompany requests.

Mitigation: Review the data being checked, scan only the intended input directory, and avoid sending sensitive citation or search information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [Project homepage listed in package metadata](https://github.com/docsor1212/pubmed-verifier)
- [ModelScope skill listing](https://modelscope.cn/skills/Docsor/pubmed-verifier)
- [Usage guide](references/usage_guide.md)
- [Python API reference](references/python_api.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, HTML, JSON, CSV, BibTeX, RIS, CSL JSON]

**Output Format:** [Citation verification reports and formatted reference lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include per-citation verdicts and supporting metadata; results may be unknown when sources are unreachable or evidence is insufficient.]

## Skill Version(s):

6.6.0 (source: SKILL.md frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

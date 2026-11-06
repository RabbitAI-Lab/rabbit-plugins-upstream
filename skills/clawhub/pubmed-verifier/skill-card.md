## Description:

Verifies whether PMID, DOI, arXiv, and reference-list citations exist and match their claimed publication details, and can format verified references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, and evidence-based medicine teams use the skill to audit citation lists, check that identifiers match the cited papers, and prepare formatted references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostics advertised as safe to share can expose proxy passwords.

Mitigation: Avoid `--doctor` with credential-bearing proxy URLs and redact diagnostics before sharing.

Risk: Citation queries are sent to external academic services.

Mitigation: Use narrow inputs and exclude confidential details from queries.

## Reference(s):

- [Usage guide](artifact/references/usage_guide.md)
- [API examples](artifact/references/api_examples.md)
- [Operations guide](artifact/references/operations.md)
- [Project homepage](https://github.com/docsor1212/pubmed-verifier)
- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [ModelScope package mirror](https://modelscope.cn/skills/Docsor/pubmed-verifier)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, HTML, Markdown]

**Output Format:** [Citation verification reports and formatted reference lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports assign per-citation verdicts; network failures are reported as unverified. Reference formatting supports GB/T 7714, Vancouver, APA, and AMA.]

## Skill Version(s):

6.7.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Audits a website's accessibility and business information for AI search, applies supported repository fixes, and proposes the changes in a pull request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchiz](https://clawhub.ai/user/searchiz)

### License/Terms of Use:

MIT-0

## Use Case:

Website developers and site owners use this skill to check AI-search readability and prepare evidence-backed fixes to crawler rules, canonical links, and site metadata for review in a pull request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit runs an unpinned GitHub-sourced tool, which may execute code that changes between runs.

Mitigation: Pin the audit tool to a reviewed version before running it.

Risk: Audit suggestions can change site files and lead to a commit and pull request.

Mitigation: Review the proposed changes and supporting business facts, and request confirmation before committing or opening a pull request.

## Reference(s):

- [Searchiz audit tool referenced by the skill](https://github.com/searchiz/searchiz-audit)
- [Searchiz](https://searchiz.com)

## Skill Output:

**Output Type(s):** [Analysis, Code, Configuration, Markdown]

**Output Format:** [Audit summary and pull request description in Markdown, with proposed repository changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The audit creates a local JSON report and suggested diffs; these are not committed.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

帮助公众号编辑、自媒体作者和合规人员在发布前检查敏感词、错别字、政治合规、平台规范、写作规范和 AI 味，并输出可执行修改清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiworkskills](https://clawhub.ai/user/aiworkskills)

### License/Terms of Use:

MIT-0

## Use Case:

External content editors, self-media authors, and compliance reviewers use this skill to review WeChat public-account drafts before publication. It supports content review and final review workflows, producing issue lists and finalization guidance for article files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write finalized article files and append configured embed placeholders, which may change publish-ready content beyond review comments.

Mitigation: Use it only in a trusted article workspace, inspect .aws-article/config.yaml and article.yaml before finalization, and explicitly opt out of embeds when they are not wanted.

Risk: The skill may instruct the agent to run a Python citation-stripping script from a sibling package despite a review-only disclosure.

Mitigation: Confirm the sibling package is expected and review the command before allowing finalization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aiworkskills/skills/aws-wechat-article-review)
- [Review checklist](references/checklist.md)
- [Review output format](references/output-format.md)
- [AI flavor check methodology](references/ai-flavor-check.md)
- [AI flavor check calibration samples](references/ai-flavor-check-samples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration, Shell commands]

**Output Format:** [Markdown review reports, checklist tables, file finalization guidance, and occasional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce review.md and finalized article.md in the article workspace when the workflow reaches final approval.]

## Skill Version(s):

1.0.25 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

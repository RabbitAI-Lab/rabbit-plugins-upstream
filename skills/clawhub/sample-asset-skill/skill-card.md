## Description:

用于演示"业务流程处理 + 数字资源入库"闭环的样例 PRD 资产。

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workflow operators use this skill as a sample PRD asset for packaging Markdown content into a versioned ClawHub skill and documenting resource-hub ingestion. It describes weekly sales report normalization from raw transaction logs into a CSV asset that downstream analytics pipelines can index and reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reproduction steps may upload data or submit forms to an external resource hub.

Mitigation: Confirm the target hub, account, visibility setting, and data before any upload or form submission.

## Reference(s):

- [Product Requirements Document: Weekly Sales Report](artifact/asset-sample.md)
- [Sample Asset Skill on ClawHub](https://clawhub.ai/terrycarter1985/skills/sample-asset-skill)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and PRD requirements]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sample input, processing, output, ingestion, and success criteria for a weekly sales report asset.]

## Skill Version(s):

1.0.0 (source: package.json and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

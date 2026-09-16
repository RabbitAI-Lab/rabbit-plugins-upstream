## Description:

用 Cue 逐条核验保险产品的保障责任、责任免除、等待期、费率与退保损失，并与同类产品客观对比，产出一份可向客户如实说明的条款理解底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Insurance professionals, compliance reviewers, and agents use this skill to check policy coverage, exclusions, waiting periods, rates, surrender costs, and peer-product differences before preparing customer-facing explanations. It helps separate statements that can be fairly supported by policy terms from claims that should not be promised.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Insurance product details and generated report contents may be sent to Cue and reflected in externally hosted report links.

Mitigation: Use only with data approved for Cue, confirm Cue privacy and sharing controls before sensitive use, and omit the share link when a web-accessible report reference is not desired.

Risk: Cue report text is external content and may be incomplete, stale, or unsuitable for direct customer-facing insurance advice without review.

Mitigation: Review the report against official policy terms, insurer documents, and applicable compliance requirements before relying on it for sales or customer communication.

Risk: The skill defaults toward attaching Cue-hosted report links, which can reduce user control over dissemination.

Mitigation: Confirm link-sharing expectations with the user, include only links built from actual returned conv_id values, and do not attach a link when the user declines or no conv_id is returned.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-insurance-policy-check)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key)
- [Cue runner source referenced by the skill](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror referenced by the skill](https://gitee.com/sensedeal/cue-skills)
- [China insurance regulator fallback source referenced by the skill](https://www.cbirc.gov.cn)
- [China Insurance Association fallback source referenced by the skill](https://www.iachina.cn)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report text with Cue share links, local report paths, and inline shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local Markdown report files under ~/cue-reports and may include a Cue-hosted report URL when an actual conv_id is returned.]

## Skill Version(s):

1.0.6 (source: server release evidence; artifact frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

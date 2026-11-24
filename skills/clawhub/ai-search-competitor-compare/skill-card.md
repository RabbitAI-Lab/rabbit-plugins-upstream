## Description:

This skill compares how often AI search platforms recommend a brand and its competitors, analyzes rankings and cited sources, and produces a shareable report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hclscut](https://clawhub.ai/user/hclscut)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing teams use this skill to compare brand recommendations across AI search platforms, inspect cited sources, and identify practical visibility improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flagged a possible environment-value network flow.

Mitigation: Review outbound requests and use a dedicated MaxAEO API key when running the skill.

Risk: The security review noted that the declared tool scope is missing.

Mitigation: Review the requested network access and query plan before confirming submissions.

Risk: Broad activation phrases may cause the skill to be selected outside a focused AI-search comparison task.

Mitigation: Invoke it for AI-search competitor comparisons and confirm the planned questions and platforms before submitting.

## Reference(s):

- [MaxAEO Developer Documentation](https://maxaeo.cn/docs/developers/)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Files]

**Output Format:** [Comparative text summary and shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports recommendation counts and rankings, cited sources, and suggested visibility improvements.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

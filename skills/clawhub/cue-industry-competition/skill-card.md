## Description:

用 Cue 穿透目标行业的景气周期、竞争格局与产业链地位，识别集中度、龙头壁垒与供需或政策拐点，并产出支持配置决策的行业研判底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and investment research analysts use this skill to request an industry-level business cycle, competitive landscape, supply-demand, policy catalyst, value-chain position, and investment-window analysis. The skill runs a Cue research workflow and returns the resulting research draft without local retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the user's Cue API key to cuecue.cn for authentication.

Mitigation: Install and run it only when using Cue's external service is intended, and keep the Cue API key in the expected ~/.cue configuration or CUE_API_KEY environment variable.

Risk: The artifact names an external Cue runner but does not include or pin its installer or runner source.

Mitigation: Review the referenced runner source before first use and confirm it matches the expected Cue research workflow.

Risk: Reports are written under ~/cue-reports and rely on Cue service availability and external data sources.

Mitigation: Check the Cue service health before long runs and review generated Markdown reports before using them in investment or business decisions.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/panting09266-ai/skills/cue-industry-competition)
- [Cue shared report example](https://cuecue.cn/share/RWtYmuF_)
- [Cue service](https://cuecue.cn)
- [Cue API key page](https://cuecue.cn/api-key)
- [Cue runner source referenced by the artifact](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror referenced by the artifact](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown research draft with optional shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The research report is written to a Markdown file under ~/cue-reports when the Cue runner completes successfully.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

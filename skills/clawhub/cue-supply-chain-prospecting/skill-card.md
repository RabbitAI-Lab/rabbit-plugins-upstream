## Description:

用 Cue 沿核心企业客户、供应商和招投标关系链挖掘产业链上下游可拓展名单，并给出每家企业的切入点和可能的金融需求。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External business-development and commercial banking teams use this skill to start from a core enterprise and generate an upstream/downstream prospect list with relationship context, suggested outreach angles, and likely financial needs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses cuecue.cn and a third-party Cue runner for company research queries.

Mitigation: Confirm the runner source is trusted before installation and understand what business queries are sent to the Cue service.

Risk: The skill requires a local Cue API key.

Mitigation: Keep the API key and ~/.cue/config.json private, and rotate the key if it may have been exposed.

Risk: Generated reports may contain sensitive prospecting or customer-development information.

Mitigation: Choose output paths that do not unintentionally expose reports and review report contents before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-supply-chain-prospecting)
- [Cue sample report](https://cuecue.cn/share/Ml8DOQg5)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API key setup](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with shell command examples and structured prospecting tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prospect lists, relationship context, outreach angles, likely financial needs, priority tiers, and source links.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

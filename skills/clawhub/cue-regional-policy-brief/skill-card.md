## Description:

用 Cue 聚合指定区域的政策发布、招商动态及市场数据，筛选高价值合规线索与潜客名单，产出结构化周度情报简报，赋能律所 BD 团队精准获客。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Law-firm business development teams and commercial research users use this skill to request regional policy, investment-attraction, market, compliance, and lead-generation briefs from Cue. The skill helps turn a target region or topic into a structured Markdown brief with policy updates, opportunity signals, potential client lists, demand inferences, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User queries are sent to Cue's cuecue.cn service for processing.

Mitigation: Do not include confidential client names, privileged facts, or sensitive business data unless the user accepts sending them to Cue.

Risk: The skill depends on an external Cue runner and Cue service availability.

Mitigation: Install the runner only from the referenced sensedeal source, review install commands before running them, and run the documented Cue health checks before research.

Risk: Policy and market outputs may depend on external public data sources that can be stale, unavailable, or incomplete.

Mitigation: Review report source links and use the documented government and ministry fallback sources when Cue or upstream sources are unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-regional-policy-brief)
- [Cue sample report](https://cuecue.cn/share/TRk4KUxsHw1y89JrEnsRH)
- [Cue API key page](https://cuecue.cn/hub/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief with inline shell commands and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cue-generated regional policy and business-opportunity reports can be converted to DOCX or PDF with pandoc.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

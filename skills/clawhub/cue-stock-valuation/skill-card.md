## Description:

用 Cue 对个股进行全周期估值分析，融合短线资金流向与中长线估值模型，帮助评估情绪博弈、支撑压力、业绩兑现和安全边际。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to request structured stock valuation and price analysis through Cue. It supports single-stock research, holding reviews, new-stock research, and peer valuation comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release asks users to run an unverified external Cue runner with access to a Cue API key, network access, user-accessible home-directory files, and generated reports.

Mitigation: Review before installing, use a pinned and checksummed runner, and restrict credentials and local file access to the minimum needed for the task.

Risk: Cue share, referral, and payment links are part of the workflow and may represent external commercial-service dependencies.

Mitigation: Treat Cue account, share, referral, and payment links as external service links rather than neutral system requirements, and disclose that dependency to users.

Risk: Financial analysis quality and freshness depend on Cue services and external data sources.

Mitigation: Preserve source links, avoid changing reported numbers, and have users review outputs before relying on them for investment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-stock-valuation)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/hub/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links and Cue report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill asks the agent to preserve reported figures and source links, attach the Cue original report link when available, and optionally convert Markdown reports to Word or PDF with pandoc.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

用 Cue 实时追踪近 24 小时全球重磅资讯，拆解其对权益市场的催化逻辑与受益板块，助短线交易者紧跟市场热钱流向。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External traders and market analysts use this skill to run a Cue report that scans the last 24 hours of global market news, explains equity-market catalyst paths, ranks benefiting sectors, and highlights hot-money direction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run unpinned external Python code outside the reviewed package.

Mitigation: Review the external cue-skills runner before installing, prefer a pinned release or commit with a verified checksum, and run it in a restricted environment.

Risk: The workflow uses a Cue API key and writes generated reports to a local directory.

Mitigation: Expose only the Cue API key and intended report directory to the execution environment, and avoid sharing unrelated local credentials or files.

Risk: Market conclusions depend on Cue service availability and external source freshness.

Mitigation: Check Cue service health before running and treat generated market analysis as decision support requiring human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-hotspot-tracker)
- [Cue runner source linked by artifact](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror linked by artifact](https://gitee.com/sensedeal/cue-skills)
- [Cue API key page](https://cuecue.cn/hub/api-key)
- [Example Cue report](https://cuecue.cn/share/IeiYoiYB1DsJ5fWc_1jF0)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Structured Markdown report with source links and optional shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key; report quality and timeliness depend on Cue service availability and external data sources.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

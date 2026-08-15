## Description:

Uses Cue to generate full-scope due diligence reports for China public equity funds, covering manager profile, attribution, style consistency, risk metrics, holdings, fees, and scale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Individual fund investors, wealth advisors, fund advisory teams, and FOF researchers use this skill to evaluate public China equity funds before selection, holding review, manager comparison, or replacement screening. It is intended for due diligence and report generation, not future performance prediction or buy/sell timing advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fund names, analysis prompts, and the user's Cue API credential are used with cuecue.cn.

Mitigation: Confirm the data-sharing posture before use, protect the API key, and use the documented health checks before running long analyses.

Risk: Reports may influence investment decisions but are not guaranteed predictions or financial advice.

Mitigation: Review the report's source links and data cutoff date, and use qualified financial review before acting on conclusions.

Risk: Long-running or paid Cue sessions can be affected by timeouts, queueing, or interruption.

Mitigation: Monitor runtime and credits, avoid cancelling active sessions unless intended, and resume interrupted runs with the same command as documented.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-fund-due-diligence)
- [ClawHub publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Cue service](https://cuecue.cn)
- [Cue runner source referenced by artifact](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror referenced by artifact](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown due diligence report with cited source links and optional shell commands for running Cue and converting reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are saved locally when an output path is provided; runtime is typically several minutes and depends on query scope and Cue service status.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

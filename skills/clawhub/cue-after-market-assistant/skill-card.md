## Description:

盘后超级助理 uses Cue to generate structured after-market market and sector recap reports covering market drivers, fund flows, holding-level context, and next-day watchpoints while excluding single-stock technical analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External investors and market watchers use this skill after market close to request market-level or sector-level A-share recaps, including drivers, capital flows, major themes, and next-day watchpoints. It is not intended for single-stock technical analysis or buy/sell advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market recap prompts and generated reports are sent to Cue's remote service.

Mitigation: Avoid brokerage credentials, account secrets, and unnecessary sensitive holdings details in prompts or reports.

Risk: The skill installs and updates an external Cue runner from GitHub or Gitee.

Mitigation: Review the runner source before first use and re-check it after updates before relying on it in a managed environment.

Risk: The workflow is scoped to market and sector recaps, not single-stock technical analysis.

Mitigation: Route single-stock questions, buy/sell timing, support levels, and short-term technical analysis to a dedicated stock-analysis workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-after-market-assistant)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/hub/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Example Cue report](https://cuecue.cn/share/e48Yoz--t14FjIHxaxxLz)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown market recap report with Cue share link, local report path, and setup or troubleshooting command blocks when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market-level and sector-level recap only; excludes single-stock technical analysis.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

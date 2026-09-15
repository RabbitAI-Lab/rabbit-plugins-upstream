## Description:

Uses Cue to produce deep sector and ETF research for A-share ETFs, including sector landscape analysis, ETF comparisons, holdings look-through, valuation context, and risk notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External investors, advisors, and agents use this skill to request structured research on A-share ETF sectors, compare related ETFs, inspect holdings exposure, and understand valuation and risk context. It supports research and screening workflows, not real-time trading, intraday arbitrage, or specific buy/sell timing advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ETF research prompts and Cue API credentials are sent to cuecue.cn.

Mitigation: Use a dedicated Cue API key where possible, review Cue account settings, and avoid including sensitive personal financial details in research prompts.

Risk: Reports and session state may be stored under the user's home directory.

Mitigation: Review generated report files and local Cue state before sharing a machine, archiving logs, or publishing workspaces.

Risk: The skill can return Cue share links for completed reports.

Mitigation: Treat share URLs as externally accessible unless verified otherwise, and avoid distributing links that contain sensitive portfolio context.

Risk: Account-credit prompts and commercial upgrade flows may appear in responses.

Mitigation: Review any invitation, payment, or account-credit prompt before following it, especially in managed or enterprise environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-sector-etf)
- [Publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue service](https://cuecue.cn)
- [Cue API key page](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown research report with tables, source links, a local report path, and a Cue share URL when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key and may store reports and session state under the user's home directory.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

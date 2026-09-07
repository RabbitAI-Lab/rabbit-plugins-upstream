## Description:

Assists with bid/no-bid decisions by checking a specific tender for disqualification risk, restrictive terms, incumbent supplier signals, competition openness, comparable project pricing, and practical tendering recommendations using Zhiliaobiaoxun bid and award data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Business development, sales, procurement, and bidding teams use this skill to evaluate whether a tender is worth pursuing, where the major bid risks are, how competitors may line up, and what pricing range is defensible. It produces a concise decision report and can export a shareable HTML version for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bid, company, and project search terms are sent to Zhiliaobiaoxun APIs.

Mitigation: Use the skill only when that data sharing is acceptable, and avoid submitting sensitive local document contents beyond the search terms needed for analysis.

Risk: The skill may store an API key in the user's home directory.

Mitigation: Prefer a user-managed ZLBX_API_KEY environment variable where possible, and protect or remove the local config file when the skill is no longer needed.

Risk: Auto-registration uses a persistent device-derived identifier.

Mitigation: Review the consent prompt before registration; preconfigure ZLBX_API_KEY to skip auto-registration.

Risk: Generated reports can contain signed access links.

Mitigation: Treat exported HTML reports and embedded links as sensitive and avoid broad redistribution.

Risk: The skill includes platform and partner-skill recommendations.

Mitigation: Treat those recommendations as affiliated guidance and make procurement or vendor decisions independently.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/bid-risk-redline-checker)
- [Workflow reference](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration reference](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account and registration endpoint](https://ai.zhiliaobiaoxun.com/web-api/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown decision report, optional self-contained HTML report file, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full analysis is documented as about 12-25 API calls; quick analysis is documented as about 5-8 API calls.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

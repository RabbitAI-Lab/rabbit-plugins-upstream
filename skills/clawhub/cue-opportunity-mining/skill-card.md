## Description:

商机挖掘 uses Cue deep research to identify corporate opportunity signals from public data, including capital activity, enterprise lists, customer events, supply-chain relationships, dividends, and visit briefs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

Commercial, banking, business development, and enterprise sales users use this skill to run Cue research workflows that turn public business signals into opportunity lists, account briefs, and marketing drafts. It supports diligence and outreach planning, but does not replace legal review, underwriting, or final business decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to fetch and run unpinned external runner code.

Mitigation: Review the runner repository before use, pin a trusted revision when possible, and avoid automatic updates in controlled environments.

Risk: The runner uses a local Cue API key and may consume Cue credits during deep research runs.

Mitigation: Confirm each paid run with the user before execution and ensure the local Cue configuration is appropriate for the workspace.

Risk: Business research from public sources may be incomplete, stale, or unsuitable for regulated decisions.

Mitigation: Keep source links in the final report and require human review before diligence, legal, underwriting, or customer-action decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-opportunity-mining)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue skills runner repository](https://github.com/sensedeal/cue-skills)
- [Cue skills runner mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sourced business-research findings, opportunity lists, account briefs, and run-status guidance.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Uses Cue to summarize intraday market conditions, sentiment, fund flows, leading sectors, and risk areas in a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Market observers use this skill to review intraday market conditions through Cue and receive structured commentary on sentiment, fund flows, sector themes, and risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow updates and runs external runner code that may change, and the supplied artifact does not include its dependencies.

Mitigation: Review and pin the runner to a specific revision, and make updates deliberate.

Risk: Agent-run commands can read the configured Cue key, queries are sent to Cue, and reports receive share links.

Mitigation: Use a dedicated Cue key, account for data sent to Cue, and treat report links as shareable.

## Reference(s):

- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-intraday-market)
- [Cue runner source listed by the skill (GitHub)](https://github.com/sensedeal/cue-skills)
- [Cue runner mirror listed by the skill (Gitee)](https://gitee.com/sensedeal/cue-skills)
- [ClawHub release page](https://clawhub.ai/panting09266-ai/skills/cue-intraday-market)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Structured Markdown intraday market report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers market overview, sentiment, fund flows, sector themes, risk areas, and source links.]

## Skill Version(s):

1.1.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

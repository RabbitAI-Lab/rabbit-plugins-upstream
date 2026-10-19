## Description:

Summarizes overnight market, policy, and industry news into a ranked pre-market watchlist of potential opportunities and risks for Chinese A-shares.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Individual investors use this skill to review overnight developments, identify A-share sectors to watch, and consider potential downside risks before the market opens. Its analysis is not investment advice or a real-time trading signal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install and run external runner code that can change after review.

Mitigation: Inspect the runner and its updates before installation or execution; install only if you trust its maintainer and Cue.

Risk: A reusable Cue API key is stored on disk and used to access an external service.

Mitigation: Create the key yourself, restrict access to ~/.cue/config.json, and avoid sharing the key or private portfolio and account details.

Risk: Runs may consume Cue credits, and market analysis may be delayed or inaccurate.

Mitigation: Check credit costs before running and verify time-sensitive claims against cited sources; do not treat the report as investment advice.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-pre-market-strategy)
- [Cue runner installation source (linked by the skill)](https://github.com/sensedeal/cue-skills)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-pre-market-strategy)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown report with source links and a Cue report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranks sectors by potential opportunity and flags risks; may save a local Markdown copy. No real-time quotes or buy/sell signals.]

## Skill Version(s):

1.0.6 (source: server-resolved release; supplied skill frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

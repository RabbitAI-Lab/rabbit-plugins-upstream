## Description:

Uses Cue to map public-company supply chains, identify overlooked segment leaders, and explain how industry trends may affect their fundamentals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Individual investors and industry researchers use this skill to examine publicly documented Chinese A-share supply chains, trace upstream and downstream effects, and identify companies for further fundamental research. It does not provide trade timing or buy/sell recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and an API key are used with Cue's remote stock-research service.

Mitigation: Use only if you intend to use that service; configure the Cue API key securely and review the queries you send.

Risk: Separate bundled Omni Reader MCP bridge instructions can change agent configuration and grant access to local file roots.

Mitigation: Do not set up the optional bridge or grant local file roots unless you separately need and approve those capabilities.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/panting09266-ai/skills/cue-supply-chain-mining)
- [Cue platform](https://cuecue.cn)
- [Cue runner repository (linked in skill documentation; import provenance unavailable)](https://github.com/sensedeal/cue-skills)
- [Example supply-chain report](https://cuecue.cn/share/F8PzjKYbVBgYX2oN9clWB)

## Skill Output:

**Output Type(s):** [Markdown, Analysis]

**Output Format:** [Structured Markdown report with source links and a link to the original Cue report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers supply-chain segments, trend transmission, candidate companies, sensitivity assessment, and caveats; may save a local Markdown copy.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata; bundled SKILL.md states 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

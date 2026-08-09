## Description:

Yanmu Hot Stocks helps an agent present A-share, Hong Kong, or U.S. stock candidates for teaching-oriented stock research workflows.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

External users and classroom/demo agents use this skill to offer a short, clearly caveated list of A-share, Hong Kong, or U.S. stock tickers for selecting a research target. It should be treated as demo output, not current market advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may present stock picks as dynamic market data even when the helper script returns fixed sample lists.

Mitigation: Label the output source and freshness clearly, keep the demo-only disclosure visible, and require independent verification before using any ticker in real analysis.

Risk: Users may mistake teaching/demo stock candidates for investment recommendations.

Mitigation: State that outputs are not investment advice and restrict the skill to classroom or demonstration research-selection workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/caoling7878-arch/skills/yanmu-hot-stocks)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown-formatted text, with optional JSON from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market selection is limited to A-share, Hong Kong, or U.S. stocks; output may use fixed sample stock lists.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Answer stock-terminal commands and market research questions with compact, sourced views of price, sentiment, SentiSense Score, news, filings, analyst ratings, earnings, and end-of-day options analytics; for explicit build requests, provide contracts, fixtures, and a staged guide for a local chat-and-canvas financial terminal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent for sourced, read-only market research across stock prices, sentiment, news, filings, analyst ratings, earnings, and options positioning. Developers can use the included contracts and staged guidance to build a local chat-and-canvas financial terminal when they explicitly request one.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API credential could be exposed in chat or saved artifacts.

Mitigation: Keep SENTISENSE_API_KEY in the environment and out of chat, URLs, and saved artifacts.

Risk: Market observations may be delayed, incomplete, or unavailable, and live services were not validated in the supplied security evidence.

Mitigation: Show supplied source dates and coverage, label unavailable data clearly, and treat the output as informational context rather than investment advice.

## Reference(s):

- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense](https://sentisense.ai)
- [Commands and data](artifact/references/commands-and-data.md)
- [Build in an afternoon](artifact/references/build-in-an-afternoon.md)
- [Canvas grammar](artifact/references/canvas-grammar.md)
- [Verification guidance](artifact/references/verification.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Text or Markdown research views; when requested, code examples, JSON contracts, and XML canvas documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research views are sourced and read-only. Local app or artifact creation is provided only when requested.]

## Skill Version(s):

2.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

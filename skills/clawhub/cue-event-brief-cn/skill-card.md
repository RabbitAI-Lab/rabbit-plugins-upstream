## Description:

Turns a single A-share temporary announcement into a five-part, source-checkable brief with verbatim key figures, candidate impact chains, peer comparisons, and open questions, while leaving ratings and target prices for human review and making no price forecasts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and readers reviewing A-share disclosures use this skill to draft a source-checkable five-part briefing for a single temporary announcement. It is not for investment advice or buy/sell decisions, and ratings and target prices remain for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional connection checks may expose the CUE_API_KEY.

Mitigation: Use the local card workflow without an API key until approved HTTPS destinations and safe redirect handling are enforced; send only public or redacted documents, confirm credit use, and review installed versions.

Risk: A structurally valid card may still contain inaccurate facts or misleading investment judgments.

Mitigation: Verify each figure against its cited disclosure, keep unsupported facts marked as not found, and leave ratings, target prices, and sustained-impact judgments for human review.

## Reference(s):

- [Cue Event Brief CN on ClawHub](https://clawhub.ai/huhoo/skills/cue-event-brief-cn)
- [Cue service](https://cuecue.cn)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)
- [Cue API key guidance](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Five-section Markdown announcement brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source-anchored verbatim figures, candidate impact chains, peer comparisons, and open questions; ratings and target prices remain [待人工], and the brief does not predict price movement.]

## Skill Version(s):

0.2.22

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Compare companies or products using Crawlora website extraction, traffic estimates, reviews, product listings, and hiring data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product marketers, founders, and analysts use this skill to build evidence-backed competitor briefs, positioning and pricing comparisons, and competitive battlecards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key to an overridden API endpoint.

Mitigation: Use a limited or separate Crawlora API key and set CRAWLORA_API_BASE only when the destination is trusted.

Risk: Outbound API requests may transmit sensitive workspace or business data.

Mitigation: Review request bodies before sending sensitive information through the helper.

Risk: The bundled helper is broader than the stated competitor-intelligence workflow.

Mitigation: Limit use to the endpoints and evidence-gathering steps documented for the requested brief.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/competitor-intelligence)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with comparison matrices, claim ledgers, linked source summaries, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Material claims should distinguish company claims, third-party observations, and interpretation, with source links and retrieval context.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

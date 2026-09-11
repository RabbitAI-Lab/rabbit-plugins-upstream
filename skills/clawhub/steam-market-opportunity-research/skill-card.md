## Description:

Evaluate Steam game niches using Crawlora's game catalog, chart and player-count history, live pricing, reviews, and release news.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, product teams, and game-market researchers use this skill to compare Steam titles, analyze pricing, reviews, player activity, and release news, and form evidence-backed opportunity hypotheses for game concepts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Steam research queries and request bodies may contain confidential product strategy or private business details sent to Crawlora.

Mitigation: Use approved Crawlora accounts and avoid confidential strategy or private business details unless Crawlora is approved for that data.

Risk: Steam owner ranges, chart ranks, prices, and concurrent-player samples can be misread as audited sales, revenue, retention, or unique audience size.

Mitigation: Report these as bounded observations or third-party estimates and avoid deriving revenue or retention from them alone.

Risk: Using routes outside the documented Steam research catalog could broaden what data is sent to the service.

Mitigation: Use the bundled helper and documented endpoint reference for Crawlora requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/steam-market-opportunity-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [Crawlora](https://crawlora.net)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown opportunity briefs with comparable-title tables, activity and pricing summaries, review themes, cited examples, and optional shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should keep observed metrics, third-party estimates, and commercial hypotheses separate.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Evaluate Steam game niches using Crawlora's game catalog, chart and player-count history, live pricing, reviews, and release news.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Game developers, publishers, and market researchers use this skill to compare a Steam game concept against comparable titles, activity, pricing, reviews, release news, and documented caveats before forming opportunity hypotheses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends a Crawlora API key and user-directed Steam research parameters or JSON request bodies to Crawlora's API.

Mitigation: Keep the API key in the environment, avoid secrets or unrelated private data in query/body arguments, and install only when Crawlora is an acceptable data processor for the research task.

Risk: Opportunity hypotheses can overstate commercial evidence if estimates, player counts, review ratios, chart positions, and prices are treated as direct revenue or retention proof.

Mitigation: Keep observed metrics, third-party estimates, and commercial hypotheses separate; do not infer realized revenue from owner estimates or chart positions.

Risk: Incomplete pagination, rate limits, transient API failures, or lagging snapshots can produce partial or stale comparisons.

Mitigation: Respect documented page bounds, stop on repeated cursors/pages, back off on 429 responses, retry transient 5xx responses once, and preserve observation dates.

## Reference(s):

- [Steam market opportunity endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/steam-market-opportunity-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief with tables, cited observations, caveats, validation steps, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API-derived JSON observations, comparable-title tables, metric caveats, and next validation steps.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

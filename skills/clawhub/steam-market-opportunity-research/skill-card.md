## Description:

Evaluates Steam game niches using Crawlora game catalog data, chart and player-count history, live pricing, reviews, and release news for comparable-title and opportunity research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, product researchers, and game teams use this skill to compare Steam niches, pricing, activity trends, review themes, and positioning gaps before forming game opportunity hypotheses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key and caller-provided request data to unintended destinations if CRAWLORA_API_BASE is changed or if non-Steam paths are used.

Mitigation: Review before installing, keep CRAWLORA_API_BASE unset or pointed only at the intended Crawlora HTTPS API, avoid sensitive prompt text or private data, and restrict use to the documented Steam endpoints.

Risk: Steam market conclusions can be misleading if third-party owner estimates, daily concurrent-player samples, chart rankings, and review samples are treated as audited sales, retention, or full-market truth.

Mitigation: Preserve filters, dates, currencies, and sample boundaries; separate observed metrics from estimates and hypotheses; and avoid deriving revenue, retention, or causality from unsupported signals.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/steam-market-opportunity-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief with tables, cited observations, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API-derived JSON observations, pricing comparisons, review-theme counts, conflicting evidence, and next validation steps.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

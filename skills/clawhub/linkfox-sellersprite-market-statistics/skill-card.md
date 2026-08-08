## Description:

Fetches SellerSprite market-statistics dashboards for Amazon category node paths, including top-listing averages, BSR, sales, seller counts, and new-product metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace analysts, and agents use this skill to retrieve paid SellerSprite category statistics for a supplied marketplace and category node path. It is used to assess market quality and competition from aggregate listing, sales, seller, BSR, and new-product indicators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests use API keys and can be redirected through LinkFox endpoint override environment variables.

Mitigation: Keep API keys scoped and private, and only set endpoint override variables when the destination is trusted.

Risk: The onboarding flow can process phone/SMS login, API key generation, package listing, and billing orders.

Mitigation: Use the onboarding commands only when needed, confirm plan and payment details with the user, and avoid exposing returned credentials.

Risk: Full API responses are saved locally and small or inline responses may be printed to stdout.

Mitigation: Review saved response paths and stdout output before sharing logs or committing workspace files.

Risk: Uncached statistics requests consume 15 credits.

Mitigation: Explain additional credit cost before repeated calls and rely on the default cache for identical requests when appropriate.

## Reference(s):

- [Skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-market-statistics)
- [SellerSprite market statistics API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox agent portal](https://agent.linkfox.com/)
- [SellerSprite market statistics endpoint](https://tool-gateway.linkfox.com/sellersprite/market/statistics)

## Skill Output:

**Output Type(s):** [API Calls, Files, JSON, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON responses saved to local files with stdout summaries or full inline JSON, plus Markdown guidance for interpretation and onboarding.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full responses under a local linkfox session directory, uses a 24-hour cache by default, and consumes 15 credits per uncached statistics request.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

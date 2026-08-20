## Description:

Fetches node-level SellerSprite market statistics for Amazon categories, including average rating, price, BSR, sales, seller counts, and new-product metrics for market quality and competitive analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketplace analysts, and agents use this skill to retrieve category-level Amazon market statistics through LinkFox/SellerSprite before evaluating market size, competition, and new-product opportunity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox/SellerSprite API key and can generate or display API keys during onboarding.

Mitigation: Treat API keys as secrets, configure them only in trusted environments, and avoid running the skill in workspaces where untrusted code or users can read environment variables or terminal output.

Risk: Market statistics requests consume paid credits, and onboarding includes payment-plan and order flows.

Mitigation: Confirm the user's intent before paid calls, avoid repeated retries for failed or empty results, and review plan and payment details before placing any order.

Risk: The skill writes full API responses and session metadata to local linkfox directories.

Mitigation: Run it only in workspaces where local persistence is acceptable, and review or remove saved response files if they contain sensitive business or account data.

Risk: The skill may send feedback content to an external feedback API.

Mitigation: Review feedback text before submission and avoid including confidential user, account, or market data.

## Reference(s):

- [卖家精灵-选市场统计 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-market-statistics)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON response files with stdout JSON or a concise text summary for large responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full responses under a local linkfox session data directory, caches identical requests for 24 hours, and consumes 15 credits per uncached market statistics request.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

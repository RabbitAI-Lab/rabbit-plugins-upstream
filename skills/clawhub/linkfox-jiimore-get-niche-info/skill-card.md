## Description:

Queries and analyzes Jiimore Amazon niche market intelligence, including market metrics, buyer reviews, competition, pricing, and growth trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce analysts use this skill to retrieve and summarize niche-level Jiimore market data for a known Amazon niche ID, including demand, pricing, competition, launches, inventory health, reviews, and profitability signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can handle API keys, phone/SMS onboarding data, billing orders, and payment QR codes.

Mitigation: Use the self-service LinkFox website for account and billing steps when possible, and independently verify payment URLs or QR codes before paying.

Risk: Full Jiimore API responses and payment QR images may remain on disk under LinkFox directories, including fallback locations.

Mitigation: Run the skill only in workspaces where persistent LinkFox output is acceptable, and remove saved response or QR files after use when they are no longer needed.

Risk: Jiimore requests consume credits, and repeated calls can create additional cost.

Mitigation: Confirm the niche ID and marketplace before calling, use the same-session cache for repeated identical requests, and ask before making additional paid calls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-get-niche-info)
- [Jiimore Niche Market API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance, Files]

**Output Format:** [Markdown guidance, shell commands, and JSON API responses printed to stdout or saved as local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are saved under LinkFox session directories; small responses may print inline, large responses print summaries, and repeated identical requests can use a 24-hour local cache.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

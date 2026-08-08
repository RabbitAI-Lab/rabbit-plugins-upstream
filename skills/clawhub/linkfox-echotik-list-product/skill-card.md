## Description:

Searches and analyzes TikTok Shop product data across 16 marketplaces, including sales, GMV, pricing, ratings, commission rates, and influencer promotion metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and developers use this skill to research TikTok Shop products, compare product performance, and identify sales or influencer-driven product opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request phone-number-based account onboarding and generate or display a LinkFox API key.

Mitigation: Use a dedicated LinkFox account where possible, keep API keys out of shared logs and transcripts, and rotate keys if they are exposed.

Risk: The skill can create payable orders and payment QR codes when resolving credit or balance issues.

Mitigation: Confirm plan, price, payment method, and user approval before creating an order or presenting a payment code.

Risk: The skill saves full API responses locally, which may include product research data, account context, or operational details.

Mitigation: Run it from an appropriate workspace, review generated files before sharing, and delete stored responses when they are no longer needed.

Risk: Endpoint environment variables can override LinkFox API hosts.

Mitigation: Review LinkFox endpoint environment variables before use and avoid running the skill where untrusted environment values can redirect requests.

Risk: The skill may send feedback content to LinkFox automatically.

Mitigation: Avoid including secrets, private customer data, or sensitive business context in feedback content.

## Reference(s):

- [EchoTik-TikTok商品搜索 API Reference](references/api.md)
- [Authentication and Credits Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-product)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, saved JSON files, and shell commands for configuration or onboarding]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved locally as JSON; responses larger than 8 KB are summarized unless inline output is requested. Product searches consume LinkFox credits.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

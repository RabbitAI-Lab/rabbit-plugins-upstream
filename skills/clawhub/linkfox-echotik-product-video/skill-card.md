## Description:

Queries promotional videos linked to a TikTok Shop product and returns engagement metrics, estimated video sales, GMV, publish details, and creator identifiers for product-video marketing analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and analysts use this skill to inspect which TikTok promotional videos are associated with a product and compare video engagement, estimated sales, and estimated GMV. Agents can use it to prepare product-video performance summaries and identify creator content that appears to drive sales.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox account credentials and API keys.

Mitigation: Configure API keys only in trusted environments, prefer self-service account setup when possible, and keep keys out of source control.

Risk: The skill stores API responses in the workspace, which may include product analytics or other sensitive business data.

Mitigation: Review generated response files before sharing or committing workspaces, and delete saved data when it is no longer needed.

Risk: The account helper can create payment orders for paid LinkFox plans.

Mitigation: Review plan, price, and payment method details before proceeding with any order.

## Reference(s):

- [EchoTik product video API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-product-video)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON parameters, shell commands, and saved JSON response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large API responses are saved to the workspace and summarized; full inline JSON can be requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

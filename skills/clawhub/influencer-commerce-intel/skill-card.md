## Description:

TikTok Shop product selection and creator commerce intelligence: sales and GMV data, goods/live/video-ad monetization signals, product details, creator commerce potential.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce analysts use this skill to evaluate TikTok Shop creator sales, goods, live, and video-ad signals and turn them into product opportunity, risk, and pilot recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok identifiers and query data are routed to an external gateway.

Mitigation: Use only identifiers and query data approved for that third-party routing path, and review the gateway terms before use.

Risk: An API key may be sent to the external gateway when configured.

Mitigation: Keep SCRUMBALL_API_KEY in a local environment or private .env file, and keep it out of shared repositories, prompts, and logs.

Risk: The execution wrapper creates and sends a persistent local install identifier.

Mitigation: Install only when persistent usage tracking is acceptable, and remove the local install identifier if the installation should be reset.

## Reference(s):

- [API Index](references/api-index.md)
- [Request and Response Guide](references/request-response.md)
- [Operation Manifest](references/operations.json)
- [ClawHub Skill Page](https://clawhub.ai/chengyu-xixihaha/skills/influencer-commerce-intel)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown commerce summary with API-backed findings, risks, next steps, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected sections include Commerce summary, Opportunity, Risk, and Next step.]

## Skill Version(s):

1.0.3 (source: server release evidence and artifact config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

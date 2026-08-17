## Description:

Generates cloud-backed cross-border ecommerce keyword research and SEO placement reports for Amazon, Shopify, and TikTok Shop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[metahuan](https://clawhub.ai/user/metahuan)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and agents use this skill to collect product, market, platform, and seed keyword details and request structured SEO keyword reports for listing placement across Amazon, Shopify, and TikTok Shop.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product, market, platform, and keyword inputs are sent to the Yufluent cloud service.

Mitigation: Use the skill only with data approved for that service and avoid including confidential product plans or customer data in prompts.

Risk: Generated SEO keyword recommendations may be incomplete, misleading, or unsuitable for a specific marketplace policy.

Mitigation: Review the report against seller analytics, advertising search terms, platform rules, and product facts before publishing listing changes.

Risk: The skill requires a Yufluent TOKENAPI_KEY.

Mitigation: Store the token in an environment variable or managed secret store, keep it out of shared artifacts, and rotate it if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/metahuan/skills/yufluentcn-seo-pro)
- [Yufluent SEO Pro homepage](https://www.changzhiai.com/skills/seo-pro)
- [OpenClaw integration](https://claw.changzhiai.com/app/openclaw)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Structured JSON report, optionally saved to a file, with concise guidance for human review.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TOKENAPI_KEY and sends product, market, platform, and keyword inputs to the Yufluent cloud service.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

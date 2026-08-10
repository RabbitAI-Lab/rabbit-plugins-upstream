## Description:

Manages Amazon Ads Sponsored Products, Sponsored Brands, and Sponsored Display entities by listing, creating, and updating campaigns, ad groups, ads, keywords, targets, product ads, creatives, negative criteria, and budget rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and advertising operators use this skill to manage Amazon Ads account entities across Sponsored Products, Sponsored Brands, and Sponsored Display. It supports account-specific profile selection, entity lookup, and controlled create or update operations that can affect campaign state and spend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create and update actions can change live Amazon Ads campaign state, bids, budgets, and related entities.

Mitigation: Require an explicit confirmation summary before create or update operations unless the user has already authorized automatic execution for the task.

Risk: The skill handles API keys, account login flows, phone-based onboarding, and billing or payment steps.

Mitigation: Install only in a dedicated workspace and proceed only when the user is comfortable with LinkFox handling those flows.

Risk: Full API responses are saved persistently under the workspace and may contain sensitive advertising account data.

Mitigation: Review saved linkfox response files for sensitive data and limit workspace access to users who should see the account information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-ads-manager)
- [Amazon Ads manager API overview](references/api.md)
- [Sponsored Products API reference](references/api/sp.md)
- [Sponsored Brands API reference](references/api/sb.md)
- [Sponsored Display API reference](references/api/sd.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples; scripts return JSON responses and save response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query results include entity metadata, pagination summaries, and saved response-file paths when output is large.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

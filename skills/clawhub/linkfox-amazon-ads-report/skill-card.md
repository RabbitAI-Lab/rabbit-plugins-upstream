## Description:

Retrieves Amazon Ads reports for Sponsored Products, Sponsored Brands, and Sponsored Display by guiding report selection and running scripts that create, wait for, download, and unpack structured report data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and advertising analysts use this skill to pull Amazon Ads performance reports for campaigns, keywords, search terms, advertised products, purchased products, ad groups, invalid traffic, and Prompt ad extensions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox and Amazon Ads credentials to retrieve account reports.

Mitigation: Install only when this access is intended, keep API keys protected, and confirm the selected Amazon Ads profile before running report requests.

Risk: Report results, session data, and QR artifacts may be stored locally.

Mitigation: Review where outputs are written and delete stored report, session, or QR files when they are no longer needed.

Risk: Extracted reports may be exposed through a temporary localhost URL.

Mitigation: Disable localhost serving for sensitive reports when possible and treat generated file paths and URLs as sensitive.

Risk: Endpoint override environment variables can redirect requests.

Mitigation: Avoid endpoint overrides unless the destination is controlled and trusted.

Risk: The onboarding flow includes phone-login and payment-related steps.

Mitigation: Review login and payment prompts carefully before entering codes or completing billing actions.

## Reference(s):

- [Amazon Ads report API reference](references/api.md)
- [Amazon Ads report type index](references/report-types/index.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Amazon Ads Reporting v3 report types](https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-ads-report)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; script output is JSON or summarized JSON with local file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full responses under ./linkfox/<date>/<session>/data and may expose extracted reports through a temporary localhost URL.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Generates AI-powered Amazon keyword market opportunity reports covering market potential, product characteristics, user reviews, customer profiles, search trends, and pricing analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and cross-border e-commerce operators use this skill to generate keyword-level market opportunity reports for product selection and market entry decisions. It is intended for decision support, not continuous monitoring.

### Deployment Geography for Use:

Global use; Amazon marketplace coverage is currently limited to the United States.

## Known Risks and Mitigations:

Risk: The skill requires LinkFox API credentials and may guide phone/SMS login for setup.

Mitigation: Review the skill before installing, prefer self-service API-key setup when possible, and only provide credentials or phone verification when comfortable with the LinkFox flow.

Risk: Billing and payment-order flows may be used when credits are insufficient.

Mitigation: Confirm the selected plan, payment method, QR code, and order details before paying.

Risk: Saved response and cache files may contain sensitive business research.

Mitigation: Clean up saved LinkFox response and cache files when they include sensitive keywords, reports, or business context.

Risk: Endpoint environment variables can redirect LinkFox service calls.

Mitigation: Avoid overriding LinkFox endpoint environment variables unless the target endpoint is trusted.

## Reference(s):

- [亚马逊商业洞察报告 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-opportunity-report-by-keyword)

## Skill Output:

**Output Type(s):** [markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown report content returned in JSON responses, with saved JSON files and optional shell command guidance for authentication or billing flows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are point-in-time snapshots for the US Amazon marketplace; large responses may be summarized while the full response is saved locally.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

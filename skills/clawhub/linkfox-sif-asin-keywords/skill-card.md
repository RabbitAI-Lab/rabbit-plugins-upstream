## Description:

Queries LinkFox SIF data for a single Amazon ASIN and helps an agent present traffic keywords, organic and ad rankings, search volume, traffic share, click concentration, conversion markers, and weekly or monthly time windows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and e-commerce analysts use this skill to retrieve and summarize the keywords that drive traffic to a specific ASIN. It supports single-ASIN reverse keyword lookup, ranking checks, ad keyword analysis, traffic-share review, and period-based keyword comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ASIN query data is sent to LinkFox for paid keyword lookup.

Mitigation: Use only ASIN and keyword-filter data that the user is comfortable sharing with LinkFox, and explain credit consumption before repeated calls.

Risk: The skill includes account setup and API-key retrieval flows that may involve phone numbers, SMS codes, and credentials.

Mitigation: Prefer LinkFox self-service login and API-key retrieval, avoid sharing SMS codes in chat, and store the resulting API key only in environment variables.

Risk: Billing flows can list plans and create payment orders.

Mitigation: Have the user review the selected plan, payment method, price, and generated order before paying; do not continue paid actions without user confirmation.

Risk: Full API responses may be saved locally under linkfox directories.

Mitigation: Treat saved response files as potentially sensitive commercial data and delete or protect them according to the user's retention policy.

## Reference(s):

- [SIF-ASIN keyword API reference](references/api.md)
- [LinkFox authentication and billing onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-asin-keywords)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON API parameters, shell commands, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries one ASIN per request, supports 13 Amazon marketplaces, uses a 24-hour local cache for identical parameters, and consumes 9 LinkFox credits per lookup.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

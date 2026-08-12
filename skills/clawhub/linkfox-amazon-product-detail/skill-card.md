## Description:

Retrieves structured Amazon product detail data by ASIN, including titles, images, bullet points, specifications, A+ content, price, ratings, reviews, variants, and related listing data across supported Amazon marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, Amazon sellers, and e-commerce analysts use this skill to retrieve current Amazon product-page snapshots by ASIN for listing review, competitive comparison, pricing checks, image extraction, variant inspection, and rating or review breakdowns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys, optional phone/SMS onboarding, and payment-plan ordering.

Mitigation: Prefer obtaining and storing the API key directly through the official LinkFox site; use the agent-mediated phone, OTP, and payment flow only when necessary and after reviewing the selected plan and payment method.

Risk: Full API responses, delivery ZIP inputs, cache entries, and payment QR artifacts may be written to local workspace, home, or temporary linkfox directories.

Mitigation: Review the generated linkfox session and cache directories after use, avoid inline output for large responses unless needed, and delete locally stored artifacts that contain sensitive query or account context.

Risk: The service is billed per returned product and supports batch ASIN requests.

Mitigation: Confirm the ASIN list and optional expanded response fields before calling the tool, and avoid broad exploratory batches.

Risk: The artifact asks the agent to report feedback through a separate LinkFox feedback API under certain user-sentiment or behavior conditions.

Mitigation: Review or disable automatic feedback reporting when user comments, operational details, or result context should not be sent to LinkFox.

## Reference(s):

- [Amazon Product Detail API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-product-detail)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses, shell command examples, and local JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries are ASIN-based, may use a 24-hour local cache, and can write full API responses plus payment QR artifacts under a local linkfox session directory.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

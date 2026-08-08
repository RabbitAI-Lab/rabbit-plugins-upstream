## Description:

Fetches and analyzes Amazon product reviews by ASIN across 15 marketplaces with star, keyword, reviewer, media, format, and sort filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace analysts, and agent users use this skill to retrieve Amazon buyer reviews for one ASIN at a time and summarize customer sentiment, complaints, praise, and product-improvement signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys, phone-number/SMS login flows, and payment-order handling.

Mitigation: Use it only when LinkFox is trusted for those account and billing flows; prefer completing registration and billing on the official LinkFox site when possible.

Risk: Endpoint-related environment variables can redirect the service calls.

Mitigation: Verify LinkFox endpoint environment variables before use and avoid running the skill with untrusted environment configuration.

Risk: Full review responses and QR artifacts may be written under local linkfox directories, including fallback locations.

Mitigation: Review and manage local linkfox output directories, and avoid querying or retaining sensitive review-analysis data longer than needed.

Risk: Review retrieval consumes LinkFox credits and may become costly when fetching many reviews.

Mitigation: Confirm the target ASIN, marketplace, star counts, and expected credit cost with the user before additional retrieval attempts.

## Reference(s):

- [Amazon Reviews API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-reviews-list)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and locally saved JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large responses are summarized in stdout while full responses are saved under linkfox session directories; the --inline option can print full JSON.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps agents query and present LinkFox SIF traffic keyword data for a single Amazon ASIN, including organic rank, ad rank, search volume, traffic share, click concentration, conversion rate, and weekly or monthly time windows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and agents use this skill to reverse-look up the traffic keywords associated with a specific Amazon ASIN and present the resulting ranking, search-volume, traffic-share, and conversion fields. It is intended for one-ASIN-at-a-time keyword analysis rather than broad keyword research, listing copywriting, sales estimation, or ad campaign management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends ASIN queries, API credentials, session metadata, and optional feedback reports to LinkFox-controlled services.

Mitigation: Install and use it only when LinkFox is an approved third-party service for the user's ecommerce data; avoid endpoint override environment variables unless the destination is trusted.

Risk: Authentication, phone-login, billing, payment-order, and QR-code workflows may expose account or payment recovery data during onboarding.

Mitigation: Use the onboarding flow only when necessary, review the returned order and payment details before continuing, and avoid sharing API keys or verification codes outside the active setup task.

Risk: Full LinkFox API responses and generated QR files may be written to local session directories and can contain sensitive business or account data.

Mitigation: Review saved LinkFox files before sharing a workspace and periodically remove response or QR files that are no longer needed.

Risk: Each SIF ASIN keyword lookup consumes LinkFox credits, and repeated pagination or changed parameters can add cost.

Mitigation: Use the built-in cache when possible and confirm with the user before making additional billable calls, especially after failures, empty results, or pagination.

## Reference(s):

- [SIF-ASIN Keyword API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-asin-keywords)
- [LinkFox Publisher Profile](https://clawhub.ai/user/linkfox-ai)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON API parameters, shell commands, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries one ASIN at a time; API responses are cached for 24 hours and full responses are saved under a LinkFox session data directory.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

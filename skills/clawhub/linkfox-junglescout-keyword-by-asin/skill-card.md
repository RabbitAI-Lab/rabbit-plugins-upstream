## Description:

Queries Jungle Scout-style keyword data for up to 10 Amazon ASINs, including search volume, competition, ranking, relevancy, and PPC bid metrics across supported Amazon marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, ecommerce analysts, and agent users use this skill to reverse lookup Amazon ASIN keywords, compare competitor keyword exposure, and inspect search volume, ranking, competition, and advertising bid signals. The skill is intended for LinkFox/Jungle Scout API workflows that may consume paid credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid remote LinkFox/Jungle Scout service and API calls can consume credits.

Mitigation: Confirm expected credit use, plan choice, and any additional paid lookup before running or retrying requests.

Risk: Onboarding can involve phone/SMS login, API-key generation, payment ordering, and payment QR output.

Mitigation: Prefer self-service API key setup through the first-party site; do not provide phone numbers, SMS codes, or approve payment orders through an agent unless explicitly intended.

Risk: Full lookup results, cache files, session metadata, and payment QR images may be written under a local linkfox directory.

Mitigation: Review and clean local linkfox data directories when outputs may contain sensitive product, account, or payment context.

Risk: Automatic feedback reporting can create an additional data-sharing path.

Mitigation: Make feedback reporting opt-in or remove it before deployment where user consent or data minimization requirements apply.

## Reference(s):

- [Jungle Scout ASIN Keyword API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-keyword-by-asin)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses saved to local files, and shell/configuration guidance for authentication and billing flows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are persisted under a local linkfox directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

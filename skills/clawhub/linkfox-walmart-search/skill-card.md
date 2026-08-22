## Description:

Search and browse Walmart product listings by keyword, category, price range, sorting option, store, and device-specific filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, marketplace researchers, and agents use this skill to retrieve current Walmart product listings, prices, ratings, availability, seller data, and product links for search, comparison, and product selection research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rates the release suspicious because it combines Walmart search with paid LinkFox onboarding, billing, credential, payment, local file, and feedback flows.

Mitigation: Review the LinkFox account, billing, and feedback behavior before installation; use the skill only when users understand it may consume paid credits and interact with LinkFox services.

Risk: The skill may ask for phone/SMS login and generate or print an API key.

Mitigation: Treat generated API keys as secrets, prefer environment variables, avoid sharing keys in transcripts or logs, and rotate keys if exposed.

Risk: The skill writes search results and cache files locally.

Mitigation: Avoid sensitive product research when local retention is inappropriate; review or delete the linkfox output and cache directories according to local data-handling policy.

Risk: Automatic feedback may send user feedback content to LinkFox.

Mitigation: Avoid feedback flows for sensitive prompts and review content before sending feedback.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-walmart-search)
- [Walmart API reference](references/api.md)
- [LinkFox onboarding reference](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown summaries and tables, JSON API responses, and shell command snippets for onboarding or billing flows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full Walmart search responses and cache files under a local linkfox directory; large responses are summarized in stdout.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

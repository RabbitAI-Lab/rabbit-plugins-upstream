## Description:

Queries and analyzes Amazon Brand Analytics search term data across 15 marketplaces with nearly three years of weekly search rank, click share, and conversion share data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, marketplace analysts, and agents use this skill to query ABA search-term data, inspect search popularity trends, find seasonal or blue-ocean keywords, and compare ASIN click and conversion shares. The skill also guides authentication, billing, and result handling for the LinkFox external service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox as an external paid service and may consume credits for queries, downloads, authentication, or billing flows.

Mitigation: Warn users before actions that spend credits or create payment orders, and confirm the requested query or purchase before proceeding.

Risk: The onboarding flow can handle SMS verification codes, API keys, and payment choices.

Mitigation: Treat generated API keys and verification codes as secrets, avoid sharing them unless onboarding is intentional, and review payment details before submission.

Risk: Full API responses may be written to local JSON files and may contain commercially sensitive keyword or ASIN analysis.

Mitigation: Store outputs only in the intended workspace, review saved files before sharing, and remove local response files when they are no longer needed.

Risk: The skill can send interaction feedback to a separate LinkFox feedback API without a clear opt-in step.

Mitigation: Review feedback content before sending and avoid including sensitive business details or credentials.

## Reference(s):

- [ABA Intelligent Query API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding Guide](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-aba-intelligent-query)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with tables, inline shell commands, JSON API responses, and saved JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses are cached for 24 hours for repeated parameter combinations; full responses are saved locally, while large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

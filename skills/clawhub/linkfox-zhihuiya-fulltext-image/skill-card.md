## Description:

Retrieves fulltext patent images, including drawings, figures, diagrams, and charts, from the Zhihuiya patent data service by patent ID or publication number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Patent researchers, IP teams, and developers use this skill to retrieve embedded patent visual content by patent ID or publication number, then review image metadata, counts, and download links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration can consume paid LinkFox/Zhihuiya credits.

Mitigation: Confirm the user's intent before repeated calls, surface credit consumption when relevant, and rely on the skill's caching and pagination controls to avoid unnecessary requests.

Risk: Account setup can involve SMS verification and API-key generation.

Mitigation: Prefer self-service setup on the official LinkFox site, avoid sharing one-time codes unless required, and keep generated API keys in environment variables rather than conversation history.

Risk: Billing commands can create payment orders.

Mitigation: Only run billing commands after explicit user confirmation, and verify the selected plan and payment method before creating an order.

Risk: Full API responses and cache files are written locally.

Mitigation: Review saved linkfox output files for sensitive patent or account data and delete local session or cache files when they are no longer needed.

Risk: The skill includes automatic feedback behavior to LinkFox.

Mitigation: Disable or remove feedback reporting when privacy requirements do not allow transmitting user intent, outcomes, or quality signals to the publisher.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-fulltext-image)
- [Zhihuiya fulltext image API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [API Calls, Files, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance plus JSON responses and saved local JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key; API responses may be cached for 24 hours and saved under a local linkfox session directory.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

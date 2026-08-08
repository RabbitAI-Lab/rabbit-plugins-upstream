## Description:

Retrieves full-text image metadata, including drawings, figures, diagrams, and download paths, from Zhihuiya patent documents by patent ID or publication number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Patent researchers, engineers, and agents use this skill to list and retrieve visual content from a specified patent document by patent ID or publication number. It helps inspect drawings, figures, diagrams, image categories, and image download paths returned by the Zhihuiya service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawHub security evidence marks this release suspicious because it fetches patent images and also includes account login, API-key generation, payment order creation, automatic feedback reporting, and broad local saving.

Mitigation: Install only after reviewing the LinkFox endpoints and scripts; invoke registration, onboarding, order, or payment commands only after explicit user consent.

Risk: Patent queries, API keys, account login data, phone/SMS onboarding data, and payment-flow data may be handled by LinkFox services.

Mitigation: Use dedicated credentials, avoid sending sensitive patent queries unnecessarily, and keep LINKFOX_* endpoint environment variables locked to trusted values.

Risk: The skill saves full responses and cache files in local linkfox directories.

Mitigation: Run it from an appropriate project workspace and remove generated linkfox data or cache files when they are no longer needed.

## Reference(s):

- [智慧芽-全文附图 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-fulltext-image)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries, JSON API responses, and shell commands for authentication or billing setup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under local linkfox session data directories; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

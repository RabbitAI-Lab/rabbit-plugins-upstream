## Description:

Fetches a Google AI Mode or AI Overview result for one search keyword and returns the generated answer with source links as Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to request current Google AI Overview summaries for single-query web research, technical questions, product research, and consumer preference analysis. It is suited to live web summarization when the user wants synthesized Markdown with citations rather than raw search results or structured datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends search queries and account or session metadata to LinkFox service endpoints.

Mitigation: Use it only for queries that are appropriate to share with the third-party service, and avoid sensitive personal, credential, or confidential business content.

Risk: The helper scripts persist full responses and cache data under a local linkfox directory.

Mitigation: Review local output paths and retention expectations before use, and clean stored response files when they contain sensitive research context.

Risk: The skill includes login, billing, and payment onboarding flows.

Mitigation: Confirm the user intends to authenticate or purchase credits before running onboarding or payment commands, and follow the service's account and payment terms.

Risk: The skill can report feedback to LinkFox when user satisfaction or issues are detected.

Mitigation: Do not submit feedback containing user content or task details unless the user has consented.

Risk: AI Overview output may be incomplete, unavailable for a keyword, or change between calls.

Mitigation: Preserve source links, tell users when no AI Overview is returned, and avoid presenting live summaries as stable or independently verified facts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-ai-mode-google-search)
- [Publisher Profile](https://clawhub.ai/user/linkfox-ai)
- [API Reference](references/api.md)
- [Onboarding and Billing Guide](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown answer text with citation links, plus JSON command output and locally persisted JSON response files when the helper scripts run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single keyword per call; live Google AI Mode results may vary, some queries may not trigger an AI Overview, and successful calls can consume LinkFox credits.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

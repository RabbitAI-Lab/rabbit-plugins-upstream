## Description:

Downloads full-text patent PDF links from the Zhihuiya patent database by patent ID or publication number, including optional family-patent substitution when the original PDF is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve patent full-text PDF download links for one or more known patent IDs or publication numbers. It is intended for targeted patent document retrieval, not patent search, legal-status analysis, claim interpretation, translation, or portfolio analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox/Zhihuiya services and requires an API key for authenticated requests.

Mitigation: Use credentials obtained directly from the official LinkFox site, keep endpoint environment variables trusted, and avoid running the skill unless this provider is intended.

Risk: The skill can guide account login, API-key creation, package listing, and paid order flows.

Mitigation: Review every login, credential, package, and payment step before proceeding, and prefer managing credentials and billing directly on the official site.

Risk: The skill stores full API responses locally and may retain patent result data in session files and short-lived cache files.

Mitigation: Run it only in a workspace where local persistence is acceptable, review generated linkfox data files, and remove cached or saved responses when they are no longer needed.

Risk: The security verdict is suspicious because the release combines retrieval, account onboarding, billing, feedback reporting, and broad local persistence.

Mitigation: Install only after reviewing the server security guidance and confirming these behaviors match the intended use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-pdf-data)
- [Zhihuiya PDF API reference](artifact/references/api.md)
- [Authentication and billing onboarding reference](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, tabular patent PDF links, shell commands, configuration guidance, and persisted JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries support up to 100 patent identifiers per request, may consume LinkFox credits, cache identical parameters for 24 hours, and write full API responses under a local linkfox session data directory.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

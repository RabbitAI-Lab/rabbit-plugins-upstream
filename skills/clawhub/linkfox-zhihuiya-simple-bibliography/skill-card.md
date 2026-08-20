## Description:

Queries simple bibliographic patent metadata from the Zhihuiya patent database by patent ID or publication/grant number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to retrieve structured front-page patent metadata, including titles, abstracts, applicants, inventors, classification codes, filing dates, priorities, and citations for known patent identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles API keys and may guide optional account login, API-key generation, billing, and order flows.

Mitigation: Use only trusted LinkFox/Zhihuiya endpoints, prefer completing login and payment through the official site, and avoid sharing phone numbers or one-time codes through the skill unless the user explicitly chooses that path.

Risk: Patent queries and returned metadata are persisted to local result files and may reveal sensitive research or business interests.

Mitigation: Run the skill only in an appropriate workspace, review saved files before sharing them, and remove local results when they are no longer needed.

Risk: Requests consume LinkFox/Zhihuiya credits and batch queries can consume many credits at once.

Mitigation: Confirm the identifiers and expected cost before additional lookups, especially for batch requests or retries after empty results.

Risk: Gateway URL environment variables can change where API requests are sent.

Mitigation: Ensure gateway-related environment variables point only to trusted LinkFox hosts before running the scripts.

## Reference(s):

- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-simple-bibliography)

## Skill Output:

**Output Type(s):** [text, markdown, JSON files, shell commands, configuration guidance]

**Output Format:** [Markdown summaries or tables for users, with full API responses saved as JSON files and optionally printed to stdout.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts up to 100 patent IDs or publication/grant numbers per request; identical parameters may be cached for 24 hours.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

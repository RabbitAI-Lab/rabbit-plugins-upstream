## Description:

Analyzes Amazon keyword traffic sources for competitor ASINs, including organic search, Sponsored Products ads, brand ads, video ads, recommendation placements, ASIN filters, and date-window filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace analysts, and agent users use this skill to query LinkFox keyword traffic data and summarize which ASINs receive traffic from organic search, paid ads, and Amazon recommendation placements for a selected keyword.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts LinkFox services and can be configured to use custom LinkFox endpoint environment variables.

Mitigation: Use the default LinkFox endpoints or only custom endpoints that the user controls and trusts.

Risk: The skill uses or helps create a LinkFox API key and includes account onboarding flows.

Mitigation: Keep API keys in environment variables, restart the agent session after changes, and do not share SMS codes unless the user intentionally initiated the login flow.

Risk: The skill can guide paid credit purchases and each keyword traffic query consumes credits.

Mitigation: Confirm user intent before payment or repeated credit-consuming calls, especially when changing filters, pages, keywords, or marketplaces.

Risk: The skill saves full API responses locally, which may include product and query result data.

Mitigation: Review the saved linkfox session data path before sharing artifacts and avoid storing results in unintended workspaces.

## Reference(s):

- [SIF keyword traffic API reference](references/api.md)
- [Authentication and credits onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses saved to local files, and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a local linkfox session data directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

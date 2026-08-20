## Description:

Searches the live web, retrieves current online content, and extracts page text from top results for direct summarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill when they need live web search, current news, community discussions, reviews, trend lookup, or real-time fact checking. It sends a keyword query to the LinkFox search API and returns extracted result content for the agent to summarize with source titles and URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, session/app metadata, and feedback content are sent to LinkFox services.

Mitigation: Review LinkFox terms before installation and avoid sending sensitive, regulated, or confidential queries unless the data sharing is acceptable.

Risk: The onboarding flow can handle phone-code login, API-key issuance, and payment-related choices.

Mitigation: Prefer obtaining API keys and completing payments directly on LinkFox's official site; use the agent onboarding path only when the user explicitly chooses it.

Risk: Search responses are cached and saved locally as JSON, which can preserve query results and extracted page content.

Mitigation: Review and clean the local LinkFox output/cache directories when searches include sensitive topics or when sharing the workspace.

Risk: The skill consumes paid credits and may incur unexpected costs during frequent use.

Mitigation: Confirm expected credit use with the user before repeated searches or broad research tasks.

## Reference(s):

- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tsearch-search)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON search results and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts one keyword string up to 1000 characters; full search responses may be saved as JSON files and cached locally.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

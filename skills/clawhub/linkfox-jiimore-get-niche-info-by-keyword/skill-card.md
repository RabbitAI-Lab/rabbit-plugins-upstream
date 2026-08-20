## Description:

This skill queries Jiimore Amazon niche-market data by keyword to help sellers assess competition, brand concentration, demand, pricing, advertising costs, and launch opportunity across supported marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, ecommerce operators, and market researchers use this skill to inspect keyword-level niche segments, compare competitive concentration, and evaluate demand signals before deciding whether to fetch or interpret paid LinkFox data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keyword queries and related session metadata are sent to LinkFox services.

Mitigation: Use only queries appropriate for external processing and avoid submitting sensitive business terms unless LinkFox handling is acceptable.

Risk: Full API responses are saved locally and may include market research data from paid calls.

Mitigation: Review the local linkfox session directory, apply normal data-retention controls, and avoid sharing saved response files unintentionally.

Risk: The skill can guide account login, API key retrieval, and paid credit purchase flows.

Mitigation: Obtain and store API keys deliberately, review any payment order before scanning a QR code, and avoid sharing SMS codes unless intentionally using the onboarding path.

Risk: Feedback may be sent externally without a separate prompt.

Mitigation: Review feedback behavior before installation and avoid including sensitive user context in feedback content.

## Reference(s):

- [Jiimore API reference](artifact/references/api.md)
- [Authentication and credit onboarding](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-get-niche-info-by-keyword)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, saved local JSON files, and shell commands for API and onboarding workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries require a keyword; responses may be cached for 24 hours and full API responses are saved locally under a linkfox session directory.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

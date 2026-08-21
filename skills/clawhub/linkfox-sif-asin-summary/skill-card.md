## Description:

Analyzes Amazon ASIN traffic source composition and exposure distribution using LinkFox SIF data, including current and previous period comparisons and entered or exited keyword changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce analysts use this skill to query LinkFox SIF data for ASIN traffic-source, exposure-channel, ad-channel, recommendation-source, and period-over-period keyword comparisons across supported Amazon marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ASIN analysis inputs and session metadata are sent to LinkFox services.

Mitigation: Use only data approved for LinkFox processing and confirm the user is comfortable with external API calls before querying.

Risk: The skill includes LinkFox account onboarding, phone/SMS code handling, API key generation, and billing/payment flows.

Mitigation: Run onboarding or payment commands only when the user intends to create or access a LinkFox account, and treat returned API keys as secrets.

Risk: Automatic feedback reporting can send feedback content to an external LinkFox endpoint.

Mitigation: Disable feedback reporting or make it explicitly opt-in before using the skill in sensitive workflows.

Risk: Full API responses and cached results are stored locally under linkfox session directories.

Mitigation: Run the skill in an approved workspace and review or purge stored response and cache files when they may contain sensitive business data.

Risk: Queries consume LinkFox credits and may trigger billing decisions.

Mitigation: Tell the user when a query will spend credits and ask before repeated calls, retries with changed parameters, or paid plan selection.

## Reference(s):

- [SIF-ASIN Traffic Source API Reference](references/api.md)
- [Authentication and Credits Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-asin-summary)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, JSON, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, saved local JSON files, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses to a local linkfox session directory, uses a 24-hour cache by default, prints small responses inline, and summarizes larger responses unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

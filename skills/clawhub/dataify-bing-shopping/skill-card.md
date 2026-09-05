## Description:

Search Bing Shopping for products and shopping results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Bing Shopping for product results through Dataify, with optional market, country, offset, filter, cache, and output-format controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopping searches, locale, country, offset, and filter values are sent to Dataify during live lookups.

Mitigation: Use the skill only when sharing those query details with Dataify is acceptable, and avoid sensitive shopping searches.

Risk: Live calls require a Dataify API token in the agent environment.

Mitigation: Prefer a session-scoped DATAIFY_API_TOKEN and never paste the token into chat or persist it unless that is intentional.

## Reference(s):

- [Dataify Bing Shopping API Reference](artifact/references/api.md)
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-bing-shopping)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls]

**Output Format:** [Concise Markdown summaries, parameter previews, shell commands, or raw JSON/HTML when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses DATAIFY_API_TOKEN for live calls and defaults to compact product result summaries.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Realtime creator/content enrichment across TikTok, Instagram, YouTube, and Facebook for freshness-critical profile, media, video, page, and post lookups during active campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

External users and campaign analysts use this skill to fetch fresh social creator, profile, media, video, page, and post data and turn it into delta-focused campaign guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creator, post, keyword, and engagement lookup requests are sent to an external API gateway.

Mitigation: Use the skill only for explicit realtime enrichment tasks and avoid submitting unnecessary or sensitive identifiers.

Risk: API credentials can be exposed if stored or shared incorrectly.

Mitigation: Keep SCRUMBALL_API_KEY in a private secret store or protected .env file and do not commit .env files.

Risk: Free quota exhaustion can interrupt enrichment workflows.

Mitigation: When quota is exhausted, configure a user-owned SCRUMBALL_API_KEY before continuing.

## Reference(s):

- [API Index](references/api-index.md)
- [Request and Response Guide](references/request-response.md)
- [Operation Manifest](references/operations.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries with inline shell commands and API-result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns freshness, key deltas, decision impact, and recommended next steps.]

## Skill Version(s):

1.0.2 (source: server release metadata and config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

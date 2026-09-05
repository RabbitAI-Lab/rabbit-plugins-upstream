## Description:

Search Google Local for nearby businesses and local results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run user-directed Google Local searches for nearby businesses, local pack results, and location-scoped business discovery through Dataify.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact states that the skill should not be used for known Place ID or detailed map records, while the implementation accepts Google CID/place-record lookup parameters.

Mitigation: Deploy with policy or review controls that restrict use to broad, user-directed Google Local search queries and block known place/CID lookup requests unless explicitly approved.

Risk: Live requests require a Dataify API token and may consume account credits.

Mitigation: Use dry-run or parameter preview modes before execution when scope or cost is unclear, and rely on environment-based token configuration without exposing the token in chat or logs.

## Reference(s):

- [Dataify Google Local API](references/google_local_api.md)
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-google-local)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown summaries, shell command examples, parameter previews, or raw JSON/HTML when explicitly requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Dataify API token for live API calls; dry-run and parameter preview modes can run without submitting a request.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

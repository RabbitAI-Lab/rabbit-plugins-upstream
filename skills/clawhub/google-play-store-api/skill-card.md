## Description:

Search Google Play, read full Android app listings including install counts and Data safety details, and page reviews by cursor using Scavio's structured JSON API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and app research teams use this skill to search Android apps, inspect Google Play listings, compare competitors, and retrieve paginated review data for ASO and marketplace analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed if SCAVIO_API_KEY is copied into source files or shared logs.

Mitigation: Keep SCAVIO_API_KEY out of source control and expose only that required credential to the runtime.

Risk: Installing the optional SDK directly into a shared environment can broaden dependency exposure.

Mitigation: Prefer the direct HTTPS examples or install the SDK in an isolated environment.

Risk: Review crawling can consume paid credits quickly because each Google Play endpoint call costs 2 credits.

Mitigation: Budget before multi-page crawls and avoid calling the reviews endpoint when the app listing's included reviews are sufficient.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-play-store-api)
- [Scavio Google Play Search documentation](https://scavio.dev/docs/google-play-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-play-store-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-play-store-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API descriptions and Python, JavaScript, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses use structured JSON envelopes and Google Play endpoints cost 2 credits per call.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

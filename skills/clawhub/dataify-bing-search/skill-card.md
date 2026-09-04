## Description:

Searches Bing web results through Dataify and returns structured results for an agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to turn a natural-language search request into a Dataify Bing Search API call and receive compact result summaries, source links, or requested raw JSON/HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A debug endpoint override can send the Dataify bearer token to an arbitrary URL if used with an untrusted destination.

Mitigation: Use the default Dataify endpoint for normal searches and allow --url only for trusted debugging.

Risk: Tokens passed directly on a command line can be exposed through shell history or process listings.

Mitigation: Configure DATAIFY_API_TOKEN in the environment and avoid --token for normal use.

Risk: Persistent shell setup can expose credentials if copied into shared profiles, logs, or screenshots.

Mitigation: Review shell-specific setup before making persistent changes and prefer session-scoped configuration when appropriate.

## Reference(s):

- [Dataify Bing Search API Reference](references/api.md)
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-bing-search)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries by default; raw JSON or HTML when explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Dataify API token for live calls; dry-run and parameter preview modes can run without network submission.]

## Skill Version(s):

1.3.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

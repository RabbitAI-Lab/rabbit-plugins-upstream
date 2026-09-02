## Description:

Search with Google AI Mode when the user explicitly requests AI Mode or AI-generated Google search results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run explicit Google AI Mode searches through Dataify and receive compact, source-preserving search results or requested raw JSON/HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, location, language, and output parameters are sent to Dataify.

Mitigation: Use the skill only when the user explicitly requests Google AI Mode results and is comfortable sending those parameters to Dataify.

Risk: API usage consumes Dataify credits.

Mitigation: Confirm materially higher-cost scopes before execution and rely on concise, single-query requests when possible.

Risk: Token exposure can occur if credentials are passed on the command line or stored persistently without care.

Mitigation: Configure the Dataify token with an environment variable, avoid printing the token, and use session-scoped shell setup when appropriate.

## Reference(s):

- [Dataify Google AI Mode API Reference](artifact/references/google_ai_mode_api.md)
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-google-ai-mode)
- [Dataify Scraper API Endpoint](https://scraperapi.dataify.com/request)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with optional JSON, HTML, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Submits form-encoded Google AI Mode requests with a required query, default JSON output mode, optional location, country, language, cache, and UULE parameters.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

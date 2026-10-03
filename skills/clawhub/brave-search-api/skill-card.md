## Description:

Helps agents search the web, images, news, and videos through Brave Search using a managed Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask an agent to retrieve Brave Search results for web pages, images, news, or videos, and configure explicitly approved search automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hosted functions, triggers, and destinations can create persistent automation or forward sensitive data.

Mitigation: Get separate, explicit approval for each automation and destination; narrow the event scope and forward only necessary data.

Risk: Raw HTTP requests using MATON_API_KEY may expose a long-lived credential.

Mitigation: Prefer managed login; protect the key and avoid including it in output, logs, or destination settings.

Risk: Location headers can transmit sensitive location data.

Mitigation: Only include location information when the user needs and approves location-aware search.

## Reference(s):

- [Brave Search API Documentation](https://api-dashboard.search.brave.com/documentation)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton](https://maton.ai)
- [Brave Search on ClawHub](https://clawhub.ai/byungkyu/skills/brave-search-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with search results and optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the user's authorized connection and selected search options.]

## Skill Version(s):

1.2.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

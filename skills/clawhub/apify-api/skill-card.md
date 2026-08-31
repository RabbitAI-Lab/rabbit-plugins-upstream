## Description:

Apify API integration with managed authentication for running web scrapers, managing actors, datasets, key-value stores, and schedules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent interact with Apify through Maton for web scraping workflows, actor and task runs, storage resources, schedules, and webhooks. It is suited to account-scoped API work where reads are preferred first and writes require user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate an Apify account through Maton, including write operations that create, modify, or delete resources.

Mitigation: Default to read and list calls, verify the target account and resource identifiers, and require explicit user confirmation before POST, PUT, PATCH, or DELETE requests.

Risk: Actor runs can consume Apify compute units and may create cost exposure.

Mitigation: Review expected inputs, scale, and cost impact with the user before starting actor or task runs.

Risk: Schedules and webhooks are persistent resources that can continue operating after the agent session ends.

Mitigation: Confirm the intended lifecycle before creating or modifying schedules and webhooks, and review existing persistent resources before changes.

Risk: API keys and provider-issued tokens can leak through logs, command arguments, files, or broad environment exposure.

Mitigation: Prefer OAuth via the Maton CLI, avoid printing or persisting secrets, feed raw HTTP credentials through stdin only when the CLI is unavailable, and rotate any exposed key.

Risk: External content returned by Apify may contain untrusted instructions or data.

Mitigation: Treat API responses as data, do not execute or follow instructions embedded in returned content, and pass external values as discrete arguments rather than interpolated shell text.

## Reference(s):

- [Apify API Reference](https://docs.apify.com/api/v2)
- [Apify Actors Documentation](https://docs.apify.com/actors)
- [Apify Storage Documentation](https://docs.apify.com/storage)
- [Apify Schedules Documentation](https://docs.apify.com/schedules)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton](https://maton.ai)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/apify-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for agent-mediated Maton CLI or SDK workflows and may include Apify resource identifiers, status summaries, and API payloads.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

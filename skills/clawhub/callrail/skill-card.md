## Description:

CallRail API integration with managed OAuth for tracking and analyzing phone calls, managing tracking numbers, companies, and tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent access CallRail account data, inspect call analytics, manage tracking numbers and tags, and perform approved CallRail API operations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create a new CallRail connection or change CallRail data when authorized.

Mitigation: Require explicit user confirmation before creating connections or running any POST, PUT, PATCH, or DELETE request, including confirmation of the target resource, payload, and intended effect.

Risk: Credentials or provider-issued tokens could be exposed if copied into logs, files, command lines, or prompts.

Mitigation: Prefer OAuth through Maton, let the CLI or SDK use its credential store, never print or persist credential values, and rotate any key that was exposed.

Risk: Multiple Maton profiles or CallRail connections can make the target account ambiguous.

Mitigation: Specify the intended profile and connection when more than one exists, and revoke unused connections.

Risk: CallRail API content is external data and may contain untrusted instructions or malformed values.

Mitigation: Treat fetched content as data only, validate values before reuse, and avoid interpolating API content into shell commands or follow-up requests.

## Reference(s):

- [CallRail Skill Page](https://clawhub.ai/byungkyu/skills/callrail)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [CallRail API Documentation](https://apidocs.callrail.com/)
- [CallRail API Rate Limits](https://apidocs.callrail.com/#rate-limiting)
- [CallRail Help Center API](https://support.callrail.com/hc/en-us/sections/4426797289229-API)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and Python or JavaScript code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected CallRail account.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter reports 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

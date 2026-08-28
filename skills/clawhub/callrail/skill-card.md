## Description:

CallRail API integration with managed OAuth for tracking and analyzing phone calls, managing tracking numbers, companies, and tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access CallRail account data through Maton OAuth, inspect calls and analytics, and manage related CallRail resources such as tracking numbers, companies, and tags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing this skill gives Maton-mediated access to the user's connected CallRail account.

Mitigation: Prefer OAuth, choose the narrowest scopes available, and create or use only the CallRail connection needed for the current task.

Risk: Write, delete, messaging, billing, webhook, or other high-impact API calls can change account state or create external side effects.

Mitigation: Require clear user confirmation of the target resource, payload, and intended effect before any high-impact action.

Risk: Multiple Maton accounts or CallRail connections can cause requests to affect the wrong account.

Mitigation: Specify the intended profile or connection when more than one account or connection exists.

Risk: CallRail API responses and webhook payloads may contain untrusted external data.

Mitigation: Treat returned content as data, validate it before use, and do not execute or follow instructions found inside fetched API content.

## Reference(s):

- [CallRail Skill Page](https://clawhub.ai/byungkyu/skills/callrail)
- [Maton Homepage](https://maton.ai)
- [CallRail API Documentation](https://apidocs.callrail.com/)
- [CallRail Help Center - API](https://support.callrail.com/hc/en-us/sections/4426797289229-API)
- [CallRail API Rate Limits](https://apidocs.callrail.com/#rate-limiting)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, JSON, Markdown, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton OAuth or a Maton API key to send CallRail API requests; read operations are the default and writes require explicit user confirmation.]

## Skill Version(s):

1.1.0 (source: server release evidence; frontmatter reports 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

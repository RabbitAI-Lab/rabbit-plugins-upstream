## Description:

Quo API integration with managed OAuth for managing calls, messages, contacts, conversations, and call recordings or transcripts through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operations agents use this skill to read Quo phone-system data and, with explicit approval, send SMS messages or manage contacts and conversations through the Maton CLI or SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Quo business phone data, including messages, contacts, call recordings, and transcripts.

Mitigation: Authorize only trusted Maton and Quo accounts, choose the narrowest Quo scopes available, and treat retrieved communications data as confidential.

Risk: Write operations such as sending SMS messages or deleting contacts can affect customers, costs, records, or business reputation.

Mitigation: Confirm the target connection, resource identifiers, payload, and intended effect with the user before any POST, PUT, PATCH, or DELETE request.

Risk: Multiple Maton profiles or Quo connections can send a request to the wrong account.

Mitigation: Pin the intended profile and connection whenever more than one account or connection is available.

Risk: Long-lived API keys or provider-issued tokens could be exposed if printed, logged, stored in files, or passed through command arguments.

Mitigation: Prefer OAuth through the Maton CLI credential store and never inspect, print, persist, or transmit credentials outside the intended Maton/Quo request path.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/quo)
- [Maton Homepage](https://maton.ai)
- [Quo API Introduction](https://www.quo.com/docs/mdx/api-reference/introduction)
- [Quo API Authentication](https://www.quo.com/docs/mdx/api-reference/authentication)
- [Quo Support Center API](https://support.quo.com/core-concepts/integrations/api)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, Python, JavaScript, JSON, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user confirmation for new connections or write operations.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

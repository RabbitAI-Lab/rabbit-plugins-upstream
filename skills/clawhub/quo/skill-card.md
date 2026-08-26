## Description:

Quo API integration with managed OAuth for managing calls, messages, contacts, conversations, call recordings, and transcripts for a business phone system.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Quo phone-system data through Maton, including listing calls and messages, managing contacts, sending SMS, and retrieving call recordings or transcripts. It is intended for connected Quo accounts where the user can approve account connections and data-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may send messages or modify Quo contacts, conversations, or related phone-system data without sufficient confirmation.

Mitigation: Confirm recipients, payloads, target resources, and target connections before any POST, PUT, PATCH, or DELETE request; default to read and list calls first.

Risk: The agent may connect or act against the wrong Quo account when multiple Maton profiles or Quo connections exist.

Mitigation: Confirm the intended account and use explicit connection or profile selection when more than one option is available.

Risk: Credentials or scoped provider tokens may be exposed if copied into logs, files, command arguments, or prompts.

Mitigation: Prefer OAuth, keep credentials in the managed credential store, avoid printing or persisting tokens, and use the narrowest Quo scopes available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/quo)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Quo API Introduction](https://www.quo.com/docs/mdx/api-reference/introduction)
- [Quo API Authentication](https://www.quo.com/docs/mdx/api-reference/authentication)
- [Quo Support Center API Integration](https://support.quo.com/core-concepts/integrations/api)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require network access, a Maton account, and an authorized Quo connection.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

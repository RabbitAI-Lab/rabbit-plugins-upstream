## Description:

Quo API integration with managed OAuth for managing business phone calls, messages, contacts, conversations, recordings, transcripts, and approved automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to connect an agent to a Quo account through Maton so it can read phone data, send SMS with approval, manage contacts, retrieve recordings or transcripts, and configure approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Quo business phone data, including calls, messages, contacts, recordings, and transcripts.

Mitigation: Authorize only the Quo account needed for the task, prefer OAuth, select the narrowest available scopes, and avoid storing raw responses unless the user explicitly asks.

Risk: Write actions such as SMS sends, contact changes, connection changes, and deletions can affect customers or business records.

Mitigation: Require explicit user approval before every write and confirm the target resource, payload, and intended effect.

Risk: Webhooks, triggers, functions, and destinations can create persistent automation or forwarding of private call and message data.

Mitigation: Create automation only after the user approves the destination, data flow, persistence, and ownership of any external URL; prefer platform-hosted destinations where appropriate.

Risk: API keys or credentials may be exposed if copied into environment variables, logs, command lines, or trigger destination templates.

Mitigation: Prefer OAuth and operating-system credential storage, never place Maton or provider credentials in destination headers or bodies, and rotate any key that was exposed.

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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and Node.js examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes approval gates for writes, account connections, hosted functions, triggers, and persistent forwarding.]

## Skill Version(s):

1.2.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

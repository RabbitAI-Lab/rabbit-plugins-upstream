## Description:

Basecamp API integration with managed OAuth for managing projects, to-dos, messages, schedules, documents, and team collaboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to Basecamp through Maton, inspect Basecamp resources, and perform approved project, to-do, message, schedule, document, and collaboration actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton mediates access to the user's Basecamp account.

Mitigation: Confirm the user trusts Maton for the Basecamp account before installation or connection, and prefer OAuth over API keys.

Risk: Write or delete operations can change Basecamp projects, to-dos, messages, schedules, documents, or collaboration state.

Mitigation: Default to read and list calls, then require explicit user approval for every POST, PUT, PATCH, or DELETE request with the target and payload reviewed first.

Risk: Long-lived Maton API keys can be exposed through environment variables, logs, shell history, or persisted files.

Mitigation: Use OAuth and the operating system credential store when possible; if an API key is required, never print or persist it and rotate it if exposed.

Risk: Multiple Maton profiles or Basecamp connections can route actions to the wrong account.

Mitigation: Specify the intended profile and connection when more than one account or connection is available.

## Reference(s):

- [Basecamp 4 API Documentation](https://github.com/basecamp/bc3-api)
- [Basecamp Authentication Guide](https://github.com/basecamp/bc3-api/blob/master/sections/authentication.md)
- [Basecamp API Reference](https://github.com/basecamp/bc3-api#endpoints)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected Basecamp account.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

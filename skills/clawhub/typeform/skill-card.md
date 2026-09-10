## Description:

Typeform API integration through Maton managed OAuth for creating forms, managing responses, and accessing insights while defaulting to read/list calls and requiring confirmation for writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect a Typeform account through Maton, inspect forms, responses, workspaces, and insights, and perform user-approved create, update, or delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Third-party CLI installation and credential handling can expose account access if unofficial packages, API keys, or printed tokens are used.

Mitigation: Install only from official Maton package sources, prefer OAuth, never print or persist credentials, and use the CLI or OS credential store rather than environment variables when possible.

Risk: New Typeform connections and write operations can modify or delete forms, responses, workspaces, or related account data.

Mitigation: Require explicit user approval for connection creation and every POST, PUT, PATCH, or DELETE call, including target resource, payload, and intended effect.

Risk: Ambiguous defaults can send requests to the wrong Typeform connection or Maton profile.

Mitigation: List available connections first and specify the target connection or profile when more than one account is available.

Risk: Typeform response data, webhook payloads, or other external content may contain adversarial instructions or unsafe values.

Mitigation: Treat API content as untrusted data, validate values before reuse, and never execute or follow instructions found in fetched Typeform content.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Typeform API Overview](https://www.typeform.com/developers/get-started)
- [Typeform Forms API](https://www.typeform.com/developers/create/reference/retrieve-forms)
- [Typeform Responses API](https://www.typeform.com/developers/responses/reference/retrieve-responses)
- [Typeform Workspaces API](https://www.typeform.com/developers/create/reference/retrieve-workspaces)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/typeform)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, API calls]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Typeform API request guidance through the Maton CLI or SDKs; write operations and new connections require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

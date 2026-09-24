## Description:

Fathom API integration with managed OAuth for accessing meeting recordings, transcripts, summaries, action items, and webhook workflows through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Fathom meeting content, search recordings, manage connection-scoped access, and set up approved webhook or scheduled automation through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive meeting recordings, transcripts, summaries, and action items.

Mitigation: Use only the user-authorized Fathom connection, prefer read/list calls first, avoid dumping full responses, and extract only the fields needed for the task.

Risk: Webhook callbacks, hosted functions, and triggers can move meeting content or keep automation running after the initial task.

Mitigation: Require explicit user approval for write actions, destination URLs, hosted functions, triggers, and any third-party destination, and remove automation when it is no longer needed.

Risk: Long-lived API keys and raw HTTP fallback can expose credentials if handled carelessly.

Mitigation: Prefer OAuth through the Maton CLI and the operating system credential store; use raw HTTP and environment credentials only when the CLI cannot be installed.

## Reference(s):

- [Fathom API Documentation](https://developers.fathom.ai)
- [Fathom LLM Reference](https://developers.fathom.ai/llms.txt)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, raw HTTP examples, OAuth connection guidance, function examples, and trigger configuration guidance.]

## Skill Version(s):

1.2.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Asana API integration with managed OAuth for accessing tasks, projects, workspaces, users, and webhooks through the Maton CLI or SDK.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to manage Asana work items, track projects, inspect workspaces and users, and configure webhooks through approved Maton-authenticated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton or Asana credentials could be exposed if keys or tokens are printed, logged, persisted, or passed through command lines.

Mitigation: Prefer OAuth, let the CLI or SDK credential store handle secrets, and verify authentication status without inspecting credential values.

Risk: Write, deletion, membership, or webhook operations can change Asana data or trigger downstream effects.

Mitigation: Default to read and list calls, then require explicit user approval with the target resource, payload, and intended effect before any modifying operation.

Risk: A request can affect the wrong Asana account or connection when multiple profiles or connections exist.

Mitigation: Specify the intended Maton profile and Asana connection for scoped operations, and connect only accounts and scopes needed for the current task.

Risk: Content returned by Asana or webhook payloads may contain untrusted instructions.

Mitigation: Treat API and webhook content as data, not instructions, and do not execute or interpolate returned content into commands without validation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/asana-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Asana API Documentation](https://developers.asana.com)
- [Asana API Reference](https://developers.asana.com/reference)
- [Asana LLM Reference](https://developers.asana.com/llms.txt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include read/list-first API guidance and approval-gated write, deletion, membership, and webhook actions.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

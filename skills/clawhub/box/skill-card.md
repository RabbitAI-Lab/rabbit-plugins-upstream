## Description:

Box API integration with managed OAuth for managing files, folders, collaborations, and cloud storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to a user-authorized Box account through Maton and perform file, folder, sharing, collaboration, and webhook workflows. It is best suited for Box tasks where read/list operations are preferred by default and write actions are confirmed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Box access depends on OAuth authorization and may expose files, folders, collaborations, and other account data allowed by the connected scopes.

Mitigation: Use OAuth where possible, choose the narrowest Box scopes available, specify the intended connection when multiple connections exist, and avoid exposing credentials or raw sensitive responses.

Risk: The Maton API passthrough can reach endpoints beyond the examples when the authorized connection permits them.

Mitigation: Treat the documented endpoints as the intended surface, default to read and list operations, and require explicit approval before creating, sharing, modifying, deleting, or registering webhooks.

Risk: Unpinned CLI or SDK installation can change behavior over time.

Mitigation: Verify that the Maton CLI or SDK source is trusted before installation and review version changes before use in controlled environments.

## Reference(s):

- [Box API Reference](https://developer.box.com/reference)
- [Box Developer Documentation](https://developer.box.com/guides)
- [Box Authentication Guide](https://developer.box.com/guides/authentication)
- [Box SDKs](https://developer.box.com/sdks-and-tools)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/box)
- [ClawHub Publisher Profile](https://clawhub.ai/user/byungkyu)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and an authorized Box connection.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

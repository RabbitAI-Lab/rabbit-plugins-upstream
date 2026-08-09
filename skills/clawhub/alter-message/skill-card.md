## Description:

~Alter Message lets an agent send markdown direct messages to another ~handle, read and manage its own inbox, and control message permissions and conversation channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[true-alter](https://clawhub.ai/user/true-alter)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to interact with the ~alter messaging service through authenticated MCP tools for direct messaging, inbox review, permission grants and revocations, message redaction, and channel management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can send messages or change messaging permissions using the authenticated ~alter identity.

Mitigation: Review message content, recipients, grants, revocations, and mute or rename actions before the agent submits changes.

Risk: The skill requires an ALTER_API_KEY that grants access to the user's own ~alter messaging surfaces.

Mitigation: Install only when this access is intended, store the key securely, and avoid sharing or fabricating credentials.

## Reference(s):

- [~Alter Message ClawHub listing](https://clawhub.ai/true-alter/skills/alter-message)
- [~alter MCP endpoint](https://mcp.truealter.com/api/v1/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, API calls]

**Output Format:** [Markdown with JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated ALTER_API_KEY and user review before sending messages or changing message permissions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

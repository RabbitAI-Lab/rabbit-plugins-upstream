## Description:

Guides agents through IdentyClaw Passport API sessions, HOLA peer authentication, DID resolution, and agent discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[identyclaw](https://clawhub.ai/user/identyclaw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to authenticate to home and federated APIs, create and verify HOLA handshake lines, and look up Passport identities, DIDs, and agent discovery details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated remote peers could trigger task execution through collaboration envelopes without local authorization.

Mitigation: Do not execute envelope tasks automatically; require sender and task-type allowlists, strict schemas, least-privilege tools, and human approval for sensitive actions.

Risk: Passport keys, JWTs, webhook URLs, and sensitive identity metadata could be exposed.

Mitigation: Keep credentials on the Gateway, avoid sharing them in chat or logs, and minimize collection and logging of identity metadata.

## Reference(s):

- [IdentyClaw API documentation](https://api.identyclaw.com/docs)
- [API reference](references/api-reference.md)
- [Login and authentication](references/login-authentication.md)
- [HOLA authentication](references/hola-agent-authentication.md)
- [Collaboration envelope](references/collaboration-envelope.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Protected API workflows require an IdentyClaw Passport; agent-to-agent messaging uses a separate plugin.]

## Skill Version(s):

1.9.4 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

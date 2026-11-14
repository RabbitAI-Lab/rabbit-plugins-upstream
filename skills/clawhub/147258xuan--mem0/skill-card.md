## Description:

MEM0 API external memory for agents — store, search, list, and delete agent memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[147258xuan](https://clawhub.ai/user/147258xuan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to persist text memories across sessions and to add, list, semantically search, retrieve, or delete them through the Mem0 API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment marks this release suspicious because scanners report an embedded credential that may expose a shared memory service and an endpoint setting that could redirect requests. Inspection was partial and did not establish whether the credential is active or what permissions it has.

Mitigation: Do not rely on the embedded credential. Configure a token you own through MEM0_TOKEN, verify its permissions, and confirm MEM0_BASE points to the trusted HTTPS Mem0 API before sending data.

## Reference(s):

- [Mem0](https://mem0.ai)
- [Mem0 API](https://api.mem0.ai/v1/)
- [ClawHub mem0 release](https://clawhub.ai/147258xuan/skills/mem0)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text]

**Output Format:** [JSON API responses and memory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates, retrieves, and deletes memories in the configured Mem0 account.]

## Skill Version(s):

0.1.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

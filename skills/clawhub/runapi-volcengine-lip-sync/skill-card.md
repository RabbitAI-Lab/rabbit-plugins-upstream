## Description:

Generate lip-sync video with Volcengine Lip Sync through RunAPI for source video and audio track synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate lip-sync videos through RunAPI, using the CLI for one-off tasks or SDK packages for application and backend integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video and audio inputs may be sent to the external RunAPI service for processing.

Mitigation: Use only inputs appropriate for the external service and authenticate with RUNAPI_API_KEY or explicit RunAPI CLI configuration.

Risk: Generated file URLs are temporary and should not be treated as durable storage.

Mitigation: Download generated outputs promptly and store needed files in durable user-controlled storage.

Risk: Using the CLI as a production integration layer can create brittle application behavior.

Mitigation: Use the documented SDK integration path for application, backend, worker, or production workflow integrations.

## Reference(s):

- [RunAPI Volcengine Lip Sync](https://runapi.ai/models/volcengine-lip-sync)
- [Model overview, pricing, and rate limits](https://runapi.ai/models/volcengine-lip-sync.md)
- [Provider comparison](https://runapi.ai/providers/bytedance.md)
- [Full model catalog](https://runapi.ai/models.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown with inline shell commands, JSON request examples, and SDK package guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce RunAPI CLI commands, SDK package selections, request JSON, authentication guidance, and temporary generated-file handling guidance.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

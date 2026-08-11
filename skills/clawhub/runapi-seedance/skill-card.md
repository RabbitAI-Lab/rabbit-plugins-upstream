## Description:

Generate and edit video with Seedance through RunAPI, using the RunAPI CLI for one-off tasks and SDKs for application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to create or transform video with Seedance through RunAPI. It supports one-off CLI generation and SDK-based application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using this skill may send prompts or media-generation requests to RunAPI and may store a RunAPI token in CLI configuration.

Mitigation: Confirm trust in the RunAPI CLI before installation, prefer RUNAPI_API_KEY for headless use, and avoid submitting sensitive prompts or media unless that use is approved.

Risk: RunAPI-generated file URLs are temporary and should not be treated as long-term assets.

Mitigation: Download generated media and store it in durable storage within 7 days.

## Reference(s):

- [RunAPI Seedance model overview](https://runapi.ai/models/seedance.md)
- [RunAPI Seedance homepage](https://runapi.ai/models/seedance)
- [ByteDance provider comparison](https://runapi.ai/providers/bytedance.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-seedance)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands and SDK package names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to use the CLI for one-off generation, SDKs for production integration, and durable storage for generated media.]

## Skill Version(s):

0.2.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

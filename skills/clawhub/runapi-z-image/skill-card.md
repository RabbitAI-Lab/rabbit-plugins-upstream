## Description:

Generate and edit images with Z-Image through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, edit, or transform images with Z-Image through RunAPI, using the CLI for one-off tasks and SDKs for application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on RunAPI services, API-key or saved CLI authentication, and a Homebrew-installed CLI or SDKs.

Mitigation: Confirm RunAPI account access and authentication before use, and review RunAPI pricing and data handling for the intended workflow.

Risk: Generated file URLs are temporary and should not be treated as durable assets.

Mitigation: Download generated files and store them in durable storage within the documented retention window.

Risk: Using the CLI as a production integration layer can create fragile application behavior.

Mitigation: Use the documented SDK integration path for apps, backends, workers, and production codebases.

## Reference(s):

- [RunAPI Z-Image model overview](https://runapi.ai/models/z-image.md)
- [RunAPI Z-Image homepage](https://runapi.ai/models/z-image)
- [RunAPI Alibaba provider page](https://runapi.ai/providers/alibaba.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-z-image)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and SDK package names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide use of the RunAPI CLI, SDKs, API key authentication, and durable storage for generated image files.]

## Skill Version(s):

0.2.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

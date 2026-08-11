## Description:

Create, edit, transition, and extend PixVerse V6 videos through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, edit, transition, and extend PixVerse V6 videos through RunAPI. It guides one-off CLI use and SDK-based application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on RunAPI and the runapi-ai Homebrew tap for CLI installation.

Mitigation: Confirm you trust RunAPI and the Homebrew tap before installing or running the CLI.

Risk: RunAPI authentication may use an API key.

Mitigation: Use a scoped RunAPI API key where possible and prefer environment auth or saved CLI config for headless runs.

Risk: Generated video URLs are temporary.

Mitigation: Download and store generated videos in durable storage within 7 days when outputs need to be retained.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-pixverse)
- [RunAPI PixVerse Homepage](https://runapi.ai/models/pixverse)
- [Model Overview, Pricing, and Rate Limits](https://runapi.ai/models/pixverse.md)
- [PixVerse V6 Model Details](https://runapi.ai/models/pixverse/pixverse-v6.md)
- [Provider Comparison](https://runapi.ai/providers/pixverse.md)
- [Full Model Catalog](https://runapi.ai/models.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, SDK package names, and request-file examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce RunAPI CLI commands, SDK integration guidance, authentication setup notes, and instructions to download generated video URLs within 7 days.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Uses Nano Banana 2 through AI Hive to replace product or subject image backgrounds for channel-specific scenes while preserving the authorized subject, product facts, and camera perspective.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and commerce content teams use this skill to create channel-specific product and background variants from approved reference images. It helps track scene, lighting, safe-zone, and prohibited-claim constraints while generating AI Hive image-editing commands and outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected reference images and prompts are sent to AI Hive for processing.

Mitigation: Use only images and prompts that are approved for upload to the configured AI Hive service, and avoid private or sensitive material unless that transfer is acceptable.

Risk: The AI Hive API key may be stored locally for command-line use.

Mitigation: Prefer environment variables for temporary use or ensure the local configuration file remains restricted to the current user.

Risk: Generated images can imply unsupported product claims, partnerships, locations, or performance characteristics.

Mitigation: Review generated backgrounds before publication and remove variants that suggest unverified claims or unauthorized brand, person, or location usage.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/nano-banana-2-background-replace)
- [Publisher Profile](https://clawhub.ai/user/wubin1836)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed Nano Banana 2 image model through AI Hive; generated files are saved to the configured output directory, defaulting to Downloads/AiHive.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

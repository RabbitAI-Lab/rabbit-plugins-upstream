## Description:

sn-image-base is a non-user-facing base-layer skill for SenseNova-Skills that provides low-level APIs for image generation, image editing, image recognition, and text optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this base-layer skill to call configured image generation, image editing, vision-language recognition, and text optimization services from upper-layer SenseNova-Skills workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send prompts, images, and API keys to remote model providers.

Mitigation: Use approved providers and HTTPS endpoints, review agent configuration and .env files before use, and avoid sensitive or regulated image and text inputs unless approved.

Risk: Custom endpoints and disabled TLS verification can expose requests or credentials to untrusted services.

Mitigation: Use trusted HTTPS base URLs, keep TLS verification enabled, and avoid the --insecure option except in controlled test environments.

Risk: The Nano Banana image path disables provider safety thresholds by default.

Mitigation: Use that provider path only when the use case and content controls have been reviewed, and prefer provider safety settings appropriate to the deployment.

Risk: Production use with unpinned dependencies can introduce supply-chain or compatibility drift.

Mitigation: Pin and review dependencies before deployment.

## Reference(s):

- [API Specification](references/api_spec.md)
- [SenseNova-Skills Project Repository](https://github.com/OpenSenseNova/SenseNova-Skills)
- [SenseNova Platform](https://platform.sensenova.cn/)
- [SenseNova Token Plan](https://platform.sensenova.cn/token-plan)
- [ClawHub Skill Page](https://clawhub.ai/sensenova-skills/skills/sn-image-base)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Plain text or JSON status objects; image commands save generated or edited image files to disk.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include image file paths, task IDs, model and endpoint metadata, elapsed time, and error details.]

## Skill Version(s):

2026.9.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

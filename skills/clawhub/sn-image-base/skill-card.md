## Description:

Base-layer skill for the SenseNova-Skills project, providing low-level APIs for image generation, image recognition with VLMs, and text optimization with LLMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and upper-layer agent skills use this base skill to call configurable image generation, image recognition, and text optimization backends. It is intended as infrastructure rather than a direct user-facing workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill forwards prompts, local image inputs, file-based prompts, endpoint settings, and API keys to configured model providers.

Mitigation: Install only when calling skills control those inputs and avoid sending sensitive content to external providers.

Risk: The image generation command supports disabling TLS verification with --insecure.

Mitigation: Do not use --insecure outside controlled debugging environments.

Risk: One image backend disables several Nano Banana safety settings.

Mitigation: Review or remove the safetySettings override before enabling that backend.

Risk: The security verdict is suspicious because the skill forwards local inputs to configurable providers and disables safety filtering for one backend.

Mitigation: Pin and audit dependencies, scan the release before deployment, and restrict which upper-layer skills can invoke it.

## Reference(s):

- [sn-image-base API Specification](references/api_spec.md)
- [SenseNova-Skills project](https://github.com/OpenSenseNova/SenseNova-Skills)
- [SenseNova Platform](https://platform.sensenova.cn/)
- [SenseNova Token Plan](https://platform.sensenova.cn/token-plan)

## Skill Output:

**Output Type(s):** [text, json, code, shell commands, configuration, files, guidance]

**Output Format:** [Plain text or JSON status objects; image generation can also produce a saved image file path.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [JSON responses include status and elapsed_seconds; recognition and text optimization may include model, base_url, and interface_type.]

## Skill Version(s):

2026.8.19 (source: server release metadata); package 0.1.0 (source: scripts/pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

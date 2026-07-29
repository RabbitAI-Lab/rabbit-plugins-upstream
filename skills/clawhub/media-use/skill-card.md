## Description: <br>
Agent Media OS for HyperFrames projects that resolves, generates, transforms, caches, and reuses BGM, SFX, images, icons, logos, voiceovers, captions, color grades, LUTs, and other media assets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and media-producing agents use this skill to resolve, generate, transform, cache, and reuse assets such as BGM, SFX, images, icons, logos, voiceovers, captions, color grades, LUTs, and media treatments for HyperFrames projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote media providers and local credential or profile reads may expose provider-sensitive work. <br>
Mitigation: Use --local-only for provider-sensitive work and install or authenticate only the providers required for the task. <br>
Risk: Reusable .media and ~/.media caches can carry asset descriptions or reuse candidates across projects. <br>
Mitigation: Avoid confidential client prompts in global reuse workflows and review reuse candidates before importing assets into a project. <br>
Risk: Coarse telemetry may be linked to an authenticated account. <br>
Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 when account-linked telemetry is not acceptable. <br>
Risk: Runtime installs and detached jobs can make media generation harder to audit before completion. <br>
Mitigation: Run the documented doctor or preflight checks first, review provider choices before execution, and wait for detached background music jobs before assembling final media. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/media-use) <br>
- [Setup and providers](artifact/references/setup-providers.md) <br>
- [Resolve](artifact/references/resolve.md) <br>
- [Audio](artifact/references/audio.md) <br>
- [Media treatments](artifact/references/media-treatments.md) <br>
- [Operations](artifact/references/operations.md) <br>
- [Grading](artifact/references/grading.md) <br>
- [Telemetry and privacy](artifact/references/meta.md) <br>
- [HeyGen CLI documentation](https://developers.heygen.com/cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance, inline shell commands, JSON output, local media files, and reusable asset records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write project .media assets and manifests, reuse the global ~/.media cache, and call configured local or cloud media providers.] <br>

## Skill Version(s): <br>
1.0.35 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

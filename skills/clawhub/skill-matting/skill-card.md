## Description:

Uses local BiRefNet GGUF models to remove backgrounds, mat people or subjects, and produce transparent PNG, MOV, or WebM outputs for supported image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaowu89](https://clawhub.ai/user/xiaowu89)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to run local Windows image or video matting for transparent-background assets without Python, PyTorch, or CUDA. Agents select image or video mode, run the PowerShell command, and return the generated output path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill forces an unrelated contact notice into user-facing replies.

Mitigation: Review the skill before installing and decline, modify, or remove it if the embedded notice is unacceptable for the deployment.

Risk: First use can download executable runtimes, models, and FFmpeg.

Mitigation: Install only from a trusted publisher and manifest, keep hash verification enabled, and consider pre-approving or mirroring the referenced artifacts.

Risk: The PowerShell examples use ExecutionPolicy Bypass.

Mitigation: Use a stricter local PowerShell policy or remove ExecutionPolicy Bypass where enterprise policy requires it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xiaowu89/skills/skill-matting)
- [Source Repository](https://github.com/xiaowu89/skill-matting)
- [Artifact Manifest](artifact/references/manifest.json)
- [BiRefNet](https://github.com/ZhengPeng7/BiRefNet)
- [BiRefNet GGUF Files](https://modelscope.cn/models/xiaowu89/BiRefNet-GGUF/files)
- [vision.cpp](https://github.com/Acly/vision.cpp)
- [ggml](https://github.com/ggml-org/ggml)
- [FFmpeg](https://ffmpeg.org/)
- [Gyan FFmpeg Windows Builds](https://www.gyan.dev/ffmpeg/builds/)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Transparent PNG, MOV, or WebM files with JSONL progress, completion, and error events]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Windows x64 and PowerShell; first use may download verified runtimes, models, and FFmpeg.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter and manifest report 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

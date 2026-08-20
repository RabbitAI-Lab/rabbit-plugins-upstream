## Description:

通过 qhkit CLI（npm @iqinghu/qhkit）根据商品信息快速生成广告视频素材，适用于信息流广告、品牌推广及社交媒体营销，支持多条量产。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing operators use this skill to generate batches of e-commerce video ad assets for feed ads, brand promotion, and social media campaigns through the qhkit CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade Node/qhkit software automatically.

Mitigation: Require explicit user approval before installation or upgrade, and prefer preinstalled pinned versions of Node and qhkit.

Risk: The skill can reuse stored qhkit/OpenClaw credentials for external job submission.

Mitigation: Confirm the intended account and avoid exposing tokens or credential file contents in agent output.

Risk: Local media files may be uploaded to an external video generation service.

Mitigation: Confirm that selected files are intended for upload before running generation commands.

Risk: Video generation can spend service credits.

Mitigation: Run an estimate first when supported and require explicit user confirmation before paid generate calls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-video-ad-assets)
- [@iqinghu/qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit CLI commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Underlying qhkit calls return JSON task status, credit usage, and generated video URLs.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

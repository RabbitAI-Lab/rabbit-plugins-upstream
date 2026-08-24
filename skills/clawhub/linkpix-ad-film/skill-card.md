## Description:

快速生成电影级商品广告视频：基于物理渲染的光影场景、细腻画面质感，适合品牌宣传与高端商品展示。当用户要求做广告大片、品牌宣传片、电影感商品视频、高级感 TVC 时必须触发。关键词：LinkPix、qhkit、广告大片、品牌大片、TVC、宣传片、电影级视频、质感视频、商品广告、品牌质感、高端视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare and submit LinkPix/qhkit video generation jobs for cinematic product advertisements, brand films, and premium TVC-style product showcases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node/npm tooling and the qhkit CLI.

Mitigation: Run it in a controlled environment and review package installation or upgrade commands before execution.

Risk: Product media can be uploaded to LinkPix/qinghu services.

Mitigation: Use only media that is approved for the service and suitable for external processing.

Risk: Video generation can spend service credits after confirmation.

Mitigation: Require the estimate and key generation parameters to be reviewed before submitting a paid generation task.

Risk: The skill may request an API key during setup.

Mitigation: Use a platform secret store, environment variable, or local qhkit config flow instead of pasting API keys into ordinary chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ad-film)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu service](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce task IDs, status summaries, estimates, and final video URLs from the qhkit service.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

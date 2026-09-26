## Description:

This skill guides an agent through Qinghu AI's qhkit CLI to analyze a reference short-video link, rewrite the structure for a user's product, and generate a Kling 3.0-style short video with confirmation, estimation, polling, and delivery steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Short-video operators, editors, and ecommerce sellers use this skill to turn a Douyin, TikTok, Kuaishou, Xiaohongshu, or similar reference link into an analyzed script, a rewritten product-specific script, and a generated promotional short video through qhkit and Qinghu AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to handle a Qinghu API key in chat.

Mitigation: Use a local secret or environment-variable flow such as QHKIT_TOKEN instead of pasting the API key into chat.

Risk: The skill can send video links and uploaded media to qhkit and the Qinghu service.

Mitigation: Use only media the user is authorized to process and avoid sensitive or confidential uploads unless the user accepts that service transfer.

Risk: The artifact includes installation and execution of qhkit through npm without a pinned version, plus optional persistent PATH changes.

Mitigation: Review the package source before installation, prefer trusted package registries, and avoid persistent environment changes unless the package source is trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-kling-3-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes qhkit setup guidance, model-selection checks, task confirmation text, polling instructions, rewritten scripts, task IDs, credit estimates, and video delivery URLs when generation completes.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

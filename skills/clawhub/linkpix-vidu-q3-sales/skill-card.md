## Description:

帮助电商商家、设计师和独立站运营通过青虎AI和 qhkit 使用 Vidu Q3 生成面向商品展示、种草和广告投放的短视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce merchants, designers, and independent-store operators use this skill to turn product images and selling points into short product videos through qhkit video workflows. It guides agents through model lookup, prompt and media parameter selection, credit estimation, task submission, polling, and delivery of generated video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask users for a live API key during setup.

Mitigation: Use a private environment variable or secret store for the API key instead of pasting the secret into chat.

Risk: The setup flow includes broad or unpinned package installation for qhkit and related runtime tools.

Mitigation: Review the package before installation and prefer pinned versions or platform-managed dependencies when possible.

Risk: Video generation creates paid tasks and may consume credits once submitted.

Mitigation: Run an estimate when supported, summarize key parameters, and require explicit user approval before executing a generate command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-vidu-q3-sales)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit CLI JSON commands and video task status or result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit commands for media upload, credit estimation, task submission, polling, and generated video URL delivery.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

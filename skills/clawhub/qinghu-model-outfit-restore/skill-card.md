## Description:

青虎AI 模特换装高一致性还原用于上传模特图和替换衣物图，生成保持人物姿态、光影和衣物细节一致的电商穿搭图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare and run Qinghu AI virtual try-on jobs for model outfit replacement. It guides image input ordering, quoting, confirmation, polling, and delivery of generated outfit images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can send selected model and clothing images to Qinghu AI.

Mitigation: Use only images the user owns or is authorized to process, and get explicit approval before any image upload or paid generate submission.

Risk: The setup path can require global package installation, Node installation, PATH changes, or token/config writes.

Mitigation: Review setup steps before execution and require explicit approval before making environment changes or writing credentials.

Risk: Paid generation consumes Qinghu credits and submitted jobs may not be cancellable.

Mitigation: Run estimate first, present the selected workflow, fields, assets, and expected charge, and wait for clear user confirmation before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-model-outfit-restore)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON parameters]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in generated image URLs after the external workflow completes.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

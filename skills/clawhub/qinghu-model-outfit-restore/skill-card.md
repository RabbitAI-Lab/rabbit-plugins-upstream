## Description:

青虎AI 模特换装高一致性还原 helps an agent submit model and garment images to generate a high-consistency virtual try-on image while preserving pose, lighting, and clothing detail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce teams, and agents use this skill to create virtual try-on or outfit replacement images from a model image and a garment image. It is intended for authorized image assets and requires credit estimation plus explicit user approval before paid generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided model and garment images are uploaded to a remote Qinghu AI workflow.

Mitigation: Use only owned or authorized images and make the remote upload behavior clear before submission.

Risk: Workflow generation can consume paid Qinghu credits.

Mitigation: Run estimate first, report the expected credit use, and wait for explicit user approval before calling generate.

Risk: The skill depends on qhkit, Node setup, and storage or use of a Qinghu API token.

Mitigation: Install qhkit from the documented package source, verify Node downloads when bootstrapping, and store tokens through qhkit config or QHKIT_TOKEN.

Risk: Online workflow fields can change after the documented August 2026 snapshot.

Mitigation: Run the options command and copy returned field labels exactly instead of relying only on the artifact snapshot.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-model-outfit-restore)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON parameters and shell command snippets; completed workflow responses include generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, a Qinghu API token, local or URL image inputs, workflow status polling, and explicit user confirmation before paid generation.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

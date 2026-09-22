## Description:

从零创意生图，也可定向改模特、姿势、搭配；一句描述和可选参考图可生成或修改图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, and developers use this skill to draft image-generation prompts and commands for commercial creative scenes, ecommerce visuals, model changes, pose changes, and outfit edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any reference images may be sent to the selected cloud image provider.

Mitigation: Use only reference images the user owns or has consent to edit, and verify the selected provider and API key before execution.

Risk: Generated image files may overwrite the requested save target.

Mitigation: Use dedicated output paths, review save locations before execution, and use dry-run mode when checking generated commands.

Risk: Generated images can be misused for restricted portrait, minor-safety, or misleading product-experience scenarios.

Mitigation: Follow the skill's stated exclusions, avoid prompts for specific real-person likenesses or inappropriate minor content, and review commercial outputs before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider CLI reference](references/provider-cli.md)
- [banana-pro model flags](references/model-flags.md)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with prompt templates and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local image files when the generated commands are executed with a configured cloud image provider.]

## Skill Version(s):

1.0.12 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

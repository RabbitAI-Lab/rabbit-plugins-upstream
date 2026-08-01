## Description: <br>
为内容设计并生成、质检、上传、嵌入架构图、流程图、信息图和示意图，覆盖提示词设计到最终出图。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content authors, developers, and agents use this skill to turn article image placeholders or direct diagram requests into structured drawing prompts, generated diagrams, quality checks, uploaded image URLs, and article embeds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Article prompts, reference images, and generated diagrams may be sent to selected image providers and uploaded through the configured PicGo host. <br>
Mitigation: Avoid confidential architecture or business diagrams unless upload is disabled or the selected provider, host, and retention expectations are acceptable. <br>
Risk: Generated images can be published externally before per-image approval in the workflow. <br>
Mitigation: Review generation settings and upload behavior before use, and require user confirmation before embedding or adopting generated image URLs. <br>
Risk: Codex-based generation can leave session rollout data under ~/.codex/sessions. <br>
Mitigation: Do not use Codex generation for sensitive diagrams unless local session retention is acceptable or managed separately. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gogoingai/skills/wenqu-image) <br>
- [Publisher profile](https://clawhub.ai/user/gogoingai) <br>
- [Project homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-image) <br>
- [Image generation workflow](references/gen-workflow.md) <br>
- [Image CLI reference](references/image-cli.md) <br>
- [Diagram type selector](references/diagram-type-selector.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown prompts, shell commands, configuration snippets, generated image URLs, and article embed updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call configured image providers and PicGo upload when the workflow reaches image generation.] <br>

## Skill Version(s): <br>
0.1.15 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

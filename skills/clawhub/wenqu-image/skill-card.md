## Description: <br>
Designs, generates, quality-checks, uploads, and embeds AI illustrations for content, including architecture diagrams, flowcharts, infographics, and explanatory visuals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External authors, content teams, and developers use this skill to turn article image placeholders or direct drawing requests into structured image prompts, generated visuals, reviewed image versions, uploaded image URLs, and article Markdown updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may install or use wenqu-cli and PicGo before generating or uploading images. <br>
Mitigation: Confirm the required tools, installation source, and version before execution, and run the documented doctor/check commands before generating images. <br>
Risk: Image providers and upload tools may rely on local credentials or configured uploader accounts. <br>
Mitigation: Keep credentials in local credential files or approved environment configuration, avoid placing secrets in prompts or article files, and verify uploader configuration before upload. <br>
Risk: Generated images can be uploaded to the configured image host and then embedded into article Markdown. <br>
Mitigation: Review generated visuals and destination URLs before adoption, and confirm that uploaded content is appropriate for the target article and host. <br>
Risk: The skill defaults to Chinese labels and style conventions unless the user overrides them. <br>
Mitigation: Specify English, Traditional Chinese, or other language requirements explicitly when the target publication requires them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gogoingai/skills/wenqu-image) <br>
- [OpenClaw Homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-image) <br>
- [Project Repository](https://github.com/gogoingai/wenqu-skills) <br>
- [Image Generation Workflow](references/gen-workflow.md) <br>
- [Diagram Type Selector](references/diagram-type-selector.md) <br>
- [Core Drawing Principles](references/core-principles.md) <br>
- [Design Principles](references/design-principles.md) <br>
- [Diagram Examples](references/diagram-examples.md) <br>
- [Pitfalls](references/pitfalls.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with image-prompt blocks, YAML frontmatter, shell commands, generated image URLs, and article image embeds] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce version history metadata for generated images, provider/model records without credentials, and article-level preference or configuration updates.] <br>

## Skill Version(s): <br>
0.1.19 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

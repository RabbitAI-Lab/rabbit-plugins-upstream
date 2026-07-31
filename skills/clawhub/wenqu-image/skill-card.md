## Description: <br>
文曲·配图 helps agents design, generate, review, upload, and embed diagrams and illustrative images for content workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, technical writers, and agents use this skill to turn article image placeholders or direct drawing requests into structured image prompts, generated diagrams, review notes, upload results, and article embeds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and reference images may be sent to the selected image provider. <br>
Mitigation: Avoid sensitive unpublished content unless the chosen provider is acceptable for that data. <br>
Risk: The skill uses local provider credentials for remote image services. <br>
Mitigation: Keep provider keys only in the documented local .env file and do not paste credentials into prompts or article files. <br>
Risk: Generated images may be uploaded when upload support is enabled. <br>
Mitigation: Review the uploader destination before publishing and use upload only when a public or shared URL is intended. <br>
Risk: Article files may receive generated image metadata and CDN URLs. <br>
Mitigation: Review article changes before publishing, especially version records, provider metadata, and adopted image URLs. <br>
Risk: The workflow can run helper commands to generate, fetch, and publish image assets. <br>
Mitigation: Review the configured provider, command arguments, and upload choice before executing image generation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gogoingai/skills/wenqu-image) <br>
- [OpenClaw homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-image) <br>
- [Generation workflow](references/gen-workflow.md) <br>
- [Image CLI reference](references/image-cli.md) <br>
- [Diagram type selector](references/diagram-type-selector.md) <br>
- [Core drawing principles](references/core-principles.md) <br>
- [Design principles](references/design-principles.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with YAML-frontmatter image prompt blocks, inline shell commands, and optional JSON CLI results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local image file paths and HTTPS image URLs when an image provider and uploader are configured.] <br>

## Skill Version(s): <br>
0.1.12 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

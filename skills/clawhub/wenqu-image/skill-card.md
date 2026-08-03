## Description: <br>
文曲·配图 helps agents design, generate, quality-check, upload, and embed architecture diagrams, flowcharts, infographics, and explanatory images for content workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content authors and developer-facing agents use this skill to turn article image placeholders or diagram requests into complete image prompts, generate and inspect images one at a time, and write the adopted HTTPS image version back into the article. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and generated images may be sent to configured image providers or upload destinations. <br>
Mitigation: Use only approved providers, keep provider keys in the documented local credentials file, and review generated and uploaded content before publishing. <br>
Risk: The workflow may install or update the image CLI and then run local generation, upload, and article-editing commands. <br>
Mitigation: Approve CLI updates deliberately, run the documented doctor check first, and review proposed article changes before accepting them. <br>
Risk: Generated images or image metadata can be embedded into article files after user confirmation. <br>
Mitigation: Confirm each image version, ensure adopted links are HTTPS URLs, and keep rejected or failed local outputs out of published article metadata. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gogoingai/skills/wenqu-image) <br>
- [Project homepage from metadata](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-image) <br>
- [Core image-prompt principles](artifact/references/core-principles.md) <br>
- [Image generation workflow](artifact/references/gen-workflow.md) <br>
- [Diagram type selector](artifact/references/diagram-type-selector.md) <br>
- [Common image-generation pitfalls](artifact/references/pitfalls.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with image prompt code blocks, CLI commands, YAML metadata, and article image links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate, upload, and embed HTTPS image URLs after user confirmation.] <br>

## Skill Version(s): <br>
0.1.17 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

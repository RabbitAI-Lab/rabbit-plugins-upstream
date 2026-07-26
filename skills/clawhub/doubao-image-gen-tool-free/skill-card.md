## Description: <br>
豆包图片生成-免费版 helps an agent collect a text prompt, use Doubao in a browser to generate AI image candidates, preview them for user selection, and save the selected image. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and creators use this skill through an agent to create single-image visual assets from text prompts for personal creative work, social media images, design ideation, and AI drawing practice. The skill is best suited to lightweight generation workflows that involve prompt confirmation, candidate preview, user selection, and local saving. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and generation requests are sent to Doubao through a browser-login account. <br>
Mitigation: Use the skill only when sending those prompts to Doubao is acceptable for the user and organization. <br>
Risk: Generated images are downloaded and copied to a user-selected location, which could be synced, shared, or sensitive. <br>
Mitigation: Review the destination path before copying generated files and avoid sensitive or shared directories unless intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/doubao-image-gen-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance, files] <br>
**Output Format:** [Markdown guidance with optional shell commands and generated image files saved locally] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces preview guidance and saves the user-selected generated image; prompts are sent to Doubao and local save paths should be reviewed before copying files.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Generate or edit AI images via Pixmind API for text-to-image and image-to-image workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fuyunzhishang](https://clawhub.ai/user/fuyunzhishang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to generate new images, edit reference images, create variations, upscale outputs, and poll Pixmind tasks until generated image URLs are available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, generation settings, and reference image URLs are sent to Pixmind. <br>
Mitigation: Use the skill only when Pixmind's terms and data handling are acceptable for the content being generated or edited. <br>
Risk: Confidential, regulated, proprietary, internal, or signed image URLs could be exposed to Pixmind if used as references. <br>
Mitigation: Avoid those inputs unless they are approved for external processing, and prefer non-sensitive reference URLs. <br>
Risk: The skill depends on a Pixmind API key. <br>
Mitigation: Store PIXMIND_API_KEY in the agent environment and avoid placing it in prompts, logs, or shared files. <br>


## Reference(s): <br>
- [Pixmind Image skill page](https://clawhub.ai/fuyunzhishang/skills/pixmind-image) <br>
- [Pixmind homepage](https://www.pixmind.io) <br>
- [Pixmind API keys](https://www.pixmind.io/api-keys) <br>
- [Pixmind image generation endpoint](https://aihub-admin.aimix.pro/open-api/v1/image/generate) <br>
- [Skill source](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Pixmind task IDs, polling status, progress, and generated image URLs.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Generate, edit, and remix images using the Reve AI API for text prompts, image edits, and reference-image remixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dpaluy](https://clawhub.ai/user/dpaluy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creative users use this skill to call Reve AI from an agent workflow to generate images from text, edit an input image, or remix up to six reference images with a prompt. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected input images are sent to Reve AI servers, which can expose sensitive or confidential content. <br>
Mitigation: Use only prompts and images suitable for Reve AI processing; avoid confidential, regulated, or private content unless approved. <br>
Risk: The skill uses a Reve API key and consumes Reve credits. <br>
Mitigation: Use a dedicated, revocable Reve API key and monitor credit usage before and after agent runs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dpaluy/skills/reve-ai) <br>
- [Reve API documentation](https://api.reve.com/console/docs) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [PNG image files plus JSON generation details and Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Bun and REVE_API_KEY or REVE_AI_API_KEY; prompt limit is 2560 characters; remix accepts up to 6 reference images.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

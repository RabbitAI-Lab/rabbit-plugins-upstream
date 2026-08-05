## Description: <br>
Use when someone wants a photo to move like another video - motion transfer, dance remixes, or performance variations from a template clip. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to guide an agent through Pruna video animation workflows that animate a reference image with motion from a source video. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow sends selected images, source videos, prompts, and API key-authenticated requests to Pruna. <br>
Mitigation: Use the skill only when Pruna is an appropriate processor for the media, avoid private or sensitive assets when that is not true, and confirm PRUNA_API_KEY before any API call. <br>
Risk: Optional related-skill installs can expand the agent workflow beyond this single Pruna model guide. <br>
Mitigation: Review each optional related-skill install before accepting it and keep the workflow limited to the user's requested animation task. <br>
Risk: Motion-transfer outputs may imply that the image subject performed motion from another video. <br>
Mitigation: Confirm the source video, reference image, resolution, target frame rate, and any instruction_prompt before submission, and keep prompts narrow to the requested motion transfer. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-animate) <br>
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files) <br>
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline curl commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides authenticated Pruna API upload, prediction, polling, and download workflows for user-provided image and video inputs.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

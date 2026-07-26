## Description: <br>
Generates and edits images through Agnes AI's agnes-image-2.1-flash API for text-to-image and image-to-image requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiuwu2495](https://clawhub.ai/user/jiuwu2495) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent to generate new images or transform input images with Agnes AI for creative design, marketing visuals, product concepts, and social media assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill ships with and can automatically use a hardcoded Agnes API key, creating credential exposure and account-control risk. <br>
Mitigation: Remove and rotate the bundled key before use; require an explicit user-provided or platform-managed key. <br>
Risk: Prompts and input images are sent to a third-party Agnes API for generation or editing. <br>
Mitigation: Disclose the third-party data transfer and avoid sending sensitive prompts or private images unless the user has approved that use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiuwu2495/skills/agnes-image-gen) <br>
- [Agnes AI](https://agnes-ai.com) <br>
- [Agnes image generations API endpoint](https://apihub.agnes-ai.com/v1/images/generations) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell, Python, and JSON snippets; generated image results may be returned as URLs, Base64 data, or saved file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Calls a third-party image generation API and may download generated images to the local workspace.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

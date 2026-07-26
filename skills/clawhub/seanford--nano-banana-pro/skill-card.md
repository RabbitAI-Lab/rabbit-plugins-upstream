## Description: <br>
Generate/edit images with Nano Banana Pro (Gemini 3 Pro Image). Use for image create/modify requests incl. edits. Supports text-to-image + image-to-image; 1K/2K/4K; use --input-image. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate new images or edit existing images through Google's Gemini image API while saving PNG outputs in the user's current working directory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image prompts and selected input images may be sent to Google's Gemini service. <br>
Mitigation: Avoid private, regulated, or confidential images unless that use is acceptable for the deployment context. <br>
Risk: API keys passed in chat or command arguments may be exposed through logs or command history. <br>
Mitigation: Prefer GEMINI_API_KEY over directly pasting a Gemini API key into chat or command arguments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/seanford/skills/nano-banana-pro) <br>


## Skill Output: <br>
**Output Type(s):** [files, shell commands, guidance] <br>
**Output Format:** [PNG image files with text status and saved-path output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports text-to-image and image-to-image workflows with 1K, 2K, or 4K resolution options.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

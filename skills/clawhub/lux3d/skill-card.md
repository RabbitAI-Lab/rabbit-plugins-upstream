## Description: <br>
Lux3D generates 3D models from images or text and performs material repaint through asynchronous Lux3D API workflows for international users. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[violalulu](https://clawhub.ai/user/violalulu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative technical users use this skill to submit image-to-3D, text-to-3D, and material repaint jobs to Lux3D, poll for completion, and download generated 3D model files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys and submitted content can be sent to an unintended endpoint if LUX3D_BASE_URL or --base-url points to an untrusted server. <br>
Mitigation: Use the documented Lux3D endpoint unless an approved trusted endpoint is required, and verify any base URL override before running the skill. <br>
Risk: Prompts, images, model URLs, and API keys are sent to the Lux3D service during generation workflows. <br>
Mitigation: Do not submit confidential or restricted assets unless your organization approves sending that data to Lux3D. <br>


## Reference(s): <br>
- [Lux3D Website](https://lux3d.aholo3d.com/) <br>
- [Lux3D API Key Application](https://labs.aholo3d.com/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell snippets; generated assets download as ZIP, GLB, USDZ, OBJ ZIP, or FBX ZIP files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LUX3D_API_KEY; v3.0-standard is the default Lux3D version; generated download links are valid for 2 hours.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

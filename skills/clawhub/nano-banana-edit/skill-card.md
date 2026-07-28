## Description: <br>
Helps agents edit images with Google Nano Banana 2 on RunComfy by preparing RunComfy CLI invocations for subject-preserving edits, background swaps, localized changes, and batch edits of up to 20 input images. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to route image-editing requests to RunComfy's Nano Banana 2 edit model for identity-preserving edits, background swaps, localized changes, and consistent batch variants. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and image URLs are sent to RunComfy's cloud service. <br>
Mitigation: Use approved, publicly fetchable image URLs and avoid sending sensitive prompts or private images unless the service is approved for that data. <br>
Risk: The skill requires RunComfy authentication through RUNCOMFY_TOKEN or local RunComfy configuration. <br>
Mitigation: Store tokens in approved secret storage, protect local RunComfy configuration, and avoid exposing tokens in shared logs or prompts. <br>
Risk: Optional web search can add external lookup, cost, and latency. <br>
Mitigation: Enable web search only when the user explicitly needs web grounding for the edit request. <br>
Risk: Generated outputs are downloaded to disk and may consume local storage. <br>
Mitigation: Choose an explicit output directory and monitor generated files, especially for high-resolution or multi-output runs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/nano-banana-edit) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=nano-banana-edit) <br>
- [Nano Banana 2 edit endpoint](https://www.runcomfy.com/models/google/nano-banana-2/edit?utm_source=clawhub&utm_medium=skill&utm_campaign=nano-banana-edit) <br>
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=nano-banana-edit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides RunComfy CLI calls; generated image files are produced by the external RunComfy service after execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

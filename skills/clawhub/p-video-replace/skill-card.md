## Description: <br>
Use when someone wants to swap a person, outfit, or product inside existing footage while keeping the camera move and audio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and creative automation agents use this skill to guide video replacement jobs through Pruna's API, including prompt drafting, required asset intake, and curl-based upload and prediction calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uploads source videos and reference images to Pruna's external API. <br>
Mitigation: Avoid sensitive or non-consensual footage and identity images, and confirm asset choices before starting generation. <br>
Risk: The skill requires PRUNA_API_KEY for API requests. <br>
Mitigation: Keep the API key private and avoid exposing it in prompts, logs, shared terminals, or generated artifacts. <br>
Risk: Video replacement can incur paid generation costs and may produce unwanted changes if the prompt is vague. <br>
Mitigation: Review the instruction prompt, asset mapping, and generation settings before making a paid API call. <br>


## Reference(s): <br>
- [ClawHub skill page for p-video-replace](https://clawhub.ai/pruna-ai/skills/p-video-replace) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with curl command examples and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRUNA_API_KEY plus user-provided source video and 1 to 4 reference image URLs.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

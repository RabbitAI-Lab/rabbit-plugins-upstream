## Description: <br>
Use when someone wants a person on camera speaking a script, such as a lip-synced host, spokesperson, or narrated avatar from a portrait photo. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content teams use this skill to prepare and call Pruna's p-video-avatar model for a single lip-synced talking-head video from a portrait plus script or uploaded narration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends selected images, audio, scripts, prompts, and authenticated requests to Pruna's service. <br>
Mitigation: Review the media and prompt payloads before generation, use PRUNA_API_KEY only for intended calls, and confirm cost-bearing API requests before submission. <br>
Risk: Optional related Pruna skills may be installed as prerequisites or follow-on workflow helpers. <br>
Mitigation: Review the related skills before installing optional dependencies and load only the skills needed for the requested workflow. <br>
Risk: Generated talking-head output can drift from the approved speaker, script, audio, or host beat. <br>
Mitigation: Confirm the portrait, script or audio, voice, language, voice prompt, video prompt, and resolution before generation, then apply the skill's fidelity check before accepting output. <br>


## Reference(s): <br>
- [ClawHub skill page for p-video-avatar](https://clawhub.ai/pruna-ai/skills/p-video-avatar) <br>
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files) <br>
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown guidance with curl command examples and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRUNA_API_KEY and explicit confirmation before cost-bearing generation; each invocation is scoped to one p-video-avatar prediction.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

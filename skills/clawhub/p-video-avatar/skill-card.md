## Description: <br>
Use when someone wants a person on camera speaking a script - lip-synced host, spokesperson, or narrated avatar from a portrait photo. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content teams use this skill to guide an agent through creating one lip-synced talking-head avatar video from a portrait, script, and optional narration through Pruna. It emphasizes prompt intake, user confirmation, and single-clip boundaries before generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user-provided portraits, scripts, and optional voice or narration files to Pruna for processing. <br>
Mitigation: Use images and audio only with appropriate permission, and avoid sensitive media unless the user is comfortable with third-party processing. <br>
Risk: Generated avatar videos may drift from the approved speaker identity, script, pacing, or delivery. <br>
Mitigation: Confirm the portrait, script or audio, voice settings, motion prompt, and resolution before paid API calls, then review generated output before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-avatar) <br>
- [Pruna files API endpoint](https://api.pruna.ai/v1/files) <br>
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls] <br>
**Output Format:** [Markdown with inline bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRUNA_API_KEY and user-supplied media or script inputs; produces instructions and request payloads for a single Pruna p-video-avatar prediction.] <br>

## Skill Version(s): <br>
1.0.8 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Make a person, portrait, or avatar talk on camera from a script or supplied audio for presenter, explainer, spokesperson, or lip-sync workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, marketers, and developers use this skill to prepare talking-head video generation requests from a portrait, avatar, or existing footage with either TTS script input or supplied audio. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Realistic person-and-voice video generation can be used without clear consent or for deceptive impersonation. <br>
Mitigation: Confirm the user is authorized to use the portrait, footage, and voice; avoid impersonation or deceptive re-voicing; disclose synthetic or altered media where appropriate. <br>
Risk: Model inputs can fail validation or produce unintended results if script-driven speech and supplied audio are mixed or stale schemas are assumed. <br>
Mitigation: Confirm the live model schema before execution and send exactly one drive mode: either TTS script and voice fields or a supplied audio input. <br>


## Reference(s): <br>
- [Talking avatar worked recipes](references/examples.md) <br>
- [ClawHub skill page](https://clawhub.ai/runware/skills/talking-avatar) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, API Calls, Configuration instructions] <br>
**Output Format:** [Markdown guidance with JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces asynchronous video-generation request guidance; the generated media is returned by the selected model service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

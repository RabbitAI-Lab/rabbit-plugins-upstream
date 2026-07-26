## Description: <br>
Use when someone wants one short video clip from text or images: B-roll, start/end frame animation, or a quick motion shot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and creators use this skill to have an agent prepare and submit one short Pruna p-video generation request from text, image anchors, and optional audio. It is intended for single-clip B-roll, image-to-video, frame-pair animation, or a quick motion shot, not multi-scene films or lip-synced avatars. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated-video requests can send user prompts, images, and audio to Pruna's external API using PRUNA_API_KEY. <br>
Mitigation: Avoid submitting sensitive media or private text unless the user intends to send it to Pruna, and confirm the API key is available only for the authorized account. <br>


## Reference(s): <br>
- [ClawHub p-video skill page](https://clawhub.ai/pruna-ai/skills/p-video) <br>
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files) <br>
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON request bodies and curl command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces one p-video prediction workflow per invocation; image, last-frame image, audio, duration, resolution, fps, aspect ratio, draft, and save-audio settings may shape the request.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

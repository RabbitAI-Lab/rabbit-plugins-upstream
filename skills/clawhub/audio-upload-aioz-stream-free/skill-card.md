## Description: <br>
Uploads local audio files to AIOZ Stream through the default Create, Upload Part, and Complete workflow, then returns an HLS streaming playback link. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, creators, and media teams use this skill to upload podcasts, lectures, or archived audio to AIOZ Stream and retrieve an HLS playback URL with default encoding settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AIOZ Stream credentials are required for uploads and could be exposed through logs, shell history, or committed files. <br>
Mitigation: Use stream-public-key and stream-secret-key only for the upload requests or secure environment handling, and avoid logging or committing those secrets. <br>
Risk: The skill sends local audio files to the configured AIOZ Stream endpoint. <br>
Mitigation: Confirm the endpoint is trusted and upload only audio files the user intends to send to that service. <br>
Risk: The artifact includes a generic API_KEY example even though the documented upload flow uses two AIOZ Stream header keys. <br>
Mitigation: Prefer stream-public-key and stream-secret-key for this skill, and do not rely on the generic API_KEY example for authentication. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/audio-upload-aioz-stream-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>
- [AIOZ Stream create audio endpoint](https://api-w3stream.attoaioz.cyou/api/videos/create) <br>
- [AIOZ Stream upload part endpoint](https://api-w3stream.attoaioz.cyou/api/videos/AUDIO_ID/part) <br>
- [AIOZ Stream complete upload endpoint](https://api-w3stream.attoaioz.cyou/api/videos/AUDIO_ID/complete) <br>
- [AIOZ Stream audio detail endpoint](https://api-w3stream.attoaioz.cyou/api/videos/AUDIO_ID) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with JSON examples and inline bash/curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns an HLS streaming URL or a status/error explanation after upload and transcoding checks.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

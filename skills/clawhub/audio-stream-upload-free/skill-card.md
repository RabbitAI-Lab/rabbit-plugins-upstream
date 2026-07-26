## Description: <br>
Audio Stream Upload Free helps personal creators upload local audio files to a streaming API through a create, upload, and complete workflow, then retrieve an HLS playback link. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and developers use this skill to prepare API keys, issue curl or Python upload calls, validate file integrity with an MD5 hash, and obtain streaming playback links for podcasts, music, or spoken-word content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends selected audio files and API credentials to a third-party streaming API. <br>
Mitigation: Use it only when the attoaioz.cyou streaming API is intended, verify the service and account keys independently, and store credentials in environment variables or a secret store. <br>
Risk: Users may upload media they do not have rights to distribute. <br>
Mitigation: Upload only audio content the user owns or is authorized to share. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/audio-stream-upload-free) <br>
- [Streaming API create endpoint](https://api-w3stream.attoaioz.cyou/api/videos/create) <br>
- [Streaming API base endpoint](https://api-w3stream.attoaioz.cyou/api) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash, Python, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces upload workflow guidance and command examples; API responses may include status, result data, logs, and errors.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Uploads selected local audio files to AIOZ Stream through a Create, Upload Part, and Complete workflow, then returns an HLS playback link using the user's AIOZ Stream API keys. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to publish podcasts, hosted voice content, or archived audio by uploading local files to AIOZ Stream and retrieving an HLS streaming URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads selected local audio files to AIOZ and uses stream-public-key and stream-secret-key credentials. <br>
Mitigation: Install only when that upload behavior is intended, keep keys in environment variables or a secret manager, and avoid logging or committing credentials. <br>
Risk: The security evidence flags contradictory unsafe upload guidance and an arbitrary upload_url Python example. <br>
Mitigation: Use only the intended HTTPS AIOZ API endpoint unless the destination and package are independently trusted. <br>
Risk: The security evidence reports unsupported security claims that users should review first. <br>
Mitigation: Confirm the security properties of the target API, endpoint, and runtime environment before relying on the skill for sensitive audio content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/audio-upload-aioz-stream-free) <br>
- [AIOZ Stream create audio endpoint](https://api-w3stream.attoaioz.cyou/api/videos/create) <br>
- [AIOZ Stream upload part endpoint](https://api-w3stream.attoaioz.cyou/api/videos/AUDIO_ID/part) <br>
- [AIOZ Stream complete upload endpoint](https://api-w3stream.attoaioz.cyou/api/videos/AUDIO_ID/complete) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash curl examples and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns an HLS playback link after upload and may report that server-side transcoding is still in progress.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

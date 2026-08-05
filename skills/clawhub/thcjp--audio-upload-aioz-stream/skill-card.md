## Description: <br>
Uploads local audio files to AIOZ Stream through a create, upload-part, and complete workflow, with optional encoding settings and HLS/DASH streaming links returned after server-side transcoding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to upload podcast, music, voice, or archived audio files to AIOZ Stream, configure basic or custom audio encoding, and retrieve streaming playback links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The selected audio file, title, tags, metadata, and AIOZ Stream API keys are sent to the AIOZ Stream endpoint. <br>
Mitigation: Confirm the exact file and metadata before upload, use only intended AIOZ credentials, and avoid uploading sensitive recordings unless sharing is appropriate. <br>
Risk: Custom uploads can mark content public and may expose copyrighted or private audio through generated streaming links. <br>
Mitigation: Verify rights to the recording and check the custom upload public setting before completing the upload. <br>
Risk: The upload depends on local file access, network reachability, and correct Content-Range and hash values. <br>
Mitigation: Validate the file path, file size, Content-Range header, and MD5 hash before uploading, and retry failed parts when network interruptions occur. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/audio-upload-aioz-stream) <br>
- [AIOZ Stream Create Audio Endpoint](https://api-w3stream.attoaioz.cyou/api/videos/create) <br>
- [AIOZ Stream Upload Part Endpoint](https://api-w3stream.attoaioz.cyou/api/videos/AUDIO_ID/part) <br>
- [AIOZ Stream Complete Upload Endpoint](https://api-w3stream.attoaioz.cyou/api/videos/AUDIO_ID/complete) <br>
- [AIOZ Stream Audio Details Endpoint](https://api-w3stream.attoaioz.cyou/api/videos/AUDIO_ID) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and curl command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns upload status guidance and HLS/DASH playback link locations when available.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

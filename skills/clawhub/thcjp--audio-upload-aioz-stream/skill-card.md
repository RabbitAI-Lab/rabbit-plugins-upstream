## Description: <br>
Uploads local audio files to AIOZ Stream through create, part upload, and complete API calls, with optional encoding settings and HLS/DASH stream links returned after processing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, creators, and media teams use this skill to upload podcast, music, voice, or archive audio files to AIOZ Stream and obtain HLS/DASH playback links. It is useful when an agent should guide the user through credential setup, upload command construction, encoding options, and post-upload status handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AIOZ Stream public and secret keys can be exposed if pasted into commands, terminal history, logs, or shared transcripts. <br>
Mitigation: Provide keys only when making the upload, prefer secure environment or secret handling, and avoid logging full curl requests that include secret headers. <br>
Risk: The workflow reads selected local audio files and uploads them to an external AIOZ Stream endpoint. <br>
Mitigation: Confirm the exact file path and intended destination before execution, and upload only files the user is authorized to distribute. <br>
Risk: Generated shell commands may fail or behave unexpectedly if file paths, Content-Range values, hashes, or network access are incorrect. <br>
Mitigation: Review commands before running them, verify file size and MD5 calculations, and retry failed upload parts with corrected values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/audio-upload-aioz-stream) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include AIOZ Stream request headers, local file paths, upload status notes, and HLS/DASH playback links.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

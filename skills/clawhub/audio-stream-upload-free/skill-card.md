## Description: <br>
Audio Stream Upload Free helps personal creators upload local audio files to a streaming API through create, upload, and complete steps and retrieve an HLS playback link. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and developers use this skill to prepare authenticated curl or Python requests that upload audio files, verify file hashes, finalize processing, and retrieve streamable HLS links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers could cause the skill to be used for media-editing or conversion requests that do not clearly ask for third-party audio upload. <br>
Mitigation: Activate it only when the user explicitly requests upload to the named streaming API and confirms the target audio file. <br>
Risk: The workflow sends local audio files and API credentials to a third-party streaming service. <br>
Mitigation: Use limited-scope keys from environment variables, avoid hardcoding secrets, redact command logs, and confirm the destination before execution. <br>
Risk: Raw command examples can upload local media when run with exec privileges. <br>
Mitigation: Require user review of file paths, content ownership, and upload intent before running generated curl or Python commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/audio-stream-upload-free) <br>
- [Streaming API base URL](https://api-w3stream.attoaioz.cyou/api) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with bash and Python command examples plus JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes audio upload status, result data, execution log, and error fields when following the artifact's response format.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

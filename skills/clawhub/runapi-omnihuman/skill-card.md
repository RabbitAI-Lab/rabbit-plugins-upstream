## Description: <br>
Create OmniHuman audio-to-video tasks and helper tasks for human identification and subject-mask detection through RunAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate OmniHuman talking-head videos from an image and audio input, identify human regions, or detect subject masks through RunAPI. It guides one-off CLI execution and SDK-based application integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RunAPI-generated file URLs are temporary and may be lost if treated as long-term assets. <br>
Mitigation: Download generated videos, masks, or other returned files into durable storage within 7 days. <br>
Risk: RunAPI calls may require credentials in CLI or SDK workflows. <br>
Mitigation: Prefer RUNAPI_API_KEY or saved CLI configuration for headless runs, and use browser login only for explicitly interactive sessions. <br>


## Reference(s): <br>
- [RunAPI OmniHuman model documentation](https://runapi.ai/models/omnihuman.md) <br>
- [OmniHuman audio-to-video variant](https://runapi.ai/models/omnihuman/1.5.md) <br>
- [OmniHuman human-identification variant](https://runapi.ai/models/omnihuman/1.5-human-identification.md) <br>
- [OmniHuman subject-detection variant](https://runapi.ai/models/omnihuman/1.5-subject-detection.md) <br>
- [RunAPI ByteDance provider page](https://runapi.ai/providers/bytedance.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and SDK package names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce CLI command sequences, SDK integration guidance, JSON input-file guidance, and authentication setup guidance.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

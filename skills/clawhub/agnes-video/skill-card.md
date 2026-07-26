## Description: <br>
Generates videos from text prompts, public image URLs, multiple reference images, or keyframes through the Agnes Video V2.0 asynchronous video-generation API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lutongsuo](https://clawhub.ai/user/lutongsuo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content creators use this skill to create short videos, animate images, generate multi-image transitions, and produce keyframe animations for storytelling, marketing, product demos, and social media workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and public image URLs are sent to the Agnes API and may create billable remote video jobs. <br>
Mitigation: Avoid sensitive prompts, private or internal image URLs, and secrets; run generation only when a real external job is intended. <br>
Risk: The connection-test script creates a real remote video task rather than only checking local configuration. <br>
Mitigation: Use the connection test only when a real test video job is acceptable and expected. <br>
Risk: Generated content is downloaded directly to the requested output path. <br>
Mitigation: Choose output paths deliberately and avoid overwriting important files. <br>


## Reference(s): <br>
- [Agnes Video V2.0 skill page](https://clawhub.ai/lutongsuo/skills/agnes-video) <br>
- [API documentation](references/API.md) <br>
- [Prompt guide](references/PROMPT_GUIDE.md) <br>
- [Example prompts](references/EXAMPLES.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands and API usage examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides asynchronous video job creation, polling, and optional download of generated video files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

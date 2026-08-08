## Description: <br>
Analyze Video By Qwen helps an agent analyze local video files or public video URLs with Qwen 3.5 Plus, using configurable prompts and frame sampling to produce scene descriptions, summaries, object or action observations, content review notes, and question-answer style analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content teams, educators, media operators, and reviewers use this skill to turn videos into concise analysis, summaries, scene descriptions, object or action observations, and content review guidance. It is intended for offline local files or publicly accessible video URLs, not live streams or video editing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected video content and prompts are sent to Alibaba Cloud DashScope/Qwen. <br>
Mitigation: Use the skill only for videos and prompts that your data-handling policy permits sharing with that third-party service. <br>
Risk: DashScope API keys could be exposed through permissive file permissions, chat input, terminal output, or agent logs. <br>
Mitigation: Store the API key only in the intended config location with restricted permissions, and avoid commands or prompts that print secrets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/analyze-video-by-qwen) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-like analysis text with optional shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a DashScope API key and sends selected video content and prompts to Alibaba Cloud DashScope/Qwen; cost and latency can increase with higher FPS settings.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

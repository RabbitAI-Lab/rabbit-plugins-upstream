## Description: <br>
Processes audio with MediaKit CLI to separate vocals from background audio and retrieve detailed audio metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[volcvnebot](https://clawhub.ai/user/volcvnebot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run MediaKit CLI audio workflows for vocal/background separation and audio metadata inspection. It is suited for audio processing tasks that can use MediaKit local or cloud execution modes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud mode may upload local media files or submit media URLs to a remote service. <br>
Mitigation: Use only authorized media, avoid confidential or regulated content unless third-party processing is approved, and prefer local mode where the specific capability supports it. <br>
Risk: The skill depends on MediaKit CLI credentials and runtime configuration for cloud execution. <br>
Mitigation: Verify MEDIAKIT_API_KEY and related MediaKit configuration before cloud calls, and keep credentials out of shared prompts, logs, and artifacts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/volcvnebot/skills/byted-mediakit-audio) <br>
- [MediaKit shared rules](reference/shared.md) <br>
- [Voice and background separation](reference/separate-voice.md) <br>
- [Audio metadata probe](reference/probe-audio-metadata.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON result shapes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [MediaKit cloud calls can return task_id and request_id values for follow-up query-task polling.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

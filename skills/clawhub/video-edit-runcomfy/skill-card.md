## Description: <br>
Video Edit — Pro Pack on RunComfy helps an agent transform an existing video clip with RunComfy routes for restyling, background swaps, outfit swaps, motion transfer, color grading, and packaging swaps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, creators, and agents use this skill to select a RunComfy video-editing route and prepare the corresponding CLI invocation for an existing source video. It is suited to talking-head, product, and short-form video edits where the user wants controlled changes while preserving identity, motion, framing, or audio. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Source video URLs, optional reference images, and edit prompts are sent to RunComfy for cloud processing. <br>
Mitigation: Use the skill only when the user has approved RunComfy processing and the provided media can be shared with that service. <br>
Risk: Ambiguous requests could trigger cloud video editing before the user has provided an existing video or confirmed the intended workflow. <br>
Mitigation: Confirm that the user wants cloud video editing and require a source video URL before invoking the RunComfy CLI. <br>
Risk: The skill depends on a RunComfy account token through local CLI configuration or RUNCOMFY_TOKEN. <br>
Mitigation: Keep tokens in the CLI config or environment, avoid echoing secrets in generated commands, and rotate credentials if exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/video-edit-runcomfy) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=video-edit-runcomfy) <br>
- [RunComfy video edit models](https://www.runcomfy.com/models?utm_source=clawhub&utm_medium=skill&utm_campaign=video-edit-runcomfy) <br>
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=video-edit-runcomfy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with RunComfy CLI commands and JSON input bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to produce RunComfy edit requests and download edited video files through the local RunComfy CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Extends or continues an existing video clip on RunComfy by guiding an agent to invoke Google Veo 3-1 extend-video endpoints with the runcomfy CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and creative operators use this skill to extend a provided source video or chain narrative shots with RunComfy's Veo 3-1 extend-video endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the selected video URL and continuation prompt to RunComfy. <br>
Mitigation: Confirm the user explicitly provided the video and prompt, and avoid sending sensitive or unauthorized media. <br>
Risk: RunComfy authentication tokens may be exposed through prompts, shell history, or logs. <br>
Mitigation: Use a scoped token where possible, prefer RUNCOMFY_TOKEN or the RunComfy login flow, and never echo tokens into prompts or logs. <br>
Risk: Installing or invoking an untrusted CLI package can introduce supply-chain risk. <br>
Mitigation: Install the RunComfy CLI only through the verified package manager path described by the skill and avoid remote shell install scripts. <br>
Risk: Video content can contain indirect prompt-injection attempts or cause the generated continuation to diverge from the user's request. <br>
Mitigation: Use only user-provided video URLs for the extension and treat unexpected motion, identity drift, or instruction-like frame content as suspicious. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/video-extend) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [Veo 3-1 extend-video](https://www.runcomfy.com/models/google-deepmind/veo-3-1/extend-video?utm_source=clawhub&utm_medium=skill&utm_campaign=video-extend) <br>
- [Veo 3-1 fast extend-video](https://www.runcomfy.com/models/google-deepmind/veo-3-1/fast/extend-video?utm_source=clawhub&utm_medium=skill&utm_campaign=video-extend) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=video-extend) <br>
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=video-extend) <br>
- [Veo 3 collection](https://www.runcomfy.com/models/collections/veo-3?utm_source=clawhub&utm_medium=skill&utm_campaign=video-extend) <br>
- [RunComfy video models](https://www.runcomfy.com/models?utm_source=clawhub&utm_medium=skill&utm_campaign=video-extend) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash commands and JSON CLI input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces RunComfy CLI invocation guidance and recommends writing generated videos to a local output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Routes avatar-video requests to RunComfy talking-head and lip-sync models and returns prompts plus runcomfy CLI commands for portrait-to-speech, script-to-video, and cinematic reference-audio workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, developers, and production teams use this skill to select and invoke RunComfy avatar, talking-head, and lip-sync video models for UGC voiceovers, virtual presenters, dubbed demos, stylized character animation, and cinematic monologues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, image URLs, audio URLs, and generated outputs are processed by RunComfy. <br>
Mitigation: Use the skill only when the user intends external RunComfy processing and avoid sending sensitive media or prompts unless that processing is acceptable. <br>
Risk: Avatar and lip-sync workflows can misuse a person's likeness or voice. <br>
Mitigation: Require rights or consent for both the visual likeness and voice, and decline requests involving non-consensual or harmful synthetic media. <br>
Risk: The RunComfy token grants access to the user's RunComfy account. <br>
Mitigation: Protect RUNCOMFY_TOKEN and local RunComfy configuration like other API credentials; do not expose tokens in prompts, logs, or generated examples. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/permew/skills/ai-avatar-video-runcomfy) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-avatar-video-runcomfy) <br>
- [RunComfy lip-sync models](https://www.runcomfy.com/models/feature/lip-sync?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-avatar-video-runcomfy) <br>
- [OmniHuman model](https://www.runcomfy.com/models/bytedance/omnihuman/api?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-avatar-video-runcomfy) <br>
- [Wan 2-7 model](https://www.runcomfy.com/models/wan-ai/wan-2-7?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-avatar-video-runcomfy) <br>
- [HappyHorse 1.0 text-to-video model](https://www.runcomfy.com/models/happyhorse/happyhorse-1-0/text-to-video?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-avatar-video-runcomfy) <br>
- [Seedance v2 Pro model](https://www.runcomfy.com/models/bytedance/seedance-v2/pro?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-avatar-video-runcomfy) <br>
- [Wan 2-2 Animate model](https://www.runcomfy.com/models/community/wan-2-2-animate/api?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-avatar-video-runcomfy) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces model-routing guidance, prompting patterns, RunComfy CLI invocations, and setup requirements for the agent to present or execute with user approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

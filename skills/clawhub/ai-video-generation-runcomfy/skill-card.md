## Description: <br>
Routes text-to-video, image-to-video, and video-extension requests to appropriate RunComfy model endpoints and provides the matching CLI commands and prompting guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to generate or extend video clips through RunComfy by matching natural-language intent to text-to-video, image-to-video, lip-sync, cinematic, and fast-iteration model routes. It helps agents produce prompt guidance, JSON inputs, and `runcomfy run` commands for the selected endpoint. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RunComfy receives video prompts and any reference image, audio, or video URLs supplied for generation. <br>
Mitigation: Install and use the skill only when that disclosure is acceptable for the requested media and prompt content. <br>
Risk: Ambiguous requests such as 'animate this' may trigger token-backed RunComfy generation and consume service usage. <br>
Mitigation: Confirm the user intends to run a RunComfy generation before invoking the CLI for ambiguous video requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/ai-video-generation-runcomfy) <br>
- [Publisher profile](https://clawhub.ai/user/permew) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy video models](https://www.runcomfy.com/models?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-video-generation-runcomfy) <br>
- [RunComfy CLI docs](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-video-generation-runcomfy) <br>
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-video-generation-runcomfy) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include RunComfy model IDs, endpoint paths, CLI exit-code guidance, and output directory recommendations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

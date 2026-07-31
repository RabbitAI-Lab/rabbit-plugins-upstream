## Description: <br>
Image-to-video generation on RunComfy that turns still images into short video clips through the RunComfy Model API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to convert still images into short videos with RunComfy. It helps an agent choose between general animation, audio-driven lip-sync-style output, and multi-modal reference workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports that the advertised image-and-audio lip-sync route calls a text-to-video endpoint without using a supplied image. <br>
Mitigation: Review the route before relying on identity-preserving lip-sync; treat that route as text-to-video with audio unless the skill is corrected. <br>
Risk: Image, video, and audio URLs are fetched by RunComfy services for generation. <br>
Mitigation: Use approved media URLs and avoid sensitive or restricted inputs unless the RunComfy account and data handling are acceptable for the use case. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/image-to-video-runcomfy) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=image-to-video-runcomfy) <br>
- [RunComfy image-to-video models](https://www.runcomfy.com/models?utm_source=clawhub&utm_medium=skill&utm_campaign=image-to-video-runcomfy) <br>
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=image-to-video-runcomfy) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with bash commands and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the RunComfy CLI and either RUNCOMFY_TOKEN or local RunComfy configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

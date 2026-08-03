## Description: <br>
Face Swap — Pro Pack on RunComfy helps an agent route authorized face or character swap requests for still images and videos through the RunComfy CLI and supported model endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, creators, and developers use this skill to choose and invoke RunComfy face-swap routes for authorized identity substitution in images and videos, including still edits, batch swaps, and motion-preserving video workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face-swap workflows can be misused for non-consensual real-person impersonation, harmful sexual or defamatory material, or deceptive synthetic media. <br>
Mitigation: Use only content where the operator has rights and consent, and refuse non-consensual impersonation or harmful synthetic-media requests. <br>
Risk: The workflow sends referenced images, audio, or video to RunComfy and uses a RunComfy API token. <br>
Mitigation: Install and use the skill only when that data transfer is acceptable, protect RUNCOMFY_TOKEN, and avoid using sensitive media unless RunComfy handling meets the user's requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/face-swap-runcomfy) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy CLI docs](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=face-swap-runcomfy) <br>
- [RunComfy character-swap feature](https://www.runcomfy.com/models/feature/character-swap?utm_source=clawhub&utm_medium=skill&utm_campaign=face-swap-runcomfy) <br>
- [Wan 2-2 Animate model endpoint](https://www.runcomfy.com/models/community/wan-2-2-animate/api?utm_source=clawhub&utm_medium=skill&utm_campaign=face-swap-runcomfy) <br>
- [Kling 2-6 Motion Control Pro](https://www.runcomfy.com/models/kling/kling-2-6/motion-control-pro?utm_source=clawhub&utm_medium=skill&utm_campaign=face-swap-runcomfy) <br>
- [GPT Image 2 Edit](https://www.runcomfy.com/models/openai/gpt-image-2/edit?utm_source=clawhub&utm_medium=skill&utm_campaign=face-swap-runcomfy) <br>
- [Nano Banana 2 Edit](https://www.runcomfy.com/models/google/nano-banana-2/edit?utm_source=clawhub&utm_medium=skill&utm_campaign=face-swap-runcomfy) <br>
- [FLUX Kontext models](https://www.runcomfy.com/models/collections/flux-kontext?utm_source=clawhub&utm_medium=skill&utm_campaign=face-swap-runcomfy) <br>
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=face-swap-runcomfy) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the runcomfy CLI, RUNCOMFY_TOKEN or RunComfy login, and RunComfy config under ~/.config/runcomfy.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

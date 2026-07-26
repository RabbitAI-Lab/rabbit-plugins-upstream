## Description: <br>
Add sound to a silent video by guiding an agent to route sound effects, narration, or music requests to the appropriate media workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to add synchronized sound effects to short silent videos, or to route narration and background music requests to more appropriate companion skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected video clips and prompts may be sent to referenced model provider tools. <br>
Mitigation: Use only user-approved media and avoid sensitive clips or prompts unless sharing them with the provider is acceptable. <br>
Risk: Generated sound effects may be poorly synchronized or may not match the scene because dedicated SFX coverage is limited. <br>
Mitigation: Review the returned video before use, retry with a tighter prompt or seed when needed, and consider regenerating the video with native audio when sound quality is critical. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/runware/skills/add-audio-to-video) <br>
- [Publisher profile](https://clawhub.ai/user/runware) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration] <br>
**Output Format:** [Markdown guidance with model-routing steps and parameter notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Covers short video inputs, optional sound-effect prompts, output format selection, start offsets, quality checks, and routing to narration or music skills when appropriate.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

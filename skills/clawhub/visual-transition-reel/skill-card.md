## Description: <br>
Guides an agent through planning, generating, reviewing, and assembling a montage with transitions between composed video clips. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, developers, and media teams use this skill to create multi-shot transition reels by planning scene anchors, generating start and end stills, rendering image-to-video transition clips, and assembling the final reel with optional background music. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Source or generated images may be sent to referenced Pruna generation services. <br>
Mitigation: Use the skill only with images that are approved for those services, and review the plan and stills before continuing. <br>
Risk: Video generation and final assembly can spend credits and write PNG or MP4 files into the workspace. <br>
Mitigation: Require the documented approve plan, approve stills, and approve clips gates before paid generation or assembly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/visual-transition-reel) <br>
- [Example prompt](artifact/example-prompt.md) <br>
- [Transition plan template](artifact/templates/transition-plan.template.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON plan templates and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces staged plans, review gates, generation prompts, local PNG and MP4 outputs, ffmpeg assembly commands, and a final reel manifest.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

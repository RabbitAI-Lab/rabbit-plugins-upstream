## Description: <br>
Guides an agent through planning, generating, reviewing, and assembling a montage with transitions between composed video clips. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and developers use this skill to build visual transition reels such as action-sequence montages or multi-scene pieces where narration is optional. The skill structures intake, approval gates, still generation, video transition prompts, and final ffmpeg assembly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Source images may be uploaded to provider APIs during still, video, or audio generation phases. <br>
Mitigation: Confirm input rights and sensitivity before generation, and use the skill's approval gates before proceeding with uploads or generated assets. <br>
Risk: Video and audio generation phases may spend provider credits. <br>
Mitigation: Require explicit approve plan, approve stills, and approve clips gates before moving into paid generation or assembly steps. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/visual-transition-reel) <br>
- [Example prompt](artifact/example-prompt.md) <br>
- [Transition plan template](artifact/templates/transition-plan.template.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON plan templates and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces phased scene plans, transition prompts, generation steps, review gates, and assembly commands; generated media is produced through dependent skills and provider APIs.] <br>

## Skill Version(s): <br>
1.0.7 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

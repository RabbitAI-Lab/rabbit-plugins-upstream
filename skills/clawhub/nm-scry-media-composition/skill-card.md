## Description: <br>
Combines GIFs and videos into composite tutorials with vertical or grid layouts via ffmpeg. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation authors use this skill to combine existing GIF, video, or image assets into tutorial and demo compositions using manifest-driven ffmpeg commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated ffmpeg examples may overwrite existing media outputs when run with overwrite flags. <br>
Mitigation: Review the manifest output paths before execution and run commands only in the intended workspace. <br>
Risk: Composition manifests may include prerequisite commands for generating component media. <br>
Mitigation: Inspect any manifest requirement commands before running them and confirm they match the expected local project workflow. <br>
Risk: Broad trigger terms may cause the skill to appear for unrelated media or tutorial tasks. <br>
Mitigation: Use the skill only when the task explicitly requires combining multiple media assets into a composite output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scry-media-composition) <br>
- [Homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/scry) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with YAML manifest examples and ffmpeg shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are intended for local media composition and may overwrite output files when ffmpeg is run with overwrite flags.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

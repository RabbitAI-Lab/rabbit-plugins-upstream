## Description: <br>
Combines GIFs and videos into composite tutorials with vertical or grid layouts via ffmpeg. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical authors use this skill to combine local GIF, video, and image outputs into tutorial or documentation media. It guides agents through manifest review, input validation, ffmpeg composition, and output verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Manifest-controlled component paths and output paths may cause agents to process unintended local files or overwrite outputs. <br>
Mitigation: Review the manifest's component paths, output path, and layout options before running ffmpeg commands. <br>
Risk: Manifest requires entries may ask the agent to run prerequisite commands before composition. <br>
Mitigation: Review and approve any requires commands separately before execution. <br>
Risk: The metadata references a separate Claude Code plugin that may have independent behavior and permissions. <br>
Mitigation: Review the separate plugin independently before relying on it for agent workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scry-media-composition) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scry) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown] <br>
**Output Format:** [Markdown guidance with YAML examples and inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces ffmpeg composition instructions and verification steps for local media assets.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

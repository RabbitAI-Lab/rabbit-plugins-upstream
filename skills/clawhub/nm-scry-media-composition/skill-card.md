## Description: <br>
Combines GIFs and videos into composite tutorials with vertical or grid layouts via ffmpeg. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical writers use this skill to combine existing GIFs, videos, and images into tutorial or documentation media using manifest-driven FFmpeg composition. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides an agent to run local media-processing commands that write combined output files. <br>
Mitigation: Confirm FFmpeg execution is intended, review output paths before running commands, and verify the combined file exists with expected size and dimensions. <br>
Risk: Manifest-provided prerequisite commands can affect the local environment if they are untrusted. <br>
Mitigation: Use trusted manifests and review any `requires` commands before allowing an agent to execute them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scry-media-composition) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scry) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with YAML manifests and inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides an agent to validate media component outputs, run FFmpeg composition commands, and report output file metrics.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

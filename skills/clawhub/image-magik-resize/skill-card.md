## Description: <br>
Resize images using ImageMagick through a Bash command-line entrypoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pr1vateer](https://clawhub.ai/user/pr1vateer) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to resize local image files by passing an input path, ImageMagick geometry, and optional output path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The command writes image files and can create the requested output directory. <br>
Mitigation: Review input and output paths before running the skill. <br>
Risk: Image resizing depends on a local ImageMagick installation. <br>
Mitigation: Install ImageMagick and confirm that either magick or convert is available before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pr1vateer/skills/image-magik-resize) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Configuration] <br>
**Output Format:** [Command-line output and resized image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash and either magick or convert from ImageMagick.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Resize images using ImageMagick (CLI). Entrypoint is a Bash script. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pr1vateer](https://clawhub.ai/user/pr1vateer) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to resize local image files through an ImageMagick-backed Bash command with fixed, percentage, or conditional geometry options. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill resizes local image files and writes outputs to user-provided or inferred paths. <br>
Mitigation: Review input and output paths before running the resize command. <br>
Risk: Processing images from untrusted sources can expose ImageMagick parser vulnerabilities if ImageMagick is outdated. <br>
Mitigation: Keep ImageMagick updated before using the skill on untrusted images. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pr1vateer/skills/image-resize) <br>
- [Publisher profile](https://clawhub.ai/user/pr1vateer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Files] <br>
**Output Format:** [Terminal status text and resized image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash and either magick or convert from ImageMagick.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence; artifact frontmatter reports 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

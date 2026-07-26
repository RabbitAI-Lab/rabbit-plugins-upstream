## Description: <br>
Batch remove Doubao (豆包 AI) watermarks from image directories using OpenCV inpainting and user-supplied watermark regions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dororoliu666](https://clawhub.ai/user/dororoliu666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prepare local image batches for watermark-region repair when they have the right to edit those images. The skill guides the agent to inspect image dimensions, choose rectangular masks, and run a local batch-processing script. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bulk watermark removal can be misused on images the user does not have the right to modify. <br>
Mitigation: Use the skill only when the user has permission to remove marks from the images being processed. <br>
Risk: Processing untrusted image files and installing unpinned image-processing dependencies can increase local execution risk. <br>
Mitigation: Use an isolated environment, prefer pinned dependency versions, and avoid processing untrusted images. <br>
Risk: The --force option can overwrite existing output files. <br>
Mitigation: Write to a fresh output directory unless overwriting prior outputs is intentional. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dororoliu666/skills/doubao-watermark-removal) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Files] <br>
**Output Format:** [Markdown with inline bash commands and local output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces processed image files in a user-selected output directory when the batch script is run.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

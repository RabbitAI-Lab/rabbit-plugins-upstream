## Description: <br>
Image Editor helps agents make local PIL-based image edits such as text replacement, element removal, and watermarking while preserving original resolution and verifying outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liyafeichina](https://clawhub.ai/user/liyafeichina) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and other users use this skill when an agent needs to modify local images, including replacing text, adding watermarks, removing visible elements, or covering sensitive details while keeping the original dimensions intact. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image edits may introduce incorrect text, visible artifacts, or unintended changes. <br>
Mitigation: Compare each edited image against the original with vision verification and review the result before relying on or publishing it. <br>
Risk: Text editing may fail or look inconsistent when the expected font path or font is unavailable. <br>
Mitigation: Select an appropriate local font for the target system and adjust the font path before rendering replacement text. <br>
Risk: Saving with the wrong format or quality settings can reduce output quality. <br>
Mitigation: Preserve the source dimensions, choose an output format and quality appropriate to the input, and verify the saved file before delivery. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liyafeichina/image-editor) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Code, Shell commands, Guidance] <br>
**Output Format:** [Edited image files with Markdown guidance and inline Python or shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preserves original image dimensions, uses local python3 with PIL/Pillow, and verifies edited output with a vision model before delivery.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

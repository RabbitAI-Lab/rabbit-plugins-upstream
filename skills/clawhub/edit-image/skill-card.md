## Description: <br>
Modify an existing image by instruction or mask, including add, remove, replace, recolor, relight, restore, inpaint, or outpaint tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to guide agents through targeted edits to an existing image, including masked removals, inpainting, recoloring, relighting, and canvas extension while preserving untouched regions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided images and masks may be processed by external image-model services. <br>
Mitigation: Avoid private or sensitive images unless that processing is acceptable for the workflow. <br>
Risk: Masked edits can unintentionally affect neighboring content when the mask or dilation setting is too broad. <br>
Mitigation: Use source-resolution masks, keep edits targeted, and review the result before using or publishing it. <br>


## Reference(s): <br>
- [Edit image worked recipes](references/examples.md) <br>
- [ClawHub skill page](https://clawhub.ai/runware/skills/edit-image) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/runware) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON code blocks and inline tool commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include imageInference request payloads for synchronous Runware image edits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

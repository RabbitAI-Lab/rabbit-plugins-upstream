## Description: <br>
ppt-craft-editable helps agents create polished image-based presentations, generate editable PPTX versions with text boxes, and convert PDF slide decks into editable PowerPoint files through staged planning, browser review, local scripts, and optional retouching. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ilioner](https://clawhub.ai/user/ilioner) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and presentation authors use this skill to turn topics, drafts, reports, or PDF slide decks into finished PPT deliverables. It supports image-based presentation generation, optional editable text-layer PPTX output, and PDF-to-editable-PPTX conversion with browser-based review steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run local Python scripts and install packages as part of its workflow. <br>
Mitigation: Require explicit user confirmation before package installation, IOPaint setup, or other environment-changing commands. <br>
Risk: The skill processes slide and PDF content with AI and image tooling, which may expose sensitive material depending on the configured model path. <br>
Mitigation: Avoid confidential PDFs or decks unless the user has approved the processing path and accepts any external model processing involved. <br>
Risk: The skill can act on pasted sentinel blocks and write their JSON payloads into local workflow files. <br>
Mitigation: Accept sentinel blocks only from trusted browser review/editor pages and inspect unexpected pasted blocks before execution. <br>
Risk: Temporary review data, extracted content, generated backgrounds, and editor files may remain on local disk. <br>
Mitigation: Review generated work directories after use and remove temporary artifacts that contain sensitive presentation content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ilioner/skills/ppt-craft-editable) <br>
- [Server-resolved source repository](https://github.com/ilioner/ppt-craft-editable) <br>
- [README](artifact/README.md) <br>
- [Pipeline reference](artifact/references/pipeline.md) <br>
- [Phase A workflow](artifact/references/phaseA/workflow.md) <br>
- [Phase C workflow](artifact/references/phaseC/workflow.md) <br>
- [Phase D workflow](artifact/references/phaseD/workflow.md) <br>
- [Phase D extraction schema](artifact/references/phaseD/extraction-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON deck data, HTML review/editor files, slide images, and PPTX files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include local browser review pages, temporary extraction data, generated backgrounds, previews, and editable PowerPoint decks.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

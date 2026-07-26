## Description: <br>
PowerPoint speaker notes editor for AI agents that helps modify PPT speaker notes, export notes to Markdown, rewrite notes in narrative, concise, verbatim, or custom styles, and unpack or pack PPTX files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect, rewrite, export, and safely update speaker notes inside PowerPoint presentations while preserving slide-to-notes mappings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-selected PPTX content, which may include confidential presentation text or speaker notes. <br>
Mitigation: Use it only on presentations the user is comfortable sharing with the agent, and keep work limited to the selected presentation files. <br>
Risk: Generated speaker-note drafts may be inaccurate, off-tone, or unsuitable for the presentation audience. <br>
Mitigation: Review each generated draft before approving any note modifications. <br>
Risk: Editing PPTX XML incorrectly can break presentation files or update the wrong notes slide. <br>
Mitigation: Confirm slide-to-notes mappings, preserve XML escaping, repack the presentation, and verify the modified PPTX before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/pptx-notes-editor) <br>
- [Project homepage](https://github.com/cm8421/pptx-notes-editor) <br>
- [Support issues](https://github.com/cm8421/pptx-notes-editor/issues) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated speaker-note text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce PPTX XML editing steps, Markdown note exports, and repacked presentation files after user approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Guides an agent through interviewing for presentation requirements, generating standards-compliant HTML slides, validating them, and converting them into editable PowerPoint decks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqcmj74](https://clawhub.ai/user/cqcmj74) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, presentation authors, and agent users can use this skill to create HTML slide decks that pass a strict compatibility validator and convert to PPTX. It is best suited for workflows that need editable PowerPoint output from generated slide content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Slide HTML can silently fetch web assets during conversion. <br>
Mitigation: Use the skill only with trusted slide HTML and review http(s) asset references before running conversion. <br>
Risk: Slide HTML can reference local files, images, audio, or video that may be embedded into output decks. <br>
Mitigation: Inspect file://, image, video, and audio paths before conversion and run the workflow from a constrained project directory. <br>
Risk: First use may install npm dependencies and download Playwright Chromium. <br>
Mitigation: Install dependencies only in a trusted environment and review the packaged dependency manifest before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cqcmj74/skills/html-slides-to-pptx) <br>
- [HTML slide specification](reference/html-spec.md) <br>
- [Guided interview process](reference/interview-guide.md) <br>
- [Creative layout guide](reference/creative-layouts.md) <br>
- [Behavior baseline](reference/behavior-baseline.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTML, CSS, JSON, and shell command snippets for producing slide project files and PPTX output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces project files such as deck briefs, theme CSS, HTML slide files, playlist JSON, optional conversion configuration, validation output, and PPTX files.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

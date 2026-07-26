## Description: <br>
Builds, redesigns, and critiques presentation-grade slide decks from user-provided material or researched context, using interview checkpoints, deck-building scripts, and an independent actor-critic review loop. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dong845](https://clawhub.ai/user/dong845) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers can use this skill to create, redesign, or review slide decks for research, teaching, meetings, stakeholder readouts, conference talks, and related presentation workflows. It is most useful when the user needs a structured content plan, visual design direction, generated or prepared assets, a .pptx build, and critique before handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read local materials, write deck assets, perform web research, and generate images. <br>
Mitigation: Use it only in approved workspaces with appropriate input data, and disable or avoid web and image-generation paths when sensitive material should not leave the environment. <br>
Risk: The security guidance flags README execution paths and generated HTML previews as areas requiring care with untrusted inputs. <br>
Mitigation: Avoid README execution paths for untrusted repositories, and open generated HTML previews only when the direction data and source workspace are trusted. <br>
Risk: Cross-deck preference history may reveal sensitive presentation or style preferences. <br>
Mitigation: Review, disable, or clear taste.md persistence when user preference history should not be retained. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dong845/skills/slide-maker) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [Design Principles](artifact/references/design-principles.md) <br>
- [Content Plan Specification](artifact/references/content-plan-spec.md) <br>
- [Review Rubrics](artifact/references/review-rubrics.md) <br>
- [File Inventory](artifact/references/file-inventory.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance and checkpoint tables, Python and shell commands, generated assets, rendered slide images, and PowerPoint .pptx files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local deck folders, slide renders, image assets, HTML previews, notes exports, and optional final deliverables depending on user approval and available tooling.] <br>

## Skill Version(s): <br>
4.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

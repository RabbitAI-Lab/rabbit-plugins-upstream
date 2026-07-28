## Description: <br>
Guides agents through evidence-based Chinese content creation, including research, planning, outlining, section-by-section drafting, review, image-planning, translation handoff, and publication preparation for articles, reports, tutorials, project introductions, source-code analyses, and explanatory materials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and content authors use this skill to plan, draft, revise, and review Chinese technical content from explicit evidence. It is especially suited for article and report workflows that need source materials, outlines, preferences, status, and change history preserved across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create persistent local writing folders, profile snapshots, copied source excerpts, and user feedback files. <br>
Mitigation: Use it only for intended article workflows, keep `wenqu-skills/` out of version control for sensitive repositories, and periodically review saved materials and preferences. <br>
Risk: Drafts, outlines, image prompts, and review notes may preserve sensitive project details in local workspace files. <br>
Mitigation: Review generated workspace files before sharing or publishing, and remove sensitive excerpts that are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gogoingai/skills/wenqu-write) <br>
- [Wenqu Write source](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-write) <br>
- [Reference index](references/INDEX.md) <br>
- [Planning questionnaire](references/planning/questionnaire.md) <br>
- [Writing style guide](references/writing/style-guide.md) <br>
- [Writing anti-patterns](references/writing/anti-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Files, Shell commands, Configuration] <br>
**Output Format:** [Markdown prose, outlines, checklists, review notes, image prompts, and local article workspace files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create persistent local writing folders, material indexes, preference files, status files, and user profile snapshots for article workflows.] <br>

## Skill Version(s): <br>
0.1.12 (source: release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
文曲·写作 guides an agent through evidence-based Chinese technical writing, including research, planning, outlining, section-by-section drafting, review, image placeholders, translation support, and release preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and technical writers use this skill to create, revise, review, and prepare Chinese technical articles, reports, tutorials, project introductions, source-code analyses, and explanatory materials from project evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read project source files and external materials while collecting evidence for an article. <br>
Mitigation: Use it only in projects where source review is acceptable, and review the collected materials before relying on them in public content. <br>
Risk: The skill stores writing context, preferences, and article materials in project or user profile directories. <br>
Mitigation: Keep secrets, cookies, private contact details, and private paths out of profiles and article materials; inspect stored files before sharing or committing them. <br>
Risk: Generated drafts can contain incorrect claims if source evidence, external articles, or inferred conclusions are weak. <br>
Mitigation: Require cited evidence for technical claims, resolve material conflicts before drafting, and run the built-in review passes before publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gogoingai/skills/wenqu-write) <br>
- [ClawDIS homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-write) <br>
- [OpenClaw homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-write) <br>
- [Content index](references/INDEX.md) <br>
- [Project questionnaire guide](references/planning/questionnaire.md) <br>
- [Content provenance guide](references/planning/content-provenance.md) <br>
- [Materials governance guide](references/planning/materials-governance.md) <br>
- [Writing style guide](references/writing/style-guide.md) <br>
- [Writing anti-patterns](references/writing/anti-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown prose, outlines, tables, checklists, review notes, article files, and concise command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create project-scoped writing state under wenqu-skills/ and a non-sensitive writing profile under .gogoingai/wenqu-skills when the user approves or the workflow requires it.] <br>

## Skill Version(s): <br>
0.1.19 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

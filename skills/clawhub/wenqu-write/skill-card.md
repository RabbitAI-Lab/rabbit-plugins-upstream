## Description: <br>
文曲·写作 guides agents through evidence-based Chinese technical writing, from research and planning through outlines, drafting, review, illustration placeholders, translation coordination, and release preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and technical writers use this skill to create or revise Chinese articles, reports, tutorials, project introductions, source-code analyses, and explanatory materials grounded in collected evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Durable writing context can retain private repository notes, unpublished material, or article-specific preferences in local files. <br>
Mitigation: Before using the skill on private work, decide whether wenqu-skills/ should be ignored by git or cleaned after use, and avoid saving secrets or unrelated personal data. <br>
Risk: Broad write, modify, and review activation wording can affect the wrong article or files if the target is unclear. <br>
Mitigation: State the target article path and intended operation before invoking the skill, especially when multiple drafts exist in the same workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gogoingai/skills/wenqu-write) <br>
- [ClawHub metadata homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-write) <br>
- [Artifact content index](references/INDEX.md) <br>
- [Content provenance guidance](references/planning/content-provenance.md) <br>
- [Materials governance](references/planning/materials-governance.md) <br>
- [Writing style guide](references/writing/style-guide.md) <br>
- [Writing anti-patterns](references/writing/anti-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown drafts, structured writing notes, and concise agent guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create durable per-article workspace files under wenqu-skills/ for context, materials, outlines, status, preferences, changes, terms, assets, and publish preparation.] <br>

## Skill Version(s): <br>
0.1.17 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

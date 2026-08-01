## Description: <br>
Translates English READMEs, papers, source comments, documentation, and articles into natural Chinese for reading and content creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and readers use this skill to translate single-article English technical material into natural Chinese while preserving Markdown structure, terminology, and context-appropriate annotations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent translation preferences can write repo-local preference files in the project being translated. <br>
Mitigation: Use the skill only when project-local preference memory is acceptable, and decline persistence for sensitive or temporary translation choices. <br>
Risk: Translations can preserve meaning poorly if the reader background or domain terminology is unclear. <br>
Mitigation: Confirm the target reader background, keep terminology consistent, and run the required R2 translation-style review after translation. <br>


## Reference(s): <br>
- [Translation Guide](references/translation-guide.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/gogoingai/skills/wenqu-translate) <br>
- [Project Homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-translate) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Files] <br>
**Output Format:** [Natural-language Chinese translation, usually in Markdown, with optional repo-local preference updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Handles single-article translation tasks; long documents, multi-article work, and multi-mode translation are directed to a fuller translation skill.] <br>

## Skill Version(s): <br>
0.1.15 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

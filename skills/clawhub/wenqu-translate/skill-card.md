## Description: <br>
文曲·翻译 helps agents translate README files, papers, source comments, documentation, and English articles into natural Chinese for content creation and reading. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and technical readers use this skill to translate English technical material into natural Chinese while preserving Markdown structure, code blocks, links, terminology, and reader-appropriate annotations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reusable translation preferences may be written into the current project under a wenqu-skills preferences file. <br>
Mitigation: Review generated preference-file changes before committing them, or instruct the agent not to persist translation preferences when read-only translation is required. <br>


## Reference(s): <br>
- [Translation Guide](artifact/references/translation-guide.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/gogoingai/skills/wenqu-translate) <br>
- [OpenClaw Homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-translate) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown or plain text translation with preserved source formatting where applicable] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May record reusable translation preferences in the current project when the user provides persistent preferences.] <br>

## Skill Version(s): <br>
0.1.17 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

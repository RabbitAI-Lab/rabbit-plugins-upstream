## Description: <br>
Reviews Chinese articles, reports, tutorials, project descriptions, and documentation for factual support, coherence, terminology, translation tone, AI-writing patterns, structure, style fit, and change closure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and documentation maintainers use this skill to review Chinese-language drafts for factual accuracy, logical flow, terminology, translation artifacts, AI-like phrasing, structural fit, and consistency after changes. It can run as a standalone review or as an inline review stage for related writing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may directly edit reviewed drafts under broad review triggers. <br>
Mitigation: Use manual review mode or ask for diff-style suggestions before allowing edits to important documents. <br>
Risk: The skill may persist review preferences in article-specific storage. <br>
Mitigation: Watch for new or changed files under `wenqu-skills/{文件名}/references/preferences.md` and confirm persistent preferences before reuse. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gogoingai/skills/wenqu-review) <br>
- [Homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-review) <br>
- [Review workflow entry](references/index.md) <br>
- [R0 fact checking](references/r0-factcheck.md) <br>
- [R1 English terminology](references/r1-english.md) <br>
- [R2 translation-tone review](references/r2-translation.md) <br>
- [R3 AI-writing pattern review](references/r3-ai-patterns.md) <br>
- [R4 structure review](references/r4-structure.md) <br>
- [R5 coherence review](references/r5-coherence.md) <br>
- [R6 style and narrative fit](references/r6-style-and-narrative-fit.md) <br>
- [R7 change closure](references/r7-change-closure.md) <br>
- [Chinese technical glossary](references/language/glossary.md) <br>
- [Chinese humanizer guidance](references/language/humanizer-zh.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown review reports and direct draft edits when the agent is authorized to modify files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports issues with locations, current wording, suggested rewrites, and scope notes; may write article-specific review preferences.] <br>

## Skill Version(s): <br>
0.1.17 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Audit and rewrite prose to remove AI-writing patterns, with detect-only scans, edit-in-place file cleanup, optional voice profiles, and a two-pass rewrite check. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Writers, editors, and developers use this skill to audit drafts for AI-sounding patterns, rewrite editable prose, or make targeted file edits while preserving quotes, code, tables, URLs, and attributed text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Edit mode can change a named file in place. <br>
Mitigation: Use detect mode first for sensitive drafts, review the resulting edits, and verify the file after changes. <br>
Risk: AI-writing signals can also appear in human, second-language, deadline-pressed, or technical prose. <br>
Mitigation: Treat findings as writing-quality signals rather than proof of authorship, and decide whether each flag matters in context. <br>
Risk: A rewrite could damage reference content if it edits protected material. <br>
Mitigation: Preserve quoted material, code blocks, tables, URLs, file paths, and attributed text; flag those spans instead of rewriting them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/conorbronsdon/skills/avoid-ai-writing) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [README.md](artifact/README.md) <br>
- [CHANGELOG.md](artifact/CHANGELOG.md) <br>
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) <br>
- [Pangram Labs](https://www.pangram.com/) <br>
- [brandonwise/humanizer](https://github.com/brandonwise/humanizer) <br>
- [blader/humanizer](https://github.com/blader/humanizer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown audit and rewrite report; edit mode may update a named text file and return a verification summary.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports rewrite, detect, and edit modes; optional voice and context profiles; iteration capped at two passes.] <br>

## Skill Version(s): <br>
3.22.3 (source: frontmatter, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

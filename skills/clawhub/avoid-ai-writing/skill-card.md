## Description: <br>
Audit and rewrite content to remove AI writing patterns ("AI-isms"). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and developers use this skill to audit prose for AI-writing patterns, rewrite flagged passages, or make targeted edits to user-named files. It is best suited for writing-quality review, not for proving whether a person or model authored text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AI-writing signals can produce false positives and should not be treated as proof of authorship. <br>
Mitigation: Use detect mode for third-party, published, academic, hiring, or other consequential writing, and pair findings with context before acting on them. <br>
Risk: Edit mode can change a user-named file in place. <br>
Mitigation: Review edit reports and file diffs before accepting changes, especially for published, quoted, code, or attributed material. <br>
Risk: Rewrites can over-smooth prose or introduce voice, facts, or emphasis not present in the source. <br>
Mitigation: Preserve original intent and specifics, avoid adding unsupported details, and use the skill's verification pass after rewriting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/avoid-ai-writing) <br>
- [Publisher profile](https://clawhub.ai/user/conorbronsdon) <br>
- [Wikipedia: Signs of AI-generated text](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) <br>
- [brandonwise/humanizer](https://github.com/brandonwise/humanizer) <br>
- [blader/humanizer](https://github.com/blader/humanizer) <br>
- [Pangram Labs](https://www.pangram.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown sections with quoted findings, rewritten text, change summaries, second-pass audits, or edit reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Edit mode may modify a user-named file and should report the locations changed plus verification results.] <br>

## Skill Version(s): <br>
3.22.1 (source: evidence release, SKILL.md frontmatter, CHANGELOG top entry dated 2026-07-31) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

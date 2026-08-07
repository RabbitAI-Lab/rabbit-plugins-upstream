## Description: <br>
Orchestrates Chinese 大女主 fiction creation from outline through drafting, polishing, review, and TXT delivery when a user explicitly asks to write a female-lead novel. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kongzichixiangjiao](https://clawhub.ai/user/kongzichixiangjiao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External writers and creative agents use this skill to generate Chinese female-lead web fiction with a fixed first-person heroine voice, coordinated outlining, chapter drafting, anti-AI-style polishing, review, and final text formatting. It is suited for short fiction by default and can adapt to longer user-requested works. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can create or overwrite outline, chapter, final Markdown, and TXT files in its selected output directory. <br>
Mitigation: Run it in a project-specific output directory and review existing files before allowing overwrite-oriented continuation. <br>
Risk: The skill is highly opinionated: the heroine, point of view, and narrative voice default strongly to 王枫 and first-person oral storytelling. <br>
Mitigation: Edit the skill or provide explicit creative constraints before use when a different protagonist, perspective, or voice is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kongzichixiangjiao/skills/danuzhu-novel-master) <br>
- [Publisher profile](https://clawhub.ai/user/kongzichixiangjiao) <br>
- [Primary skill definition](artifact/SKILL.md) <br>
- [README and example prompt](artifact/README.md) <br>
- [Narrative writer reference](artifact/references/09-八卦女生叙事人格/SKILL.md) <br>
- [Logic checker reference](artifact/references/06a-逻辑检查/SKILL.md) <br>
- [Text checker reference](artifact/references/06b-文字检查/SKILL.md) <br>
- [Narrative review reference](artifact/references/06c-叙事审稿/SKILL.md) <br>
- [Typesetting reference](artifact/references/07-排版/SKILL.md) <br>
- [Anti-AI-style polishing reference](artifact/references/08-去AI味/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Guidance] <br>
**Output Format:** [Markdown outlines and chapter files, final plain-text novel files, and concise status guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or overwrites outline, chapter, final Markdown, and TXT files in the selected output directory.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

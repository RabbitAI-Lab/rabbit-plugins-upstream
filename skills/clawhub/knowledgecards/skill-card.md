## Description: <br>
知识卡片 generates Chinese Obsidian-style Markdown knowledge cards that analyze a single concept through five dimensions or a custom framework for informal concepts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xtoyun](https://clawhub.ai/user/xtoyun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to turn a single concept or term into a structured Chinese knowledge card for study, note-taking, and concept analysis. It is especially suited to Obsidian workflows that benefit from YAML frontmatter, callouts, and wikilinks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on ordinary requests to explain a concept and produce a full knowledge-card response. <br>
Mitigation: Use explicit prompts and depth parameters when a full card is desired; otherwise ask for a shorter explanation outside the skill workflow. <br>
Risk: When --file is used, the skill may create a Markdown file in the current directory. <br>
Mitigation: Use --file only when local file output is intended, then review the generated filename and card content before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xtoyun/skills/knowledgecards) <br>
- [Publisher homepage](https://www.xtocn.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Obsidian-flavored Markdown with YAML frontmatter, callouts, and wikilinks; optionally saved as a .md file when --file is used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports quick, standard, and deep depth modes, optional focus by dimension, and plain-text concept links with --no-wikilinks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

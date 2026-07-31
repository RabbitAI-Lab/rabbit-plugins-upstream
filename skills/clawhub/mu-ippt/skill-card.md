## Description: <br>
PPT智能设计师 helps agents generate and edit PowerPoint presentations across from-scratch decks, technical diagrams, consulting templates, and existing deck edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[muippt](https://clawhub.ai/user/muippt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to plan, generate, verify, and edit PowerPoint decks from documents, URLs, Markdown, plain text, or existing PPTX files. It supports native editable PPTX output, SVG-based technical diagrams, consulting-style slide templates, and post-processing checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can fetch URLs and process user-provided documents, which may expose sensitive deck or source content. <br>
Mitigation: Use only trusted URLs and documents, avoid private or internal URLs, and review generated project files before sharing them. <br>
Risk: The skill can call external AI image providers and depends on API credentials. <br>
Mitigation: Keep API keys scoped, rotate them as needed, and configure provider endpoints only for trusted hosts. <br>
Risk: The security evidence flags watermark-removal guidance as a concern. <br>
Mitigation: Do not use watermark-removal workflows unless the user has the legal right to remove the watermark. <br>
Risk: Generated presentations and diagrams may contain inaccurate, misleading, or visually inconsistent content. <br>
Mitigation: Review all outputs and run the required visual verification and post-processing checks before delivery. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/muippt/skills/mu-ippt) <br>
- [Main workflow](artifact/SKILL.md) <br>
- [Agent overview](artifact/AGENTS.md) <br>
- [FAQ](artifact/docs/faq.md) <br>
- [Style, color, and layout tables](artifact/references/style-color-layout-tables.md) <br>
- [Source conversion documentation](artifact/scripts_ppt/docs/conversion.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated PPTX/project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create project workspaces, source conversions, SVG assets, and editable PPTX exports.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Analyzes an author's articles to reconstruct thinking patterns and writing style, then produces a dedicated writing persona sub-skill and reusable style prompt from WeChat Official Account content, pasted text, or local files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content creators, operations teams, brand teams, and style researchers use this skill to analyze multiple source articles, capture an author's voice and reasoning patterns, and generate a reusable writing persona for consistent same-style content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a third-party RedFox API key and fetch platform content. <br>
Mitigation: Use only authorized materials, confirm the key source and revocation path, and avoid exposing REDFOX_API_KEY in prompts, code, logs, or output files. <br>
Risk: The skill can create or update persistent local persona skills. <br>
Mitigation: Review generated SKILL.md files before installation or update, and keep backups before modifying existing personas. <br>
Risk: Generated personas may reproduce an author's style inaccurately or create misleading content. <br>
Mitigation: Review the analysis summary and final writing output for style fit, factual accuracy, and appropriate rights to use the source material. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-copywrite-alchemy) <br>
- [RedFoxHub](https://redfox.hk) <br>
- [Core Workflow](references/core_workflow.md) <br>
- [Writing Style and Thinking Framework](references/7-dimensions-framework.md) <br>
- [Writing Persona Template](references/persona-template.md) <br>
- [Writing Formula Reference](references/writing-formulas.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Guidance, Markdown, Code, Configuration, Files] <br>
**Output Format:** [Markdown guidance, style prompts, and generated local skill files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires source articles and a REDFOX_API_KEY when collecting materials through RedFoxHub.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

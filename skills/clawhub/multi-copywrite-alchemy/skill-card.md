## Description: <br>
复刻蒸馏写作技能分析一位作者的多篇文章，深度还原其思维方式与写作风格，并生成专属写作分身子技能与风格提示词。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content creators, operators, brands, and style researchers use this skill to collect or provide an author's writing samples, analyze the author's thinking and writing patterns, and generate reusable style prompts plus a local writing-persona sub-skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses REDFOX_API_KEY for RedFox platform collection, and RedFox API calls may spend platform credits. <br>
Mitigation: Configure the key only as an environment variable, confirm its scope and revocation options, and have the agent disclose planned collection calls before using platform collection. <br>
Risk: The skill can create or update a local persona sub-skill under ~/.workbuddy/skills/[author]-style/. <br>
Mitigation: Ask the agent to show the exact target path and review the generated or updated SKILL.md before relying on the persona. <br>
Risk: Writing-style distillation can produce inaccurate, overconfident, or unauthorized impersonation-like outputs if source material is insufficient or not authorized for analysis. <br>
Mitigation: Use writing samples you own or are authorized to analyze, keep the documented minimum corpus thresholds, and review generated persona guidance and outputs before publication. <br>


## Reference(s): <br>
- [Core Workflow](references/core_workflow.md) <br>
- [Writing Style and Thinking Framework](references/7-dimensions-framework.md) <br>
- [Writing Formula Reference](references/writing-formulas.md) <br>
- [Writing Persona Skill Template](references/persona-template.md) <br>
- [RedFoxHub API Key Management](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [ClawHub Skill Page](https://clawhub.ai/redfox-data/skills/multi-copywrite-alchemy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with generated style prompts, analysis summaries, and local skill-file content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update ~/.workbuddy/skills/[author]-style/SKILL.md after the user confirms the target persona and source material.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

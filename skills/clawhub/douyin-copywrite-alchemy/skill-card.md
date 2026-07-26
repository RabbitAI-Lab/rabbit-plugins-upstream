## Description: <br>
Analyzes an author's Douyin or provided writing samples to distill thinking patterns and writing style, then produces a reusable style prompt and local persona writing skill. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content creators, operators, brands, and style researchers use this skill to analyze a target author's corpus, build a high-fidelity writing-style persona, and produce future content in that persona's voice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can fetch third-party Douyin content and spend RedFox API credits. <br>
Mitigation: Confirm the intended source account, collection size, API key scope, and expected credit usage before running collection. <br>
Risk: Generated persona skills are persisted locally under ~/.workbuddy/skills and may affect later agent behavior. <br>
Mitigation: Review the generated SKILL.md before enabling or invoking it, and keep a clear backup or uninstall path for generated persona skills. <br>
Risk: Style replication can create content that readers may mistake for the original author. <br>
Mitigation: Use authorized source material, avoid deceptive impersonation, and label generated content when authorship could be unclear. <br>
Risk: A REDFOX_API_KEY is required and could be exposed through prompts, logs, code, or output files if handled carelessly. <br>
Mitigation: Store the key only as an environment variable, avoid pasting it into conversations or files, and rotate or revoke it if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/douyin-copywrite-alchemy) <br>
- [README.en.md](artifact/README.en.md) <br>
- [Core Workflow](artifact/references/core_workflow.md) <br>
- [Writing Style and Thinking Framework](artifact/references/7-dimensions-framework.md) <br>
- [Persona Template](artifact/references/persona-template.md) <br>
- [Writing Formulas](artifact/references/writing-formulas.md) <br>
- [RedFoxHub API key management](https://redfox.hk/settings/api-keys?source=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown and generated local SKILL.md content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write a generated persona skill under ~/.workbuddy/skills/[author-name]-style/ and may provide a reusable style prompt.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

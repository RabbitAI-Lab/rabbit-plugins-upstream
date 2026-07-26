## Description: <br>
Wyld Stallyns lets agents summon a roster of persona-style legends and councils to provide reflective perspectives for decisions, creative work, and hard questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[brucko](https://clawhub.ai/user/brucko) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent operators use this skill to load persona lenses, summon individual legends or groups, and optionally create new persona files through a forge workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Forge outputs can add or change persona files and council registry entries. <br>
Mitigation: Review the generated legend Markdown and council.json entry before keeping them, then scan the skill before deployment. <br>
Risk: Crisis-themed or meaning-focused prompts could be mistaken for emergency, clinical, or self-harm support. <br>
Mitigation: Use the skill only as reflective guidance and rely on qualified professional or emergency resources for clinical, emergency, or self-harm situations. <br>
Risk: Unsafe or unclear legend IDs can make generated files and registry entries harder to audit. <br>
Mitigation: Use simple, safe slugs for new legend IDs and confirm the generated paths and registry values before keeping changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/brucko/skills/wyld-stallyns) <br>
- [Publisher profile](https://clawhub.ai/user/brucko) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [FORGE.md](artifact/FORGE.md) <br>
- [Legend registry](artifact/assets/council.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Conversational Markdown with optional Markdown and JSON file updates for forged legends and council entries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Persona responses are generated from selected legend modules; forge outputs should be reviewed before keeping.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Character Builder generates complete character Skill files from arbitrary character concepts by filling a three-layer, twelve-dimension character model and assembling reusable role-generation materials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn character concepts into reusable character Skill files with a structured twelve-dimension profile, consistency checks, and downgrade behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated characters may be persisted as local skills without a clear confirmation or overwrite boundary. <br>
Mitigation: Review the target path before writing, avoid overwriting existing skill folders, and install only when a reusable Skill file is intended. <br>
Risk: Broad invocation phrases can cause unintended auto-routing in environments that trigger skills by text match. <br>
Mitigation: Narrow invocation phrases and review generated skill triggers before deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wangjiaocheng/skills/character-builder) <br>
- [Character Catalog](references/character-catalog.md) <br>
- [Character Requirements](references/character-requirements.md) <br>
- [Exemplars Index](references/exemplars.md) <br>
- [Combined Character Builder Prompt](references/character-builder-prompt.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown Skill files with supporting reference material] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist generated Skill files locally when file-system writing is available.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

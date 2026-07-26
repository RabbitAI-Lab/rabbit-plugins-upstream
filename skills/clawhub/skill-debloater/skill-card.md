## Description: <br>
Diagnoses and slims down bloated, flaky Agent Skills by using a four-axis method to reorganize content losslessly, identify deterministic steps for scripts, and gate deletions on explicit user confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liyi-ai](https://clawhub.ai/user/liyi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent-skill maintainers use this skill to audit, debloat, and stabilize local skill directories that have grown long, stale, or inconsistent. It supports lossless reorganization, script-based checks, user-reviewed deletion decisions, backups, and before/after verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads and refactors files inside a target skill directory, so a wrong target path could expose or modify unintended local skill content. <br>
Mitigation: Review the target path before running the workflow and inspect the proposed changes before accepting them. <br>
Risk: Deleting stale or orphaned files can permanently remove information the user still needs. <br>
Mitigation: The workflow defaults to keeping files, requires explicit user confirmation for each deletion, and requires a backup before deletion. <br>
Risk: Moving core guidance into references or compressing prose can make the target skill less reliable if important behavior is no longer loaded at the right time. <br>
Mitigation: Keep uncertain core/background boundary content in the skill body and run three-way verification against representative tasks after changes. <br>


## Reference(s): <br>
- [The Four-Axis Debloating Methodology](references/methodology.md) <br>
- [Interaction & Verification](references/interaction-and-verify.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/liyi-ai/skills/skill-debloater) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, audit findings, proposed file changes, and confirmation prompts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Deletion proposals require explicit user confirmation and a usable backup before removal.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

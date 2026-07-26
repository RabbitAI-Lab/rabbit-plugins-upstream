## Description: <br>
Use this skill when reorganizing data/ and context_hooks in a briefing_package to avoid token waste. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ice26985850](https://clawhub.ai/user/ice26985850) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
TRPG briefing-package authors and maintainers use this skill to decide which game data belongs in always-loaded data files and which larger references should move behind context_hooks triggers. It supports token-efficient organization of AI GM resources, config.yaml hooks, and rules_sections files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may propose moving data files, editing config.yaml context_hooks, or deleting duplicate originals after migration. <br>
Mitigation: Confirm the target is a briefing_package and review proposed moves, hook edits, and cleanup actions before applying them. <br>
Risk: Incorrectly classifying core per-turn data as hook-triggered reference material could make an AI GM miss information during play. <br>
Mitigation: Apply the skill's every-turn test before migration and keep small, required core data in data/ files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ice26985850/skills/trpg-data-context-hooks) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with YAML configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose data file moves, rules_sections placement, context_hooks keyword updates, and duplicate-file cleanup steps for a briefing_package.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

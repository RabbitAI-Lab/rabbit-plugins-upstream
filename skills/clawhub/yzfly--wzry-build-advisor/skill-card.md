## Description:

Provides concise 王者荣耀 (Honor of Kings) equipment build advice, using local hero, equipment, and counter-rule data to recommend the next item and a final build path.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yzfly](https://clawhub.ai/user/yzfly)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent assistants use this skill during 王者荣耀 matches to turn a player's hero, enemy threats, current equipment, and game state into short, actionable build guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Equipment and hero recommendations may become outdated when 王者荣耀 changes its game balance or item data.

Mitigation: Verify important builds against current game data and refresh the local references when the upstream data source is updated.

## Reference(s):

- [Counter Rules](references/counter-rules.md)
- [Equipment Data](references/equipment.md)
- [Hero Data](references/heroes.md)
- [WZRY Atlas Source Data](https://github.com/LangGPT/wzry-atlas)
- [WZRY Atlas Online Reference](https://langgpt.github.io/wzry-atlas/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Concise Markdown advice with fixed Chinese sections for next item, follow-up items, final build, and reminders.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations are intentionally brief and depend on local reference data.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

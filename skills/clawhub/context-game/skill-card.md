## Description:

A multi-genre open-world conversational game skill where the agent acts as world simulator, narrator, and rules adjudicator for free-text player actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[charlesresearch001](https://clawhub.ai/user/charlesresearch001)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to run a persistent text adventure with selectable worlds, rule-based adjudication, dice rolls, evolving events, and save files. It is intended for interactive gameplay rather than factual decision support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Save-slot validation can allow game files to be written outside the intended saves folder.

Mitigation: Install in a dedicated workspace, use simple slot names such as default or slot_01, and avoid dot or dot-dot slot names until slot validation is fixed.

Risk: The skill runs a local Python save engine and writes persistent game files.

Mitigation: Review workspace writes before deployment and keep gameplay saves away from sensitive project directories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/charlesresearch001/skills/context-game)
- [Publisher profile](https://clawhub.ai/user/charlesresearch001)
- [Artifact README](artifact/README.md)
- [World library overview](artifact/world/README.md)
- [Core rules](artifact/rules/rules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown narrative with structured game-state updates and shell command invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces persistent local save files, memory summaries, world data, and roll logs through the bundled Python save engine.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

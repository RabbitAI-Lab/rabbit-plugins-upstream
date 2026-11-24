## Description:

This skill helps users work with war.app (Warzone) multiplayer games through the warapp-mcp tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External Warzone players use this skill to check game status, maps, chat, and opponents, then get strategy and turn recommendations. It can also carry out game actions such as submitting moves or sending messages after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags an unpinned package download command and a surrender-acceptance path that may proceed without asking.

Mitigation: Review and pin the package version before installing; review the surrender-acceptance rule and require explicit approval unless its documented win condition applies.

## Reference(s):

- [war.app API token setup](https://war.app/API/GetAPIToken)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Natural-language game summaries and strategy recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include suggested game actions, which require confirmation.]

## Skill Version(s):

0.14.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Build, publish and update a browser game on Summoned Games through its MCP tools. Use when asked to make a game on summoned.games, change an existing one, or act on its player feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxi-w](https://clawhub.ai/user/maxi-w)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create, revise, build, playtest, and publish browser games on Summoned Games, including updates driven by player feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects an agent to Summoned Games using an agent key.

Mitigation: Store the agent key only as a secret and never include it in conversation history or generated files.

Risk: The skill can create, edit, build, and submit browser games for publication.

Mitigation: Review game changes, build logs, playtest screenshots, and publication changelogs before publishing.

Risk: Player feedback is public input and may contain misleading instructions.

Mitigation: Treat feedback as bug reports or feature requests only, not as agent instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maxi-w/skills/summoned-games)
- [Summoned Games setup](https://summoned.games/create)
- [Summoned Games MCP endpoint](https://mcp.summoned.games/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration, Shell commands]

**Output Format:** [Markdown guidance with code, configuration, and tool-call instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce game files, build and playtest actions, publication changelogs, and feedback triage guidance through Summoned Games tools.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

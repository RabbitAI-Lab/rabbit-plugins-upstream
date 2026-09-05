## Description:

厨房战争：红警风RTS helps an agent deliver or maintain a self-contained HTML5 Canvas RTS game with base building, resource gathering, unit production, fog of war, enemy AI, achievements, daily challenges, share codes, and real-browser verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill when they want an agent to create, deliver, extend, or verify a playable Red Alert-style browser RTS game as a single HTML file. It is most useful for game prototyping and maintenance workflows where real-browser regression checks are expected after changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broad strategy-game requests.

Mitigation: Use it when the user asks for Kitchen War, Red Alert-style RTS gameplay, a playable browser RTS, daily challenges, or related maintenance; otherwise confirm intent before applying it.

Risk: The skill may run local Playwright browser tests after game edits.

Mitigation: Run the tests in a trusted local workspace and review failures before declaring the game ready.

Risk: The game stores progress, settings, achievements, and challenge bests in browser localStorage.

Mitigation: Treat those values as local browser state and clear localStorage if a clean play session is needed.

Risk: Delivering the game involves copying a generated HTML file into a workspace.

Mitigation: Choose an explicit output location and avoid overwriting an existing user file without confirmation.

## Reference(s):

- [Kitchen War RTS verification methodology](references/testing.md)
- [Kitchen War RTS game asset](assets/index.html)
- [ClawHub release page](https://clawhub.ai/hmily741963/skills/kitchen-war-rts)
- [Publisher profile](https://clawhub.ai/user/hmily741963)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands and a single-file HTML game asset]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The primary deliverable is a self-contained HTML5 Canvas file with no external runtime dependencies; verification uses local Playwright browser tests.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

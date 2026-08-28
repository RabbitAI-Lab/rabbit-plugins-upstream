## Description:

This skill helps an agent deliver or modify Kitchen War, a zero-dependency single-file HTML5 Canvas RTS game with base building, resource gathering, unit production, enemy AI, fog of war, achievements, speed controls, pause, and screenshot sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to provide, extend, fix, or re-verify a playable browser RTS game inspired by classic Red Alert-style mechanics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be selected for broad browser strategy game requests beyond this specific Kitchen War RTS package.

Mitigation: Confirm the requested game scope before applying the skill, and use it for Kitchen War RTS delivery, extension, repair, or verification work.

Risk: The game stores local progress and settings in browser localStorage.

Mitigation: Disclose that persistence is local to the browser and clear localStorage if a clean test or reset is needed.

Risk: Changes to the game can introduce browser runtime errors or multi-frame gameplay regressions.

Mitigation: Run the bundled real-browser verification gate after edits and require zero page errors or console errors before release.

## Reference(s):

- [Kitchen War RTS verification methodology](artifact/references/testing.md)
- [ClawHub skill page](https://clawhub.ai/hmily741963/skills/kitchen-war-rts)

## Skill Output:

**Output Type(s):** [Files, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with file delivery instructions, code edits, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or modifies a local single-file HTML game and may provide verification steps for browser-based testing.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

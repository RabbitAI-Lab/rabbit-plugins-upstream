## Description:

Kitchen War RTS delivers a playable, single-file HTML5 Canvas kitchen strategy game with Red Alert-style base building, resource gathering, unit production, fog of war, enemy AI, achievements, speed controls, pause, and screenshot sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to deliver, play, extend, or verify a browser-based RTS game. The skill provides the game file, gameplay guidance, and real-browser regression testing expectations for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The game persists preferences, achievements, and best scores in browser localStorage.

Mitigation: Use a suitable browser profile for playtesting and clear the site's localStorage when persisted game state should be removed.

Risk: Modifying the game can introduce runtime or gameplay regressions that are not visible in one-frame checks.

Mitigation: Run the documented real-browser Playwright verification gate after changes and require zero page errors or console errors before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hmily741963/skills/kitchen-war-rts)
- [Testing methodology](references/testing.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with a self-contained HTML file and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The delivered game stores preferences, achievements, and best scores in browser localStorage.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

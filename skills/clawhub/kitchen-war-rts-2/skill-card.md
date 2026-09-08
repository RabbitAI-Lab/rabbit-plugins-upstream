## Description:

厨房战争：红警风RTS generates and helps maintain a playable, single-file HTML5 Canvas RTS game with base building, resource gathering, unit production, fog of war, enemy AI, achievements, daily challenges, share codes, screenshots, speed controls, and a real-browser verification gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to deliver or extend a self-contained browser RTS game inspired by Red Alert with a kitchen-war theme. It also guides agents to verify gameplay changes with bundled real-browser tests before release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill copies a single-file HTML game into a workspace, so a poorly chosen destination could overwrite an existing file.

Mitigation: Review the destination path before copying assets/index.html and avoid overwriting files that matter.

Risk: The browser game stores progress and preferences in local browser storage.

Mitigation: Treat localStorage as local user state and clear browser site data when resetting or sharing a browser profile.

## Reference(s):

- [Kitchen War RTS verification methodology](references/testing.md)
- [ClawHub skill listing](https://clawhub.ai/hmily741963/skills/kitchen-war-rts-2)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Single-file HTML, Markdown guidance, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a browser game asset and verification guidance; no external runtime dependencies are declared for the game file.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

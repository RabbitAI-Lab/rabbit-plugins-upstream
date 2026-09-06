## Description:

厨房战争：经典即时战略 helps agents deliver and maintain a self-contained HTML5 Canvas RTS game with base building, resource collection, unit production, fog of war, enemy AI, daily challenges, share codes, and browser verification assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when asked to create, extend, repair, or verify a playable browser-based RTS game. It provides a single-file game artifact plus guidance and Playwright checks for preserving real browser playability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser game stores gameplay preferences, achievements, best times, and challenge records in localStorage.

Mitigation: Tell users that records are local to their browser and can be cleared through browser site data controls.

Risk: Maintainer verification scripts launch Playwright browser automation.

Mitigation: Run the scripts only from the reviewed artifact when maintaining or validating the skill.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/hmily741963/skills/kitchen-war-rts-cn)
- [Kitchen War RTS verification methodology](references/testing.md)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with a self-contained HTML file and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The delivered game is local browser content; maintainer tests use Playwright and the game stores small gameplay preferences and records in browser localStorage.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

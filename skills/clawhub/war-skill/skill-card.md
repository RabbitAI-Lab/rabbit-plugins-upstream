## Description:

Delivers and maintains Kitchen War RTS, a self-contained HTML5 Canvas Red Alert-style browser strategy game with base building, resource harvesting, unit production, fog of war, enemy AI, a superweapon, and browser-based verification scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to deliver, extend, repair, and verify a playable Red Alert-style Kitchen War browser RTS for users who ask for a web strategy game.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broader browser strategy game requests beyond this exact Kitchen War RTS workflow.

Mitigation: Confirm the user wants the Kitchen War or Red Alert-style browser RTS workflow before copying, modifying, or presenting the bundled game.

Risk: Game changes can regress multi-frame UI interactions or unit movement without obvious syntax failures.

Mitigation: Run the documented real-browser verification scripts after edits and require zero console errors, page errors, and failed assertions.

Risk: Verification scripts launch the bundled HTML game in a local browser and require local Node and Playwright availability.

Mitigation: Run verification only in an environment where local browser automation is acceptable and the required test dependencies are installed.

## Reference(s):

- [Kitchen War RTS Verification Methodology](references/testing.md)
- [ClawHub Skill Page](https://clawhub.ai/hmily741963/skills/war-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with code/file edits, shell commands, and a self-contained HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a single-file HTML5 Canvas game and local Playwright verification commands; no external game dependencies.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

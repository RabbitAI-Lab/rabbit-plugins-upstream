## Description:

Creates and edits playable PowPow City maps from real-world map data or generated terrain, with optional simulation, screenshots, and share links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Players, creators, and developers use this skill to create and edit IsoCity maps, import real-world geography, and deliver playable city saves or share links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: City creation and editing write local save files and backups.

Mitigation: Use a scratch workspace and review generated cities before importing or sharing them.

Risk: Map generation can send place names or coordinates to external mapping and geocoding services.

Mitigation: Avoid sensitive locations and use generated terrain when external requests are unnecessary.

Risk: Optional screenshot and simulation features require installing Playwright and a browser.

Mitigation: Install pinned dependencies only when those features are needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpowcity-map-editor)
- [PowPow City game](https://powpowcity.powpow.online/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files, Guidance]

**Output Format:** [Text guidance and CLI output; JSON city saves, optional PNG screenshots, and share URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Editing creates local backup files; screenshots and simulation require an accessible game and optional Playwright installation.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

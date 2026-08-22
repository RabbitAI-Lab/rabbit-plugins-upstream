## Description:

Generates reproducible endgame-only Path of Exile 1 build analyses from permitted PoE Ninja, public character, or PoB character-code inputs and verifies metrics with Path of Building Community through pob-cli when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qpooqp777](https://clawhub.ai/user/qpooqp777)

### License/Terms of Use:

MIT-0

## Use Case:

External Path of Exile 1 players and build analysts use this skill to produce reproducible endgame build recommendations, preserve imported character data, and separate PoE Ninja observations from verified PoB calculations and unverified estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private or unintended character data may be exposed if users provide sensitive PoB XML, character codes, or output paths.

Mitigation: Use only public or user-approved inputs, avoid private character data unless local analysis is intended, and write only to explicit user-provided output paths.

Risk: Build metrics can be misleading when LuaJIT, the PoB root, compatible XML, or skill metadata are unavailable.

Mitigation: Report blocked or failed verification states and keep unverified values separate from official PoB calculations.

Risk: A public pobb.in link can publish character data unintentionally.

Mitigation: Use dry-run code generation by default and require explicit user confirmation before any public sharing command.

Risk: PoE Ninja data can be stale, incomplete, or unsuitable for reconstructing a complete build from static pages.

Mitigation: Use permitted JSON, data dumps, user-provided exports, public character data, or PoB codes, and record retrieval time, filters, schema, sample size, and limitations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qpooqp777/skills/poe1-build-analyst)
- [Path of Exile 3.29.0 announcement](https://www.pathofexile.com/forum/view-thread/3985332)
- [PoE Ninja Path of Exile 1 builds](https://poe.ninja/poe1/builds)
- [qpooqp777/pob-cli](https://github.com/qpooqp777/pob-cli)
- [Path of Building Community Fork](https://github.com/PathOfBuildingCommunity/PathOfBuilding)
- [API reference](references/api_reference.md)
- [Research notes](references/research_notes.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with JSON artifacts and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Endgame-only build records with source assumptions, PoB verification status, warnings, and explicit public-sharing state.]

## Skill Version(s):

0.1.2 (source: server release evidence and VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

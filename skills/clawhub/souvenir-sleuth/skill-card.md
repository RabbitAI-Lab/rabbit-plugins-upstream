## Description:

Find authentic, locally-made souvenirs at any destination and dodge tourist traps. Provides fair local price ranges, where locals actually shop, authenticity tells for handcrafts vs factory fakes, customs/import rules, and trap checks for specific items. Use when the user asks what to buy in a city, whether a souvenir is authentic or a tourist trap, or what gifts they can bring through customs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Travelers and agents use this skill to identify authentic local souvenirs, compare fair local price ranges, avoid tourist traps and illegal items, and prepare customs-aware shopping guidance for a destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customs and import rules for food, plants, animal products, and protected materials can change or vary by destination-home-country pair.

Mitigation: Verify restricted items against official customs and CITES sources before buying or importing them.

Risk: Current shop hours, availability, and seasonal details may be outdated or incomplete without live research.

Mitigation: Confirm the top recommendations with current web sources before relying on shop or availability details.

Risk: The skill expects the agent to run a local Python helper and may create JSON dossier files.

Mitigation: Review generated commands and output paths before execution, especially when creating local files.

## Reference(s):

- [Customs & Import Quick Guide for Souvenirs](references/customs-guide.md)
- [Authenticity Tells: Real Handcraft vs Factory Handmade](references/authenticity-tells.md)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/souvenir-sleuth)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or plain text guidance with optional JSON dossier files and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ranked souvenir dossiers, trap checks, customs flags, fair price ranges, and web-research prompts for current shop details.]

## Skill Version(s):

1.0.0 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

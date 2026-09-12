## Description:

Find authentic, locally-made souvenirs at any destination and dodge tourist traps. Provides fair local price ranges, where locals actually shop, authenticity tells for handcrafts vs factory fakes, customs/import rules, and trap checks for specific items. Use when the user asks what to buy in a city, whether a souvenir is authentic or a tourist trap, or what gifts they can bring through customs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Travelers and agents use this skill to identify locally meaningful souvenirs, compare fair local prices, avoid tourist-trap goods, and check customs-sensitive categories before purchase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customs and import rules can change and vary by traveler home region, especially for food, plants, animal products, protected species, and restricted materials.

Mitigation: Review official customs sources before relying on travel import advice and declare uncertain items.

Risk: The skill may have an agent run a bundled Python script and perform current web research for shop hours or customs details.

Mitigation: Review the script and command arguments before execution, and treat live research results as current but still subject to verification.

## Reference(s):

- [Authenticity Tells](references/authenticity-tells.md)
- [Customs & Import Quick Guide](references/customs-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/souvenir-sleuth)
- [Server-Resolved GitHub Provenance](https://github.com/voronindenis5/souvenir-sleuth)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional shell commands and JSON dossier output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can run a bundled offline Python helper and can enrich recommendations with current web research.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

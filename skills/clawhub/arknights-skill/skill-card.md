## Description:

Answers Arknights operator, investment, lore, terminology, resource-planning, and stage-strategy questions while using a local Doctor profile for personalization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[morandot](https://clawhub.ai/user/morandot)

### License/Terms of Use:

MIT-0

## Use Case:

External Arknights players use this skill to get account-aware advice on operator investment, stage clears, mechanics, lore, and resource planning. The skill is also useful for agents that need a structured answer style with freshness caveats for version-sensitive game questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill maintains a local Doctor profile containing account and roster facts.

Mitigation: Use the default local profile path or an intentional ARKNIGHTS_MEMORY_DIR override, and avoid adding facts the user did not explicitly provide.

Risk: Manual shell installation can run a remote installer from GitHub.

Mitigation: Review the installer before execution and pin a known release ref instead of installing from main when repeatability matters.

Risk: Version-sensitive Arknights advice can become stale.

Mitigation: Use live lookup for current events, banners, and meta assessments, or clearly state when an answer is not based on current version data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/morandot/skills/arknights-skill)
- [Server-Resolved GitHub Source](https://github.com/morandot/arknights-skill/tree/main/arknights-skill)
- [Project Homepage](https://github.com/morandot/arknights-skill)
- [Quick Start](references/quickstart.md)
- [Doctor Profile Schema](references/doctor-profile-schema.md)
- [Answer Templates](references/answer-templates.md)
- [Style Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with optional shell command blocks and structured guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read or update a local Doctor profile JSON file when explicit account facts are provided.]

## Skill Version(s):

1.6.1 (source: ClawHub release metadata; artifact frontmatter reports 1.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

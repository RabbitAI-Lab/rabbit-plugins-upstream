## Description:

Builds a personalized vegetable seed-starting and sowing calendar from last and first frost dates, crop choices, and household size, including tray math, row-footage estimates, succession schedules, and optional moon-phase annotations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External gardeners and agents assisting them use this skill to plan frost-date-driven annual vegetable gardens, including when to start seeds indoors, direct-sow, transplant, schedule successions, and estimate seed tray and row-footage needs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Planting recommendations can be inaccurate if users rely on rough zone-based frost estimates or outdated local frost dates.

Mitigation: Verify last spring frost and first fall frost dates with local extension or NOAA data before relying on the calendar.

Risk: Moon-phase annotations may be mistaken for evidence-based agronomic advice.

Mitigation: Treat moon-phase output as optional folklore annotation; do not use it to shift planting dates.

## Reference(s):

- [Seed Crop Library](references/seed-crop-library.md)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/seed-calendar-planner)
- [Server-Resolved GitHub Provenance](https://github.com/voronindenis5/seed-calendar-planner)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, plus optional JSON from the bundled command-line tool.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated dates depend on user-provided frost dates, crop list, household size, and optional command flags.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

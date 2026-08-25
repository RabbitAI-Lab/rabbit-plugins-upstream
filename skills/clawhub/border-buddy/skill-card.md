## Description:

Pre-trip border intelligence for visa requirements by nationality, passport validity, Schengen 90/180 day stay calculations, yellow fever certificate requirements, customs limits, and transit visa checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External travelers, travel planners, and AI agents use this skill for first-pass checks of trip entry requirements, transit visa exposure, passport validity, customs allowances, yellow-fever certificate needs, and Schengen 90/180-day planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Offline travel-rule snapshots may be stale or incomplete for a planned route.

Mitigation: Verify current visa, passport, transit, health, and customs rules with the named official authority before booking or travel.

Risk: Schengen 90/180 calculations are sensitive to entry and exit date conventions and borderline edge cases.

Mitigation: Use departure dates as exclusive exit dates, keep a 1-2 day safety margin, and confirm borderline cases with official calculators or authorities.

Risk: Trip-planning outputs could be mistaken for legal or immigration advice.

Mitigation: Limit use to short-stay travel screening and refer work, study, residency, asylum, waiver, or criminal-record cases to official channels or qualified counsel.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/border-buddy)
- [Schengen 90/180 Rule Algorithm](references/schengen-180.md)
- [Visa Rules Knowledge Model](references/visa-rules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown and plain-text travel readiness reports with inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an offline rule snapshot and should surface named official authorities for live verification.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

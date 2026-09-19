## Description:

Panoramic training analysis for Garmin Connect data that pulls activities, per-kilometer splits, recovery and load metrics, merges Open-Meteo weather, and renders an offline dark-themed HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runzhenghengbin](https://clawhub.ai/user/runzhenghengbin)

### License/Terms of Use:

MIT

## Use Case:

Runners, coaches, and developers use this skill to fetch Garmin Connect training, recovery, and GPS/weather data and generate period-based or focused-activity HTML reports for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Garmin credentials and detailed health, sleep, recovery, and GPS activity history.

Mitigation: Install only when comfortable granting that access, prefer environment variables or this skill's own credential file, and remove sibling-skill credential fallbacks before use.

Risk: Generated data and HTML reports can contain sensitive health metrics and precise location history.

Mitigation: Protect or delete generated data and reports after use, and consider disabling or coarsening Open-Meteo lookups when precise location disclosure is a concern.

Risk: The skill depends on a pinned Garmin Connect client and performs external service lookups.

Mitigation: Use an isolated pinned Python environment and review the scripts before running them against a real account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runzhenghengbin/skills/garmin-panorama-training-analysis)
- [Server-Resolved Source Repository](https://github.com/runzhenghengbin/garmin-panorama-training-analysis)
- [Imported Provenance Commit](https://github.com/runzhenghengbin/garmin-panorama-training-analysis/tree/3e5892b046cb0b2030c79bba99f3ac2b189c5719)
- [README](README.md)
- [Heat Metrics Reference](references/heat_metrics.py)
- [Load Balance Reference](references/load_balance.py)
- [Body Composition Reference](references/body_composition.py)
- [Upstream COROS Version](https://github.com/yoyojay/coros-panorama-training-analysis)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with shell commands; generated JSON data and offline HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated data and reports may contain Garmin credentials-derived health, recovery, sleep, and GPS activity history.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

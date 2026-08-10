## Description:

Generates an offline WorkBuddy usage dashboard from local WorkBuddy data, covering token and credit consumption, thinking-time efficiency, model distribution, date filtering, error monitoring, and usage-spike analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT-0

## Use Case:

WorkBuddy users and developers use this skill to generate a private, offline report of local WorkBuddy usage, costs, model mix, errors, and high-usage periods. It supports usage supervision and cost review without sending usage data to external services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated report files may contain private usage metadata, including session titles, model names, token counts, credit use, errors, and partial session identifiers.

Mitigation: Keep the generated HTML, JSON, and JavaScript files private and avoid sharing them outside trusted review contexts.

Risk: The --home option can direct the extractor to an alternate data root.

Mitigation: Use --home only with a trusted WorkBuddy data directory and review the selected path before running the script.

Risk: The dashboard is a snapshot of local WorkBuddy data and may not reflect later activity.

Mitigation: Regenerate the dashboard before making decisions that depend on current usage or cost information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clancy-feng/skills/workbuddy-usage-status)
- [Data Guide](DATA-GUIDE.md)
- [README](README.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Code, Markdown, Shell commands, Guidance]

**Output Format:** [Local HTML dashboard plus JSON and JavaScript data files, with optional Markdown or shell command guidance from the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a self-contained offline dashboard and local aggregate data files in the selected output directory.]

## Skill Version(s):

1.1.0 (source: release evidence, frontmatter, and changelog; released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
